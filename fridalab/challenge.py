import frida,sys

def on_message(message,data):
    if(message['type'] == 'error'):
        print(message['description'])
    else:
        print(message)
    
jscode = """
Java.perform(function(){
    // chall01 : set challenge_01 class's chall01 variable to 1
    var chall01Class = Java.use("uk.rossmarks.fridalab.challenge_01");
    chall01Class.chall01.value = 1;
    console.log("[+] challenge 01 solved!");
    
    // set var main reference MainActivity Instance
    var main;
    Java.choose("uk.rossmarks.fridalab.MainActivity",{
        onMatch: function(instance){
            main = instance;
        },
        onComplete: function(){}
    })
    
    // chall02 : Run chall02()
    main.chall02();
    console.log("[+] challenge 02 solved!");
    
    // chall03 : overload chll03() to return true
    main.chall03.overload().implementation = function(){
      return true;
  }
    console.log("[+] challenge 03 solved!");
    
    // chall04 : call chall04() with argument "frida"
    main.chall04("frida");
    console.log("[+] challenge 04 solved!");
    
    // chall05 : overload chall05() to always call chall05("frida")
    main.chall05.overload('java.lang.String').implementation = function(arg0){
        this.chall05("frida");
    }
    console.log("[+] challenge 05 solved!");
    
    
    // chall07 : Bruteforce check07Pin()
    var chall07Class = Java.use("uk.rossmarks.fridalab.challenge_07");
    var i;
     
    for(i=1000;i<9999;i++){
        if(chall07Class.check07Pin(i.toString())){
            main.chall07(i.toString())
            console.log("[+] challenge 07 solved!");
        }
    }
    
    // chall08 : Change 'check' button's text value to 'Confirm'
    var RIdClass = Java.use('uk.rossmarks.fridalab.R$id');
    var buttonClass = Java.use('android.widget.Button');
    var StringClass = Java.use('java.lang.String');
    var RIdCheck = RIdClass.check.value; 
    var view = main.findViewById(RIdCheck);
    var button = Java.cast(view,buttonClass);
    button.setText(StringClass.$new("Confirm"));
    console.log("[+] challenge 08 solved!");
    
    // chall06이 chall08 보다 먼저 실행되면, setTimeout안에서 main을 가지고 있어서 main Thread가 하나 더 생긴다.
    // 근데 새로 생긴 Thread로는 chall08의 view를볼 수 없다. (main Thread만 가능) 따라서 chall06을 마지막에 실행 
    
    // chall06 : Run chall06() after 10 seconds with true value
    setTimeout(function(){
        var chall06Class = Java.use("uk.rossmarks.fridalab.challenge_06");
        main.chall06(chall06Class.chall06.value);
        console.log("[+] challenge 06 solved!");
    },10000)
})

"""

session = frida.get_usb_device(timeout=1).attach("FridaLab")
script = session.create_script(jscode)
script.on("message",on_message)
script.load()

sys.stdin.read()
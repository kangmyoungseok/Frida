import frida
import sys
def on_message(message,data):
    print(message)

jscode = """
Java.perform(function(){
    var chall07Class = Java.use('uk.rossmarks.fridalab.challenge_07');
    var i
    for(i=1000;i<9999;i++){
      if(chall07Class.check07Pin(i.toString())){
        console.log("find the key");
        console.log(i);
        break;
      }
    }
    var main;
    var MainActivityClass = Java.choose('uk.rossmarks.fridalab.MainActivity',{
      onMatch: function(instance){
        main = instance;
      },
      onComplete: function(){}
    });
    main.chall07(i.toString());

});
"""
process = frida.get_usb_device(timeout=1).attach("fridalab")
script = process.create_script(jscode)
script.on("message",on_message)
script.load()

sys.stdin.read()
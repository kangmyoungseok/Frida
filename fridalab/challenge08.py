import frida,sys

def on_message(message,data):
    print(message)

jscode = """
Java.perform(function(){
    var main;
    Java.choose('uk.rossmarks.fridalab.MainActivity',{
        onMatch: function(instance){
            main= instance;

        },
        onComplete: function(){
            console.log("[+] chall08 solved");
        }
    })
    var buttonClass = Java.use('android.widget.Button');
    var checkid = main.findViewById(2131165231);
    var buttonIdCheck = Java.cast(checkid,buttonClass);
    console.log(buttonIdCheck.getText());
    var string = Java.use('java.lang.String');
    buttonIdCheck.setText(string.$new("Confirm"));
    console.log("[+] challenge 08 solved!");
})
"""
jscode1 = """
Java.perform(function(){
    Java.choose('uk.rossmarks.fridalab.MainActivity',{
        onMatch: function(instance){
            var buttonClass = Java.use("android.widget.Button");
            var buttonIdCheck = Java.cast(instance.findViewById(2131165231),buttonClass);
            var stringClass = Java.use("java.lang.String");
            buttonIdCheck.setText(stringClass.$new("Confirm"));
        },
        onComplete: function(){
            console.log("[+] chall08 solved");
        }
    })
})
"""


session = frida.get_usb_device(timeout=1).attach("FridaLab")
script = session.create_script(jscode)
script.on("message",on_message)
script.load()
sys.stdin.read()
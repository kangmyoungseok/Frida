import frida
import sys
def on_message(message,data):
    print(message)

jscode = """
Java.perform(function(){
    var main;
    Java.choose('uk.rossmarks.fridalab.MainActivity', {
    onMatch: function(instance) {
        main = instance;
    },
    onComplete: function() {}
    });

    main.chall05.overload('java.lang.String').implementation = function (arg0) {
        this.chall05("frida");
        console.log("chall05 method is overloaded");
    };
});
"""


process = frida.get_usb_device(timeout=5).attach("fridalab")
script = process.create_script(jscode)
script.on("message",on_message)
script.load()

sys.stdin.read()
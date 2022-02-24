import frida,sys

def on_message(message,data):
    print(message)
    
PACKAGE = "owasp.mstg.uncrackable2"
jscode = """
Java.perform(function(){
    console.log("success");
    var MainActivity = Java.use("sg.vantagepoint.uncrackable2.MainActivity");
    MainActivity.a.overload('java.lang.String').implementation = function(param){
        console.log("[+] hooking a(exit) function : "param);
    }


})

"""

device = frida.get_usb_device(timeout=5)
pid = device.spawn([PACKAGE])
process = device.attach(pid)
device.resume(pid)
script = process.create_script(jscode)
script.on('message',on_message)
script.load()
sys.stdin.read()


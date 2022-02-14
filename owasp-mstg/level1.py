import frida,sys

def on_message(message,data):
    print(message)
    
    
jscode = """
Java.perform(function(){
    console.log("[+] hooking System API");
    var SystemClass = Java.use("java.lang.System");
    console.log(SystemClass);
    SystemClass.exit.overload('int').implementation = function(param1){
        console.log("[+] System.exit called");
    }
    
    var SecretClass = Java.use("sg.vantagepoint.uncrackable1.a");
    var Base64Class = Java.use("android.util.Base64");
    var secret1 = SecretClass.b("8d127684cbc37c17616d806cf50473cc");
    var secret2 = Base64Class.decode("5UJiFctbmgbDoLXmpL12mkno8HT4Lv8dlat8FxR2GOc=", 0);
    
    var EncryptClass = Java.use("sg.vantagepoint.a.a");
    var bArry = EncryptClass.a(secret1,secret2);
    
    var StringClass = Java.use("java.lang.String");
    console.log(StringClass.$new(bArry));
})

"""

session = frida.get_usb_device(timeout=1).attach("Uncrackable1")
script = session.create_script(jscode)
script.on("message",on_message)
script.load()
sys.stdin.read()
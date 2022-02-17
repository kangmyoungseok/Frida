import frida,sys
def on_message(message,data):
    if(message['type'] == 'error'):
        print(message['description'])
    else:
        print(message)
PACKAGE = "com.hspace.pengsu"
jscode="""
setTimeout(function(){
    setImmediate(function(){
        Java.perform(function(){
            var rootcheck = Java.use("com.hspace.pengsu.RootCheck");
            rootcheck.rootCheck.implementation = function(){
                console.log("[+] root check bypass");
                return false
            }
            var bypass = Java.use("android.app.Activity");
            bypass.finish.overload().implementation = function(){}
            var main = Java.use("com.hspace.pengsu.MainActivity");
            main.v.value=100;
            console.log("끝");
        })
    })
},100)
"""
print('[*] start')
device = frida.get_usb_device(timeout=5)
pid = device.spawn([PACKAGE])
process = device.attach(pid)
device.resume(pid)
script = process.create_script(jscode)
script.on('message',on_message)
script.load()
sys.stdin.read()

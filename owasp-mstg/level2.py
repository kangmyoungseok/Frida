import frida,sys

def on_message(message,data):
    print(message)
    
PACKAGE = "owasp.mstg.uncrackable2"
jscode = """
Java.perform(function(){
    // 파이썬으로 후킹할때는 타이밍 문제 때문에 a 함수가 아닌, exit 함수를 후킹해야 한다.
    // 파이썬 코드가 후킹하기 전에 이미 a 함수가 실행되버리기 때문.

    var System = Java.use('java.lang.System');
    System.exit.overload('int').implementation = function(param1){
        console.log("hooking exit function ");
    }


    // 현재 Async task에서 Debug.isDebuggerConnected()를 계속 탐지하고 있다.
    // While문을 계속 탐지하면서 isDebuggerConnected()가 return true이면, a 함수를 호출해서 
    // Debugger detected를 띄워줌. 현재 a 함수를 후킹했기 때문에 아래의 내용은 할 필요가 없는데 그냥 후킹해보고 싶어서 썼음
    // return false로 하면, [+] hooking Debugger check가 무한루프에서 계속 반복되기 때문에 엄청 뜨고,
    // return true로 하면, 바로 while문을 끝내고, 나오기 때문에 한번만 호출된다.
    var Debug = Java.use("android.os.Debug");
    Debug.isDebuggerConnected.implementation = function(){
        console.log("[+] hooking Debugger check")
        return true;
    }

    Interceptor.attach(Module.findExportByName("libfoo.so","strncmp"),{
        onEnter: function(args){
            var param1 = Memory.readUtf8String(args[0]);
            var param2 = Memory.readUtf8String(args[1]);
            if(param1.indexOf('01234567890123456789012')!== -1){
                console.log(param1);
                console.log(param2);
            }
        },
        onLeave: function(){}
    })
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


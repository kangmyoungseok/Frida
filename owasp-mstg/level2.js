Java.perform(function(){
    var MainActivity = Java.use('sg.vantagepoint.uncrackable2.MainActivity');
    MainActivity.a.overload('java.lang.String').implementation = function(param1){
        console.log("[+] hooking Mainactivity.a :" + param1);
    }


    // 현재 Async task에서 Debug.isDebuggerConnected()를 계속 탐지하고 있다.
    // While문을 계속 탐지하면서 isDebuggerConnected()가 return true이면, a 함수를 호출해서 
    // Debugger detected를 띄워줌. 현재 a 함수를 후킹했기 때문에 아래의 내용은 할 필요가 없는데
    // 그냥 후킹해보고 싶어서 썼음
    // return false로 하면, [+] hooking Debugger check가 무한루프에서 계속 반복되기 때문에 엄청 뜨고,
    // return true로 하면, 바로 while문을 끝내고, 나오기 때문에 한번만 호출된다.
    var Debug = Java.use("android.os.Debug");
    Debug.isDebuggerConnected.implementation = function(){
        console.log("[+] hooking Debugger check")
        return false;
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






Java.perform(function(){
    console.log("success");
    var MainActivity = Java.use("sg.vantagepoint.uncrackable2.MainActivity");
    MainActivity.a.overload('java.lang.String').implementation = function(param){
        console.log(param);
    }
    // libfoo.so 모듈에서 strncmp 함수에 어떠한 값들이 들어가는지 봐야함
    
    Interceptor.attach(Module.getExportByName('libfoo.so','strncmp'),{
        onEnter: function(args){
            var param1 = args[0];
            var param2 = args[1];
            var param3 = args[2];

            if(param3 == 23 && (Memory.readUtf8String(param1) == '01234567890123456789012')){
                console.log('[+] param1 : ' + Memory.readUtf8String(param1));
                console.log('[+] param2 : ' + Memory.readUtf8String(param2));
            }
        }
    })

})
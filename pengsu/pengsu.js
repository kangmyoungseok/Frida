Java.perform(function(){
    var rootcheck = Java.use("com.hspace.pengsu.RootCheck");
    rootcheck.rootCheck.implementation = function(){
        console.log("[+] root check bypass");
        return false
    }

    setTimeout(function(){
        var MainActivity;
        Java.choose('com.hspace.pengsu.MainActivity',{
            onMatch: function(instance){
                console.log("[+] get MainActivity Instance");
                console.log("[+] oncreate score = " + instance.v.value);
                MainActivity = instance;
            },
            onComplete: function(){}
        })
    

        MainActivity.v.value = 100;
        console.log("[+] set score 100");    
        var random = Java.use("java.util.Random");
        random.nextInt.overload('int').implementation = function(args){
            console.log('[+] hooking the random class. return 0');
            return 0;
        }

        console.log("[+] Now Click the App");
    
        // c.b.a.a.a 에서 d함수를 호출하는 걸 보는 것
        // var aClass = Java.use('c.b.a.a.a');
        // aClass.d.implementation = function(arg1,arg2,arg3){
        //     console.log('arg1 : ' + arg1);
        //     console.log('arg2 : ' + arg2);
        //     var ret = this.d(arg1,arg2,arg3);
        //     var buffer = Java.array('byte', ret);
        //     console.log(buffer.length);
        //     var result = "";
        //     for(var i = 0; i < buffer.length; ++i){
        //         result+= (String.fromCharCode(buffer[i]));
        //     }
        //     console.log(result);
        //     return ret;
        // }
    
        var log = Java.use("android.util.Log");
        log.d.overload('java.lang.String','java.lang.String').implementation = function(tag,msg){
            console.log("[+] Log.d tag : " + tag);
            console.log("[+] Log.d msg : " + msg)
            var ret = this.d(tag,msg);
            return ret
        }
    
        // console.log(rootcheck.a());
        
    },3000);
    
})
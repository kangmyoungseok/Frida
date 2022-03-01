console.log("[*] start scripting");


Interceptor.attach(Module.findExportByName("libc.so","strncpy"),{
    onEnter: function(args){
        var param1 = Memory.readUtf8String(args[0]);
        console.log(param1);
        console.log(args[2]);
        if(args[2].toInt32() == 24){
            console.log(param1);
        }
    }
})

Interceptor.attach(Module.findExportByName("libc.so","strstr"),{
    onEnter: function(args){
        var param1 = Memory.readUtf8String(args[0]);
        if(param1.indexOf('frida') !== -1 || param1.indexOf('xposed') !== -1){
            this.ret = Boolean(1);
        }
    },
    onLeave: function(retval){
        if(this.ret){
            retval.replace(0);
        }
        return retval;
    }
})



Java.perform(function(){
    var MainActivity = Java.use("sg.vantagepoint.uncrackable3.MainActivity");
    MainActivity.showDialog.overload('java.lang.String').implementation = function(string){
        console.log("[+] hooking MainActivity.showDialog : " + string)
    }



})
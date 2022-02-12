import frida
import sys
def on_message(message,data):
    print(message)

jscode = """
Java.perform(function(){
  setTimeout(function(){
    console.log("setTimeout 함수 실행");
    var chall06Class = Java.use('uk.rossmarks.fridalab.challenge_06');
    Java.choose('uk.rossmarks.fridalab.MainActivity',{
      onMatch: function(instance){
        console.log("find the MainActivity Instance");
        instance.chall06(chall06Class.chall06.value);
        console.log("clear chall06");        
      },
      onComplete: function(){}
    })
  },1000);
});
"""
process = frida.get_usb_device(timeout=1).attach("fridalab")
script = process.create_script(jscode)
script.on("message",on_message)
script.load()

sys.stdin.read()
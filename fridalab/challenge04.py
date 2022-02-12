import frida
import sys

# Java.choose(className, callbacks): enumerate live instances of the className class by scanning the Java heap, where callbacks is an object specifying:

def on_message(message,data):
  print(message)

jscode = """
Java.perform(function(){
  var main;
  var MainActivityInstance = Java.choose('uk.rossmarks.fridalab.MainActivity',{
    onMatch: function(instance){
      main = instance
    },
    onComplete: function(){}
  })
  main.chall04("frida");

})
"""

session = frida.get_usb_device(timeout=3).attach("FridaLab")
script = session.create_script(jscode)
script.on("message",on_message)
script.load()
sys.stdin.read()
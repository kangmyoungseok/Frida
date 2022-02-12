import frida
import sys

# Java.choose(className, callbacks): enumerate live instances of the className class by scanning the Java heap, where callbacks is an object specifying:

def on_message(message,data):
  print(message)

jscode = """
Java.perform(function(){
  var main;
  Java.choose('uk.rossmarks.fridalab.MainActivity',{
    onMatch: function(instance){
      main = instance
    },
    onComplete: function(){}
  })
  main.chall02();

})
"""

session = frida.get_usb_device(timeout=3).attach("FridaLab")
script = session.create_script(jscode)
script.on("message",on_message)
script.load()

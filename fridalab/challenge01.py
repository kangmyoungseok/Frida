import frida
import sys

def on_message(message,data):
    print(message)
    
# static method 를 이용해서 그냥 바꾸기
jscode="""
Java.perform(function(){
    var chall01Class = Java.use('uk.rossmarks.fridalab.challenge_01');
    console.log(chall01Class.chall01.value);
    chall01Class.chall01.value = 1;    
})
"""

# 이렇게 인스턴스로 바꿔도 무방
jscode2 = """
Java.perform(function(){
    var RClass = Java.use('uk.rossmarks.fridalab.R$id');
    console.log(RClass.check.value)

})
"""

session = frida.get_usb_device(timeout=3).attach("FridaLab")
script = session.create_script(jscode2)
script.on("message",on_message)
script.load()
sys.stdin.read()

import frida
import sys

def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


jscode = """
Java.perform(function () {

  var MainActivity = Java.use('com.fireeye.flarebear.FlareBearActivity');
  var play = MainActivity.play;

  // Function to hook is defined here
  play.implementation = function (v) {

      // Show a message to know that the function got called
      send('play fn hooked');

      // define function to call instead of original play function
      var getState = MainActivity.getState.overload('java.lang.String', 'java.lang.String');
      var getStat = MainActivity.getStat;

      // call the getState function and send back the result
      var state = getState.call(this, 'activity', '');
      send("get activity shared preferences: " + state);
  };



});
"""


process = frida.get_usb_device().attach('com.fireeye.flarebear')

script = process.create_script(jscode)
script.on('message', on_message)

print('[*] tracing flarebar...')

script.load()
sys.stdin.read()

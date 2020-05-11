import frida
import sys

def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


jscode = """
Java.perform(function () {
  // Function to hook is defined here
  var MainActivity = Java.use('com.fireeye.flarebear.FlareBearActivity');

  var play = MainActivity.play;
  play.implementation = function (v) {

    // Show a message to know that the function got called
    send('play fn hooked');

    var setStateStr = MainActivity.setState.overload('java.lang.String', 'java.lang.String');
    var getStateStr = MainActivity.getState.overload('java.lang.String', 'java.lang.String');

    send("set activity shared prefs to calculated solution [8,2,4]");
    setStateStr.call(this, 'activity', 'ffffffffccpppp');

    send("get activity shared prefs: " + getStateStr.call(this, 'activity', ''));

    var getStat = MainActivity.getStat;

    send("getStat for value f: " + getStat.call(this, 'f'));
    send("getStat for value p: " + getStat.call(this, 'p'));
    send("getStat for value c: " + getStat.call(this, 'c'));

    var setState = MainActivity.setState.overload('java.lang.String', 'int');

    send("setting mass to 72");
    setState.call(this, 'mass', 72);

    send("setting happy to 30");
    setState.call(this, 'happy', 30);

    send("setting clean to 0");
    setState.call(this, 'clean', 0);

    var getState = MainActivity.getState.overload('java.lang.String', 'int');

    send("actual mass: " + getState.call(this, 'mass', 0));
    send("actual clean: " + getState.call(this, 'clean', 0));
    send("actual happy: " + getState.call(this, 'happy', 0));

    var isEcstatic = MainActivity.isEcstatic;
    send("is Ecstatic? " + isEcstatic.call(this));

    var getPassword = MainActivity.getPassword;
    send("password is: " + getPassword.call(this));

    var danceWithFlag = MainActivity.danceWithFlag;
    send("called danceWithFlag");
    danceWithFlag.call(this);

    // Call the original function
    //play.call(this, v);
  };



});
"""


process = frida.get_usb_device().attach('com.fireeye.flarebear')

script = process.create_script(jscode)
script.on('message', on_message)

print('[*] tracing flarebar...')

script.load()
sys.stdin.read()

NetAddr.langPort;

OSCFunc.trace(hideStatusMsg: true)

OSCFunc.trace(false)


s.boot;


// Using globals feels evil--maybe try to
// figure out a way around this.

f
d

// Receives and returns filepath from Python.
OSCdef.new(\filepath, {
	arg msg, time, addr, port;

	f = msg[1];

}, "/filepath")


// Receives and returns duration from Python.
OSCdef.new(\duration, {
	arg msg, time, addr, port;

	d = msg[1];

}, "/duration")


// Starts a new recording
OSCdef.new(\record, {
	arg msg, time, addr, port;

	if (msg[1].isKindOf(Boolean),
		{ //If val is a boolean
			if (msg[1] == true,
				{ // If val is true
					(
						Routine({
							"MADE IT".postln;
							s.record(path:f,duration:d);
					wait(0.02);
						}).play;
					)
				},
				{ // If val is false
					s.stopRecording;
				}
			)
		},
		{ // If val is not a boolean
			"FUCK".postln;
			Exception.throw("Unrecognized message; boolean input only.");
		}
	)

}, "/record");


ScampUtils.instrumentFromSynthDef(

	SynthDef("Valerie",{
		arg freq=640, volume=0.7, gate=0;
		var sig = SinOsc.ar(pitch);
		var env = EnvGate(gate:gate,fadeTime:0.1);
		Out.ar(0, sig * volume * env);
	});

);


s.freeAll
ScampUtils.startRecordingListener

(
OSCdef.new(\recordStart, {
	arg msg, time, addr, port;
	[msg,time,addr,port].postln;
}, "/recording/start");
)

(
OSCdef.new(\recordEnd, {
	arg msg, time, addr, port;
	[msg,time,addr,port].postln;
}, "/recording/end");
)

(
ScampUtils.instrumentFromSynthDef(
	SynthDef("Valerie",{
		arg pitch, volume=0.7, gate=0;
		var sig = SinOsc.ar(pitch);
		var env = EnvGate(gate:gate,fadeTime:0.1);
		Out.ar(0,sig * volume * env);
	})
)
)

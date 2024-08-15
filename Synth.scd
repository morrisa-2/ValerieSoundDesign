NetAddr.langPort;

OSCFunc.trace(hideStatusMsg: true)

OSCFunc.trace(false)

Routine({
	s.boot;


	// Using globals feels evil--maybe try to
	// figure out a way around this.

	f; // Filepath
	d; // Duration
	p = List.new(2); // Pitches
	r = List.new(2); // Rhythm
	v = SynthDef(\valerie, { |out, gate = 1,
	freq = 440, freqlag = 0.1, detun = 1.008, pan = 0,
	ffreq = 1200, ffreqMul = 3, ffreqDcy = 0.15, rq = 0.2,
	atk = 0.005, dcy = 0.2, sus = 0.6, rel = 0.1|

	// Voicer uses 'gate' for velocity
	var amp = Latch.kr(gate, gate).linlin(0, 1, 0.05, 0.25);

	var freqs = Lag.kr(freq, freqlag) * [1, detun];

	var filtEg = EnvGen.kr(Env([ffreqMul, ffreqMul, 1], [0, ffreqDcy], \exp), gate);
	var eg = EnvGen.kr(Env.adsr(atk, dcy, sus, rel), gate, doneAction: 2);

	var sig = SinOsc.ar(freqs).sum;

	sig = RLPF.ar(sig, (ffreq * filtEg).clip(20, 20000), rq);

	Out.ar(out, Pan2.ar(sig, pan, amp * eg));
});


	// Receives and returns filepath from Python.
	OSCdef.new(\filepath, {
		arg msg, time, addr, port;

		f = msg[1].asString;

	}, "/filepath");


	// Receives and returns duration from Python.
	OSCdef.new(\duration, {
		arg msg, time, addr, port;

		d = msg[1] + 0.5;

	}, "/duration");


	// Starts a new recording
	OSCdef.new(\record, {
		arg msg, time, addr, port;

		if (msg[1].isKindOf(Boolean),
			{ //If val is a boolean
				if (msg[1] == true,
					{ // If val is true
						(
							Routine({
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
				Exception.throw("Unrecognized message; boolean input only.");
			}
		)

	}, "/record");


	OSCdef.new(\initialize, {
		arg msg;

		if (msg[1].isKindOf(Boolean),
			{ // If val is a boolean
				if (msg[1] == true,
					{ // If val is true
						v.add;
					},
					{ // If val is false
						SynthDef.removeAt(\valerie);
					}
				)

			},
			{ // If val is not a boolean
				Exception.throw("Unrecognized message; boolean input only.");
			}
		)
	}, "/initialize");


	OSCdef.new(\pitches, {
		arg msg;

		for(1,msg.size-1){
			arg i;
			p.add(msg[i]);
		};
		p = Pseq(p,1).asStream;

	}, "/pitches");


	OSCdef.new(\rhythm, {
		arg msg;

		for(1,msg.size-1){
			arg i;
			/*e = msg[i] / TempoClock.default.tempo;
			e.postln;
			r.add(e);*/
			r.add(msg[i]);
		};
		r = Pseq(r,1).asStream;

	}, "/rhythm");


	OSCdef.new(\tempo, {
		arg msg;

		TempoClock.default.tempo = msg[1] / 60;

	}, "/tempo");


	OSCdef.new(\generate, {

		v = MonoPortaVoicer(1, \valerie);
		v.portaTime = 0.15;
		Routine({
			var dur, pitch;
			// Add a short silence before each recording.
			0.15.wait;
			while{
				dur = r.next;
				pitch = p.next;
				dur.notNil;
			} {
				arg i;
				v.trigger(pitch,dur);
				dur.wait;
				v.release(pitch);
			}
		}).play;

	}, "/generate");


	/*OSCdef.new(\debug, {
		arg msg;
		if(msg[1] == true,{
			// If val is true

		})
	}, "/debug");*/


}).play;



s.freeAll
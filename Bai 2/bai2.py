
import numpy as np
import wave
import struct

def create_and_save(file_name, freq):
    audio = []
    sampling_rate = 44100.0
    num_samples = 44100
    x = np.arange(num_samples)
    y = np.sin(2 * np.pi* freq * x / sampling_rate)

    # Open up a wav file
    wav_file=wave.open(file_name,"w")

    # wav params
    nchannels = 1

    sampwidth = 2

    nframes = len(audio)
    comptype = "NONE"
    compname = "not compressed"
    wav_file.setparams((nchannels, sampwidth, sampling_rate, nframes, comptype, compname))

    for sample in y:
        wav_file.writeframes(struct.pack('h', int( sample * 32767.0 )))

    wav_file.close()

    return
#main
freq_list = [440]
k = 1.05946309436 # 2 ** 1/12
for t in range(1,12) :

	freq_list.append(freq_list[t-1] * k)
        note_name =       ["A4.wav","A#4.wav","B4.wav","C5.wav","C#5.wav","D5.wav", "D#5.wav", "E5.wav", "F5.wav", "F#5.wav","G5.wav","G#5.wav"] 	   		
        freq_note = [[x, y] for x, y in zip (note_name, freq_list)]


for [filename, freq] in freq_note :
	 print("Creating" + filename)
	 print freq
	 create_and_save(filename, freq)
print ("Done")

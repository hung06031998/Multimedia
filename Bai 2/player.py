import simpleaudio as sa
from os import listdir
from os.path import isfile, join

files = [f for f in listdir(".") if isfile(f)]

file_name = input("Filename: ")
if file_name in files:
	if '.wav' in file_name :
		wave_obj = sa.WaveObject.from_wave_file(file_name)

		while True :
			play_obj = wave_obj.play()
			play_obj.wait_done()
	else :	
		print ("Invalid file extension !")
else :
	print ("File not found!")

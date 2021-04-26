"""
import speech_recognition as sr


def listen():
	r = sr.Recognizer()
	a = 0
	while(a != 1):
		with sr.Microphone() as source:
				 r.adjust_for_ambient_noise(source) #the program is taking out all the the ambient noise from around the mic
				 alive = 0
				 print('Please say something...') #this is printed to the consoul
				 audio = r.listen(source) #r is listening to the microphone
				 f = open("transcript.txt", "a") #creates a file called transcript unless one is already created
				 try:
					 print('\nTranscript will be provided shortly:\n')
					 transcript =  r.recognize_google(audio) #send the audio to google to be deciphered
					 print('User:' + transcript) #the program is done and is printing what you have
					 print("\nUser: " + transcript, file=f) #adds what was said to the transcript function
					 f.close() #closes the file and saves
				 except Exception as e:
					 print("Error: " + str(e))


"""
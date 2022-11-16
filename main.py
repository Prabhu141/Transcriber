import speech_recognition as sr

r = sr.Recognizer()

with sr.AudioFile('Bruce Lee.wav') as source:
    audio_text = r.listen(source)

    try:
        text = r.recognize_google(audio_text)
        print('converting audio transcripts into text.....')
        print(text)
    except:
        print('sorry.... run again........!!!!')



"""
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('speak Anything : ')
    audio_text = r.listen(source)
    print("Analyzing speech, Thanks")
  
  try:
    #text = r.recognize_google(audio)
    #print('You said : {}'.format(text))
    print("Text: "+r.recongnize_google(audio_text))
  except:
    print('sorry could not recognize your voice, please repeat  ')

"""


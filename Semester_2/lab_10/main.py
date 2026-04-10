import json, time
import pyttsx3, pyaudio, vosk
import requests
import webbrowser

class Speech:
    def __init__(self):
        self.tts = pyttsx3.init('sapi5')
        voices = self.tts.getProperty('voices')
        if voices:
            self.tts.setProperty('voice', voices[0].id)

    def text2voice(self, text):
        self.tts.say(text)
        self.tts.runAndWait()

class Recognize:
    def __init__(self):
        model = vosk.Model('vosk-model-small-en-us-0.15')
        self.record = vosk.KaldiRecognizer(model, 16000)
        self.stream()

    def stream(self):
        pa = pyaudio.PyAudio()
        self.stream = pa.open(format=pyaudio.paInt16,
                         channels=1,
                         rate=16000,
                         input=True,
                         frames_per_buffer=8000)

    def listen(self):
        while True:
            data = self.stream.read(4000, exception_on_overflow=False)
            if self.record.AcceptWaveform(data) and len(data) > 0:
                answer = json.loads(self.record.Result())
                if answer['text']:
                    yield answer['text']

def speak(text):
    speech = Speech()
    speech.text2voice(text)


word_data = {}
def info_word(word):
    global word_data
    try:
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        response = requests.get(url)
        data = response.json()
        word_data = data
        print(f"word({word_data[0]['word']}) saved")
    except:
        print(f"word({word}) not found")



rec = Recognize()
text_gen = rec.listen()
rec.stream.stop_stream()
speak('Starting')
time.sleep(0.5)
rec.stream.start_stream()


flag = 0
for text in text_gen:
    if text == 'close' or text == 'exit':
        speak('bb')
        quit()
    elif text[:5] == "find ":
        info_word(text[5:])
        flag = 1
    elif text == 'example' and flag != 0:
        for i in range(len(word_data[0]["meanings"])):
            if word_data[0]['meanings'][i]['definitions'][0].get('example') != None:
                print('example:', word_data[0]['meanings'][i]['definitions'][0].get('example'))
                break
            else:
                pass
    elif text == "sound" and flag != 0:
        print(word_data[0]['phonetics'][0]['audio'])
        rec.stream.stop_stream()
        speak(word_data[0]["word"])
        time.sleep(0.5)
        rec.stream.start_stream()
    elif text == 'save' and flag != 0:
        with open('save_words.txt', 'a') as file:
            file.write(word_data[0]['word'] + '\n')
        print("сохранено в 'save_words.txt'")
    elif text == "link" and flag != 0:
        webbrowser.open(f'{word_data[0]["phonetics"][0]["sourceUrl"]}')
        print(f'{word_data[0]["phonetics"][0]["sourceUrl"]}')
    else:
        print(f'команда не распознана({text})')
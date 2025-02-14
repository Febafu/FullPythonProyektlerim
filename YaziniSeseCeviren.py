import pyttsx3

def text_to_speech():
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech

    text = input("Enter text to speak: ")
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    text_to_speech()

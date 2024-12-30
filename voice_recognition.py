import speech_recognition as sr
# Библиотека, которая умеет читать текст вслух, используя встроенные в ОС голоса
import pyttsx3

# Инициализация голосового движка
engine = pyttsx3.init()
# set property - метод, позволяющий менять настройки голоса
# Скорость речи 150, чтобы она звучала комфортнее
engine.setProperty('rate', 150)
# Изменение голоса, если необходимо
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA'
                            '_11.0')

# Функция для преобразования текста в речь
def speak(text):
    # engine.say() только записывает текст в очередь воспроизведения
    engine.say(text)
    # engine.runAndWait() заставляет созданный выше движок выполнить все задачи, стоящие в очереди (в данном случае
    # озвучить текст)
    engine.runAndWait()

# Функция ничего не принимает, но возвращает текст, который распознала из речи пользователя или None, если что-то
# пошло не так
def listen():
    # sr.recognizer - объект из библиотеки Speech Recognition который отвечает за распознование речи
    recognizer = sr.Recognizer()
    # Использование микрофона
    with sr.Microphone() as source:
        print("Слушаю...")
        try:
            # Робот слушает с микрофона и ждет 10 секунд по их прошествии выдаёт ошибку если человек молчит
            audio = recognizer.listen(source, timeout=10)
            # recognizer.recognize_google(audio, language="ru-RU") отправляет записанный звук в сервис Google Speech
            # Recognition чтобы преобразовать его в текст
            query = recognizer.recognize_google(audio, language="ru-RU")
            # Выводит текст, который распознал робот в консоль
            print(f"Вы сказали: {query}")
            # Возвращает этот самый текст чтобы программа могла с ним дальше работать
            return query
        except sr.UnknownValueError:
            speak("Извините, я не понял. Повторите, пожалуйста.")
            return None
        except sr.RequestError:
            speak("Проблемы с подключением. Попробуйте позже.")
            return None

# Основной цикл
if __name__ == "__main__":
    speak("Привет! Чем я могу тебе помочь?")
    while True:
        command = listen()
        if command:
            if "привет" in command.lower():
                speak("Привет! Рад тебя слышать!")
            elif "стоп" in command.lower():
                speak("До встречи!")
                break
            else:
                speak("Извините, я пока этого не умею.")
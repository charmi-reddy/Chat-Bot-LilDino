# ────────────────────────────────────────────────────────────────
# Lil Dino 🦖 - Your Gentle Terminal Chatbot
# Author: Charmi Reddy
# Description: A calm, soft-spoken chatbot that chats with you in the terminal.
# Chat logs are saved, and Dino can even speak (gently!) using pyttsx3.
# ────────────────────────────────────────────────────────────────

from chatbot import ChatBot
import os
from datetime import datetime
from colorama import init, Fore, Style
import pyttsx3

# Initialize colorama and speech engine
init(autoreset=True)

LOG_FILE = "logs/chat_history.txt"

def log_message(sender, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:  #added encoding
        f.write(f"[{timestamp}] {sender}: {message}\n")


import re

def speak(text):
    engine = pyttsx3.init()

    for voice in engine.getProperty('voices'):
        if "zira" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break

    engine.setProperty('rate', 145)
    engine.setProperty('volume', 0.7)

    # Replace Dino with phonetic version
    text_for_speech = text.replace("Lil Dino", "Lil Die-no")

    # Strip emojis
    import re
    text_for_speech = re.sub(r'[^\x00-\x7F]+', '', text_for_speech)

    engine.say(text_for_speech)
    engine.runAndWait()



def main():
    bot = ChatBot("data/responses.json")
    greeting = greeting = "Hi, I’m Lil Dino 🦖! Type 'bye' to exit whenever you’re done chatting."
    print(Fore.CYAN + f"ChatBot: {greeting}")
    log_message("ChatBot", greeting)
    speak(greeting)

    while True:
        user_input = input(Fore.YELLOW + "You: " + Style.RESET_ALL)
        log_message("You", user_input)

        if user_input.lower() == "bye":
            farewell = "Bye! Have a nice day!"
            print(Fore.CYAN + f"ChatBot: {farewell}")
            log_message("ChatBot", farewell)
            speak(farewell)
            break

        response = bot.get_response(user_input)
        print(Fore.CYAN + "ChatBot:", response)
        log_message("ChatBot", response)
        speak(response)

if __name__ == "__main__":
    os.makedirs("logs", exist_ok=True)
    main()

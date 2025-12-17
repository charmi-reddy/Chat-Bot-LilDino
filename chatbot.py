import json
from utils.text_cleaner import clean_text

class ChatBot:
    def __init__(self, responses_path):
        with open(responses_path, 'r', encoding='utf-8') as f:
            self.responses = json.load(f)

    def get_response(self, user_input):
        cleaned_input = clean_text(user_input)

        for key in self.responses:
            if key in cleaned_input:
                return self._choose_response(self.responses[key])

        return self._choose_response(self.responses.get("default", ["I don't understand."]))

    def _choose_response(self, responses):
        import random
        return random.choice(responses)

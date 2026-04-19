import re
import random

def chatbot():
    print("CODSOFT Bot: Hi! I'm your AI assistant. Type 'bye' to exit.")
    
    # Dictionary of patterns and possible responses
    responses = {
        'greeting': {
            'patterns': [r'\b(hi|hello|hey)\b', r'good (morning|evening)'],
            'replies': [
                "Hello there! How can I help you today?",
                "Hi! Great to see you.",
                "Hey! What can I do for you?"
            ]
        },
        'how_are_you': {
            'patterns': [r'how are you', r'how\'s it going'],
            'replies': [
                "I'm just code, but I'm running great! How about you?",
                "All systems operational! You?",
                "Doing well, thanks for asking!"
            ]
        },
        'name': {
            'patterns': [r'your name', r'who are you'],
            'replies': ["I'm CODSOFT Bot, your rule-based assistant."]
        },
        'codsoft': {
            'patterns': [r'codsoft', r'internship'],
            'replies': [
                "CODSOFT internships help you learn and grow! Complete 3 tasks for your certificate.",
                "This CODSOFT AI internship is all about hands-on learning. You've got this!"
            ]
        },
        'help': {
            'patterns': [r'\bhelp\b', r'what can you do'],
            'replies': ["I can chat about greetings, my name, CODSOFT, or the weather. Try asking!"]
        },
        'thanks': {
            'patterns': [r'thank', r'thanks'],
            'replies': ["You're welcome! 😊", "Happy to help!", "Anytime!"]
        },
        'bye': {
            'patterns': [r'\b(bye|exit|quit)\b'],
            'replies': ["Goodbye! Thanks for chatting.", "See you later!", "Exiting... Good luck with your tasks!"]
        }
    }
    
    while True:
        user_input = input("You: ").lower().strip()
        matched = False
        
        for intent, data in responses.items():
            for pattern in data['patterns']:
                if re.search(pattern, user_input):
                    print(f"CODSOFT Bot: {random.choice(data['replies'])}")
                    matched = True
                    if intent == 'bye':  # exit after saying goodbye
                        return
                    break
            if matched:
                break
                
        if not matched:
            print("CODSOFT Bot: Hmm, I didn't get that. Try 'help' to see what I can talk about.")

if __name__ == "__main__":
    chatbot()
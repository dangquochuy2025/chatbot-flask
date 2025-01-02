import random

def get_response(user_message):
    user_message = user_message.lower()

    # Các câu trả lời với nhiều câu trả lời chi tiết hơn
    responses = {
        "hi": ["Hello!", "Hi there! How's it going?", "Hey! How can I assist you today?"],
        "how are you": [
            "I'm doing great, thanks for asking! How about you?",
            "I'm fine, just a bit busy being your chatbot. How are you?",
            "I'm good! Feeling digital and ready to help you."
        ],
        "what is your name": [
            "I am your friendly chatbot, at your service!",
            "I don't have a name, but you can call me whatever you like.",
            "I go by many names, but today I am Chatbot!"
        ],
        "bye": ["Goodbye! Hope to chat with you soon.", "See you later! Take care!", "Goodbye, come back if you need me!"],
        "thank you": [
            "You're welcome! I'm always here to help!",
            "No problem! It's my pleasure.",
            "Anytime! Let me know if you need anything else."
        ],
        "how old are you": [
            "I don't really have an age, but I was created to help you anytime!",
            "Age is just a number, especially for a chatbot like me!",
            "I'm ageless, existing only in the digital world!"
        ],
        "what is your favorite color": [
            "If I could see colors, I think I'd like blue or green!",
            "I don't have favorites, but blue sounds nice, don't you think?",
            "I imagine I would love all colors, but blue feels like the perfect one."
        ],
        "tell me a joke": [
            "Why don't skeletons fight each other? They don't have the guts!",
            "Why did the computer go to the doctor? Because it had a virus!",
            "Why don't programmers like nature? It has too many bugs!"
        ],
        "what can you do": [
            "I can chat with you, tell jokes, assist with programming, and much more!",
            "I can help you with basic tasks, answer questions, and even entertain you with some fun facts!",
            "Need help? I'm here to assist with coding, jokes, or just to chat!"
        ],
        "default": [
            "Sorry, I didn't understand that. Could you try asking something else?",
            "I didn't get that. Can you ask again in a different way?",
            "Hmm, that's a bit too complicated for me. Can you rephrase it?"
        ]
    }

    # Tìm kiếm câu trả lời từ danh sách câu trả lời
    for key in responses:
        if key in user_message:
            return random.choice(responses[key])

    # Nếu không tìm thấy, trả về câu mặc định
    return random.choice(responses["default"])

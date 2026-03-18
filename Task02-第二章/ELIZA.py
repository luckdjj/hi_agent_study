import re
import random

# 1. 代词转换字典：将用户输入中的第一人称转为第二人称 
REFLECTIONS = {
    "am": "are",
    "was": "were",
    "i": "you",
    "i'd": "you would",
    "i'm": "you are",
    "i'll": "you will",
    "my": "your",
    "are": "am",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

# 2. 规则库：包含分解规则（模式）和重组规则（回应） 
# 格式：(正则表达式模式, [回应列表])
RULES = [
    (r'I need (.*)', [
        "Why do you need {0}?",
        "Would it really help you to get {0}?",
        "Are you sure you need {0}?"
    ]),
    (r'Why don\'t you (.*)', [
        "Do you really think I don't {0}?",
        "Perhaps eventually I will {0}.",
        "Do you really want me to {0}?"
    ]),
    (r'I am (.*)', [
        "Is it because you are {0} that you came to me?",
        "How long have you been {0}?",
        "How do you feel about being {0}?"
    ]),
    (r'Are you (.*)', [
        "Why does it matter whether I am {0}?",
        "Would you prefer it if I were not {0}?",
        "Perhaps you believe I am {0}."
    ]),
    (r'Because (.*)', [
        "Is that the real reason?",
        "What other reasons come to mind?",
        "Does that reason explain anything else?"
    ]),
    (r'(.*) mother (.*)', [
        "Tell me more about your mother.",
        "How was your relationship with your mother?",
        "How do you feel about your mother?"
    ]),
    (r'quit', [
        "Thank you for talking with me. Goodbye!",
        "Good-bye.  That will be $150.  Have a good day!"
    ]),
    (r'(.*)', [
        "Please tell me more.",
        "Let's change the focus a bit... tell me about your family.",
        "Can you elaborate on that?",
        "Why do you say that?"
    ])
]

def reflect(fragment):
    """进行代词转换 """
    tokens = fragment.lower().split()
    return " ".join([REFLECTIONS.get(token, token) for token in tokens])

def analyze_input(user_input):
    """核心算法：模式匹配与替换 [cite: 17, 18]"""
    for pattern, responses in RULES:
        match = re.match(pattern, user_input, re.IGNORECASE)
        if match:
            # 随机选择一个重组规则 
            response = random.choice(responses)
            # 获取捕获组并进行代词转换 [cite: 17, 18]
            if '{0}' in response:
                captured_groups = reflect(match.group(1))
                return response.format(captured_groups)
            return response

# 模拟交互循环
print("ELIZA: Hello. How are you feeling today?")
while True:
    user_val = input("YOU: ")
    if user_val.lower() == 'quit':
        print(f"ELIZA: {analyze_input('quit')}")
        break
    print(f"ELIZA: {analyze_input(user_val)}")
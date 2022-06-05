from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?", ]
    ],
    [
        r"(.*) your name ?",
        ["My name is SoftUni BOT, but you can just call me robot and I'm a chatbot .", ]
    ],
    [
        r"what is python(.*) ?",
        ["Phyton is an interpreted, object-oriented, high-level programming language"]
    ],
    [
        r"i'm (.*) (good|well||okay|ok)",
        ["Nice to hear that, how can I help you?"]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there", ]
    ],
    [
        r"(.*)created(.*)",
        ["Mario Zahariev created me using Python's NLTK library "]
    ],
    [
        r"(.*) (location|city)",
        ['Sofia, Bulgaria', ]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :)", "It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['That is nice to hear']
    ],
]


print("Please type lowercase English language to start conversation. "
      "Type quit to leave. \n\n Hi, I'm SoftUni BOT...\nWhat is your name?")

chat = Chat(pairs, reflections)

chat.converse()
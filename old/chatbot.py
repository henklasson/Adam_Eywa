from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot(
    'Norman',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
    )

stock = "BIG_BAD_BULLY"

trainer = ListTrainer(chatbot)
for training in range(10):
    trainer.train([
        'Hi!',
        'Hello, How are you?',
        'I am good.',
        'That is good to hear.',
        'Thank you',
        'You are welcome.',
    ])

    trainer.train([
        'How are my stocks doing?',
        f'Your current holings are, {stock}, META and Adam, They are all up 5%',
        'Great, thanks for the update',
    ])

    trainer.train([
        'Hello',
        'Hi! What can i do for you today?',
        'What is your name?',
        'My name is Adam, what is your name?',
        'My name is Henrik',
        'Cool, I\'ll try to remember that',
    
    ])

    
trainer = ChatterBotCorpusTrainer(chatbot)
for training in range(100):
    trainer.train(
        "chatterbot.corpus.english.greetings"
    )
    
    trainer.train(
        "chatterbot.corpus.english.conversations"
    )
    
    

    
face_detected = False
while not face_detected:
    camera = input("Face yes or no: ")
    if camera.lower()=="yes":
        face_detected = True



while face_detected:   
    try:
        bot_input = chatbot.get_response(input())
        print(bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
       break
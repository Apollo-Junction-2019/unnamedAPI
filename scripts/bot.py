from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("Apollo", read_only=True)
chatbot.storage.drop()
trainer = ListTrainer(chatbot)

trainer.train([
    'Hi',
    'Hello to you too ',
    'How are you?',
    'I am good, how are you?',
    'That is good to hear.',
    'Thank you',
    'You are welcome.',
])
trainer.train([
    'instagram',
    ''
])
trainer.train([
    'ssl',
    'Oh, you want to know something about https? Checkout https://en.wikipedia.org/wiki/HTTPS !',
    'https',
    'Oh, you want to know something about https? Checkout https://en.wikipedia.org/wiki/HTTPS !',
])
trainer = ChatterBotCorpusTrainer(chatbot)

while True:
    try:
        bot_input = chatbot.get_response(input())
        print(bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break

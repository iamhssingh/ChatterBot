# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.storage import ArangoStorageAdapter


bot = ChatBot(
    'Terminal',
    storage_adapter='chatterbot.storage.ArangoStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    filters=[
        'chatterbot.filters.RepetitiveResponseFilter'
    ],
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    username='vitarthabot',  # Enter user name here (required)
    password='vitartha@123',  # Enter password here (required)
    database='vitartha',  # Enter database name here (default: chatterbot-database)
    collection='statements',  # Enter collection name here (default: statements)
    host='localhost',  # Enter host name (default: localhost)
    port='8529',  # Enter port name (default: 8529)
    protocol='http',  # Enter protocol name (default: http)
    logging=True  # Enter logging condition (default: True)
)

bot.set_trainer(ListTrainer)
bot.train(["Hi",
           "Hello Sir",
           "How may I help you?",
           "Planning to Invest money",
           "Sir Where would you like to Invest?",
           "Just saw your advertisement on Mutualfundsahihai",
           "Sir at beginning everyone feels fear and confused in investing money",
           "But how much safe is the mutual fund",
           "By patience everyone learns to make money work",
           "What is the guarantee of the money?",
           "Guarantee of your expectation is always on the market risk. We can assure you the atmost growth of your money",
           "How much money you are planning to invest?",
           "As I am just starting it would be 5K",
           "Sir is it for a month or year?",
           "It will be for a month",
           "Sir how you want your money working?, What do you expect from your investment?",
           "It should have growth and neither willing to lose",
           "Sir you want to play safe?",
           "Probably Yes but also it should have fast growth rate",
           "My suggestion for you will be SIP and balanced fund",
           "What is SIP?",
           "Sir SIP is systematic Investment Planning",
           "Tell me more about it and what should I know",
           "SIP swirls around with market risk as this is investing money monthly,yearly till you need it, Simply it is smart planning of risk and growth"
           "How would you explain me the balance fund?"
           "Balanced fund is nothing but rather than investing in one we invest in different company",
           "How much will be the return of investment?",
           "The investment shall be in many varying methods you would get about 11 to 12 per cent of return on SIP",
           "What if I want higher return?"
           "For investment in balanced funds it will be more than 18 per cent and it will be stocks and bonds which sometime is a slight risk if you are not willing to take one",
           "Hmm. Where should I invest the money?"
           "So Sir where you would like to invest the money? Low risk average return or High risk More return?",
           "I would first try with good and safe returns so I would go with SIP",
           "But if I want my money after one or two years then?",
           "No problem sir,you have to apply for it and you will get it within 2 days of time",]
          )

print('Type something to begin...')

while True:
    try:
        bot_input = bot.get_response(None)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break

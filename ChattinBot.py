import datetime 
import random 

def greet_user():
    greetings = ["Hi!", "Hello!", "Hey there!", "Namaste!", "Welcome!"]
    return random.choice(greetings)

def get_time():
    now = datetime.datetime.now()
    return now.strftime("The Time is %I:%M %p.")

def get_date():
    today = datetime.date.today()
    return today.strftime("Today's Date is %B %d, %Y.")

def tell_joke():
    jokes = [
        "Why don't Scientist trust atoms ? Because they made up everything!", 
        "Why did the Computer go to therapy ? It had too many Bytes.", 
        "What do you call a bear with no teeth? A gummy Bear!"
             ]
    return random.choice(jokes)

def tell_fact():
    facts = [
        "A cloud weighs around a million tonnes.",
        "Identical twins don’t have the same fingerprints.",
        "Giraffes are 30 times more likely to get hit by lightning than people.",
        "The largest piece of fossilised dinosaur poo discovered is over 30cm long and over two litres in volume",
        "The Universe's average colour is called 'Cosmic latte'.",
        "Animals can experience time differently from humans.",
        "Water might not be wet. This is because most scientists define wetness as a liquid’s ability to maintain contact with a solid surface, meaning that water itself is not wet, but can make other objects wet.",
        "A chicken once lived for 18 months without a head.",
        "Wearing a tie can reduce blood flow to the brain by 7.5 per cent",
        "The fear of long words is called Hippopotomonstrosesquippedaliophobia"
    ]
    return random.choice(facts)
    

def respond(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return greet_user()
    elif "time" in user_input :
        return get_time()
    elif "date" in user_input:
        return get_date()
    elif "joke" in user_input:
        return tell_joke()
    elif "fact" in user_input:
        return tell_fact()
    elif "bye" in user_input:
        return "Goodbye! Have a Great Day!"
    else :
        return "Sorry , I didn't understand that. Can you ask something else? "
    
print("🤖 Chatbot : Hello! Ask me something.")
while True :
        user_input = input("You:")
        response = respond(user_input)
        print("🤖 Chatbot : " , response)

        if "bye" in user_input.lower():
            break
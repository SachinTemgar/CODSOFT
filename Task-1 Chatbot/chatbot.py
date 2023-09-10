from datetime import datetime

def Function_forInput(Input_user):

    # converting user input to lowercase
    Input_user = Input_user.lower()
    
    if Input_user in ['hello', 'hii', 'hi', 'hey']:
        response = 'Hello sir/Madam'

    elif Input_user in ['who are you','what is your name?', 'what is your name', 'whats your name?', 'what is your name','your name','who are you']:
        response = 'I am a simple chatbot. And My name is MAXX. I can try and answer some of your Questions.'

    elif Input_user in ['how are you?', 'how are you']:
        response = 'I am fine, thank you for asking. How are you ?'

    elif Input_user in ['good', 'well', 'fine', 'happy']:
        response = "That's fantastic."

    elif Input_user in ['bye', 'good bye','goodbye']:
        response = 'Goodbye! Have a wonderful day!'

    elif Input_user in ['thankyou','thank you','thanks you']:
        response = "Your're Welcome"

    elif Input_user in ['what time is it', 'what time is it?','time','time?','what is the time']:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        response = f'The time is {current_time}.'

    elif Input_user in ['what is the date today?', "what is today's date","today's date",'date?',"today's date?",'what is todays date','what is the date','what is the date today']:
        now = datetime.now()
        current_date = now.strftime("%Y-%m-%d")
        response = f'Today\'s date is {current_date}.'

    elif Input_user in ['what day is it today?', "what day today is","what day today is?",'todays day',"today's day?",'what is todays day','todays day','what day is today','what day is it today']:
        now = datetime.now()
        current_day = now.strftime("%A")
        response = f'Today is {current_day}.'

    elif Input_user in ["how is today's weather", 'what is the weather like',"today's weather",'todays weather','how is todays weather']:
        response = "I'm sorry, but I'm not able to provide weather information."

    elif Input_user in ['which languages can you speak','which languages do you speak?','which languages can you speak?','which language can you speak']:
        response = "I speak only English language"

    elif Input_user in ['who made you?','who made you']:
        response = 'The Name of my Creator is SACHIN'

    elif Input_user in ['tell me a joke','can you tell me a joke']:
        response = "What's an egg's favorite vacation spot? New Yolk City"

    elif Input_user in ['suggest a book','do you like books','can you suggest me a book']:
        response = "Zero to One: Peter theil"

    elif Input_user in ['suggest a movie','do you like movies']:
        response = "Dark Knight"

    elif Input_user in ['are you a robot',"are you a robot?", "am I talking to a chatbot?", "are you a real person?", "am I talking to a chatbot?"]:
        response = 'I am a simple chatbot.'

    else:
        response = "I apologise for not understanding your query. Could you please redo it?"
    
    # returning the response
    return response

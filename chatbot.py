import random
print('Hello, I am Phoebe ! let us chat, If u feel boring or like to stop type -bye/stop')
while True:
    x=input(); x=x.lower()
    if x=='stop' or x=='bye': print('good bye');break
    y=x.split()
    if len(y)==0:print('please say something')
    elif x[-1]=='?':print('why do you ask that')
    elif 'hello' in y or 'hi' in y :print('hello,Good day')
    elif 'goodmorning' in y or 'morning' in y:print('Wishing for a very good morning')
    elif 'how' and 'are' and 'you' in y: print('doing excellent')
    elif 'thankyou' in y or 'thanks' in y : print('Always welcome')
    elif 'joke'in y or 'jokes' in y: print('i am bad at telling and getting jokes')
    elif 'goodnight' in y or 'night' in y: print('good night and sweet dreams')
    elif 'mother' in y:print('Tell me more about your mother')
    elif 'father' in y: print('Tell me more about your father')
    elif 'love' in y:print('Love is an emotion not known to me')
    elif 'music' in y:print('I love all genres of music')
    elif 'repeat' in y: print('repetition is not creative')
    elif 'friend' in y:print('Friend in need is a friend indeed')
    elif 'sun' in y:print('sun is the source of all energy')
    elif 'age' in y: print(random.choice(['I am ageless !','age is just a number']))
    elif 'colors' in y: print('what a colorful question !')
    elif 'rain' in y or 'rainining' in y: print('I know that most humans love rain, but I cant stand in it')
    elif 'dance'in y or 'dancing' in y: print('I love dancing even if i dont know to ')
    elif y[0]=='i' and y[1]=='feel' : print('what makes you feel so?')
    else: print('go on')
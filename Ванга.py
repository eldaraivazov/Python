from random import randint
question = input('Введіть ваше питання та натисніть Enter:  ')
b =(randint(0,10000+1))
if(2500<b<=5000):
    print('Так')
elif(b<=2500):
    print('Так,безсумнівно!')
elif(7500>=b>5000):
    print('Ні')
elif(b>7500):
    print('Ні, навіть не думай!')
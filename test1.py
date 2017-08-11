import random
print ('Привет Арслан это игра называется отгодай число')
print ('хотя ты и сам занешь ведь ты же ее создал')
print ('итак правила просты надо отгадать число при минимальном кооличестве попыток')
number = random.randint(1,100) 
guess = int(input ('а ну введи ка ты число братка: '))
popitka = 1
while guess != number:
    if  guess> number:
        print("Меньше")
    else:
        print('больше')
    guess = int(input('вводи давай: '))   
    popitka += 1
print('Поздравляю ты угадал число')    
print('количество попыток -', int(popitka))


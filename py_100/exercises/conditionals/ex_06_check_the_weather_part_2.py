import random
weather_list = ['sunny', 'rainy', 'snowy', 'windy', 'smoggy']
weather = weather_list[random.randint(0,len(weather_list)-1)]

match weather:
    case 'sunny':
        print("It's a beautiful day!")
    case 'rainy':
        print('Grab your umbrella.')
    case 'snowy':
        print('Put on a coat.')
    case 'windy':
        print('I feel a draft.')
    case _:
        print("Let's stay inside.")

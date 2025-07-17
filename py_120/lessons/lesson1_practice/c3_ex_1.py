class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0
        self.on = False
    
    def engine_on(self):
        if not self.on:
            self.on = not self.on
            print(f"The {self.model} comes to life as its engine starts.")
        else:
            print(f"The {self.model}'s engine whines as the ignition is engaged, but the engine is already running")

    def accelerate(self):
        print(f"The {self.model} accelerates slightly.")
        self.speed += 1
        self.current_speed()

    def brake(self):
        if self.speed > 0:
            print(f"As you brake, your seatbelt pushes against you and the {self.model} slows down.")
                    
            self.speed -= 1
            self.current_speed()
        else:
            print(f"You brake and the {self.model} remains motionless.")

    def engine_off(self):
        if self.on:
            if self.speed > 0:
                print(f"The {self.model}'s engine shuts off and you slowly roll to a halt.")
                self.speed = 0
                self.on = not self.on
            else:
                print(f"The {self.model} rests as its engine stops.")
                self.on = not self.on
        else: 
            print(f"The {self.model}'s engine is already off")

    def current_speed(self):
        print(f"The {self.model}'s current speed is {self.speed} mph.")

while True:
    print("You're testing out cars today.")
    model = input('Which model would you like to try first? ').capitalize()
    year = input('Which year are you interested in? ')
    color = input('Which color? ').capitalize()
    test_vehicle = Car(model, year, color)

    print("You're in the vehicle on a straight test road. What do you do?")
    print("(1) start engine, (2) accelerate, (3) brake, (4) stop engine")

    while True:
        while True:
            action = input('').lower()

            match action:
                case '1' | 'start' | 'start engine' | 'on':
                    test_vehicle.engine_on()
                case '2' | 'accelerate' | 'gas' | 'speed up':
                    test_vehicle.accelerate()
                case '3' | 'brake' | 'slow down':
                    test_vehicle.brake()
                case '4' | 'stop' | 'stop engine' | 'off':
                    test_vehicle.engine_off()
                case _:
                    print("Invalid input. You may do one of the following: 1) start engine, 2) accelerate, 3) brake, 4) stop engine")
                    continue
            break
        if not test_vehicle.on:
            break

    if input("Do you want to drive another car? (y/n)").lower() != 'y':
        print('Thank you for driving with us! Goodbye!')
        break
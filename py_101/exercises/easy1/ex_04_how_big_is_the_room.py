def prompt(text):
    print(f'>> {text}')

prompt('Which measurement type should be used? 1) feet, 2) meters')
measurement_type = input()

if measurement_type == '1':
    prompt('Enter the length of the room, in feet.')
    length = input()

    prompt('Enter the width of the room, in feet.')
    width = input()

    area_ft2 = float(length) * float(width)
    area_m2 = area_ft2 / 10.7639
    

    print(f'Area of the room is {area_ft2:.2f} square feet ({area_m2:.2f} square meters).')
else:
    prompt('Enter the length of the room, in meters.')
    length = input()

    prompt('Enter the width of the room, in meters.')
    width = input()

    area_m2 = float(length) * float(width)
    area_ft2 = area_m2 * 10.7639

    print(f'Area of the room is {area_m2:.2f} square meters ({area_ft2:.2f} square feet).')

user_pet_type = input('Enter your animal >>>').strip(' ,.^*@%$&!_-=+1234567890').lower()
user_pet_name = input('Enter your animal name >>>').strip(' ,.^*@%$&!_-=+1234567890').title()

your_animal_dog = False

if user_pet_type == 'dog':
    your_animal_dog = True

if  your_animal_dog:
    print('\U0001F415')

your_animal_dog = False

if user_pet_type == 'dog':
    your_animal_dog = True

if  your_animal_dog:
    print('I_am_afraid_of_dogs')

your_animal_cat = False

if user_pet_type == 'cat':
    your_animal_cat = True

    if your_animal_cat:
        print('\U0001F408')

your_animal_cat = False

if user_pet_type == 'cat':
    your_animal_cat = True

    if your_animal_cat:
        print('cat_catches_mice')

your_animal_fish = False

if user_pet_type == 'fish':
    your_animal_fish = True

    if your_animal_fish:
        print('\U0001F41F')
your_animal_fish = False

if user_pet_type == 'fish':
    your_animal_fish = True

    if your_animal_fish:
        print('Do_not_cook_homemade_fish')

your_animal_hamster = False

if user_pet_type == 'hamster':
    your_animal_hamster = True

    if your_animal_hamster:
        print('\U0001F439')

your_animal_hamster = False

if user_pet_type == 'hamster':
    your_animal_hamster = True

    if your_animal_hamster:
        print('Hamsters are very small')

your_animal_turtle = False

if user_pet_type == 'turtle':
    your_animal_turtle = True

    if your_animal_turtle:
        print('\U0001F422')

your_animal_turtle = False

if user_pet_type == 'turtle':
    your_animal_turtle = True

    if your_animal_turtle:
        print('The turtle has a strong shell')

your_animal_swim = False

if user_pet_type == 'turtle' or user_pet_type == 'fish':
    your_animal_swim = True

if your_animal_swim:
    print('You must buy aquarium')

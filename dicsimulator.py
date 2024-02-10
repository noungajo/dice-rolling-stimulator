import random
from face_print import faces


repeat_again = 'y'
#looping
while repeat_again == 'y':
    #developping a random number
    random_number = random.randint(1,len(faces))
    #check the number
    # Imprimer le visage correspondant au nombre aléatoire généré
    print("\n".join(faces[random_number - 1]))  # Soustrayez 1 car les indices commencent à partir de 0

    repeat_again = input("Do you want to continue ? y/n ")
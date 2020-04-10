zoo = ("okapi", "duiker", "tapir", "bongo", "red river hog", "eland", "springbok", "bontebok", "rhino", "giraffe")

print(zoo.index("tapir"))

animal_to_find = "pudu"
if animal_to_find in zoo:
    print(f"The {animal_to_find} is safe and sound")
else: 
    print(f"The {animal_to_find} has escaped!")

(animal1, animal2, animal3, animal4, animal5, animal6, animal7, animal8, animal9, animal10) = zoo

print(animal1)

zoo_list = list(zoo)

print(zoo_list)

zoo_list.extend(["sitatunga", "pudu", "kudu"])

print(zoo_list)

zoo_tuple = tuple(zoo_list)

print(zoo_tuple)






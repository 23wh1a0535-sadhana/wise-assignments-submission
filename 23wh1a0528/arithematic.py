initial_number = 25
progression = [initial_number]

for _ in range(4):  # Adjust the range to change the number of terms in the progression
    initial_number += random.randint(1, 10)
    progression.append(initial_number)

print("Random Arithmetic Progression:",
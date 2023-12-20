#Problem 2
#Take any four-digit number, using at least two different digits (leading zeros are allowed).
#Arrange the digits in descending and then in ascending order to get two four-digit numbers,adding leading zeros if necessary.
#Subtract the smaller number from the bigger number.
#Go back to step 2 and repeat. This process stops after a few steps, that is step 3 produces the same number. 
#DO this with paper and pen to understand the same Start with 1945
#9541–1459=8082
#8820–0288=8532
#8532–2358=6174
#7641–1467=6174
#Given a suitable starting number generate the sequence. It should not repeat; that is it should stop before the repetition.
#For example if 1945 is input it should return [1945,8082,8532,6174]


def sequence(starting_number):
    seq = [starting_number]

    while True:
        descending_number = int(''.join(sorted(str(starting_number), reverse=True)).lstrip('0'))
        ascending_number = int(''.join(sorted(str(starting_number))).lstrip('0'))

        result = descending_number - ascending_number
        seq.append(result)

        if result == seq[-2]:  # Check for repetition
            break

        starting_number = result

    return seq

result_sequence = sequence(1945)
print(result_sequence)

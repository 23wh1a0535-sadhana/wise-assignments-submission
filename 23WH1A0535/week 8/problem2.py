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

# Example usage with starting number 1945
result_sequence = sequence(1945)
print(result_sequence)

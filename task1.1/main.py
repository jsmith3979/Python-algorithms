#rules:
# • it must include at least one element from each category;
# • it must start with letters (capital or lower-case);
# • it must not include more than two capital letters;
# • it must not include more than two special symbols.

import random
import time
start_time = time.time()
def has_at_least_one_capital(word):
    return any(char.isupper() for char in word)


def has_two_capitals(word):
    count = sum(1 for char in word if char.isupper())
    return count == 2


def generate_passwords(length):
    digits = ['1', '2', '3', '4', '5']
    special_symbols = ['$', '&', '%']
    letters = ['a', 'b', 'c', 'd', 'e', 'A', 'B', 'C', 'D', 'E']
    chosen_letters = []
    num_digits = random.choice([1, 2])
    num_symbols = random.choice([1, 2])

    for _ in range(1000000):
        # randomly selects two elements from letters array
        while True:
            random_letters = random.sample(letters, k=2)

            # Check if both letters are uppercase
            if all(letter.isupper() for letter in random_letters):
                # print("Randomizing again because all letters are uppercase.") # Exit the loop if both letters are uppercase
                continue
            else:
                break
        # print(random_letters)

        # randomly selects a digit from 1 to 2
        if num_digits == 1:
            dig = random.choice(digits)
        else:
            dig = ''.join(random.choices(digits))

        sym_count = random.choice([1, 2])
        sym = ''.join(random.sample(special_symbols, k=min(sym_count, len(special_symbols))))
        last_item = [sym].pop()
        split_parts = list(last_item)
        random_letters.extend([dig])
        random_letters.extend(split_parts)

        # print(len(random_letters))

        if len(random_letters) > length:
            random_letters.pop()
        # print(random_letters)

        while True:
            remaining_length = length - len(random_letters)
            # print("start")
            # print(len(random_letters))
            # print(length)
            # print(remaining_length)

            rest_characters = [random.choice(letters + digits) for _ in range(remaining_length)]
            # rest_characters = [random.choice(letters + digits) for _ in range(remaining_length)]
            # print("rest")
            # print(random_letters)
            # print(rest_characters)
            combined = random_letters + rest_characters
            # print(combined)
            # print(random_letters.extend(rest_characters))

            # Check if there are at least two uppercase letters in rest_characters
            if sum(char.isupper() for char in combined) >= 2:
                # print("Randomizing again because there are too many uppercase letters.") # Exit the loop if there are at least two uppercase letters
                continue
            else:
                break
        # print(rest_characters)

        components = rest_characters
        random.shuffle(components)
        combined = ''.join(random_letters + components)


        # checks if random_letters do not have duplicates in the array and whether there is more than 1 capital letter and has at least 1 capital letter; if these demands are not met, they won't get appended
        if combined not in chosen_letters and has_at_least_one_capital(combined) and not has_two_capitals(combined):
            chosen_letters.append(combined)
        else:
            if has_two_capitals(combined):
                # print(f"{combined} has two capital letters and will not be added.")
                continue
            elif not has_at_least_one_capital(combined):
                # print(f"{combined} does not have at least one capital letter and will not be added.")
                continue
            else:
                # print(f"{combined} already exists in the array.")
                continue

    print(chosen_letters)
    print(len(chosen_letters))
    end_time = time.time()
    print("Runtime:", end_time - start_time, "seconds")


# Example: Call the function with a specific length (e.g., 8)
while True:
    user_input = int(input("Enter the length of the passwords, it must be more than 4: "))
    if user_input < 4:
        print("Enter a length higher than 3: ")
    else:
        break




generate_passwords(user_input)



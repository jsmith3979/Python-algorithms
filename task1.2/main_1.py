from collections import Counter
def find_letters_until_duplicate(file_name):

    with open(file_name, 'r') as file:
        content = file.read()
        current_len = []
        max_len = []

    for i in range(len(content)):
        for char in content[i:]:

            current_len.append(char)
            char_counts = Counter(current_len)

            count_at_least_2 = sum(1 for count in char_counts.values() if count > 1)

            if count_at_least_2 > user_input:
                current_len.pop()
                break
            print("new substring: ",current_len)


        if len(current_len) > len(max_len):
            max_len.clear()
            max_len.extend(current_len)
            current_len.clear()
        else:
            current_len.clear()
    print("max length: ",max_len)


user_input = int(input("Enter K length: "))

while user_input > 10:
    user_input = int(input("Enter K length: "))
file_name = "letters.txt"
result = find_letters_until_duplicate(file_name)
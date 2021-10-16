def run():
    print("Please enter a word")
    user_word = input()
    count = 0
    for position in range(0, len(user_word), 1):
        count = count + 1
    print(count)

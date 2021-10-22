#function to display certain number of chars
def display_chars(file_path, characters):
    with open(file_path) as file:
        data = file.read(characters)
        print(data)


#function to display first line

def display_line(file_path):
    with open(file_path) as file:
        data = file.readline()
        print(data)

#function to display all the text

def display_text(file_path):
    with open(file_path) as file:
        data = file.read()
        print(data)


def run():
    display_chars("library.txt", 5)
    print()
    display_line("library.txt")
    display_text("library.txt")

if __name__ == "__main__":
    run()
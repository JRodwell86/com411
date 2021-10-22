def display_chars(file_path, characters):
  with open(file_path) as file:
    letters = file.read(characters)
    print(letters)


display_chars("library.txt", 5)


def display_line(file_path):
  with open(file_path) as file:
    firstline = file.readline()
    print(firstline)


display_line("library.txt")


def display_text(file_path):
  with open(file_path) as file:
    data = file.read()
    print(data)


display_text("library.txt")

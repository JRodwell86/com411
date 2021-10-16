#ask user to enter number of mountains
def run():
   print("How many mountains should I display?")
   mountains = int(input())
   print(f"{mountains}")
   print("Displaying...")
   #display mountains
   for count in range(mountains):
      print("  ♦")
      print(" ♦  ♦")
      print("♦    ♦")


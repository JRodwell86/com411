import json

def read(file_path):

  with open(file_path) as file:
    data = json.load(file)
    # display the name of the city
    city = data["city"]
    print(f"City Name: is: {city}")
    # display the population size
    population = data["population"]
    print(f"Population Size: {population}")

    # display the name of each bot and stats
    bots = data["bots"]
    for bot in bots:
      bot_name = bot["name"]
#the below is the next level 'down' - stats is inside bot name.
      bot_stats = bot["stats"]
      speed = bot_stats["speed"]
      strength = bot_stats["strength"]


      print(f"{bot_name} has a strength level of {strength} and a speed level of {speed}.")

def run():
  read("robocity.json")

if __name__ == "__main__":
  run()
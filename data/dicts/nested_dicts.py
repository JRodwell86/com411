def short_pattern():
    pattern = {}
    pattern = {"sequence": "101", "occurrences": 5}
    return pattern

def medium_pattern():
    pattern = {}
    pattern = {"sequence": "111000", "occurrences": 25}
    return pattern

def long_pattern():
    pattern = {}
    pattern = {"sequence": "1100110011001100", "occurrences": 50}
    return pattern

def run():
    print("Analysing Patterns...")
    #need to add new 'keys' in quotation marks and then the colon because i've made a new dictionary and each part needs classicfication
    patterns = {"Short sequences": short_pattern(),
                "Medium sequences": medium_pattern(),
                "Long sequences": long_pattern()
                }

    for key, value in patterns.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
  run()
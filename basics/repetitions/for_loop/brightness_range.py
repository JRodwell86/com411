#user input brightness
def run():
    brightness_wanted = int(input("What level of brightness is required?"))
    print("\nAdjusting brightness...\n")
    for brightness in range(2,brightness_wanted + 1,2):
        print(f"Beep brightness level: {'*' * brightness}")
        print(f"Bop Brightness Level: {'*' * brightness}\n")

    print("adjustments completed")
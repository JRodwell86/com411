def run():

        bars_to_charge = int(input("How many bars should I charge?"))
        bars_charged = 0
        while bars_charged < bars_to_charge:
            bars_charged = bars_charged + 1
            print(f"Charging: {'█' * bars_charged}")
        print("The battery is fully charged")
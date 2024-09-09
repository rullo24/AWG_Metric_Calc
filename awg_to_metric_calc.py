import keyboard
import math

def calc_wire_area_mm2_from_awg(awg: int):
    return 0.012668 * 92**((36-awg)/19.5) # mm2 calc

def calc_wire_diameter_mm_from_awg(awg: int):
    return 0.127 * 92**((36-awg)/39) # mm calc

def calc_awg_from_wire_area_mm2(area_mm2: float):
    return 36 - 19.5 * math.log(area_mm2 / 0.012668, 92)

def calc_awg_from_wire_diameter_mm(diameter_mm: float):
    return 36 - 39 * math.log(diameter_mm / 0.127, 92)

def main():
    # Printing the user menu to stdout
    menu: str = """
    1.) AWG --> Metric
    2.) Metric --> AWG
    """
    print(menu)

    # Responding to user selection for required conversion
    resp: str = input("Selection: ")
    if resp == "1": # AWG --> Metric
        awg_val: int = int(input("Input AWG Value: "))
        mm_val: float = calc_wire_diameter_mm_from_awg(awg=awg_val)
        mm2_val: float = calc_wire_area_mm2_from_awg(awg=awg_val)
        print("========================")
        print(f"\n{awg_val} AWG | Diameter (mm): {round(mm_val, 3)} | Area (mm2): {round(mm2_val, 3)}\n")

    elif resp == "2": # Metric --> AWG
        diameter_or_area_selection: str = input("Selection | Diameter (d) or Area (a) to AWG: ")

        # selecting option based on user input
        if diameter_or_area_selection == "d":
            mm_val: float = float(input("Input Diameter (mm) Value: "))
            awg_val: float = calc_awg_from_wire_diameter_mm(mm_val)
            print("========================")
            print(f"\nDiameter (mm) {mm_val} | AWG {round (awg_val, 3)}")
        elif diameter_or_area_selection == "a":
            mm2_val: float = float(input("Input Area (mm2) Value: "))
            awg_val: float = calc_awg_from_wire_area_mm2(mm2_val)
            print("========================")
            print(f"\nArea (mm2) {mm2_val} | AWG {round (awg_val, 3)}")
        else:
            raise ValueError("invalid response provided")
    else:
        raise ValueError("invalid response provided")

if __name__ == "__main__":
    main()
    print("\n WAITING FOR <ENTER> KEY TO CLOSE")
    keyboard.wait("enter")
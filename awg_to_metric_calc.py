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
    3.) Conversion Table
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
    elif resp == "3": # print AWG <--> Metric table
        basic_conv_table: str = """
        AWG\t|\t⌀[Inch]\t|\t⌀[mm]\t|\t⌀[mm²]\t|\tResistance [Ohm/m]
        4/0\t|\t0.460\t|\t11.7\t|\t107\t|\t0.000161
        3/0\t|\t0.410\t|\t10.4\t|\t85.0\t|\t0.000203
        2/0\t|\t0.365\t|\t9.26\t|\t67.4\t|\t0.000256
        1/0\t|\t0.325\t|\t8.25\t|\t53.5\t|\t0.000323
        1\t|\t0.289\t|\t7.35\t|\t42.4\t|\t0.000407
        2\t|\t0.258\t|\t6.54\t|\t33.6\t|\t0.000513
        3\t|\t0.229\t|\t5.83\t|\t26.7\t|\t0.000647
        4\t|\t0.204\t|\t5.19\t|\t21.1\t|\t0.000815
        5\t|\t0.182\t|\t4.62\t|\t16.8\t|\t0.00103
        6\t|\t0.162\t|\t4.11\t|\t13.3\t|\t0.00130
        7\t|\t0.144\t|\t3.66\t|\t10.5\t|\t0.00163
        8\t|\t0.128\t|\t3.26\t|\t8.36\t|\t0.00206
        9\t|\t0.114\t|\t2.91\t|\t6.63\t|\t0.00260 
        10\t|\t0.102\t|\t2.59\t|\t5.26\t|\t0.00328
        11\t|\t0.0907\t|\t2.30\t|\t4.17\t|\t0.00413
        12\t|\t0.0808\t|\t2.05\t|\t3.31\t|\t0.00521
        13\t|\t0.0720\t|\t1.83\t|\t2.62\t|\t0.00657
        14\t|\t0.0641\t|\t1.63\t|\t2.08\t|\t0.00829
        15\t|\t0.0571\t|\t1.45\t|\t1.65\t|\t0.0104
        16\t|\t0.0508\t|\t1.29\t|\t1.31\t|\t0.0132
        17\t|\t0.0453\t|\t1.15\t|\t1.04\t|\t0.0166
        18\t|\t0.0403\t|\t1.02\t|\t0.823\t|\t0.0210
        19\t|\t0.0359\t|\t0.912\t|\t0.653\t|\t0.0264
        20\t|\t0.0320\t|\t0.812\t|\t0.518\t|\t0.0333
        21\t|\t0.0285\t|\t0.723\t|\t0.410\t|\t0.0420
        22\t|\t0.0253\t|\t0.644\t|\t0.326\t|\t0.0530
        23\t|\t0.0226\t|\t0.573\t|\t0.258\t|\t0.0668
        24\t|\t0.0201\t|\t0.511\t|\t0.205\t|\t0.0842
        25\t|\t0.0179\t|\t0.455\t|\t0.162\t|\t0.106
        26\t|\t0.0159\t|\t0.405\t|\t0.129\t|\t0.134
        27\t|\t0.0142\t|\t0.361\t|\t0.102\t|\t0.169
        28\t|\t0.0126\t|\t0.321\t|\t0.0810\t|\t0.213 
        29\t|\t0.0113\t|\t0.286\t|\t0.0642\t|\t0.268
        30\t|\t0.0100\t|\t0.255\t|\t0.0509\t|\t0.339
        31\t|\t0.00893\t|\t0.227\t|\t0.0404\t|\t0.427
        32\t|\t0.00795\t|\t0.202\t|\t0.0320\t|\t0.538
        33\t|\t0.00708\t|\t0.180\t|\t0.0254\t|\t0.679
        34\t|\t0.00631\t|\t0.160\t|\t0.0201\t|\t0.856
        35\t|\t0.00562\t|\t0.143\t|\t0.0160\t|\t1.08
        36\t|\t0.00500\t|\t0.127\t|\t0.0127\t|\t1.36
        37\t|\t0.00445\t|\t0.113\t|\t0.0100\t|\t1.72
        38\t|\t0.00397\t|\t0.101\t|\t0.00797\t|\t2.16
        39\t|\t0.00353\t|\t0.0897\t|\t0.00632\t|\t2.73
        40\t|\t0.00314\t|\t0.0799\t|\t0.00501\t|\t3.44 
        """
        print(basic_conv_table)
    else:
        raise ValueError("invalid response provided")

if __name__ == "__main__":
    main()
    print("\n WAITING FOR <ENTER> KEY TO CLOSE")
    keyboard.wait("enter")
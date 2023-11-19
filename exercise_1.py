weight = float(input("Enter weight "))
unit = input("(K)g or (L)bs: ").lower()

KG_TO_LBS_VALUE = 0.453592

if unit == "k":
    converted_weight = weight
elif unit == "l":
    converted_weight = weight * KG_TO_LBS_VALUE
else:
    raise Exception('Invalid entry')

string_weight = str(int(converted_weight))

if unit == "k":
    print("Weight in Kg " + string_weight)
else:
    print("Weight in Lbs " + string_weight)

import requests
import sys

if len(sys.argv) != 3:
    print("Usage: python3 day16.py ip filename_with_odd_numbers")
    sys.exit(1)
with open(sys.argv[2]) as file:
    for i in file:
        r = requests.get(f"http://{sys.argv[1]}/api/{i.strip()}")
        r_data = r.text
        if "Error. Key not valid!" not in r_data:
            print(f"The valid key is {i}")
        else:
            print(f"{i} is invalid is invalid")

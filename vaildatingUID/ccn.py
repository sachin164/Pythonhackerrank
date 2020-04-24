import re


for _ in range(int(input())):
    num = input()

    k1 = bool(re.match(r"^[456]\d{15}$", num))
    k2 = bool(re.match(r"^[456]\d{3}\-\d{4}\-\d{4}\-\d{4}$", num))
    num = num.replace("-", "")
    k3 = bool(re.match(r"(?!.*(\d)(-?\1){3})", num))
    if (k1 or k2) and k3:
        print("Valid")
    else:
        print("Invalid")
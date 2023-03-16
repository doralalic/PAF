while True:
    try:
        x1 = float(input("Upiši x koordinatu za prvu točku: "))
        y1 = float(input("Upiši y koordinatu za prvu točku: "))
        x2 = float(input("Upiši x koordinatu za drugu točku: "))
        y2 = float(input("Upiši y koordinatu za drugu točku: "))
        break
    except ValueError:
        print("Pogrešan unos, pokušaj ponovno.")

if x1 == x2:
    print(f"Jednadžba pravca je x = {x1}")
else:
    k = (y2 - y1) / (x2 - x1)
    n = y1 - k * x1
    print(f"Jednadžba pravca je y = {k}x + {n}")
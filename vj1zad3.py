def jednadzba_pravca(x1, y1, x2, y2):
    if x1 == x2:
        print(f"Jednadžba pravca je x = {x1}")
    else:
        k = (y2 - y1) / (x2 - x1)
        n = y1 - k * x1
        print(f"Jednadžba pravca je y = {k}x + {n}") 

jednadzba_pravca(0, 0, 2, 3)
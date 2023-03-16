import matplotlib.pyplot as plt

def jednadzba_pravca(x1, y1, x2, y2, prikazi=True, ime_pdf=None):
    if x1 == x2:
        print(f"Jednadžba pravca je x = {x1}")
        plt.axvline(x=x1, color='r', linestyle='--')
    else:
        k = (y2 - y1) / (x2 - x1)
        n = y1 - k * x1
        print(f"Jednadžba pravca je y = {k}x + {n}")
        x = [x1, x2]
        y = [y1, y2]
        plt.plot(x, y, 'bo')
        plt.plot(x, [k * i + n for i in x], 'r--')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    
    if prikazi:
        plt.show()
    else:
        if ime_pdf is None:
            ime_pdf = 'graf.pdf'
        plt.savefig(ime_pdf)

jednadzba_pravca(0, 0, 2, 3, prikazi=False, ime_pdf='moj_graf.pdf')

jednadzba_pravca(1, 1, 4, 7)
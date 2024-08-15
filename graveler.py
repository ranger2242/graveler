import random as rn
import time
from multiprocessing import Process
import locale

locale.setlocale(locale.LC_ALL, '')
valid_hex = '0123456789ABCDEF'.__contains__

clrs = ["F08080", "FFB6C1", "FFA07A", "FFD700", "FFFF00", "90EE90", "00FF00", "00FFFF", "0000FF", "8A2BE2", "9400D3",
        "FF00FF", "A52A2A", "D2691E", "CD853F", "F4A460", "DEB887", "D2B48C", "BC8F8F", "FFE4C4", "FFDEAD", "F5DEB3",
        "FFF8DC", "FAFAD2", "FFFFE0", "808080", "C0C0C0", "FFFFFF", "333333", "2F4F4F", "696969", "778899"]


def color(text, hexcode):
    """print in a hex defined color"""
    code = int(''.join(filter(valid_hex, hexcode)), 16)
    return f"\x1B[38;2;{code >> 16};{code >> 8 & 0xFF};{code & 0xFF}m{text}\x1B[0m"


def proc(inst):
    max = 0
    runs = 0
    start = time.time()
    while True:
        rolls = 0
        while rn.randint(1, 4) == 1: rolls += 1
        runs += 1
        if rolls >= max:
            max = rolls
            print(f'{color(inst, clrs[inst])}:\t\t{rolls}:\t\t({int(time.time() - start)}s):\t\t{runs:n}')
        if max >= 177 or runs==1000000000:
            print(time.time() - start)
            exit()


if __name__ == "__main__":
    procs = list()
    childs = 16
    for i in range(childs):
        p = Process(target=proc, args=(i,))
        p.start()
        procs.append(p)
    for p in procs:
        p.join()

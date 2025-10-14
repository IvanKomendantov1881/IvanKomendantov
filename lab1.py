def flag():
    RED = "\x1b[41m"
    WHITE = "\x1b[47m"
    BLUE = "\x1b[44m"
    RESET = "\x1b[0m"

    width = 25

    flag = [
        (RED, 2),
        (WHITE, 2),
        (BLUE, 4),
        (WHITE, 2),
        (RED, 2)
    ]

    for color, lines in flag:
        print((color + " " * width + RESET + "\n") * lines, end="")
flag()
RESET = '\x1b[0m'
BLUE = '\x1b[44m'

def uzor_line(offset1, length1, offset2, length2):
    print(" " * offset1 + f'{BLUE}{" " * length1}{RESET}' +
          " " * offset2 + f'{BLUE}{" " * length2}{RESET}')

def uzor_picture():
    height = 15
    offset1_start, offset2_start = 40, 0
    length1_start, length2_start = 1, 1
    uzor_line(39, 1, 0, 2)
    for i in range(2, height):
        offset1 = int(offset1_start - (i**1.5) * 0.6)
        offset2 = int(offset2_start + (i**1.5) * 0.6)
        length1 = int(length1_start + (i**1.3) * 0.5)
        length2 = int(length2_start + (i**1.3) * 0.5)
        uzor_line(offset1, length1, offset2, length2)
uzor_picture()
RESET = '\x1b[0m'
BLUE = '\x1b[44m'

def graph():
    height = 12  
    width = 40   
    scale_x = 0.2
    scale_y = height / 2
    for y in range(height, 0, -1):
        line = ""
        flag = False
        for x in range(1, width + 1):
            graph_y = int(scale_y / (x * scale_x))
            if y == graph_y:
                line += f"{BLUE}{' '}{RESET}"
                flag = True
            else:
                line += " "
        if flag:
            print(line)

graph()

with open('sequence.txt') as f:
    nums = [float(x.strip()) for x in f if x.strip()]
less = sum(x < 5 for x in nums)
greater = sum(x > 5 for x in nums)
total = less + greater
p_less = less * 100 / total
p_greater = greater * 100 / total
bar_len = 50
bar_less = int(bar_len * less / total)
bar_greater = bar_len - bar_less

print(f"Меньше 5: {p_less}% | Больше 5: {p_greater}%")
print(f"[{BLUE}{' ' * bar_less}{RESET}{'-' * bar_greater}]")


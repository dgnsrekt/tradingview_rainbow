from colour import Color

MAX_COLORS = 35

red = Color("red")
blue = Color("blue")
colors = [c.get_hex_l().upper() for c in red.range_to(blue, MAX_COLORS)]

START_CODE_BLOCK = "bar_color = "
CODE_BLOCK_ZERO = "color_index > {} ?"
CODE_BLOCK = "color_index > {} ? {} : "
CODE_BLOCK_END = "color_index > {} ? {} : {}"

position = [n for n in range(MAX_COLORS, 0, -1)]

print()
print("//GENERATED-START", end="\n\n")

print(f"color_index = bar_index % {MAX_COLORS}", end="\n\n")

print(START_CODE_BLOCK, end="")

for idx, (color, pos) in enumerate(zip(colors, position)):
    if idx < 1:
        print("    " * idx, CODE_BLOCK.format(pos, color))

    elif idx >= len(colors) - 1:
        print("    " * idx, CODE_BLOCK_END.format(pos, color, color))
    else:
        print("    " * idx, CODE_BLOCK.format(pos, color))


print("\n")
print("barcolor(bar_color)")
print("\n")


CODE_BLOCK = "plot(sma(close, {}), color={})"
for idx, color in enumerate(colors):
    if idx < 1:
        continue
    print(CODE_BLOCK.format(idx, color))

print()
print("//GENERATED-END")
print()

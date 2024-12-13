colors = ['red', 'green', 'blue']
c1, c2, *rest = colors
print(c1, c2, rest)

new_colors = [*colors]
print(*new_colors)

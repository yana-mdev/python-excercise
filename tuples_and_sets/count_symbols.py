text = input()

symbols = set()
for ch in text:
    symbols.add(ch)

for ch in sorted(symbols):
    print(f"{ch}: {text.count(ch)} time/s")
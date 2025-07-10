# 7. Multi-line Quote Saver

# Concepts: triple quotes, .strip(), .count()
# Accept multi-line quotes using triple quotes
# Strip spaces and count how many lines the quote has (based on \n)


print("Enter your multi-line quote (Press Enter twice to finish):")

lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

quote = "\n".join(lines).strip()

line_count = quote.count('\n') + 1 if quote else 0

print("\n--- Saved Quote ---")
print(quote)
print(f"\nTotal number of lines: {line_count}")

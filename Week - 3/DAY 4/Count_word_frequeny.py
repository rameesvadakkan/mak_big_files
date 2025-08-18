from collections import Counter

# Open and read file
with open("week_3_revision.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Convert to lowercase and split into words
words = text.lower().split()

# Count word frequency
word_count = Counter(words)

# Print word frequency
for word, freq in word_count.items():
    print(f"{word}: {freq}")

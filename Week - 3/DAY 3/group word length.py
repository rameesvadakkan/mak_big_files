words = ["apple", "bat", "cat", "banana", "dog", "mango"]

grouped = {}

for word in words:
    length = len(word)
    if length not in grouped:
        grouped[length] = []   # create list if not present
    grouped[length].append(word)  # add word to its length group

print(grouped)

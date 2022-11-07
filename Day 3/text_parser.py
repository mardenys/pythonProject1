text = input("input a text: ")
text = text.lower()

letters = []
letters.append(input("Enter the first letter: ").lower())
letters.append(input("Enter the second letter: ").lower())
letters.append(input("Enter the thirs letter: ").lower())

# Count how many letters are in the text
print("\n")
print("LETTER REPETITION")
count1 = text.count(letters[0])
count2 = text.count(letters[1])
count3 = text.count(letters[2])
print(f"Letter '{letters[0]}' appears {count1} time(s)")
print(f"Letter '{letters[1]}' appears {count2} time(s)")
print(f"Letter '{letters[2]}' appears {count3} time(s)")

# Print first and last letter of the text
print("\n")
print("FIRST AND LAST LETTER")
first_letter = text[0]
last_letter = text[-1]
print(f"First letter of your text is: {first_letter}")
print(f"Last letter of your text is: {last_letter}")

# Count how many words are in the text
print("\n")
print("NUMBER OF WORDS")
text = text.split()
print(f"Your text have {len(text)} words")

# Invert the order of the word
print("\n")
print("INVERTED TEXT")
text.reverse()
inverted_text = ' '.join(text)
print(f"This is your text reverted: '{inverted_text}'")

# Is word python in yoyr text?
print("\n")
print("LOOKING FOR A WORD PYTHON")
search_result = "python" in text
print(f"Is python in your text: {search_result}")

# Input from user
text = input("Enter a sentence: ")

# Step 1: Clean extra spaces
clean_text = " ".join(text.split())

# Step 2: Remove special characters (keep letters, numbers, spaces)
clean_text = "".join([ch for ch in clean_text if ch.isalnum() or ch.isspace()])

# Step 3: Convert to lowercase for consistency
clean_text = clean_text.lower()

# Step 4: Count vowels
vowels = "aeiou"
vowel_count = sum(1 for ch in clean_text if ch in vowels)

# Step 5: Word frequency
words = clean_text.split()
word_freq = {word: words.count(word) for word in set(words)}

# Output
print("\n--- Results ---")
print("Cleaned Text:", clean_text)
print("Vowel Count:", vowel_count)
print("Word Frequency:", word_freq)
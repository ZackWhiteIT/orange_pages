def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

text = input("Enter text: ")
print(f"Vowel count: {count_vowels(text)}")
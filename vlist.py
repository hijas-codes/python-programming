def extract_vowels(word):
    vowels = "aeiouAEIOU"  
    vowel_list = [char for char in word if char in vowels]
    return vowel_list
word = input("Enter a word: ")
vowels_in_word = extract_vowels(word)
print(f"Vowels in the word '{word}': {vowels_in_word}")


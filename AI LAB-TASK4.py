def luhn_check(card_number):
    # Reverse the card number and convert each digit to an integer
    digits = [int(d) for d in str(card_number)][::-1]
    
    total = 0
    for i, digit in enumerate(digits):
        if i % 2 == 1:  # Double every second digit from the right (1-indexed from the right)
            doubled = digit * 2
            if doubled > 9:
                doubled -= 9
            total += doubled
        else:
            total += digit

    return total % 10 == 0

# Example usage
card = "4539578763621486"
if luhn_check(card):
    print("Valid card number")
else:
    print("Invalid card number")

#punctuation remover
import string

def remove_punctuation(text):
    # Create a translation table to remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

# Example usage
input_string = "Hello, world! It's a beautiful day :)"
cleaned_string = remove_punctuation(input_string)

print("Original:", input_string)
print("Without Punctuation:", cleaned_string)


#sort alphabetically

def sort_sentence(sentence):
    # Remove punctuation and convert to lowercase
    import string
    translator = str.maketrans('', '', string.punctuation)
    cleaned_sentence = sentence.translate(translator).lower()
    
    # Split the sentence into words and sort
    words = cleaned_sentence.split()
    words.sort()
    
    # Join the sorted words back into a sentence
    return ' '.join(words)

# Example usage
input_sentence = "The quick brown fox jumps over the lazy dog!"
sorted_sentence = sort_sentence(input_sentence)

print("Original:", input_sentence)
print("Sorted:", sorted_sentence)


def clean_and_reverse_text(text):
    cleaned_text = ' '.join(text.split()) 
    return cleaned_text[::-1]  

text_input = input("\nEnter a line of text with extra spaces: ")
print("Reversed Cleaned Text:", clean_and_reverse_text(text_input))

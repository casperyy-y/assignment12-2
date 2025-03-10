def shift_text(text, num_chars, num_lines, direction):
    text = (text * ((num_chars // len(text)) + 1))[:num_chars]  
    
    lines = []
    for _ in range(num_lines):
        if direction.lower() == "left":
            text = text[1:] + text[0]  
        elif direction.lower() == "right":
            text = text[-1] + text[:-1]  
        lines.append(text)

    return lines

text_to_shift = input("\nEnter text to shift: ")
num_chars_per_line = int(input("Enter number of characters per line: "))
num_lines_to_print = int(input("Enter number of lines to print: "))
shift_direction = input("Enter direction (left/right): ")

print("Shifted Text Output:")
for line in shift_text(text_to_shift, num_chars_per_line, num_lines_to_print, shift_direction):
    print(line)

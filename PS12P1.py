def parse_name(full_name):
    parts = full_name.strip().split()
    if len(parts) != 2:  # Ensure exactly two parts
        return "Invalid input. Enter in 'Firstname Lastname' format."
    
    first, last = parts
    return f"{last}, {first[0]}."

full_name = input("Enter full name (Firstname Lastname): ")
print("Formatted Name:", parse_name(full_name))

def process_csv(csv_string):
    items = [item.strip() for item in csv_string.split(",")]  
    return items

csv_input = input("\nEnter comma-separated values: ")
print("Processed CSV Values:")
for item in process_csv(csv_input):
    print(item)

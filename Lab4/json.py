import json

# Load the sample data from the JSON file
with open('sample-data.json', 'r') as file:
    data = json.load(file)

# Create the header of the table
output = "Interface Status \n"
output += "=" * 80 + "\n"
output += "DN                               Description           Speed    MTU\n"
output += "-" * 80 + "\n"

# Parse the JSON data and extract relevant details
for item in data:
    dn = item.get("DN", "")
    description = item.get("Description", "inherit")
    speed = item.get("Speed", "")
    mtu = item.get("MTU", "")
    
    # Format each line of output
    output += f"{dn:<50} {description:<20} {speed:<8} {mtu:<6}\n"

# Print the formatted output
print(output)

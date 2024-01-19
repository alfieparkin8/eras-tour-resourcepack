import os
import re

starting_map_id = 1077
file_path = r'C:\Users\Alfie\MultiMC\instances\ships\.minecraft\resourcepacks\Eras Tour\assets\other\pmc\lover.mcfunction'
output_file_path = r'C:\Users\Alfie\MultiMC\instances\ships\.minecraft\resourcepacks\Eras Tour\assets\other\pmc\lover_modified.mcfunction'

if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(output_file_path, 'w') as output_file:
        for i, line in enumerate(lines):
            # Using regular expression to find and replace the map values
            updated_line = re.sub(r'(map:\d+)', f'map:{starting_map_id + i}', line)
            output_file.write(updated_line)

    print(f"Modified commands exported to: {output_file_path}")
else:
    print(f"File not found: {file_path}")

import fileinput
import subprocess

# Specify the file path
file_path = r'C:\IES - V10 - 5Gen in 100 bus - line fault.py'

# Define the range of new_outage_num values
new_outage_num_range = range(0, 53)

# Loop through the range of new_outage_num values
for new_outage_num in new_outage_num_range:
    # Use fileinput to modify the file
    with fileinput.FileInput(file_path, inplace=True) as file:
        for line in file:
            if 'outage_num =' in line:
                # Replace the existing value with the new one
                line = f'outage_num = {new_outage_num}\n'
            print(line, end='')

    # Run the modified code
    try:
        subprocess.run(['python', file_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error while running the code: {e}")

print("Code execution with different outage_num values completed.")

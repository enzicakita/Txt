import glob
import os

# Get the current directory where the script is located
current_directory = os.path.dirname(os.path.abspath(__file__))

# Define the output file where merged content will be saved
output_file = "merged_output.txt"

# Get a list of all text files in the current directory
text_files = glob.glob(f"{current_directory}/*.txt")

# Open the output file in write mode
with open(output_file, "w") as merged_file:
    for text_file in text_files:
        with open(text_file, "r") as current_file:
            # Write the name of the text file in all caps
            merged_file.write(f"\n\n\n\n\n\n\n\nTitle: {os.path.basename(text_file).upper()}\n\n\n\n\n\n\n\n")
            # Write the content of the text file
            merged_file.write(current_file.read())
            # Add a separator between files
            merged_file.write("\n\n\n\n---------------------\n\n\n\n")

print(f"All text files in the current directory have been merged into {output_file}.")
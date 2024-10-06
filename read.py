# def read_and_write_values(input_file, output_file, num_values=50000):
#     try:
#         with open(input_file, 'r') as infile:
#             # Read the entire line from the input file
#             line = infile.readline().strip()
#             # Split the line into individual values
#             values = line.split()

#         # Ensure we have enough values to write
#         if len(values) < num_values:
#             print(f"Warning: The file contains only {len(values)} values, writing all of them.")
#             num_values = len(values)

#         # Select the first num_values values
#         selected_values = values[:num_values]

#         with open(output_file, 'w') as outfile:
#             # Write each value to the output file, separated by spaces
#             outfile.write(' '.join(selected_values) + '\n')

#         print(f"Successfully wrote {num_values} values to {output_file}.")
#     except FileNotFoundError:
#         print(f"The file {input_file} does not exist.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Example usage
# input_file_path = 'tsp10000_train_lkh3.txt'  # Replace with your input file path
# output_file_path = 'output.txt'  # Replace with your desired output file path
# read_and_write_values(input_file_path, output_file_path)

# def count_values_in_file(input_file):
#     try:
#         with open(input_file, 'r') as infile:
#             # Read the entire line from the input file
#             line = infile.read().strip()
#             # Split the line into individual values
#             values = line.split()
#             # Count the number of values
#             num_values = len(values)

#         print(f"The file contains {num_values} values.")
#         return num_values
#     except FileNotFoundError:
#         print(f"The file {input_file} does not exist.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Example usage
# input_file_path = 'tsp10000_train_lkh3.txt'  # Replace with your input file path
# count_values_in_file(input_file_path)

def split_file(input_file, output_file1, output_file2, split_line=6000):
    try:
        with open(input_file, 'r') as infile:
            lines = infile.readlines()

        # Check if the file has at least the number of lines we want to split
        if len(lines) < split_line:
            print(f"The file contains only {len(lines)} lines, cannot split as requested.")
            return

        # Write the first 6,000 lines to the first output file
        with open(output_file1, 'w') as outfile1:
            outfile1.writelines(lines[:split_line])

        # Write the remaining 400 lines to the second output file
        with open(output_file2, 'w') as outfile2:
            outfile2.writelines(lines[split_line:])

        print(f"Successfully split the file into {output_file1} and {output_file2}.")
    except FileNotFoundError:
        print(f"The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file_path = 'tsp10000_train_lkh3.txt'      # Replace with your input file path
output_file1_path = 'output1.txt'  # Path for the first 6,000 lines
output_file2_path = 'output2.txt'  # Path for the remaining 400 lines
split_file(input_file_path, output_file1_path, output_file2_path)

# Imports the Pandas library to work with data frames in Python.
import pandas as pd

# Reads the input CSV file named "cleaned_chsv1.csv" into a Pandas data frame named "input_df".
input_df = pd.read_csv("cleaned_chsv1.csv")

# Sets the output CSV file name to "output.csv".
output_file = "output.csv"

# Sets the path to the directory where the input and output files are located.
data_dir = "/home/rajashri/Documents/Visual_Code_Working_directory/INEURON_INTERNSHIP/data/"

# Removes rows containing -9 in any column
input_df = input_df[~(input_df == -9).any(axis=1)]

# Opens a file named "cleaned_chsv.csv" in write mode for writing cleaned data.
output = open(data_dir+output_file, 'w')
# This line of code writes a header line with the names of the columns to the output file. The header includes the names of the 14 columns: 
output.write("age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,num\n") # Add column names

# Initializes counters for the total number of input and output records.
total_input = len(input_df)
total_output = 0

# Iterates over each row in the input data frame using the iterrows() function.
for index, row in input_df.iterrows():
    # Extracts the first 14 values from the current row into a Python list named "features_list".
    features_list = row.values[0:14]
    # Converts the list of features to a comma-separated string and stores it in a variable named "corrected_line".
    corrected_line = ",".join(map(str, features_list))
    # Writes the cleaned row to the output file, followed by a new line character.
    output.write(corrected_line+"\n")
    # Increments the output record counter.
    total_output += 1

# Prints the total number of input and output records processed.
print('Total records read in: %i' % total_input)
print('Total records written out to %s: %i' % (output_file, total_output))
# Closes the output file after writing cleaned data.
output.close()


# Imports the Pandas library to work with data frames in Python.
import pandas as pd

# Reads the input CSV file named "combined_chsv_a.csv" into a Pandas data frame named "input_df".
input_df = pd.read_csv("combined_chsv_a.csv")

# Sets the output CSV file name to "cleaned_chsv.csv".
output_file = "cleaned_chsv1.csv"

# Sets the path to the directory where the input and output files are located.
data_dir = "/home/rajashri/Documents/Visual_Code_Working_directory/INEURON_INTERNSHIP/data/"

# Opens a file named "cleaned_chsv.csv" in write mode for writing cleaned data.
output = open(data_dir+output_file, 'w')
# This line of code writes a header line with the names of the columns to the output file. The header includes the names of the 14 columns: 
output.write("age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,num\n") # Add column names

# Initializes counters for the total number of input and output records.
total_input = 0
total_output = 0

# Iterates over each row in the input data frame using the iterrows() function.
for index, row in input_df.iterrows():
    # Increments the input record counter.	
    total_input += 1
    
    # Checks if the current row has any missing values, i.e., "-9", "?", or NaN values, and if not, proceeds with the data cleaning process. If the row has missing values, it is skipped.
    if not any([val == "-9" or val == "?" or pd.isna(val) for val in row.values]):
        # Converts the "sex" column to binary values (0 for female, 1 for male).
        if row['sex'] == 0:
            row['sex'] = 'female'
        else:
            row['sex'] = 'male'
            
        # Converts the "fbs" and "exang" columns to binary values (0 for False, 1 for True).
        row['fbs'] = 1 if row['fbs'] == 1 else 0
        row['exang'] = 1 if row['exang'] == 1 else 0
        
        # Extracts the first 14 values from the current row into a Python list named "features_list".
        features_list = [row['age'], row['sex'], row['cp'], row['trestbps'], row['chol'], row['fbs'], row['restecg'], row['thalach'], row['exang'], row['oldpeak'], row['slope'], row['ca'], row['thal'], row['num']]
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


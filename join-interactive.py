# Join 2 CSV files on a column
#
# Usage: python3 join.py
# Dependencies: pandas (so run "pip3 install pandas" without the quotes)
#
# Mustafa Hussain
#
# Thanks to:
# stackoverflow.com/questions/16265831

# The "pandas" package has lots of useful functionality for data management
import pandas as pd

import sys

try:
    # Get the command line arguments
    print("I can join two CSV files!") 
    input("First, move 2 CSV files into the same folder as this script. Then hit Enter.")
    in1 = input("Next, type the name of one of your CSV files (like in1.csv), and then press Enter: ")
    in2 = input("Thanks! Now, tell me the name of your other CSV file: ")
    joincol = input("Almost done! What column should I join them on? ")

    # Read, merge, write
    a = pd.read_csv(in1)
    b = pd.read_csv(in2)
    a[joincol] = a[joincol].astype(str)
    b[joincol] = b[joincol].astype(str)
    merged = a.merge(b, on=joincol)
    outname = in1[:-4] + in2[:-4] + '.csv'
    merged.to_csv(outname, index=False)

    print("Done! Now open " + outname)

except:
    print('Hmm...seems I am having some difficulty. Sorry about that!')

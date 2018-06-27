# Join 2 CSV files on a column
#
# Usage: python3 join.py in1.csv in2.csv columntojoinon
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

    in1 = sys.argv[1]
    in2 = sys.argv[2]
    joincol = sys.argv[3]

    # Read in the files
    a = pd.read_csv(in1)
    b = pd.read_csv(in2)

    # Turn the joincol to string in both dataframes
    a[joincol] = a[joincol].astype(str)
    b[joincol] = b[joincol].astype(str)

    # Merge dataframes
    merged = a.merge(b, on=joincol)

    # Write
    merged.to_csv(in1[:-4] + in2[:-4] + '.csv', index=False)

except:
    print('Usage: python3 join.py in1.csv in2.csv columntojoinon')

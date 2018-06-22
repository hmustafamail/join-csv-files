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

    # Read, merge, write
    a = pd.read_csv(in1)
    b = pd.read_csv(in2)
    merged = a.merge(b, on=joincol)
    merged.to_csv(in1[:-4] + in2[:-4] + '.csv', index=False)

except:
    print('Usage: python3 join.py in1.csv in2.csv columntojoinon')

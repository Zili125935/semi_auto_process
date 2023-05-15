import pandas as pd
import numpy as np
import os
import sys
from datetime import datetime


def main():
    cwd = os.getcwd()
    # filedir = cwd +  os.path.join(cwd,"export.xlsx")
    filedir = r"%s\%s" % (cwd, 'export.xlsx')
    print('processing...')
    df = pd.read_excel(filedir)
    df = df[['Customer', 'Sales Doc.', 'Created on', 'SaTy', 'Name 1', 'ItCa', 'Net price', 'Ship-to char', 
                'Promotion Code Text', 'Promotion Code']]
    df = df.drop_duplicates(subset = 'Sales Doc.', keep = 'first')
    df = df.dropna(subset = 'Sales Doc.')
    df_filtered = df[(df['Ship-to char'].isnull())| (df['Ship-to char'].str.match(r'^\d{8}$'))]
    time_string = datetime.now().strftime('%Y-%m-%d_%H%M%S')
    output_filedir = 'sun_output' + time_string + '.xlsx'
    df_filtered.to_excel(output_filedir, index=False)
    print('completed! Result file stored as ' + output_filedir)

if __name__ == "__main__":
    sys.exit(main())
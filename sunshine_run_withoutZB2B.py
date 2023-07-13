import pandas as pd
import numpy as np
import os
import sys
from datetime import datetime


def main():
    cwd = os.getcwd()
    # filedir = cwd +  os.path.join(cwd,"export.xlsx")
    filedir = r"%s\%s" % (cwd, 'EXPORT.xlsx')
    print('processing...')
    df = pd.read_excel(filedir)
    df = df[['Customer', 'Sales Doc.', 'Created on', 'SaTy', 'Name 1', 'ItCa', 'Net price', 'Ship-to char', 
                'Promotion Code Text', 'Promotion Code']]
    df = df.drop_duplicates(subset = 'Sales Doc.', keep = 'first')
    #df = df.dropna(subset = 'Sales Doc.')
    # df['Ship-to char'] = df['Ship-to char'].astype('str')
    df_filtered = df[~df['Ship-to char'].astype(str).str.contains(r'\b\d{10}\b', regex=True, na=False)]
    df_selected = df_filtered[df_filtered['SaTy'] != 'ZB2B']
    time_string = datetime.now().strftime('%Y-%m-%d_%H%M%S')
    output_filedir = 'sun_output' + time_string + '.xlsx'
    df_selected.to_excel(output_filedir, index=False)
    print('completed! Result file saved as ' + output_filedir)

if __name__ == "__main__":
    sys.exit(main())
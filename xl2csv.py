try:
    import pandas as pd
    print("This utility is to convert excel(.xlsx) file into dataset readable(.csv) file")
    input_filename = input("Enter the Excel filename to convert: ")
    head_skip_rows = int(input("Enter the number of lines to avoid from the start: "))
    foot_skip_rows = int(input("Enter the number of lines to avoid from the end: "))
    output_filename = input("Enter the csv filename to save: ")

    old_df = pd.read_excel(input_filename)
    df = pd.read_excel(input_filename, header=0, skiprows=head_skip_rows, skipfooter=foot_skip_rows)
    df.dropna(axis=1, how='all',inplace=True)
    df.to_csv(output_filename, index=False)

    print("\nConversion completed")
    print("Details")
    print('-'*7)
    print("Given FileName          : ",input_filename)
    print("Given (rows,columns)    : ",old_df.shape)
    print("\nResult")
    print('-'*6)
    print("Converted FileName      : ",output_filename)
    print("Converted (rows,columns): ",df.shape)
    del old_df, df
except Exception as error:
    print("\nAn error has occurred !")
    print(str(error))
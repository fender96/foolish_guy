from modules import exporter, importer, cleaner, analyzer



# ---- Import ----


input_file_path = r'C:\Users\valer\PycharmProjects\Regression\venv\Lib\site-packages\sklearn\datasets\data\boston_house_prices.csv'
Importer = importer.Importer(input_file_path)
raw = Importer.readCsv()
df_raw = Importer.raw2dataframe(raw)


# ---- Clean ----

Cleaner = cleaner.Cleaner(df_raw)
Cleaner.setRowsToDrop([0,18])
Cleaner.setColumnsToDrop(['CRIM', 'CHAS', 'ZN', 'INDUS', 'RM', 'AGE', 'MEDV'])
df = Cleaner.removeColumns()
df = Cleaner.removeRows()

# ---- Analyzer ----

Analyzer = analyzer.Analyzer()
print("Reduction of file size is: {} %".format(str(Analyzer.calculateReductionFactor(df_raw, df))))

#----- Export ----


output_data_path = r'C:\Users\valer\boston_house_prices_new.csv'
Exp = exporter.Exporter(output_data_path)
Exp.setOutputDataFormat('.csv')
Exp.appendOutputFileName('_ciao')
#Exp.writeOutputDataFormat()
Exp.exportFile(df)
print('Exported file in {}'.format(output_data_path))




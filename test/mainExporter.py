from modules import exporter, importer



# ---- Import ----


input_file_path = r'C:\Users\valer\PycharmProjects\Regression\venv\Lib\site-packages\sklearn\datasets\data\boston_house_prices.csv'
Importer = importer.Importer(input_file_path)
raw = Importer.readCsv()
df = Importer.raw2dataframe()


#----- Export ----


output_data_path = r'C:\Users\valer\boston_house_prices_new.csv'
Exp = exporter.Exporter(output_data_path)
Exp.setOutputDataFormat('.csv')
Exp.writeOutputDataFormat()
Exp.exportFile(df)

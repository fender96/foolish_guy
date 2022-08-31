from modules import cleaner, importer

input_file_path = r'C:\Users\valer\PycharmProjects\Regression\venv\Lib\site-packages\sklearn\datasets\data\boston_house_prices.csv'
Importer = importer.Importer(input_file_path)
raw = Importer.readCsv()
df = Importer.raw2dataframe()

Cleaner = cleaner.Cleaner(df)
Cleaner.setRowsToDrop([0, 18])
Cleaner.setColumnsToDrop(['CRIM', 'CHAS'])
df = Cleaner.removeColumns()
df = Cleaner.removeRows()
print('a')


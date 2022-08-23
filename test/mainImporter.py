from modules import importer


input_file_path = r'C:\Users\valer\PycharmProjects\Regression\venv\Lib\site-packages\sklearn\datasets\data\boston_house_prices.csv'

Importer = importer.Importer(input_file_path)

#Importer.setInputFilePath()
raw = Importer.readCsv()
df = Importer.raw2dataframe()
stats = Importer.dataframeStatistics()
print(stats)

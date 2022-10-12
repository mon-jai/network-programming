from urllib.request import urlretrieve
import json
from pandas import DataFrame

jsonFileName, _ = urlretrieve(
    'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
)

with open(jsonFileName, 'r', encoding='UTF-8') as jsonFile:
    data = json.load(jsonFile)
    dataFrame = DataFrame(data)

    # print(DataFrame([
    #     {key: value for key, value in row.items() if key in ['sno', 'sna', 'tot']}
    #     for row in [row for row in [row for row in data if int(row['tot']) > 80]]
    # ]))

    print(dataFrame.loc[dataFrame['tot'] > 80][['sno', 'sna', 'tot']])

    print(dataFrame.groupby('sarea')['tot'].sum().reset_index(name ='total_tot'))

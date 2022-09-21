from pandas import read_csv

data = read_csv("pig.csv")
data.columns = ["total_amt", "average_weight", "average_price"]

print(f"全年成交平均重量的成交頭數，最低前 5 筆資料(平均重量) {data.sort_values('average_weight').head(5)['average_weight'].values.tolist()}")
print(f"全年成交平均價格的成交頭數，最高前 5 筆資料(平均價格) {data.sort_values('average_price',ascending=False).head(5)['average_price'].values.tolist()}")
print(f"全年成交平均重量的成交頭數，最低前 5 筆資料，原本資料的次序編號) {data.sort_values('total_amt').head(5)['total_amt'].index.tolist()}")

import csv
file1 = "/Users/madhupaluru/Desktop/WhiteHatjr/Class - 104/Class - 104/Weight.csv"
with open(file1, newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)
new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append((n_num))
n = len(new_data)
new_data.sort()

if n % 2 == 0:
    median1 = new_data[int(n/2)]
    median2 = new_data[int(n/2 - 1)]
    print(median1, median2)
    median12 = float(median1) + float(median2)
    medianTotal = median12 / 2.0
else:
    medianTotal = new_data[n/2]
print("Median is:", str(medianTotal))
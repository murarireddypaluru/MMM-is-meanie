import csv
file1 = "/Users/madhupaluru/Desktop/WhiteHatjr/Class - 104/Class - 104/Weight.csv"
with open(file1, newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)
new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(float(n_num))
n = len(new_data)
t = 0
for x in new_data:
    t += x
mean = t/n
print("Mean is:", str(mean))

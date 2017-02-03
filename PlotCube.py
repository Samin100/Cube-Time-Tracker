import openpyxl
import matplotlib.pyplot as plt

path = 'Cube Times.xlsx'
wb = openpyxl.load_workbook(path, read_only=True)
sheet = wb['Sheet1']
cubeTimes = []

for row in sheet.rows:
    cell = row[1].value
    if cell:
        cubeTimes.append(cell)

cubeTimes.__delitem__(0)  # deletes the 'Time' row

solve_times = []
for entry in cubeTimes:
    split1 = str.split(entry,':')
    split2 = str.split(split1[1], '.')
    splitted = [split1[0], split2[0], split2[1]]
    solveTime = int(splitted[0]) + (int(splitted[1]) / 60) + (int(splitted[2]) / 60)
    solve_times.append(solveTime)

plt.plot(solve_times)
plt.ylabel('Minutes')
plt.xlabel('Cube Solve #')
plt.show()

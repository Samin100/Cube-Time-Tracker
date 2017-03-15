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
bestTime = 999
for entry in cubeTimes:
    split1 = str.split(entry,':')
    split2 = str.split(split1[1], '.')
    splitted = [split1[0], split2[0], split2[1]]
    timeEntry = int(splitted[0]) + int(splitted[1]) / 60 + (int(splitted[2]) / 3600)
    solve_times.append(timeEntry)

    if timeEntry < bestTime:
        bestTime = timeEntry


print('Best time: ' + str(bestTime // 1) + ' min and '+ str((bestTime * 60) % 60) + ' seconds')
plt.plot(solve_times)
plt.ylabel('Minutes')
plt.xlabel('Cube Solve #')
plt.show()

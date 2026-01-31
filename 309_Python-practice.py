#predict the output of the following code\total = 0
data = {"pen": 10, "pencil": 5, "eraser": 3, "marker": 15}
total=int()
for item in data:
    if len(item) >= 5:
        total+=data[item]
        print(total)
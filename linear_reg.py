import random

size = int(((random.random()*20)+3)**3)
x = 0
data = []
squares = {}
slope = int(random.random()*10)
while x < size:
    first_eq = slope*x
    sec_eq = slope*x + 3
    third_eq = (slope-1)*x + 2
    data.append((x, first_eq))
    data.append((x+1, sec_eq))
    data.append((x+2, third_eq))
    x = x + 1

data_tot = 0

for tup in data:
    data_tot = data_tot + tup[1]
average = float(data_tot)/float(len(data))
new_slope = 10.0
reps = 10.0
while new_slope > -reps:
    square_sum = 0
    for pair in data:
        this_y = new_slope*pair[0] + average
        square = (this_y - pair[1])**2
        square_sum = square_sum + square
    squares[new_slope] = square_sum
    new_slope = new_slope - 0.1

sorted_squares = sorted(squares.items(), key=lambda x: x[1], reverse=False)
least_square = sorted_squares[0][0]
print("Best fit: " + "f(x) = " + str(least_square)+ "x + " + str(average))


sim = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]


letterTable = {
    1:"A",
    2:"B",
    3:"C",
    4:"D",
    5:"E",
    6:"F",
    7:"G",
    8:"H"
}



#water
for r in range(1, 9):
    for c in range(1, 9):
        amt = 300 - (10*(r-1) + 10*(c-1))
        sim[r-1][c-1] += amt
for i in sim:
    print(i)

print(" ")


#blue
for r in range(1, 9):
    for c in range(1, 9):
        amt = 10*(c-1)
        sim[r-1][c-1] += amt

for i in sim:
    print(i)

#green
for c in range(1, 9):

    for r in range(1, 9):

        amt = 10*(r-1)
        sim[r-1][c-1] += amt

print(sim)

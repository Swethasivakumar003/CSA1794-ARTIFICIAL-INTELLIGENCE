X = [[213,72,33],
    [90 ,930,63],
    [71 ,658,99]]

Y = [[615,84,11],
    [69,87,386],
    [421,59,69]]

result = [[X[i][j] + Y[i][j]  for j in range(len(X[0]))] for i in range(len(X))]

for r in result:
   print(r)

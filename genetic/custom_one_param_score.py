
def hiddenfunction(x):
  return x ** 2 + 2 * x + 3

def buildhiddenset():
  rows = []
  for i in range(200):
    x = i
    rows.append([x, hiddenfunction(x)])
  return rows

def scorefunction(treeNode, hiddenSet):
  difs = 0
  for row in hiddenSet:
    v = treeNode.evaluate([row[0]]) # row[x, y, value of hidden function]
    difs += abs(v - row[1])
  return difs

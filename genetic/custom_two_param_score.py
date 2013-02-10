
def hiddenfunction(x, y):
  return x ** 2 + 2 * y + 3 + x + 5

def buildhiddenset():
  rows = []
  for i in range(200):
    x = i % 10
    y = i / 10
    rows.append([x, y, hiddenfunction(x, y)])
  return rows

def scorefunction(treeNode, hiddenSet):
  difs = 0
  for row in hiddenSet:
    v = treeNode.evaluate([row[0], row[1]]) # row[x, y, value of hidden function]
    difs += abs(v - row[2])
  return difs

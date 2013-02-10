
def buildhiddenset():
  srows = [ord('i'),ord('g'),ord('o'),ord('r')]
  rows = [[i, srows[i]] for i in range(len(srows))]
  return rows

def scorefunction(treeNode, hiddenSet):
  difs = 0
  for row in hiddenSet:
    v = treeNode.evaluate([row[0]])
    difs += abs(v - row[1])
  return difs

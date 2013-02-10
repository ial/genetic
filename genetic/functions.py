class fwrapper:
  def __init__(self, function, childcount, name):
    self.function = function
    self.childcount = childcount
    self.name = name


addw = fwrapper(lambda l:l[0]+l[1], 2, 'add')
subw = fwrapper(lambda l:l[0]-l[1], 2, 'substract')
mulw = fwrapper(lambda l:l[0]*l[1], 2, 'multiply')

def iffunc(l):
  if l[0] > 0: return l[1]
  else: return l[2]

ifw = fwrapper(iffunc, 3, 'if')

def isgreater(l):
  if l[0]>l[1]: return 1
  else: return 0

gtw = fwrapper(isgreater, 2, 'isgreater')

def getFunctions():
  return [addw, gtw, ifw, mulw, subw]
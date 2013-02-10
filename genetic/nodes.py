
class node:
  def __init__(self, fw, children):
    self.function = fw.function
    self.name = fw.name
    self.children = children

  def evaluate(self, inp):
    results=[n.evaluate(inp) for n in self.children]
    return self.function(results)

  def display(self, indent = 0):
    print (' ' * indent) + self.name
    for c in self.children:
      c.display(indent + 1)

class paramnode:
  def __init__(self, idx):
    self.idx = idx
 
  def evaluate(self, inp):
    return inp[self.idx]

  def display(self, indent = 0):
    print '%sp%d' % (' ' * indent, self.idx)

class constnode:
  def __init__(self, v):
    self.v = v

  def evaluate(self,inp):
    return self.v

  def display(self, indent = 0):
    print '%s%d' % (' ' * indent, self.v)


from random import random, randint, choice
from copy import deepcopy
from math import log

import functions
import nodes


def makerandomtree(pc, maxdepth = 4, fpr = 0.5, ppr = 0.6):
  if random() < fpr and maxdepth > 0:
    f = choice(functions.getFunctions())
    children = [makerandomtree(pc, maxdepth - 1, fpr, ppr)
                for i in range(f.childcount)]
    return nodes.node(f, children)
  elif random() < ppr:
    return nodes.paramnode(randint(0, pc - 1))
  else:
    return nodes.constnode(randint(0, 255))

def hiddenfunction(x, y):
  #return x ** 2 + 2 * y + 3 + x + 5
  return x*y+2*y+33


def buildhiddenset():
  rows = []
  for i in range(200):
    x = i % 10
    y = i / 10
    rows.append([x, y, hiddenfunction(x, y)])
  return rows

def scorefunction(tree, s):
  difs = 0
  for data in s:
    v = tree.evaluate([data[0], data[1]])
    difs += abs(v - data[2])
  return difs


def mutate(t, pc, probchange = 0.1):
  if random() < probchange:
    return makerandomtree(pc)
  else:
    result = deepcopy(t)
    if isinstance(t, nodes.node):
      result.children = [mutate(c, pc, probchange) for c in t.children]
    return result

def crossover(t1, t2, probswap = 0.7, top = 1):
  if random() < probswap and not top:
    return deepcopy(t2)
  else:
    result = deepcopy(t1)
    if (isinstance(t1, nodes.node) and isinstance(t2, nodes.node)):
      result.children = [crossover(c, choice(t2.children), probswap, 0)
                         for c in t1.children]
    return result

def getrankfunction(dataset):
  def rankfunction(population):
    scores = [(scorefunction(t, dataset), t) for t in population]
    scores.sort()
    return scores
  return rankfunction

def evolve(pc, popsize, rankfunction, maxgen = 100, mutationrate = 0.1, breedingrate = 0.4, pexp = 0.7, pnew = 0.05):
  def selectindex():
    return int(log(random()) / log(pexp))

  population = [makerandomtree(pc) for i in range(popsize)]
  for i in range(maxgen):
    scores = rankfunction(population)
    print scores[0][0]
    if scores[0][0] == 0: break

    newpop = [scores[0][1], scores[1][1]]

    while len(newpop) < popsize:
      if random() > pnew:
        newpop.append(mutate(
                             crossover(scores[selectindex()][1],
                                       scores[selectindex()][1],
                                       probswap = breedingrate), 
                             pc, probchange = mutationrate))
      else:
        newpop.append(makerandomtree(pc))

    population = newpop
  scores[0][1].display()
  return scores[0][1]


random1 = makerandomtree(2)
random2 = makerandomtree(2)

hs = buildhiddenset()


rf = getrankfunction(hs)
print evolve(2, 500, rf, mutationrate = 0.2, breedingrate = 0.1, pexp = 0.7, pnew = 0.1).display()

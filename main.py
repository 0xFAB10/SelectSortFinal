import matplotlib as mpl
from random import randint
mpl.use('Agg')
import matplotlib.pyplot as plt
import timeit

def desenhaGrafico(x,y, yl = "Saídas",xl = "Entradas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Melhor Tempo")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(yl+'_graph.png')
 
def geraLista(tam):
    lista = []
    while len(lista) < tam:
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista

def select(xb):
  count = 0
  while len(lis) > 1:
    minimo = lis[0]
    aux=0
    for a in range(len(lis)):
      if (minimo > lis[a]):
        aux = a
        minimo = lis[a]
      count=count+1
    lis.pop(aux)
    lisFinal.append(minimo)
  return count

x = [100, 200, 400, 600]
y = []
z = []

for i in range(len(x)):
  lis = geraLista(x[i])
  lisFinal = []
  y.append(select(x[i]))
  z.append(timeit.timeit('select({})'.format(x[i]),setup="from __main__ import select",number=1))
print(y)
print(z)
desenhaGrafico(x,y, "nops")
desenhaGrafico(x,z, "Tempo")
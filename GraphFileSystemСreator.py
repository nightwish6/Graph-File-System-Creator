import networkx as nx
import os
import matplotlib.pyplot as plt


def buildGraphFileSystem(root='/home',graph = nx.Graph()):
    if not os.access(root, os.R_OK): # Проверяем на право чтения данных директории
        return
    graph.add_node(root, size=getSize(root), color=getColor(root)) # Добавляем узел с атрибутами
    dirs =[dir for dir in os.listdir(root) if dir[0]!='.']# Составляем список данных дириктории, проверяем скрыты ли данные или нет
    for dir in dirs:
        graph.add_node(os.path.join(root,dir), size=getSize(os.path.join(root,dir)),
                       color=getColor(os.path.join(root,dir)))
        graph.add_edge(root, os.path.join(root,dir))# Создаем связи корня с узлами
        if os.path.isdir(os.path.join(root,dir)): # Если фаил явлется директорией, то вызвываем его в функции
            buildGraphFileSystem(root=os.path.join(root,dir),graph=graph)# Функция рекурсивна
    return graph


def getSize(path): # Определяем размер файли или директории в байтах, размер узла зависит от его объема
    if os.path.isfile(path):
        return float(os.path.getsize(path)/1000/1000) # Возвращаем результат в мегабайтах
    else:
        size=0
        for dirs, folders, files in os.walk(path):
            for file in files:
                try: size += os.path.getsize(os.path.join(dirs, file))
                except FileNotFoundError:
                    continue
        return float(size/1000/1000)

def getColor(path):
    if os.path.isfile(path):# Если объект является файлом то он голубого цвета, если папкой то красного
        return 'blue'
    else:
        return 'red'


def showGraphFileSystem(graph, with_labels=False, node_color="blue", alpha=0.6, node_size=5,
                        graphName='home'):
    nx.draw_networkx(G=graph, with_labels=with_labels, node_color=node_color,
                     alpha=alpha, node_size=node_size)
    plt.savefig(graphName+str(graph.size())+'.pdf')
    plt.show()# Отображаем графически граф


if __name__ == "__main__":
    g=buildGraphFileSystem('/home')
    showGraphFileSystem(graph=g, with_labels=False,
                        node_color=[g.node[key]['color'] for key in g.node],
                        node_size=[g.node[key]['size'] for key in g.node])














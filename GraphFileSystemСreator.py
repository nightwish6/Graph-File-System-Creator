import networkx as nx
import os
import matplotlib.pyplot as plt


def buildGraphFileSystem(root='/home',graph = nx.Graph()):
    if not os.access(root, os.R_OK): # Проверяем на право чтения данных директории
        return
    dirs =[dir for dir in os.listdir(root) if dir[0]!='.']# Составляем список данных дириктории, проверяем скрыты ли данные или нет
    for dir in dirs:
        graph.add_edge(root, os.path.join(root,dir))# Создаем связи корня с узлами
        if os.path.isdir(os.path.join(root,dir)): # Если фаил явлется директорией, то вызвываем его в функции
            buildGraphFileSystem(root=os.path.join(root,dir),graph=graph)# Функция рекурсивна
    return graph



def showGraphFileSystem(graph, with_labels=False, node_color="blue", alpha=0.6, node_size=5,
                        graphName='home'):
    nx.draw_networkx(G=graph, with_labels=with_labels, node_color=node_color,
                     alpha=alpha, node_size=node_size)
    plt.savefig(graphName+str(graph.size())+'.pdf')
    plt.show()# Отображаем графически граф


if __name__ == "__main__":
    showGraphFileSystem(graph=buildGraphFileSystem(root='/var'),graphName='var')













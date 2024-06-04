
import matplotlib.pyplot as plt
import numpy as np
from gauss_calc import Gauss
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns
import pandas as pd

# %matplotlib
from smeg_matrix import *
import matplotlib.patches as patches
# from rebuilding import Rebuilding
# from calculation import Calculate
from matplotlib.animation import ArtistAnimation
from matplotlib.ticker import NullLocator

file_path = '/Users/ruslanpepa/CoveringFlow/covering.txt'
VERTEX = 8  # количество вершин в многограннике
EDGES = 30  # количество ребер в многограннике
FACES = 12  # количестов граней в многограннике
TIMES = 200  # количество шагов по времени
step_time = 0.005  # шаг по времени
list_faces = []  # список, который будет содержать все грани
with open(file_path) as fl_wth_fs:  # выгрузим из файла все номера вершин
    lines = fl_wth_fs.readlines()
for line in lines:  # все номера вершин загоним в списко файлову
    ns_vx = line.rstrip('\n').split()
    print(type(ns_vx))  # получили только числа из каждой строки
    a = int(ns_vx[0])
    b = int(ns_vx[1])
    c = int(ns_vx[2])
    list_faces.append(Faces(a, b, c))

two_dim_lst_fs = []
two_dim_lst_fs.append(list_faces)

max_gauss_curv = np.ones(TIMES, float) # график максимальной кривизнв веришне 
min_gauss_curv = np.ones(TIMES, float) # график минимальной кривизнв веришне
gauss_curvature = np.zeros((VERTEX, TIMES), float) # гауссова кривизна в начальный момент времени
radius_vertex = np.zeros((VERTEX, TIMES), float ) # матрица радиусов в точке
length_complex = np.ones((EDGES, TIMES), float) # экспериментальная матрица для отображения длин рёбер

adj_matx = adjacency_matrix(list_faces, VERTEX)  # матрица смежности длин рёбер
adj_matx_numpy = adj_matx.toarray()
for i in range(0, VERTEX):
    for j in range(0, VERTEX):
        if (adj_matx_numpy[i][j] != 0):
            adj_matx_numpy[i][j] = 1
        else:
            adj_matx_numpy[i][j] = 0

adj_matx_numpy.astype(int)



range_of_length = 5. # выбираем диапозон, с которого будет изменяться значение радиусов в каждой точке
start_lenght = 2. # диапозон заканчивается на 7

length_complex = []
length_complex.append(adj_matx)
times_of_finding = 0
while True:
    times_of_finding += 1
    print("times_of_finding:", times_of_finding)
    for i in range(0, VERTEX):
        radius_vertex[0][i] = np.random.uniform(start_lenght, start_lenght + range_of_length)
    while True:
        random_i = np.random.randint(0, VERTEX)
        random_j = np.random.randint(0, VERTEX)
        if adj_matx[random_i, random_j] != 0:
            break
    
    # length_complex[0][random_i, random_j] = length_complex[0][random_j, random_i] = np.random.uniform(0.9, 1.2)
    length_complex[0] = get_matrix_lenght(radius_vertex[0], weighted,len(radius_vertex[0]))
    Gauss_Curve = Gauss(length_complex[0], list_faces)
    Gauss_Curve.date_prepare()
    Gauss_Curve.gauss_calculate()
    if Gauss_Curve.existence == 0:
        break
    # if len(gauss_curve_calculate(length_complex[0])) != 0:
        # break

# numerate_of_edges = {}

Gauss_Curve = Gauss(length_complex[0], list_faces)
Gauss_Curve.date_prepare()
Gauss_Curve.gauss_calculate()
gauss_curve = Gauss_Curve.gauss_curve
# gauss_curve = gauss_curve_calculate(length_complex[0], list_faces)


# for i in range(0, VERTEX):
#     gauss_curvature[i, 0] = gauss_curve[i]
#     # print('gauss_curvature in vertex', i, gauss_curvature[i, 0])
# for j in range(0, VERTEX):
#     for k in range(0, VERTEX):
#         print(float("{0:.10f}".format(length_complex[0][j, k])), end='\t')
#     print('\n')
# length_complex
# fig, ax = plt.subplots()
# im = ax.imshow(length_complex[0])
# sns.heatmap(length_complex[0])



# ax.set_title("Harvest of local farmers (in tons/year)")
# fig.tight_layout()
# plt.show()

for i in range(0, VERTEX):
    gauss_curvature[i, 0] = gauss_curve[i]
    print('gauss_curvature in vertex', i, gauss_curvature[i, 0])


sns.heatmap(length_complex[0].toarray(), annot=True)
# type(length_complex[0])
# sns.heatmap(length_complex[0])
# fig, ax = plt.subplots()
# im = ax.imshow(length_complex[0])
# plt.plot(x,y)
# plt.show()

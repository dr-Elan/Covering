from init import *


# Gauss_Curve = Gauss(length_complex[0], list_faces)
# Gauss_Curve.date_prepare()
# Gauss_Curve.gauss_calculate()
# gauss_curve = Gauss_Curve.gauss_curve
# # gauss_curve = gauss_curve_calculate(length_complex[0], list_faces)

# fig, axs = plt.subplots(2, 2)
# len_edges = [] # список длин ребер
# for i in range(VERTEX):
#     for j in range(i,VERTEX):
#         if adj_matx_numpy[i][j] != 0:
#             len_edges.append(length_complex[0][i,j])
# axs[0, 0].bar(np.array(range(0,len(len_edges))), len_edges)
# axs[0, 0].set_title('Длины ребер')
# axs[0, 1].imshow(weighted_matrix, cmap='winter', aspect='equal', vmin=0, vmax=1, origin="lower")
# axs[0, 1].set_title('Веса ребер')
# axs[1, 0].bar(np.array(range(0,VERTEX)),radius_vertex[0])
# axs[1, 0].set_title('Радиусы')
# axs[1, 1].bar(np.array(range(0,VERTEX)),gauss_curve)
# axs[1, 1].set_title('Кривизны')
# lines = []
# lines.append(axs[1, 1].bar(np.array(range(0,VERTEX)),gauss_curve))
fig, axs = plt.subplots(2, 2, figsize=(8, 6))
# axs[0,0].set_ylim([-10, 10])
# axes[0,0].set_xlim([-10, 10])
# axes[0,1].set_ylim([-1.5, 0.5])
# axes[0,0].set_xlim([1, -1])
# axes[1,0].set_ylim([-1.5, 0.5])
# axes[0,0].set_xlim([1, -1])
# axes[1,1].set_ylim([-1.5, 0.5])
# axes[0,0].set_xlim([1, -1])

def animate (t):
    Gauss_Curve = Gauss(length_complex[t], list_faces)
    Gauss_Curve.date_prepare()
    Gauss_Curve.gauss_calculate()
    gauss_curve = Gauss_Curve.gauss_curve
# gauss_curve = gauss_curve_calculate(length_complex[0], list_faces)
    calc = Calculate(gauss_curve, list_faces, radius_vertex[t], weighted_matrix,order_branch, step_time)
    radius_vertex[t+1] = calc.radius_calculate()
    length_complex.append(get_matrix_lenght(length_complex[t], radius_vertex[t+1], weighted_matrix))
    # Gauss_Curve = Gauss(length_complex[t+1], list_faces)
    # Gauss_Curve.date_prepare()
    # Gauss_Curve.gauss_calculate()
    # gauss_curve = Gauss_Curve.gauss_curve
    


    # fig, axs = plt.subplots(2, 2)
    len_edges = [] # список длин ребер
    for i in range(VERTEX):
        for j in range(i,VERTEX):
            if adj_matx_numpy[i][j] != 0:
                len_edges.append(length_complex[t+1][i,j])
    axs[0, 0].cla()            
    axs[0, 0].bar(np.array(range(0,len(len_edges))), len_edges)
    axs[0, 0].set_title('Длины ребер')
    axs[0, 1].cla()
    axs[0, 1].imshow(weighted_matrix, cmap='winter', aspect='equal', vmin=0, vmax=1, origin="lower")
    axs[0, 1].set_title('Веса ребер')
    axs[1, 0].cla()
    axs[1, 0].bar(np.array(range(0,VERTEX)),radius_vertex[t+1])
    axs[1, 0].set_title('Радиусы')
    axs[1, 1].cla()
    axs[1, 1].bar(np.array(range(0,VERTEX)),gauss_curve)
    axs[1, 1].set_title('Кривизны')
    # plt.show()

    return axs[0,0], axs[0,1], axs[1,0], axs[1,1]

ani = animation.FuncAnimation(fig, animate, interval=100, save_count=500, blit=False, frames=100)
ani.save('/Users/ruslanpepa/CoveringFlow/ani1.gif')
# print('DONE')

# for t in range(0, TIMES-1):
#     calc = Calculate(gauss_curve, list_faces, radius_vertex[t], weighted_matrix,order_branch, step_time)
#     radius_vertex[t+1] = calc.radius_calculate()
#     length_complex.append(get_matrix_lenght(length_complex[t], radius_vertex[t+1], weighted_matrix))
#     Gauss_Curve = Gauss(length_complex[t+1], list_faces)
#     Gauss_Curve.date_prepare()
#     Gauss_Curve.gauss_calculate()
#     gauss_curve = Gauss_Curve.gauss_curve
    


#     fig, axs = plt.subplots(2, 2)
#     len_edges = [] # список длин ребер
#     for i in range(VERTEX):
#         for j in range(i,VERTEX):
#             if adj_matx_numpy[i][j] != 0:
#                 len_edges.append(length_complex[t+1][i,j])
#     axs[0, 0].bar(np.array(range(0,len(len_edges))), len_edges)
#     axs[0, 0].set_title('Длины ребер')
#     axs[0, 1].imshow(weighted_matrix, cmap='winter', aspect='equal', vmin=0, vmax=1, origin="lower")
#     axs[0, 1].set_title('Веса ребер')
#     axs[1, 0].bar(np.array(range(0,VERTEX)),radius_vertex[t+1])
#     axs[1, 0].set_title('Радиусы')
#     axs[1, 1].bar(np.array(range(0,VERTEX)),gauss_curve)
#     axs[1, 1].set_title('Кривизны')
#     lines.append(axs[1, 1].bar(np.array(range(0,VERTEX)),gauss_curve))

    
    






# Loop over data dimensions and create text annotations.
# for i in range(VERTEX):
#     for j in range(VERTEX):
#         axs[0,0].text(j, i, length_complex[0][i, j],
#                        ha="center", va="center", color="w")
#         axs[0,1].text(j, i, weighted_matrix[i, j],
#                        ha="center", va="center", color="w")


# ax.set_title("Harvest of local farmers (in tons/year)")
# fig.tight_layout()
# plt.show()
# plt.hist(gauss_curve)
# for i in range(0, VERTEX):
#     gauss_curvature[i, 0] = gauss_curve[i]
#     print('gauss_curvature in vertex', i, gauss_curvature[i, 0])


# sns.heatmap(length_complex[0].toarray(), annot=True)
# type(length_complex[0])
# sns.heatmap(length_complex[0])
# fig, ax = plt.subplots()
# im = ax.imshow(length_complex[0])
# plt.plot(x,y)
# plt.show()
# 
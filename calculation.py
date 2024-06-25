import numpy as np
class Calculate():
    def __init__(self, gauss_curve, list_faces, radius_of_circle, wgtd_mtx,branch_order, time_step):

        self.curv_gauss_vrtx = gauss_curve
        self.l_o_f = list_faces
        self.rad_of_circ = radius_of_circle
        self.vertex = len(self.rad_of_circ)
        self.step_time = time_step
        self.wght = wgtd_mtx
        self.b = branch_order
        
        
        # print(self.vertex, "тестируем класс калькулейт")
        # print("длина массива конформал вейт:", len(self.conf_weght))

    def radius_calculate(self):
        new_radius = []
        for j in range(0, self.vertex):
            k0 = - (self.curv_gauss_vrtx[j] - 2*np.pi*self.b) * self.rad_of_circ[j]
            k1 = - (self.curv_gauss_vrtx[j] - 2*np.pi*self.b) * (self.rad_of_circ[j] + self.step_time * k0 / 2.)
            k2 = - (self.curv_gauss_vrtx[j] - 2*np.pi*self.b) * (self.rad_of_circ[j] + self.step_time * k1 / 2.)
            k3 = - (self.curv_gauss_vrtx[j] - 2*np.pi*self.b) * (self.rad_of_circ[j] + self.step_time * k2)
            new_radius.append(self.rad_of_circ[j] + (self.step_time/6.) * (k0 + k1*2. + k3*2. + k3))
        return new_radius



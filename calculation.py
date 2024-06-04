import numpy as np
class Calculate():
    def __init__(self, gauss_curve, list_faces, radius_of_circle, time_step):

        self.curv_gauss_vrtx = gauss_curve
        self.l_o_f = list_faces
        self.rad_of_circ = radius_of_circle
        self.vertex = len(self.rad_of_circ)
        self.step_time = time_step
        
        
        # print(self.vertex, "тестируем класс калькулейт")
        # print("длина массива конформал вейт:", len(self.conf_weght))

    def radius_calculate(self):
        new_radius = []
        for j in range(0, self.vertex):
            k0 = - (self.curv_gauss_vrtx[j]*self.alpha_wght[j] - self.lambda_const) * self.rad_of_circ[j]
            k1 = - (self.curv_gauss_vrtx[j]*self.alpha_wght[j] - self.lambda_const) * (self.rad_of_circ[j] + self.step_time * k0 / 2.)
            k2 = - (self.curv_gauss_vrtx[j]*self.alpha_wght[j] - self.lambda_const) * (self.rad_of_circ[j] + self.step_time * k1 / 2.)
            k3 = - (self.curv_gauss_vrtx[j]*self.alpha_wght[j] - self.lambda_const) * (self.rad_of_circ[j] + self.step_time * k2)
            new_radius.append(self.rad_of_circ[j] + (self.step_time/6.) * (k0 + k1*2. + k3*2. + k3))
        return new_radius
    def generate_faces(self, length_matrix, i ):
        for fs in self.l_o_f:
            
                a = length_matrix[i + 1][fs[0], fs[1]]
                b = length_matrix[i + 1][fs[1], fs[2]]
                c = length_matrix[i + 1][fs[2], fs[0]]
        # print(a, b, c)


                hafl_perim = (a + b + c)/2.
                kl_mng = 0
        # print('sting NUMBER 86: exception:', exceptions)
                kl_mng = float("{0:.10f}".format(hafl_perim * (hafl_perim - a) * (hafl_perim - b) * (hafl_perim - c)))
        # print(kl_mng)

        # print('times_for_faces%', times_for_faces,kl_mng )

                if kl_mng > 0:
            # kl_mng = Error:failed to create a child event loop
            # print('try', half_perimetr * (half_perimetr - a) * (half_perimetr - b) * (half_perimetr - c))
                    a_cos = (b ** 2 + c ** 2 - a ** 2) / (2. * c * b)
                    b_cos = (c ** 2 + a ** 2 - b ** 2) / (2. * a * c)
                    c_cos = (a ** 2 + b ** 2 - c ** 2) / (2. * a * b)
                    a_sin = np.sqrt(1. - a_cos ** 2)
                    b_sin = np.sqrt(1. - b_cos ** 2)
                    c_sin = np.sqrt(1. - c_cos ** 2)
            # print("keyli menger:", kl_mng)
            # kayli_manger[TIMES, i + 1] = kl_mng
                else:
                    print('hello, we are ready for exit!',  "time's of iteration: ", i)
                    break


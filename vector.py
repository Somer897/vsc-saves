import math as m

class vector:

    #конструктор
    def __init__(self, x, y, length, angle):

        #параметры
        self.x = x
        self.y = y
        self.length = length
        self.angle = angle

    #показ вектора
    def __str__(self):
        return (f'х: {self.x} ,y: {self.y} , length: {self.length} , angle (in PI(1 = PI/3 or 60 degree)): {self.angle}')

    #сложение векторов
    def __add__(vec1,  vec2):

        #опись параметров векторов
        x1 = vec1.x
        x2 = vec2.x
        y1 = vec1.y
        y2 = vec2.y
        len1 = vec1.length
        len2 = vec2.length
        angle1 = vec1.angle
        angle2 = vec2.angle

        #максимальный и минимальный вектора
        angle_max = max(angle1, angle2)
        angle_min = min(angle1, angle2)

        #длина 3 вектора
        len3 =(len1**2 + len2**2 - 2*len1*len2*(m.cos(m.pi - angle_max + angle_min)))**0.5     #теорема косинусов

        #угол 3-го вектора
        #если максимальный угол у 2-го вектора
        if angle_max == angle2:
            angle3 = angle_min + m.asin(len2 * m.sin(m.pi - angle_max + angle_min) / len3) #добавляем к минимальному углу угол треугольника
        #если максимальный угол у 1-го вектора                                               (высчитан через теорему синусов)
        else:
            angle3 = angle_min + m.asin(len1*m.sin(m.pi - angle_max + angle_min)/len3)

        #итог расчетов
        return vector(x1, y1, len3, angle3)

    #диструктор
    def __del__(self):
        print('Успешно удалено')

#наши вектора
vec1 = vector(2, 3, 5, m.pi /2)
vec2 = vector(3, 4, 6, m.pi / 6)

#сумма
print(vec1 + vec2)

import math as m
import random as r

class Vec3:
    def __init__(self, x = 0.0, y = 0.0, z = 0.0):
        self.e = [x, y, z]
    
    def __str__(self):
        return f"Vec3: {self.e}"
    
    def x(self):
        return self.e[0]
    
    def y(self):
        return self.e[1]
    
    def z(self):
        return self.e[2]
    
    def __neg__(self):
        return Vec3(-self.e[0], -self.e[1], -self.e[2])
    
    def __getitem__(self, i):
        return self.e[i]
    
    def __iadd__(self, v):
        self.e[0] += v[0]
        self.e[1] += v[1]
        self.e[2] += v[2]
        return self
    
    def __imul__(self, t):
        self.e[0] *= t
        self.e[1] *= t
        self.e[2] *= t
        return self

    def __itruediv__(self, t):
        self.e[0] /= t
        self.e[1] /= t
        self.e[2] /= t
        return self

    def lenght_squared(self):
        return self.e[0] ** 2 + self.e[1] ** 2 + self.e[2] ** 2
    
    def lenght(self):
        return m.sqrt(self.lenght_squared())
    
    def __add__(self, v):
        return Vec3(self.e[0] + v[0], self.e[1] + v[1], self.e[2] + v[2])
    
    def __sub__(self, v):
        return Vec3(self.e[0] - v[0], self.e[1] - v[1], self.e[2] - v[2])

    def __mul__(self, t):
        if isinstance(t, Vec3):
            return Vec3(self.e[0] * t[0], self.e[1] * t[1], self.e[2] * t[2])
        else:
            return Vec3(self.e[0] * t, self.e[1] * t, self.e[2] * t)
    
    def __truediv__(self, t):
        if isinstance(t, Vec3):
            return Vec3(self.e[0] / t[0], self.e[1] / t[1], self.e[2] / t[2])
        else:
            return Vec3(self.e[0] / t, self.e[1] / t, self.e[2] / t)

def dot(u, v):
    return u[0] * v[0] + u[1] * v[1] + u[2] * v[2] 

def unit_vector(v):
    return v / v.lenght()

def cross(u, v):
    return Vec3(u[1] * v[2] - u[2] * v[1],
                u[2] * v[0] - u[0] * v[2],
                u[0] * v[1] - u[1] * v[0])

def random():
    return Vec3(r.random(), r.random(), r.random())

def random(min, max):
    return Vec3(r.uniform(min, max), r.uniform(min, max), r.uniform(min, max))

def random_unit_vector():
    while True:
        p = random(-1, 1)
        lensq = p.lenght_squared()
        if 1e-160 < lensq and lensq <= 1:
            return p / m.sqrt(lensq)
        
def random_on_hemisphere(normal):
    on_unit_sphere = random_unit_vector()
    if dot(on_unit_sphere, normal) > 0.0:
        return on_unit_sphere
    else:
        return -on_unit_sphere

class Point3(Vec3):
    pass





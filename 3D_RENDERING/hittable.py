import vectors
class HitRecord:
    def __init__(self, p, t, mat):
        self.p = p
        self.t = t
        self.mat = mat
        
    def set_face_normal(self, r, outward_normal):       
        self.front_face = vectors.dot(r.direction(), outward_normal) < 0
        if self.front_face:
            self.normal = outward_normal
        else:
            self.normal = -outward_normal



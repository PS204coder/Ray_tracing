import vectors, math, hittable
class Sphere:
    def __init__(self, center, radius, mat):
        self.center = center
        self.radius = radius
        self.mat = mat
        
    def hit(self, r, ray_tmin, ray_tmax):
        oc = self.center - r.origin()
        a = r.direction().lenght_squared()
        h = vectors.dot(r.direction(), oc)
        c = oc.lenght_squared() - self.radius * self.radius
        discriminant = h*h - a*c
        if discriminant < 0.0:
            return None
        sqrtd =  math.sqrt(discriminant)
        root = (h - sqrtd) / a
        if root <= ray_tmin or ray_tmax <= root:
            root = (h + sqrtd) / a
            if root <= ray_tmin or ray_tmax <= root:
                return None

        t = root
        p = r.at(t)
        outward_normal = (p - self.center) / self.radius
        rec = hittable.HitRecord(p, t, self.mat)
        rec.set_face_normal(r, outward_normal)
        return rec



        
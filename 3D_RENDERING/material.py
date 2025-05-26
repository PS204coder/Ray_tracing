import vectors,ray
class Lambertian:
    def __init__(self, albedo):
        self.albedo = albedo

    def scatter(self, r_in, rec):
        scatter_direction = rec.normal + vectors.random_unit_vector()
        scatter = ray.Ray(rec.p, scatter_direction)
        return [self.albedo, scatter]
import hittable,vectors

class HittableList:
    def __init__(self):
        self.objects = []
    
    def clear(self):
        self.objects = []

    def add(self, object):
        self.objects.append(object)

    def hit(self, r, ray_tmin, ray_tmax):
        temp_rec = None
        closest_so_far = ray_tmax

        for object in self.objects:
            rec = object.hit(r, ray_tmin, closest_so_far)
            if rec != None:
                closest_so_far = rec.t
                temp_rec = rec


        return temp_rec


import vectors
import math as m

class Color(vectors.Vec3):
   pass

def write_color(file, pixel_color):
        r = m.sqrt(pixel_color.x())
        g = m.sqrt(pixel_color.y())
        b = m.sqrt(pixel_color.z())

        ir = int(255.999 * r)
        ig = int(255.999 * g)
        ib = int(255.999 * b)
        string = f"{ir} {ig} {ib} \n"
        file.write(string)
       
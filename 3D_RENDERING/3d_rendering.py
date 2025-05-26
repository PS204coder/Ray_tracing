#3D_RENDERING


import color, vectors, ray, math, rtweekend, hittable, hittable_list, sphere, random, material


samples_per_pixel = 100
pixel_samples_scale = 1.0 / samples_per_pixel
max_depth = 10
aspect_ratio = 16.0/9.0
IMAGE_WIDTH = 400
IMAGE_HEIGHT = max(1,int(IMAGE_WIDTH/ aspect_ratio))
#screen = pygame.surface.Surface((IMAGE_WIDTH, IMAGE_HEIGHT))

viewport_height = 2.0
viewport_width = viewport_height * (IMAGE_WIDTH/IMAGE_HEIGHT)

focal_lenght = 2.0
camera_center = vectors.Point3(0,0,0)


viewport_u = vectors.Vec3(viewport_width, 0, 0)
viewport_v = vectors.Vec3(0, -viewport_height, 0)

pixel_delta_u = viewport_u / IMAGE_WIDTH
pixel_delta_v = viewport_v / IMAGE_HEIGHT

viewport_upper_left = camera_center - vectors.Vec3(0, 0, focal_lenght) - viewport_u/2 - viewport_v/2
pixel00_loc = viewport_upper_left + (pixel_delta_u + pixel_delta_v) * 0.5

material_ground = material.Lambertian(color.Color(0.8,0.8,0.0))
material_center = material.Lambertian(color.Color(0.1,0.2,0.5))

world = hittable_list.HittableList()
world.add(sphere.Sphere(vectors.Vec3(0,0,-1), 0.25, material_center))
world.add(sphere.Sphere(vectors.Vec3(0,-100.25,-1), 100, material_ground))

def ray_color(r, depth, world):
    if depth <= 0:
        return color.Color(0,0,0)

    rec = world.hit(r, 0.001, math.inf)
    if rec != None:
        [attenuation, scattered] = rec.mat.scatter(r, rec)
        if attenuation != None:
            return attenuation * ray_color(scattered, depth - 1, world)
        else:
            return color.Color(0,0,0)
    unit_direction = vectors.unit_vector(r.direction())
    a = 0.5 * (unit_direction.y() + 1.0)
    return color.Color(1.0,1.0,1.0) * (1.0 - a) + color.Color(0.5, 0.7, 1.0) * a

def sample_square():
    return vectors.Vec3(random.random() - 0.5, random.random() - 0.5, 0)

def get_ray(i, j):
    offset = sample_square()
    pixel_sample = pixel00_loc + (pixel_delta_u * (i + offset.x())) + (pixel_delta_v * (j + offset.y()))
    ray_direction = pixel_sample - camera_center
    return ray.Ray(camera_center, ray_direction)


file = open("image_01.ppm", "w")
string = f"P3\n{IMAGE_WIDTH} {IMAGE_HEIGHT}\n255\n"
file.write(string)

for j in range(IMAGE_HEIGHT):
    print("Scanlines remaining:", (IMAGE_HEIGHT- j))
    for i in range(IMAGE_WIDTH):
        pixel_color = color.Color(0,0,0)
        for sample in range(samples_per_pixel):
            r = get_ray(i, j)
            pixel_color += ray_color(r,max_depth, world)
        color.write_color(file, pixel_color * pixel_samples_scale)

file.flush()
file.close()


print("Finished!!!")


    
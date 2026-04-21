## Ray tracing in python

### The tutorial i used
[Is](https://raytracing.github.io/books/RayTracingInOneWeekend.html). I had to translate the C++ to python at that point in life I had zero idea how C++ works but this helped to understand it later.

### Vectors
I had to write all of the vector operations my self when im thinking about this now I havo no ideea why we (me and my dad) did not use a library but we followed the tutorial so yeah

### How the code works
I wrote this a long time ago but basicly I had to create a camera and a 3d space. Than I had to code a ray so I could shoot the ray and see what it hit and based on that we chose the color of the pixel.
The code was really inefficient beacouse python is so slow and we had to check every pixel so we switched to pypy for it to be faster.

Also there are some cheap shadows that when a ray hits the same pixelr more times it gets darker and darker which creates an illusion of a shadow.

### Summary
This project was really had beacouse of my lack of knowledge of anything about this topic but with the help of my dad and the tutorial and countless hours worked on this I learned a lot of thing that are usefull now.
I may not have remembered evry detail of this project but it was a great learning experience + bonding with my dad. Also I know how fancy raytracing graphicks in games work. And I learned that python is really slow.


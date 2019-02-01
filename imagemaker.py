file = open ('image.ppm', 'w')
file.write ('P3\n500 500\n256')

for i in range(500):
    for n in range(500):
      file.write(i + ' ' + (i + n) + ' ' + (i * n))
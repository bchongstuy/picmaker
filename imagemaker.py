file = open ('image.ppm', 'w')
file.write ('P3\n500 500\n256\n')

for i in range(500):
    for n in range(500):
      file.write(str(i % 256) + ' ' + str((i + n) % 256) + ' ' + str((i * n) % 256) + ' ')
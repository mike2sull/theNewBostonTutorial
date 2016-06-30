fw = open('sample.txt', 'w')
fw.write('Writing some stuff in my text file!\n')
fw.write('And write something else on this line\n')
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
fr.close()

print(text)
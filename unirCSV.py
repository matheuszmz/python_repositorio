import os
import glob
#os.chdir("C:\\Users\\f7022470\\Downloads")

diretorio = os.getcwd()
output = '{}\\Output\\{}'.format(diretorio,'propostas.csv')

extension = 'csv'
all_files = [i for i in glob.glob('*.{}'.format(extension))]
text_file = []


for file in all_files:
    arquivo = open(file, 'r')
    for linha in arquivo.readlines():
        text_file.append(linha)
    arquivo.close()


head = text_file[0]
for file in text_file:
    try:
        text_file.remove(head)
    except:
        pass
text_file.insert(0, head)

saida = open(output, "w")
for line in text_file:
    saida.write(line)
saida.close()
print("Concluido")



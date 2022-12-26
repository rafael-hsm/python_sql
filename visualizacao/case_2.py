import os


bacterium = "16s_bacteria.fasta"
human = "18s_humano.fasta"

genome = os.getcwd() + os.sep + "visualizacao" + os.sep + "data_code" + os.sep + human

file_genome = open(genome).read()
output_file_genome = open(f"{human}.html", "w")

cont = {}

for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        cont[i+j] = 0

file_genome = file_genome.replace("\n", "")

for k in range(len(file_genome) -1):
    cont[file_genome[k] + file_genome[k + 1]] += 1

print(cont)

# HTML

i = 1
for k in cont:
    transparency = cont[k]/max(cont.values())
    output_file_genome.write("<div style='width:100px; border:1px solid #111; color:#fff; height:100px; float:left; background-color:rgba(0, 0, 0, "+str(transparency)+"')>"+k+"</div>")

    if i % 4 == 0:
        output_file_genome.write("<div style='clear:both'></div>")
    
    i += 1

output_file_genome.close()

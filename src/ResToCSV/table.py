import re

e6res = open("../../results/e7res.txt", "r")
table_dir = "results/"
pat = r'.*?\"(.*)".*'

#structure of the txt file
for i in range(2):
    print("skipped",e6res.readline()[:-1])
Lines = e6res.readlines()

table_columns = "Sequence, Sequence Full Name, Results, Starting, Hydrogenicity score\n"
e6table = open("../../results/e7table.csv", "a")
e6table.write(table_columns)

titleline = True
for line in Lines:
    if(len(line) == 1):
        continue
    text = line[:-1]
    
    if titleline:
        full_name = re.match(pat, text)
        full_name = str(full_name.group(1))
        text = text.replace('\"', '').split(' ')
        results = text[2]
        sequence = text[5]
        starting = text[len(text)-1]
        e6table.write(sequence + ', ' + full_name  + ', ' + results  + ', ' + starting + ', ')
        
    else:
        e6table.write(text + '\n')
    titleline = not titleline


e6table.close()
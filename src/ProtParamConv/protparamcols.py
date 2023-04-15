ifile = open('prot1.csv', 'r')
ofile = open('format.csv', 'w')
keys = 'A, R, N, D, C, Q, E, G, H, I, L, K, M, F, P, S, T, W, Y, V, O, U'.split(', ')
finalstr = ["" for i in range(len(keys))]

ofile.write('A, R, N, D, C, Q, E, G, H, I, L, K, M, F, P, S, T, W, Y, V, O, U\n')
for line in ifile:
    text = line
    text = text.replace('\n','')
    text = text.split(',')
    if(text[0] == 'B' or text[0] == 'Z' or text[0] == 'X'):
        continue
    ind = keys.index(text[0])
    formatnum = text[2].split('.')

    if(len(formatnum) == 1):
        finalstr[ind] = formatnum[0]
    else:
        finalstr[ind] = str(formatnum[0]) + '.' + str(formatnum[1][0:2])


for i in finalstr:
    ofile.write(i + ',')
ifile.close()
ofile.close()
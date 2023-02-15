from sys import stdin

res = {}
lista = []

line = stdin.readline()
while line:
    line = line.split()
    if line == '\n':
        lista.append(' ')
    else:
        line = [int(i) for i in line]
        lista.append(line)


for lelistas in lista:
    if lelistas == '':
        print()
    elif len(lelistas) != 9:
        continue
    else:
        total = sum(lelistas)
        res['BCG'] = total - lelistas[0] - lelistas[5] - lelistas[7]
        res['BGC'] = total - lelistas[0] - lelistas[4] - lelistas[8]
        res['CBG'] = total - lelistas[2] - lelistas[3] - lelistas[7]
        res['CGB'] = total - lelistas[2] - lelistas[4] - lelistas[6]
        res['GBC'] = total - lelistas[1] - lelistas[3] - lelistas[8]
        res['GCB'] = total - lelistas[1] - lelistas[5] - lelistas[6]

        print(min(res, key=res.get) + " " + str(res[min(res, key=res.get)]))

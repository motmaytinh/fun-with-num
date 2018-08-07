VECSIZE = 17
SYMBOLS = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}


def num2vec(num):
    vec = [0] * VECSIZE
    for i in range(len(num)):
        vec[VECSIZE - 1 -i] = SYMBOLS[num[i]]
    return vec


if __name__ == "__main__":
    data = open("data.csv","w")

    with open("chart.txt", 'r') as filehandle:
        for line in filehandle:
            lline = line.rstrip('\n').split('=')
            vec = num2vec(lline[1])
            data.write(lline[1] + ' ' + lline[0] + ' ' + ' '.join(str(x) for x in vec) + '\n')
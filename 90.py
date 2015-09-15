size = 7

matrix = [[ 0 for x in range(size) ] for x in range(size) ]

#--deklaracja elementu startowego--#
matrix[0][size/2] = 1

#--wypisywanie--#
def show():
    for i in range(size):
        #for j in range(size):
            print matrix[i]
        #print "\n"
show()


tmp = [0]*3

#90!!!!!1111111111
for i in range(0, size-1):#wiersze
    for j in range(1, size-1):#kolumny
        if (j-1)<0:
            tmp[0] = 0
        else:
            tmp[0] = matrix[i][j-1]
            
        tmp[1] = matrix[i][j]
        
        if j+1 > 5:
            tmp[2] = 0
        else:
            tmp[2] = matrix[i][j+1]
        #--switch--#
        # 1 0 0
        if tmp[0] == 1:
            if tmp[1] == 1:
                if tmp[2] == 0:
                    matrix[i+1][j] = 1
        # 0 1 1
        if tmp[0] == 1:
            if tmp[1] == 0:
                if tmp[2] == 0:
                    matrix[i+1][j] = 1
        # 0 1 0
        if tmp[0] == 0:
            if tmp[1] == 1:
                if tmp[2] == 1:
                    matrix[i+1][j] = 1

        # 0 0 1
        if tmp[0] == 0:
            if tmp[1] == 1:
                if tmp[2] == 0:
                    matrix[i+1][j] = 1
        # 0 0 1
        if tmp[0] == 0:
            if tmp[1] == 0:
                if tmp[2] == 1:
                    matrix[i+1][j] = 1
        #--switch off--#


print "\n"
show()

import numpy as np
import matplotlib.pyplot as plt

def rulerun(N, matrix):
    for i in range(N):
        for j in range(N):
            sum = matrix[i][(j+1)%N]+matrix[(i+1)%N][j]
            sum = sum+matrix[(i-1)%N][j]+matrix[i][(j-1)%N]+matrix[(i+1)%N][(j-1)%N]
            sum = sum+matrix[(i-1)%N][(j+1)%N]+matrix[(i+1)%N][(j+1)%N]+matrix[(i-1)%N][(j-1)%N]

            if(sum < 2 or sum > 3):
                matrix[i][j] = 0
            else:
                matrix[i][j] = 1


def main():
    maingrid = np.random.choice([0,1], 10*10, p=[0.5, 0.5]).reshape(10,10)
    for x in range(10):
        rulerun(10, maingrid)
        plt.imshow(maingrid)
        plt.show()
        plt.clf()
    return

main()
import matplotlib.pylab as plt
filename = './data.txt'
with open(filename) as f:
    lines = f.readlines()
    x = [line.split()[0] for line in lines]
    y = [line.split()[1] for line in lines]
    plt.plot(x, y, c='blue', lw=2)
    plt.show()

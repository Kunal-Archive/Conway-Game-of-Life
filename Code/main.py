import sys, argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ON = 255
OFF = 0
vals = [ON, OFF]

def randomGrid(N):
    """Returns a grid of NxN random valuse either  0 or  255"""
    return np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)

def addGlider(i, j, grid):
    """Adds a glider with top left cell at (i, j)"""
    glider = np.array([
        [0, 0, 255],
        [255, 0, 255],
        [0, 255, 255]
    ])
    grid[i:i+3, j:j+3] = glider

def addGosperGun(i, j, grid):
    """Adds a Gosper Gun Pattern """
    gosper = np.array([
        [0, 0, 255, 255, 0, 0, 0, 0],
        [0, 255, 0, 0, 0, 255, 0, 0],
        [255, 0, 0, 0, 0, 0, 255, 0],
        [255, 0, 0, 0, 255, 0, 255, 255],
        [255, 0, 0, 0, 0, 0, 255, 0],
        [0, 255, 0, 0, 0, 255, 0, 0],
        [0, 0, 255, 255, 0, 0, 0, 0],
    ])
    grid[i:i+7, j:j+8] = gosper

def readPattern(filepath):
    """Reads the pattern form the given text file and make the new array """
    with open(filepath, 'r') as file:
        M = int(file.readline())
        newpattern = np.zeros((M, M), dtype=int).reshape(M, M)

        for i in range(M):
            fullline = file.readline()
            each = fullline.split(" ")
            for j in range(M):
                newpattern[i, j] = each[j]
    
    return newpattern
        
def pattern(array, i, j, grid):
    """Add the given pattern to the grid by using ayyay form txt file"""
    shape = array.shape
    grid[i:i+(shape[0]), j:j+(shape[1])] = array

def update(frameNum, img, grid, N):
    # Copy grid since we require 8 neigbors for calculation
    # and we go line by line

    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            # compute 8 neigbors sum using toroidal boundary condition
            # x and y wraps around so that the simulation 
            # takes place on a toroidal surface
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N]+
                        grid[(i-1)%N,j] + grid[(i+1)%N, j]+
                        grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N]+
                        grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255)
            
            #apply conway's rule
            if grid[i, j] == ON:
                if(total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON

    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,
        
def main():
    #command line arguments are in sys.argv[1], sys.argv[2], ...
    #sys.argv[0] is the script name and can be ignored
    #parse argument
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life simulation.")

    # add arguments
    parser.add_argument('--grid-size', dest='N', required=False)  
    parser.add_argument('--mov-file', dest='movfile', required=False)
    parser.add_argument('--interval', dest='interval', required=False)
    parser.add_argument('--glider', action='store_true', required=False)
    parser.add_argument('--gosper', action='store_true', required=False)
    parser.add_argument('--pattern-file', dest='txt', required=False)
    
    args = parser.parse_args()

    # set the grid
    N = 100
    if args.N and (int(args.N) > 8):
        N = int(args.N)

    # set the animation update interval
    updateInterval = 50
    if args.interval:
        updateInterval = int(args.interval)

    # declare grid
    grid = np.array([])
    #check if glider demo flag is specified
    if args.glider:
        grid = np.zeros((N, N), dtype=int)
        addGlider(1, 1, grid)
    elif args.txt:
        txt = args.txt
        array = readPattern(txt)
  
        grid = np.zeros((N, N), dtype=int)
        pattern(array,1, 1, grid)
    elif(args.gosper):
        grid = np.zeros((N, N), dtype=int)
        addGosperGun(1, 1, grid)
    else:
        # populate grid with random on/off - more off than on
        grid = randomGrid(N)

    # set up the animation 
    fig, ax = plt.subplots()

    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ),
                                frames=10,
                                interval=updateInterval,
                                save_count = 50)

    # set the output file
    if args.movfile:
        ani.save(args.movfile, fps=30, extra_args=['-vcodec', 'libx264'])

    plt.show()

#call the main
if __name__=='__main__':
    main()


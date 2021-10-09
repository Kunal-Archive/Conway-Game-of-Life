# set the grid
N = 100
if args.N and (args.N > 8):
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
    addlgider(1, 1, grid)
else:
    # populate grid with random on/off - more off than on
    grid = randomGrid(N)
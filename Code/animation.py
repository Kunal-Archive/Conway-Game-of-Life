# set up the animation 
fig, ax = plt.subplot()

img = ax.imshow(grid, interpolation='nearest')
ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ),
                                frames=10,
                                interval=updateInterval,
                                save_count = 50)

# set the output file
if args.movfile:
    ani.save(args.movfile, fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()


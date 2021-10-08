#apply conway's rule
if grid[i, j] == ON:
    if(total<2) or (total >3):
        newgrid[i, j] = OFF
else: #it is off
    if total==3:
        newgrid[i, j] = ON
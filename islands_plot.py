from get_land_neighbors import get_land_neighbors

def islands_plot(a):

	num_islands = 0
	seen = []
	grid = len(a)
	colums = len(a[0])
	for i in range(grid):
		for j in range(colums):
			if a[i][j] and (i,j) not in seen:
				seen.append(a[i][j])
				num_islands += 1
				neighbors = get_land_neighbors(i,j, grid)
				while neighbors:
					current = neighbors.pop()
					if current in seen:
						continue
					else:
						neighbors.extend(get_land_neighbors(current))
						seen.append(current)

print(islands_plot([[1,1,0],
					[0,1,0],
					[0,0,1],
					[1,1,0],
					[1,1,1]]))
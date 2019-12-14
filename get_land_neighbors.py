def get_land_neighbors(i, j, grid):
	""" returns list of neighbor's positions """
	output = []
	for ni, nj in [(i+1, j),(i-1, j),(i, j+1),(i, j-1)]:
		if(0 <= ni <= len(grid) and 0 <= nj < len(grid[0]) and grid[ni, nj]):
			output.append(ni, nj)
		return output
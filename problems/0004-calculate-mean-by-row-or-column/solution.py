import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	arr = np.array(matrix)
	axis = int(mode == "row")

	means = np.mean(arr, axis)

	return means
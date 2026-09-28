def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
    if len(a) != len(b):
        return -1
    
    temp_list: list = []
    final_list: list = []
    for col in a:
        for i in range(0, len(a)):
            temp_list.append(col[i] * b[i])
        final_list.append(sum(temp_list))
        temp_list.clear()
	return final_list



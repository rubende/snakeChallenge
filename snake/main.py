

def next_step(board, snake, depth, last_step):

	coordinate_steps = [[0, 1], [1, 0], [0, -1], [-1, 0]]					# Cordinates representing each possible step

	new_head = [sum(n) for n in zip(snake[0], last_step)]					
	if (0 <= new_head[0] < board[0] and 0 <= new_head[1] < board[1] 			# Check if new head position is on the table
			and new_head not in snake[:-1]):					# Check if new head position is not on the previous snae position (except tail)
		remove_step = (coordinate_steps.index(last_step) + 2)%4				# Remove step that return to previously position
		coordinate_steps.pop(remove_step)
		new_snake = [new_head] + snake[:-1]						# New snake body position
		if depth == 1:									# If we have reached the end of the valid path, we consider it correct
			return 1
		else:										# If we have not reached the end of the path, next step
			return (next_step(board, new_snake, depth-1, coordinate_steps[0]) + next_step(board, new_snake, depth-1, coordinate_steps[1]) + next_step(board, new_snake, depth-1, coordinate_steps[2]));
	else:		
		return 0		


def numberOfAvailableDifferentPaths(board, snake, depth):
	"""
	Search how many valids paths of length p can the snake make on the board
	Args:
		board: array describing the dimensions of 
			the board. [row, columns].
 		snake: array that describes the configuration 
 			of the snake's body on the board. From 
 			head (position 0) to tail (position -1).
		depth: integer with paths depth.
	Returns:
		Number of valids paths.
	"""

	# Check that board is a list
	if not isinstance(board, list):																					
		raise TypeError('Error type: {} for board whereas list is expected'.format(type(board))) 

	# Check that snake is a list
	if not isinstance(snake, list):
		raise TypeError('Error type: {} for snake whereas list is expected'.format(type(snake))) 

	# Check that depth is a int
	if not isinstance(depth, int):
		raise TypeError('Error type: {} for depth whereas int is expected'.format(type(depth))) 


	coordinate_steps = [[0, 1], [1, 0], [0, -1], [-1, 0]]					# Cordinates representing each possible step

	remove_step = [snake[1][0] - snake[0][0], snake[1][1] - snake[0][1]]			# Remove step with the following snake body part
	coordinate_steps.pop(coordinate_steps.index(remove_step))


	return (next_step(board, snake, depth, coordinate_steps[0]) +				# Possible next steps
           next_step(board, snake, depth, coordinate_steps[1]) +
           next_step(board, snake, depth, coordinate_steps[2]));



if __name__ == '__main__':

	# Initialization and execution of the proposed tests

	# Test 1
	board_1 = [4, 3]
	snake_1 = [[2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [0, 0]]
	depth_1 = 3


	print("Test 1 Result: {}".format(numberOfAvailableDifferentPaths(board_1, snake_1, depth_1)))

	# Test 2
	board_2 = [2, 3]
	snake_2 = [[0, 2], [0, 1], [0, 0], [1, 0], [1, 1], [1, 2]]
	depth_2 = 10

	print("Test 2 Result: {}".format(numberOfAvailableDifferentPaths(board_2, snake_2, depth_2)))

	# Test 3
	board_3 = [10, 10]
	snake_3 = [[5, 5], [5, 4], [4, 4], [4, 5]]
	depth_3 = 4

	print("Test 1 Result: {}".format(numberOfAvailableDifferentPaths(board_3, snake_3, depth_3)))

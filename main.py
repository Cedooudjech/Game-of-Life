import numpy
import os
import time

frame = numpy.array([[0, 0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0, 0],
					[0, 0, 1, 1, 1, 0, 0],
					[0, 0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0, 0]])

def compute_number_of_neighbors(padded_frame, index_row, index_column):
	number_of_neighbors = 0
	for i in range(-1, 2):
		for j in range(-1, 2):
			if (i == 0 and j == 0):
				continue
			number_of_neighbors += padded_frame[index_row + i, index_column + j]
	return number_of_neighbors


def compute_next_frame(frame):
	padded_frame = numpy.pad(frame, 1, mode='constant') 
	new_frame = frame.copy()

	for i in range(1, padded_frame.shape[0] - 1):
		for j in range(1, padded_frame.shape[1] - 1):
			number_of_neighbors = compute_number_of_neighbors(padded_frame, i, j)
			if padded_frame[i, j] == 1:
				if number_of_neighbors < 2 or number_of_neighbors > 3:
					new_frame[i - 1, j - 1] = 0
				else:
					new_frame[i - 1, j - 1] = 1
			else:
				if number_of_neighbors == 3:
					new_frame[i - 1, j - 1] = 1
				else:
					new_frame[i - 1, j - 1] = 0

	return new_frame


while True:
	print(frame)
	frame = compute_next_frame(frame)
	time.sleep(0.5)
	os.system('cls' if os.name == 'nt' else 'clear')
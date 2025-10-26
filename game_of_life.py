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

def compute_number_of_neighbors(paded_frame, index_row, index_column):
	return number_of_neighbors


def compute_next_frame(frame):

	paded_frame = numpy.pad(frame, 1, mode="constant")

	return frame


while True :
	print(frame)
	time.sleep(1)
	os.system("cls")
	compute_next_frame(frame)
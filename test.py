import os
starting_value = 1


file_name = 'A:\Coding_and_Scripting\Miniconda3\_PROJECTS\pygta5-master\training_data-{}.npy'.format(starting_value)

if os.path.isfile(file_name):
	print('File exists, moving along',starting_value)
	starting_value += 1
else:
	print(ValueError)
	print('File does not exist, starting fresh!',starting_value)
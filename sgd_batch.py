from numpy import random



def get_mini_batches(X, Y, batch_size):
	random_idxs = random.choice(len(Y), len(Y), replace=False)
	x_shuffled = X[random_idxs, :]
	y_shuffled = Y[random_idxs]

	mini_batches = [(x_shuffled[i:i+batch_size, :], y_shuffled[i:i+batch_size])
					for i in range(0, len(Y), batch_size)]

	return mini_batches

















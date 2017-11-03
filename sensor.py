import numpy as np
import scipy.spatial

########################################################################
#########  Data Generating Functions ###################################
########################################################################
def generate_sensors(k = 7, d = 2):
	"""
	Generate sensor locations. 
	Input:
	k: The number of sensors.
	d: The spatial dimension.
	Output:
	sensor_loc: k * d numpy array.
	"""
	sensor_loc = 100*np.random.randn(k,d)
	return sensor_loc

def generate_data(sensor_loc, k = 7, d = 2, 
				 n = 1, original_dist = True):
	"""
	Generate the locations of n points.  

	Input:
	sensor_loc: k * d numpy array. Location of sensor. 
	k: The number of sensors.
	d: The spatial dimension.
	n: The number of points.
	original_dist: Whether the data are generated from the original 
	distribution. 

	Output:
	obj_loc: n * d numpy array. The location of the n objects. 
	distance: n * k numpy array. The distance between object and 
	the k sensors. 
	"""
	assert k, d == sensor_loc.shape

	obj_loc = 100*np.random.randn(n, d)
	if not original_dist:
	   obj_loc += 1000
	   
	distance = scipy.spatial.distance.cdist(obj_loc, 
										   sensor_loc, 
										   metric='euclidean')
	distance += np.random.randn(n, k)  
	return obj_loc, distance 











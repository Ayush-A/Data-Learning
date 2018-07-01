from numpy import *

# Performing Gradient Descent
def gradient_descent(b_current, m_current, points, learning_rate):
	b_gradient = 0
	m_gradient = 0
	N = float(len(points))
	for i in range(0, len(points)):
		x = points[i, 0]
		y = points[i, 1]
		b_gradient += -(2/N) * (y - (m_current * x + b_current))
		m_gradient += -(2/N) * x * (y - (m_current * x + b_current))
	new_b = b_current - (learning_rate * b_gradient)
	new_m = m_current - (learning_rate * m_gradient)
	return [new_b, new_m]

# Computing Sum of Square Error
def ssError(b, m, points):
	totalError = 0
	for i in range(0, len(points)):
		x = points[i, 0]
		y = points[i, 1]
		totalError += (y - (m * x + b)) ** 2
	return totalError / float(len(points))

def main():

    # Read x and y values from the dataset and store them as an array in points.
	points = genfromtxt("data.csv", delimiter=",")

	# Hyperparameter (How fast our model learns)
	learning_rate = 0.0001

	# y = mx + b
	b = 0
	m = 0
	num_iterations = 1000

	print("Before Gradient Descent: b: {}, m: {}, Error: {}".format(b, m, ssError(b, m, points)))

	# Iteratively calculating new slope and y-intercepts for each row in the dataset.
	for i in range(num_iterations):
		b, m = gradient_descent(b, m, array(points), learning_rate)

	print("After Gradient Descent: b: {}, m: {}, Error: {}".format(b, m, ssError(b, m, points)))

if __name__ == "__main__":
	main()
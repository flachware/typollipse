def bezier(a, b, c, d, t):
	return a * pow((1 - t), 3) + 3 * b * pow((1 - t), 2) * t + 3 * c * (1 - t) * pow(t, 2) + d * pow(t, 3)

def bezier_prime(a, b, c, d, t):
	return -3 * a * pow((1 - t), 2) + 3 * b * pow((1 - t), 2) - 6 * b * (1 - t) * t + 6 * c * (1 - t) * t - 3 * c * pow(t, 2) + 3 * d * pow(t, 2)

def bezier_second(a, b, c, d, t):
	return 6 * a * (1 - t) - 6 * b * (1 - t) - 6 * b * (1 - t) + 6 * b * t + 6 * c * (1 - t) - 6 * c * t - 6 * c * t + 6 * d * t

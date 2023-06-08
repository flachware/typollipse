from bezier import bezier, bezier_prime, bezier_second


def getCurvature(self, anisotropy, segment):
	precision = 6
	p1 = (segment[0].position[0], segment[0].position[1])
	p4 = (segment[3].position[0], segment[3].position[1])
	self.logToConsole(p1)
	self.logToConsole(p4)
	
	def curvature(x1, x2, x3, x4, y1, y2, y3, y4, t):
		x_1 = bezier_prime(x1, x2, x3, x4, t)
		y_1 = bezier_prime(y1, y2, y3, y4, t)
		x_2 = bezier_second(x1, x2, x3, x4, t)
		y_2 = bezier_second(y1, y2, y3, y4, t)
		curvature = (x_1 * y_2 - x_2 * y_1) / pow((pow(x_1, 2) + pow(y_1, 2)), 3 / 2)

		return curvature * -1


	def max_curvature(points):
		t1 = 0
		t4 = 1
		max_curvature = 0
		searching = True

		while searching == True:
			t2 = 2 * t1 / 3 + t4 / 3
			t3 = t1 / 3 + 2 * t4 / 3

			c_t2 = curvature(points['x1'], points['x2'], points['x3'], points['x4'], points['y1'], points['y2'], points['y3'], points['y4'], t2)
			c_t3 = curvature(points['x1'], points['x2'], points['x3'], points['x4'], points['y1'], points['y2'], points['y3'], points['y4'], t3)

			if c_t2 > c_t3:
				t4 = t3

			elif c_t3 > c_t2:
				t1 = t2

			elif c_t2 == c_t3:
				t1 = t2
				t4 = t3

			current_curvature = max(c_t2, c_t3)

			if round(current_curvature, precision * 2) == round(max_curvature, precision * 2):
				searching = False

			max_curvature = current_curvature

		return max_curvature


	def create_points(p1, p4, superness):
		width = abs(p4[0] - p1[0])
		height = abs(p4[1] - p1[1])
		
		if height >= width:
			height = height * (1 + anisotropy)
		
		else:
			width = width * (1 + anisotropy)
		
		d = dict()

		d['x1'] = 0
		d['x2'] = superness * width
		d['x3'] = width
		d['x4'] = width

		d['y1'] = height
		d['y2'] = height
		d['y3'] = superness * height
		d['y4'] = 0

		return d


	def min_curvature(p1, p4):
		c1 = 0.5522847498307936
		c4 = 1
		superness = 0
		searching = True

		while searching == True:
			c2 = 2 * c1 / 3 + c4 / 3
			c3 = c1 / 3 + 2 * c4 / 3

			cv_c2 = max_curvature(create_points(p1, p4, c2))
			cv_c3 = max_curvature(create_points(p1, p4, c3))

			if cv_c2 < cv_c3:
				c4 = c3
				current_cv = c2

			elif cv_c3 < cv_c2:
				c1 = c2
				current_cv = c3

			elif cv_c2 == cv_c3:
				c1 = c2
				c4 = c3
				current_cv = c2
			
			#self.logToConsole(current_cv)
			
			if round(current_cv, precision) == round(superness, precision):
				searching = False

			superness = current_cv

		return superness


	return min_curvature(p1, p4)

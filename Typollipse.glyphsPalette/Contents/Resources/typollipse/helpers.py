from GlyphsApp import Glyphs, CURVE
from .algorithm import getCurvature
from AppKit import NSPoint

def getPaths(self):
	paths = []

	for layer in Glyphs.font.selectedLayers:
		for path in layer.paths:
			nodes = []
			segments = []

			# Get selected curve nodes only
			for node in path.nodes:
				if node.selected is True and node.type == CURVE:
					nodes.append(node)

			for node in nodes:
				segment = []

				# Get all nodes of the segment
				for i in range(3, -1, -1):
					n = path.nodes[node.index - i]

					# Check if the nodes are selected
					if n.selected is True:
						segment.append(n)

				# Check if the segment is complete
				if len(segment) == 4:
					segments.append(segment)

			# Check if the path has a selected segment
			if len(segments) != 0:
				paths.append(segments)

	return paths


def update(self, anisotropy, paths):
	for path in paths:
		for segment in path:
			width = abs(segment[3].position[0] - segment[0].position[0])
			height = abs(segment[3].position[1] - segment[0].position[1])
			curvature = getCurvature(self, anisotropy, segment)
			xDirection = None
			yDirection = None
			x1Direction = None
			y1Direction = None
			x2Direction = None
			y2Direction = None

			# Up
			if segment[3].position[0] > segment[0].position[0]:
				xDirection = 1

			# Down
			if segment[3].position[0] < segment[0].position[0]:
				xDirection = -1

			# Right
			if segment[3].position[1] > segment[0].position[1]:
				yDirection = 1

			# Left
			if segment[3].position[1] < segment[0].position[1]:
				yDirection = -1

			# Node 1 is a horizontal tangent
			if segment[1].position[0] != segment[0].position[0] and segment[1].position[1] == segment[0].position[1]:
				x1Direction = 1
				y1Direction = 0

			# Node 1 is a vertical tangent
			if segment[1].position[0] == segment[0].position[0] and segment[1].position[1] != segment[0].position[1]:
				x1Direction = 0
				y1Direction = 1

			# Node 2 is a horizontal tangent
			if segment[2].position[0] != segment[3].position[0] and segment[2].position[1] == segment[3].position[1]:
				x2Direction = 1
				y2Direction = 0

			# Node 2 is a vertical tangent
			if segment[2].position[0] == segment[3].position[0] and segment[2].position[1] != segment[3].position[1]:
				x2Direction = 0
				y2Direction = 1

			# Check if the segment has valid coordinates
			if all(v is not None for v in [xDirection, yDirection, x1Direction, y1Direction, x2Direction, y2Direction]):
				x1 = segment[0].position[0] + width * curvature * xDirection * x1Direction
				y1 = segment[0].position[1] + height * curvature * yDirection * y1Direction
				x2 = segment[3].position[0] - width * curvature * xDirection * x2Direction
				y2 = segment[3].position[1] - height * curvature * yDirection * y2Direction

				segment[1].position = NSPoint(x1, y1)
				segment[2].position = NSPoint(x2, y2)

			else:
				# Inform user that there is an invalid segment
				pass

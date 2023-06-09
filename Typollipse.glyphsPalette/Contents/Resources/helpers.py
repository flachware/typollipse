from GlyphsApp import *
from GlyphsApp.plugins import *
from algorithm import getCurvature


def getPaths(self):
	paths = []
	
	for layer in Glyphs.font.selectedLayers:
		for path in layer.paths:
			nodes = []
			segments = []
			
			# Get selected curve nodes only
			for node in path.nodes:
				if node.selected is True and node.type is 'curve':
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
				if len(segment) is 4:
					segments.append(segment)
			
			# Check if the path has a selected segment
			if len(segments) is not 0:
				paths.append(segments)
	
	return paths


def update(self, anisotropy, paths):
	for path in paths:
		for segment in path:
			width = abs(segment[3].position[0] - segment[0].position[0])
			height = abs(segment[3].position[1] - segment[0].position[1])
			curvature = getCurvature(self, anisotropy, segment)
			
			xDirection = 1 if segment[3].position[0] > segment[0].position[0] else -1
			yDirection = 1 if segment[3].position[1] > segment[0].position[1] else -1

			if segment[1].position[0] != segment[0].position[0]:
				x1Direction = 1
				y1Direction = 0
			else:
				x1Direction = 0
				y1Direction = 1

			if segment[2].position[0] != segment[3].position[0]:
				x2Direction = 1
				y2Direction = 0
			else:
				x2Direction = 0
				y2Direction = 1

			x1 = segment[0].position[0] + width * curvature * xDirection * x1Direction
			y1 = segment[0].position[1] + height * curvature * yDirection * y1Direction
			x2 = segment[3].position[0] - width * curvature * xDirection * x2Direction
			y2 = segment[3].position[1] - height * curvature * yDirection * y2Direction

			segment[1].position = NSPoint(x1, y1)
			segment[2].position = NSPoint(x2, y2)

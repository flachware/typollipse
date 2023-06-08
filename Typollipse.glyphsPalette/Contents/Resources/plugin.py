from __future__ import division, print_function, unicode_literals
import objc
from GlyphsApp import *
from GlyphsApp.plugins import *
from helpers import getPaths, update


class typollipse (PalettePlugin):
	dialog = objc.IBOutlet()
	textField = objc.IBOutlet()
	anisotropy = 0
	
	@objc.python_method
	def settings(self):
		self.name = Glyphs.localize({
			'en': 'Typollipse',
			'de': 'Typollipse',
			'fr': 'Typollipse',
			'es': 'Tipolipse',
			'pt': 'Tipolipse',
			})

		# Load .nib dialog (without .extension)
		self.loadNib('IBdialog', __file__)
	
	@objc.python_method
	def start(self):
		Glyphs.addCallback(self.opened, DOCUMENTOPENED)
		Glyphs.addCallback(self.closed, DOCUMENTCLOSED)
	
	@objc.python_method
	def opened(self, sender):
		anisotropy = self.windowController().document().font.userData['anisotropy']
		
		if anisotropy is not None:
			self.anisotropy = anisotropy
		
		self.textField.setFloatValue_(self.anisotropy)
	
	@objc.python_method
	def closed(self, sender):
		Glyphs.removeCallback(self.opened)
		Glyphs.removeCallback(self.closed)

	@objc.python_method
	def __del__(self):
		Glyphs.removeCallback(self.opened)
		Glyphs.removeCallback(self.closed)

	@objc.IBAction
	def setAnisotropy_(self, sender):
		self.anisotropy = sender.floatValue()
		Glyphs.font.userData['anisotropy'] = self.anisotropy
	
	@objc.IBAction
	def handleClick_(self, sender):
		paths = getPaths(self)
		
		update(self, self.anisotropy, paths)
	
	@objc.python_method
	def __file__(self):
		return __file__

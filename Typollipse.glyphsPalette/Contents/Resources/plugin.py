# encoding: utf-8

###########################################################################################################
#
#
#	Palette Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Palette
#
#
###########################################################################################################

from __future__ import division, print_function, unicode_literals
import objc
from GlyphsApp import *
from GlyphsApp.plugins import *

class typollipse (PalettePlugin):

	dialog = objc.IBOutlet()
	textField = objc.IBOutlet()
	
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

	@objc.IBAction
	def setAnisotropy_(self, sender):
		self.logToConsole(sender.floatValue())
	
	@objc.IBAction
	def setCurvature_(self, sender):
		self.logToConsole('Button clicked')

	@objc.python_method
	def __file__(self):
		return __file__

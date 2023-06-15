from __future__ import division, print_function, unicode_literals
import objc
from GlyphsApp import *
from GlyphsApp.plugins import *
from helpers import getPaths, update


class typollipse (PalettePlugin):
	dialog = objc.IBOutlet()
	label = objc.IBOutlet()
	textField = objc.IBOutlet()
	button = objc.IBOutlet()
	anisotropy = 0
	
	@objc.python_method
	def settings(self):
		self.name = Glyphs.localize({
			'en': 'Typollipse',
			'cs': 'Typolipsa',
			'de': 'Typollipse',
			'es': 'Tipolipse',
			'fr': 'Typollipse',
			'it': 'Tipollisse',
			'pt': 'Tipolipse',
			'ru': 'Типоллипс',
			'tr': 'Tipolips',
			})

		# Load .nib dialog (without .extension)
		self.loadNib('IBdialog', __file__)
	
	@objc.python_method
	def start(self):
		self.label.setStringValue_(Glyphs.localize({
			'en': 'Anisotropy:',
			'cs': 'Anizotropie',
			'de': 'Anisotropie:',
			'es': 'Anisotropía',
			'fr': 'Anisotropie',
			'it': 'Anisotropia',
			'pt': 'Anisotropia',
			'ru': 'Анизотропия',
			'tr': 'Anizotropi',
			}))
		
		self.button.setTitle_(Glyphs.localize({
			'en': 'Apply',
			#'cs': 'Apply', todo
			'de': 'Anwenden',
			'es': 'Aplicar',
			'fr': 'Appliquer',
			'it': 'Applica',
			'pt': 'Aplicar',
			'ru': 'Применить',
			'tr': 'Uygula',
			}))
		
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

		if paths:
			update(self, self.anisotropy, paths)

		else:
			# Inform user that there is no valid selection
			pass

	@objc.python_method
	def __file__(self):
		return __file__

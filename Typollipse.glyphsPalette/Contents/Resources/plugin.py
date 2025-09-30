from __future__ import division, print_function, unicode_literals
import objc
from GlyphsApp import Glyphs
from GlyphsApp.plugins import PalettePlugin
from typollipse.helpers import getPaths, update
from typollipse.strings import pluginName, labelTitle, buttonTitle


class typollipse(PalettePlugin):
	dialog = objc.IBOutlet()
	label = objc.IBOutlet()
	textField = objc.IBOutlet()
	button = objc.IBOutlet()
	anisotropy = 0

	@objc.python_method
	def settings(self):
		self.name = Glyphs.localize(pluginName)

		# Load .nib dialog (without .extension)
		self.loadNib('IBdialog', __file__)

	@objc.python_method
	def start(self):
		self.label.setStringValue_(Glyphs.localize(labelTitle))
		self.button.setTitle_(Glyphs.localize(buttonTitle))

	@objc.typedSelector(b'v@:@') # void, self, SEL, id
	def setWindowController_(self, windowController):
		try:
			self._windowController = windowController
		except:
			LogError(traceback.format_exc())
		if not windowController:
			return

		anisotropy = windowController.document().font.userData['anisotropy']

		if anisotropy is not None:
			self.anisotropy = anisotropy

		self.textField.setFloatValue_(self.anisotropy)

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

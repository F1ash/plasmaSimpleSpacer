# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyKDE4.kdeui import KIntSpinBox
from PyKDE4.kdecore import KGlobal
from PyKDE4.plasma import Plasma
from PyKDE4 import plasmascript
import os.path

class plasmaSpacer(plasmascript.Applet):
	def __init__(self, parent = None):
		plasmascript.Applet.__init__(self, parent)

		self.kdehome = unicode(KGlobal.dirs().localkdedir())
		self.iconPath = self.kdehome + '/share/apps/plasma/plasmoids/plasmaSimpleSpacer/contents/icons/Spacer.png'
		self.icon = Plasma.IconWidget()
		self.icon.setIcon(self.iconPath)

	def init(self):
		self.setImmutability(Plasma.Mutable)
		self.layout = QGraphicsLinearLayout(self.applet)
		self.layout.setSpacing(0)
		multiplier = self.config().readEntry('Multiplier', QString('5')).toInt()[0]

		if self.formFactor() == Plasma.Horizontal :
			self.layout.setOrientation(Qt.Horizontal)
			self.size_ = self.config().readEntry('Width', QString('20')).toInt()[0], 20
			val = (self.size_[0] - 20) / multiplier
			self.Control = ControlWidget(Qt.Horizontal, self, multiplier, val)
		else :
			self.layout.setOrientation(Qt.Vertical)
			self.size_ = 20, self.config().readEntry('Height', QString('20')).toInt()[0]
			val = (self.size_[1] - 20) / multiplier
			self.Control = ControlWidget(Qt.Vertical, self, multiplier, val)

		self.setLayout(self.layout)
		self.setMinimumSize(self.size_[0], self.size_[1])
		self.resize(self.size_[0], self.size_[1])

		Plasma.ToolTipManager.self().setContent( self.applet, Plasma.ToolTipContent( \
								self.Control.slider.toolTip(), \
								QString(''), self.icon.icon() ) )

	def mouseDoubleClickEvent(self, ev):
		ev.ignore()
		if self.Control.isVisible() :
			self.Control.hide()
		else:
			self.Control.move(self.popupPosition(self.Control.size()))
			self.Control.show()

class ControlWidget(Plasma.Dialog):
	def __init__(self, orient = Qt.Horizontal, obj = None, factor = 5, val_ = 1, parent = None):
		Plasma.Dialog.__init__(self, parent)
		self.prnt = obj
		self.orient = orient
		self.factor = factor

		self.slider = QSlider()
		self.slider.setOrientation(self.orient)
		self.slider.setValue(val_)
		self.slider.setToolTip('plasmaSimpleSpacer')
		self.slider.valueChanged.connect(self.resizeSpacer)
		self.multiplier = KIntSpinBox(1, 20, 1, self.factor, self)
		self.multiplier.setToolTip('Multiplier')
		self.multiplier.setMaximumWidth(40)
		self.multiplier.valueChanged.connect(self.multiplierValue)
		self.layout = QGridLayout()
		self.layout.setSpacing(0)
		self.layout.addWidget(self.slider, 0, 0)
		if self.prnt.formFactor() == Plasma.Horizontal :
			self.layout.addWidget(self.multiplier, 0, 1)
		else :
			self.layout.addWidget(self.multiplier, 1, 0)
		self.setLayout(self.layout)

	def multiplierValue(self, val):
		self.prnt.config().writeEntry('Multiplier', val)
		self.factor = val

	def resizeSpacer(self, vol):
		if self.prnt.formFactor() == Plasma.Horizontal :
			self.prnt.size_ = 20 + vol * self.factor, 20
		else :
			self.prnt.size_ = 20, 20 + vol * self.factor
		self.prnt.setMinimumSize(self.prnt.size_[0], self.prnt.size_[1])
		self.prnt.resize(self.prnt.size_[0], self.prnt.size_[1])
		self.prnt.config().writeEntry('Width', self.prnt.size_[0])
		self.prnt.config().writeEntry('Height', self.prnt.size_[1])
		self.prnt.setLayout(self.prnt.layout)

def CreateApplet(parent):
	return plasmaSpacer(parent)

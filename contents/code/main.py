# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
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
		self.layout.setSpacing(10)
		self.slider = Plasma.Slider()
		self.slider.setToolTip('plasmaSimpleSpacer')
		self.layout.setAlignment(self.slider, Qt.AlignCenter)
		self.slider.hide()

		if self.formFactor() == Plasma.Horizontal :
			self.layout.setOrientation(Qt.Horizontal)
			self.slider.setOrientation(Qt.Horizontal)
			self.size_ = self.config().readEntry('Width', QString('20')).toInt()[0], self.geometry().height()
		else :
			self.layout.setOrientation(Qt.Vertical)
			self.slider.setOrientation(Qt.Vertical)
			self.size_ = self.geometry().width(), self.config().readEntry('Height', QString('20')).toInt()[0]

		#print self.size_[0], self.size_[1]
		#with open('/dev/shm/plasmaSimpleSpacer.data', 'wb') as f :
		#	f.write(str(self.size_[0]) + ' ' + str(self.size_[1]) + '\n')
		self.setLayout(self.layout)
		self.setMinimumSize(self.size_[0], self.size_[1])
		self.resize(self.size_[0], self.size_[1])

		Plasma.ToolTipManager.self().setContent( self.applet, Plasma.ToolTipContent( \
								self.slider.toolTip(), \
								QString(''), self.icon.icon() ) )

	def mouseDoubleClickEvent(self, ev):
		ev.ignore()
		if self.slider.isVisible() :
			self.slider.valueChanged.disconnect(self.resizeSpacer)
			self.slider.hide()
			self.layout.removeItem(self.slider)
		else:
			self.layout.addItem(self.slider)
			self.slider.setMaximumSize(self.size_[0] / 2, self.size_[1] / 2)
			self.slider.show()
			self.slider.valueChanged.connect(self.resizeSpacer)
			self.setMinimumSize(self.size_[0], self.size_[1])
			self.resize(self.size_[0], self.size_[1])
		self.setLayout(self.layout)

	def resizeSpacer(self, vol):
		if self.formFactor() == Plasma.Horizontal :
			self.size_ = 20 + vol * 5.0, 20
		else :
			self.size_ = 20, 20 + vol * 5.0
		#self.slider.setMaximumSize(20,20)
		self.slider.setMaximumSize(self.size_[0] / 2, self.size_[1] / 2)
		self.setMinimumSize(self.size_[0], self.size_[1])
		self.resize(self.size_[0], self.size_[1])
		self.config().writeEntry('Width', self.size_[0])
		self.config().writeEntry('Height', self.size_[1])
		# with open('/dev/shm/plasmaSimpleSpacer.data', 'a') as f :
		#	f.write(str(self.size_[0]) + ' ' + str(self.size_[1]) + '\n')

def CreateApplet(parent):
	return plasmaSpacer(parent)

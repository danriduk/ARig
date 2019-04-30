'''
fk joint chain class
'''

import maya.cmds as mc
from . import jointChain, controls, utils


class fkChain(jointChain.jntChain):
	def __init__(
		self,
		prefix='c',
		name='fkChain',
		shape='circle',
		color='auto',
		posList=[(0,0,0)]
		):

		# init parent class
		jointChain.jntChain.__init__(self,
								prefix=prefix,
								name=name,
								suffix='jnt'
								)

		self.prefix = prefix
		self.name = name
		self.shape = shape
		self.color = color

		self.posList = posList

		# global members
		self.cons = []

	def build(self):
		# call parent class build method
		jointChain.jntChain.build(self, pos=self.posList)

		# build
		self._addControls()

	def _addControls(self):
		if len(self.jnts) < 1:
			return

		conGrps = []
		for jnt in self.jnts:
			fkCon = controls.Control(
						prefix=self.prefix,
						name=self.name,
						suffix='con',
						shape=self.shape,
						translateTo=jnt,
						rotateTo=jnt,
						color=self.color
						)

			conGrps.append(fkCon.grps[0])
			self.cons.append(fkCon.con)

			# constrain joint too control
			mc.parentConstraint(fkCon.con, jnt)

	def _fkParenting(self):
		pass

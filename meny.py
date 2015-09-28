




//все выделеные риды старт эт 1
def allStartFramesToOne():
	for node in nuke.selectedNodes():
	    node.knob('frame').setValue('1')
	    node.knob('frame_mode').setValue('1')

//референс фрейм у корнерпина
def cornerPinRefFrame():
	t1 = nuke.selectedNode().knob('to1')
	t2 = nuke.selectedNode().knob('to2')
	t3 = nuke.selectedNode().knob('to3')
	t4 = nuke.selectedNode().knob('to4')

	xx = t1.x()
	yy = t1.y()

	xy1 = [t1.x(), t1.y()]
	xy2 = [t2.x(), t2.y()]
	xy3 = [t3.x(), t3.y()]
	xy4 = [t4.x(), t4.y()]

	nuke.selectedNode().knob('from1').setValue(xy1)
	nuke.selectedNode().knob('from2').setValue(xy2)
	nuke.selectedNode().knob('from3').setValue(xy3)
	nuke.selectedNode().knob('from4').setValue(xy4)



	nuke.selectedNode().knob('motionblur').setValue(1)
	nuke.selectedNode().knob('shutter').setValue(0.3)
	nuke.selectedNode().knob('shutteroffset').setValue(0)







//меню
sdMenu = menubar.addMenu('&sdMenu')
sdSubMenu = sdMenu.addMenu('mySubMenu')
sdMenu.addCommand('All selected Reads start frames to 1', 'allStartFramesToOne()')
sdMenu.addCommand('Selected corner pin ref frame', 'cornerPinRefFrame()')









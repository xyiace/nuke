nuke
====


bla = nuke.nodes.CheckerBoard1
selected = nuke.selectedNodes()
for node in nuke.selectedNodes():
    print node.input(0).name()
    node.setInput(0,nuke.toNode('CheckerBoard1'))
    

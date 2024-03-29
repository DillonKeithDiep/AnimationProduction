import maya.cmds as cmds

selectionList = cmds.ls(orderedSelection=True, type='transform')

# aims at first target
if len(selectionList) >= 2:

	targetName = selectionList[0]
	selectionList.remove(targetName)
	loatorGroupName = cmd.group(empty=True, name='expansion_locator_grp#')

	maxExpansion = 100
	newAttributeName = 'expansion'

	# create new attribute for expansion		
	if not cmds.objExists('%s.%s' % (targetName, newAttributeName)):
		cmds.select(targetName)
		cmds.addAttr(longName=newAttributeName, shortName='exp',
					attributeType='double', min=0, max=maxExpansion,
					defaultValue=maxExpansion, keyable=True)

	for objectName in selectionList:
		coords = cmds.getAttr('%s.translate' % (objectName))[0]
		locatorName = cmds.spaceLocator(posiiton=coords, name='%s_loc#' % (objectName))[0]
		cmds.xform(locatorName, centerPivots=True)
		cmds.parent(locatorName, locatorGroupName)

		pointConstraintName = cmds.pointConstraint([targetName, locatorName], objectName, name='%s_pointConstraints#' % (objectName))[0]
'''
		cmds.expression(alwaysEvaluate=True, name='%s_attractWeight' % (objectName),
						object=pointConstraintName, string='%sW0=%s-%s.%s' % (targetName,
						maxExpansion, targetName, newAttributeName) )
'''
	cmds.xform(locatorGroupName, centerPivots=True)


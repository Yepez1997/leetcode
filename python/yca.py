# grab the youngest common ancestory in an n-ary tree 
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
	nodeOneDepth = getNodeDepth(descendantOne, topAncestor)
	nodeTwoDepth = getNodeDepth(descendantTwo, topAncestor)
	if nodeOneDepth > nodeTwoDepth:
		return backTrackNodes(descendantOne, descendantTwo, nodeOneDepth - nodeTwoDepth)
	else:
		# pass in the actual nodes ...
		return backTrackNodes(descendantTwo, descendantOne, nodeTwoDepth - nodeOneDepth)

def getNodeDepth(fromNode, toRoot):
	depth = 0
	while fromNode != toRoot:
		depth += 1
		fromNode = fromNode.ancestor
	return depth

def backTrackNodes(nodeLong, nodeShort, diff):
	while diff > 0:
		nodeLong = nodeLong.ancestor
		diff -= 1
	# once the nodes are on the same level playing field, check until the values are ==
	while nodeLong != nodeShort:
		nodeShort = nodeShort.ancestor
		nodeLong = nodeLong.ancestor
	return nodeShort

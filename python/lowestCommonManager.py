def getLowestCommonManager(topManager, reportOne, reportTwo):
    # Write your code here.
	return getOrgInfo(topManager, reportOne, reportTwo).lowestCommonManager

def getOrgInfo(manager, reportOne, reportTwo):
	numberReports = 0
	for directedReport in manager.directReports:
		orgInfo = getOrgInfo(directedReport, reportOne, reportTwo)
		if orgInfo.lowestCommonManager is not None:
			return orgInfo
		numberReports += orgInfo.numberImportantReports
	if manager is reportOne or manager is reportTwo:
		numberReports += 1
	lowestCommonManager = manager if numberReports == 2 else None
	return OrgInfo(lowestCommonManager, numberReports)



class OrgInfo:
	def __init__(self, lowestCommonManager, numberImportantReports):
		self.lowestCommonManager = lowestCommonManager
		self.numberImportantReports = numberImportantReports

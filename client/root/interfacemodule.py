## search for:
import uiScriptLocale

## add under:
import uiselectskills

## search for:
		self.wndGuildBuilding = None

## add under:
		self.wndSelectSkills = None

## search for:
		self.wndChatLog.Destroy()

## add above:
		if self.wndSelectSkills:
			self.wndSelectSkills.Destroy()

## search for:
		del self.wndItemSelect

## add under:
		del self.wndSelectSkills
		
## search for:
if __name__ == "__main__":

## add above:

	def SelectSkillsInit(self):
		if not self.wndSelectSkills:
			self.wndSelectSkills = uiselectskills.SelectSkillsDialog()
			self.wndSelectSkills.Hide()

	def SelectSkillsSetQid(self, qid):
		if self.wndSelectSkills:
			self.wndSelectSkills.SetQid(qid)

	def SelectSkillsSetData(self, data):
		if self.wndSelectSkills:
			self.wndSelectSkills.SetData(data)

	def SelectSkillsHide(self):
		if self.wndSelectSkills:
			self.wndSelectSkills.Hide()
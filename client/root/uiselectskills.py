import ui, localeinfo, constinfo, event, net, uicommon
class SelectSkillsDialog(ui.ThinBoard):
	def __init__(self):
		ui.ThinBoard.__init__(self)
		self.qid = 0
		self.skill = {
			0: [localeinfo.SKILL_GROUP_WARRIOR_1, localeinfo.SKILL_GROUP_WARRIOR_2],
			1: [localeinfo.SKILL_GROUP_ASSASSIN_1, localeinfo.SKILL_GROUP_ASSASSIN_2],
			2: [localeinfo.SKILL_GROUP_SURA_1, localeinfo.SKILL_GROUP_SURA_2],
			3: [localeinfo.SKILL_GROUP_SHAMAN_1, localeinfo.SKILL_GROUP_SHAMAN_2],
			4: [localeinfo.JOB_WOLFMAN1],
		}
		self.characterClass = 0
		self.LoadWindow()

	def __del__(self):
		ui.ThinBoard.__del__(self)

	def LoadWindow(self):
		self.textLine = ui.TextLine()
		self.textLine.SetParent(self)
		self.textLine.SetPosition(0, 25)
		self.textLine.SetHorizontalAlignCenter()
		self.textLine.SetWindowHorizontalAlignCenter()
		self.textLine.SetText(localeinfo.SELECT_SKILLS_TEXT)
		self.textLine.Show()

		self.button1 = ui.Button()
		self.button1.SetParent(self)
		self.button1.SetPosition(-50, 40)
		self.button1.SetWindowHorizontalAlignCenter()
		self.button1.SetWindowVerticalAlignBottom()
		self.button1.SetUpVisual("d:/ymir work/ui/game/windows/tab_button_large_01.sub")
		self.button1.SetOverVisual("d:/ymir work/ui/game/windows/tab_button_large_02.sub")
		self.button1.SetDownVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.button1.SetText("")
		self.button1.SetEvent(lambda arg=1: self.AskSelectSkills(arg))
		self.button1.Show()

		self.button2 = ui.Button()
		self.button2.SetParent(self)
		self.button2.SetPosition(50, 40)
		self.button2.SetWindowHorizontalAlignCenter()
		self.button2.SetWindowVerticalAlignBottom()
		self.button2.SetUpVisual("d:/ymir work/ui/game/windows/tab_button_large_01.sub")
		self.button2.SetOverVisual("d:/ymir work/ui/game/windows/tab_button_large_02.sub")
		self.button2.SetDownVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.button2.SetText("")
		self.button2.SetEvent(lambda arg=2: self.AskSelectSkills(arg))
		self.button2.Show()

		self.SetSize(300, 100)

		self.SetCenterPosition()

	def Destroy(self):
		self.textLine = None
		self.button1 = None
		self.button2 = None
		self.queststionDialog = None
		self.qid = 0
		self.skill = 0
		self.characterClass = 0

	def SetData(self, character_class):
		self.button1.Hide()
		self.button2.Hide()
		self.characterClass = int(character_class)
		if self.characterClass == 4:
			self.button1.SetText(self.skill[self.characterClass][0])
			self.button1.SetPosition(0, 40)
			self.button1.Show()
		else:
			self.button1.SetText(self.skill[self.characterClass][0])
			self.button2.SetText(self.skill[self.characterClass][1])
			self.button1.SetPosition(-50, 40)
			self.button2.SetPosition(50, 40)
			self.button1.Show()
			self.button2.Show()

		self.Show()

	def SetQid(self, qid):
		self.qid = int(qid)

	def AskSelectSkills(self, index):
		self.queststionDialog = uicommon.QuestionDialog()
		self.queststionDialog.SetText(localeinfo.SELECT_SKILLS_CONFIRM % self.skill[self.characterClass][index-1])
		self.queststionDialog.SetAcceptEvent(lambda arg=index: self.AnswerSelectSkills(arg, True))
		self.queststionDialog.SetCancelEvent(lambda arg=index: self.AnswerSelectSkills(arg, False))
		self.queststionDialog.Open()

	def AnswerSelectSkills(self, index, flag):
		if flag:
			constinfo.INPUT_DATA = str(index)
			self.QuestCmd()

		self.queststionDialog.Close()

	def QuestCmd(self):
		event.QuestButtonClick(self.qid)
		net.SendQuestInputStringPacket(constinfo.INPUT_DATA)

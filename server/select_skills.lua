quest select_skills begin
	state start begin
		when login or levelup or kill with pc.get_level() >= 5 and pc.skillgroup == 0 begin
			build_cmd("SelectSkillsInit")
			build_cmd("SelectSkillsSetQid", q.getcurrentquestindex())
			build_cmd("SelectSkillsSetData", pc.get_job())
		end
		when button or info begin
			local data = tonumber(get_input("GetInput"))
			if string.find(string.lower(data), "nan") then
				return
			end
			if data < 1 or data > 2 then
				return
			end
			pc.set_skill_group(data)
			pc.clear_skill()
			build_cmd("SelectSkillsHide")
			select_skills.give_skills_level(59)
			syschat("Wybrano drogê umiejêtnoœci. Przeloguj siê jeœli nie masz umiejêtnoœci na poziomie P.")
		end
		function give_skills_level(level)
			-- uncomment it if you don't have 6th skill for warrior and ninja
			--local last = 5
			--if pc.get_job() > 1  then
			--	last = 6
			--end
			local last = 6
			for i=1, last do
				skill_id = i+(pc.get_job()*30)+((pc.get_skill_group()-1)*15)
				pc.set_skill_level(skill_id, level)
			end
		end
	end
end
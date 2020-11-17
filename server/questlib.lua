function get_input(par)
	cmdchat("GetInputStart")
	local ret = input(cmdchat(par))
	cmdchat("GetInputStop")
	return ret
end
function build_cmd(cmd,...)
	local str = cmd
	for i, v in ipairs(arg) do
		str = str.." "..tostring(v)
	end
	cmdchat(str)
	--if pc.is_gm() then
	--	chat(str)
	--end
end
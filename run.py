from threading import Thread
from time import sleep
import python.control as control
import python.scan as scan
import json

scn = scan.scanner()
cnt = control.control()
cnt.run()
command_file = "json/command.json"
info_file = "json/info.json"
info = {"scaned" : "0","target" : ""}
while True:
    try:
        command = json.load(open(command_file))
        if (command['command'] == "0"):
            cnt.stop()
        elif (command['command'] == "1"):
            cnt.forward()
        elif (command['command'] == "2"):
            cnt.left()
        elif (command['command'] == "3"):
            cnt.right()
        elif (command['command'] == "4"):
            cnt.bacward()
        elif (command['command'] == "5"):
            scn.scan() # senkronize edilecek
            cnt.scan_360()
            info['scaned'] = "1"
            info['target'] = scn.founded_colors[0] + scn.founded_colors[1] + scn.founded_colors[2] + scn.founded_colors[3]
            print(info['target'])
            info_str = open(info_file,"w")
            json.dump(info,info_str)
            info_str.close()
        elif (command['command'] == "51"):
            #cnt.go_red()
			pass
        elif (command['command'] == "52"):
            #cnt.go_green()
			pass
        elif (command['command'] == "53"):
            #cnt.go_blue()
			pass
        elif (command['command'] == "54"):
            #cnt.go_yellow()
			pass
        sleep(0.1)
    except KeyboardInterrupt:
        cnt.pc.isBusy = False
        break

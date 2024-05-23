
'''  Data set for 50 random single line fault  '''

import os,sys
import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd
import shutil
import csv



# Path stuff
sys.path.append(r"C:\Program Files\PTI\PSSE35\35.3\PSSPY37")
sys.path.append(r"C:\Program Files\PTI\PSSE35\35.3\PSSBIN")
sys.path.append(r"C:\Program Files\PTI\PSSE35\35.3\PSSLIB")
sys.path.append(r"C:\Program Files\PTI\PSSE35\35.3\EXAMPLE")
os.environ['PATH'] = (r"C:\Program Files\PTI\PSSE35\35.3\PSSPY37;" 
  + r"C:\Program Files\PTI\PSSE35\35.3\PSSBIN;" 
  + r"C:\Program Files\PTI\PSSE35\35.3\EXAMPLE;" + os.environ['PATH'])

 
#pssbindir  = r"C:\Program Files\PTI\PSSE35\PSSBIN"
#os.environ['PATH'] = pssbindir + ';' + os.environ['PATH']
#os.system("pssplt -inpdev test.idv")

import psse35
psse35.set_minor(3)


import psspy
import pssplot

import redirect
redirect.psse2py()

psspy.psseinit(1500)

import dyntools
import matplotlib.pyplot as plt
from psspy import _i, _f, _s, _o




####### while lines = 167 lines ######## [80, 79], [80, 77], [80, 97]
line_list= [[1, 2], [1, 3], [2, 12], [3, 5], [3, 12], [4, 5], [4, 11], [5, 6], [5, 11], [6, 7], 
         [7, 12], [8, 9], [8, 30], [9, 10], [11, 12], [11, 13], [12, 14], [12, 16], [12, 117], 
         [13, 15], [14, 15], [15, 17], [15, 19], [15, 33], [16, 17], [17, 18], [17, 31], [17, 113], 
         [18, 19], [19, 20], [19, 34], [20, 21], [21, 22], [22, 23], [23, 24], [23, 25], [23, 32], 
         [24, 70], [24, 72], [25, 27], [26, 30], [27, 28], [27, 32], [27, 115], [28, 29], [29, 31], 
         [30, 38], [31, 32], [32, 113], [32, 114], [33, 37], [34, 36], [34, 37], [34, 43], [35, 36], 
         [35, 37], [37, 39], [37, 40], [38, 65], [39, 40], [40, 41], [40, 42], [41, 42], [42, 49], 
         [43, 44], [44, 45], [45, 46], [45, 49], [46, 47], [46, 48], [47, 49], [47, 69], [48, 49], 
         [49, 50], [49, 51], [49, 54], [49, 66], [49, 69], [50, 57], [51, 52], [51, 58], [52, 53], 
         [53, 54], [54, 55], [54, 56], [54, 59], [55, 56], [55, 59], [56, 57], [56, 58], [56, 59], 
         [59, 60], [59, 61], [60, 61], [60, 62], [61, 62], [62, 66], [62, 67], [63, 64], [64, 65], 
         [65, 68], [66, 67], [68, 81], [68, 116], [69, 70], [69, 75], [69, 77], [70, 71], [70, 74], 
         [70, 75], [71, 72], [71, 73], [74, 75], [75, 77], [75, 118], [76, 77], [76, 118], [77, 78], 
         [77, 82], [78, 79], [80, 96], [80, 98], [80, 99], [82, 83], 
         [82, 96], [83, 84], [83, 85], [84, 85], [85, 86], [85, 88], [85, 89], [86, 87], [88, 89],
         [89, 90], [89, 92], [90, 91], [91, 92], [92, 93], [92, 94], [92, 100], [92, 102], [93, 94], 
         [94, 95], [94, 96], [94, 100], [95, 96], [96, 97], [98, 100], [99, 100], [100, 101], [100, 103],
         [100, 104], [100, 106], [101, 102], [103, 104], [103, 105], [103, 110], [104, 105], [105, 106], 
         [105, 107], [105, 108], [106, 107], [108, 109], [109, 110], [110, 111], [110, 112], [114, 115]]




outage_num = 52
#for outage_num in range(2):  # Perform two random line outages
    
psspy.case(r"""C:\IEEE118_V33.sav""")


psspy.machine_data_4(54,r"""2""",[1,1,0,0,0,0,0],[ 36.0,-4.82283, 40.0,-40.0, 50.0,0.0, 100.0,0.0, 0.23,0.0,0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],r"""1""")
psspy.machine_data_4(54,r"""3""",[1,1,0,0,0,0,0],[ 36.0,-4.82283, 40.0,-40.0, 50.0,0.0, 100.0,0.0, 0.23,0.0,0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],r"""1""")
psspy.machine_data_4(54,r"""4""",[1,1,0,0,0,0,0],[ 36.0,-4.82283, 40.0,-40.0, 50.0,0.0, 100.0,0.0, 0.23,0.0,0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],r"""1""")
psspy.machine_data_4(54,r"""5""",[1,1,0,0,0,0,0],[ 36.0,-4.82283, 40.0,-40.0, 50.0,0.0, 100.0,0.0, 0.23,0.0,0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],r"""1""")



psspy.machine_data_4(111,r"""2""",[1,1,0,0,0,0,0],[ 36.0,-4.82283, 40.0,-40.0, 50.0,0.0, 100.0,0.0, 0.23,0.0,0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],r"""1""")
psspy.machine_data_4(111,r"""3""",[1,1,0,0,0,0,0],[ 36.0,-4.82283, 40.0,-40.0, 50.0,0.0, 100.0,0.0, 0.23,0.0,0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],r"""1""")
psspy.machine_data_4(111,r"""4""",[1,1,0,0,0,0,0],[ 36.0,-4.82283, 40.0,-40.0, 50.0,0.0, 100.0,0.0, 0.23,0.0,0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],r"""1""")
psspy.machine_data_4(111,r"""5""",[1,1,0,0,0,0,0],[ 36.0,-4.82283, 40.0,-40.0, 50.0,0.0, 100.0,0.0, 0.23,0.0,0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],r"""1""")

psspy.fdns([0,0,0,1,1,0,99,0])



psspy.dyre_new([1,1,1,1],r"""C:\118 Cyber GAN\IEEE118.dyr""","","","")




#54, id=2 -->PV
psspy.machine_chng_4(54,r"""2""",[_i,_i,_i,_i,_i,2,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],_s)

psspy.add_wind_model(54,r"""2""",1,r"""REGCA1""",1,[0],[""],14,[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
psspy.change_wnmod_con(54,r"""2""",r"""REGCA1""",1, 0.017)
psspy.change_wnmod_con(54,r"""2""",r"""REGCA1""",2, 10.0)
psspy.change_wnmod_con(54,r"""2""",r"""REGCA1""",3, 0.1)
psspy.change_wnmod_con(54,r"""2""",r"""REGCA1""",4, 0.05)
psspy.change_wnmod_con(54,r"""2""",r"""REGCA1""",5, 1.22)
psspy.change_wnmod_con(54,r"""2""",r"""REGCA1""",6, 1.2)
psspy.change_wnmod_con(54,r"""2""",r"""REGCA1""",7, 0.2)
psspy.change_wnmod_con(54,r"""2""",r"""REGCA1""",8, 0.05)
psspy.change_wnmod_con(54,r"""2""",r"""REGCA1""",9,-1.3)
psspy.change_wnmod_con(54,r"""2""",r"""REGCA1""",10, 0.02)
psspy.change_wnmod_con(54,r"""2""",r"""REGCA1""",12, 99.0)
psspy.change_wnmod_con(54,r"""2""",r"""REGCA1""",13,-99.0)
psspy.change_wnmod_con(54,r"""2""",r"""REGCA1""",14, 0.7)

psspy.add_wind_model(54,r"""2""",2,r"""REECB1""",5,[0,0,0,0,0],["","","","",""],25,[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
psspy.change_wnmod_con(54,r"""2""",r"""REECB1""",1, 0.5)
psspy.change_wnmod_con(54,r"""2""",r"""REECB1""",2, 1.1)
psspy.change_wnmod_con(54,r"""2""",r"""REECB1""",3, 0.01)
psspy.change_wnmod_con(54,r"""2""",r"""REECB1""",4,-0.1)
psspy.change_wnmod_con(54,r"""2""",r"""REECB1""",5, 0.1)
psspy.change_wnmod_con(54,r"""2""",r"""REECB1""",6, 2.0)
psspy.change_wnmod_con(54,r"""2""",r"""REECB1""",7, 1.0)
psspy.change_wnmod_con(54,r"""2""",r"""REECB1""",8,-1.0)
psspy.change_wnmod_con(54,r"""2""",r"""REECB1""",9, 1.0)
psspy.change_wnmod_con(54,r"""2""",r"""REECB1""",10, 0.01)
psspy.change_wnmod_con(54,r"""2""",r"""REECB1""",11, 0.6)
psspy.change_wnmod_con(54,r"""2""",r"""REECB1""",12,-0.6)
psspy.change_wnmod_con(54,r"""2""",r"""REECB1""",13, 1.2)
psspy.change_wnmod_con(54,r"""2""",r"""REECB1""",14, 0.8)
psspy.change_wnmod_con(54,r"""2""",r"""REECB1""",15, 1.0)
psspy.change_wnmod_con(54,r"""2""",r"""REECB1""",16, 1.0)
psspy.change_wnmod_con(54,r"""2""",r"""REECB1""",17, 1.0)
psspy.change_wnmod_con(54,r"""2""",r"""REECB1""",18, 1.0)
psspy.change_wnmod_con(54,r"""2""",r"""REECB1""",19, 0.01)
psspy.change_wnmod_con(54,r"""2""",r"""REECB1""",20, 1.0)
psspy.change_wnmod_con(54,r"""2""",r"""REECB1""",21,-1.0)
psspy.change_wnmod_con(54,r"""2""",r"""REECB1""",22, 1.0)
psspy.change_wnmod_con(54,r"""2""",r"""REECB1""",24, 1.0)
psspy.change_wnmod_con(54,r"""2""",r"""REECB1""",25, 0.01)
psspy.change_wnmod_icon(54,r"""2""",r"""REECB1""",3,1)
psspy.change_wnmod_icon(54,r"""2""",r"""REECB1""",4,1)

psspy.add_wind_model(54,r"""2""",7,r"""REPCA1""",7,[0,0,0,0,0,0,0],["","","","","","",""],27,[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
psspy.change_wnmod_con(54,r"""2""",r"""REPCA1""",1, 0.02)
psspy.change_wnmod_con(54,r"""2""",r"""REPCA1""",2, 0.0008)     #Kp, Reactive power PI control proportional gain (pu)
psspy.change_wnmod_con(54,r"""2""",r"""REPCA1""",3, 0.008)      #Ki, Reactive power PI control integral gain (pu)
psspy.change_wnmod_con(54,r"""2""",r"""REPCA1""",5, 0.05)
psspy.change_wnmod_con(54,r"""2""",r"""REPCA1""",10, 0.1)
psspy.change_wnmod_con(54,r"""2""",r"""REPCA1""",11,-0.1)
psspy.change_wnmod_con(54,r"""2""",r"""REPCA1""",14, 0.75)
psspy.change_wnmod_con(54,r"""2""",r"""REPCA1""",15,-0.75)
psspy.change_wnmod_con(54,r"""2""",r"""REPCA1""",16, 1.0)
psspy.change_wnmod_con(54,r"""2""",r"""REPCA1""",18, 0.25)
psspy.change_wnmod_con(54,r"""2""",r"""REPCA1""",19,-0.00083)
psspy.change_wnmod_con(54,r"""2""",r"""REPCA1""",20, 0.00083)
psspy.change_wnmod_con(54,r"""2""",r"""REPCA1""",21, 99.0)
psspy.change_wnmod_con(54,r"""2""",r"""REPCA1""",22,-99.0)
psspy.change_wnmod_con(54,r"""2""",r"""REPCA1""",23, 1.0)
psspy.change_wnmod_con(54,r"""2""",r"""REPCA1""",24,-0.667)
psspy.change_wnmod_con(54,r"""2""",r"""REPCA1""",25, 0.1)
psspy.change_wnmod_con(54,r"""2""",r"""REPCA1""",26, 126.0)
psspy.change_wnmod_con(54,r"""2""",r"""REPCA1""",27, 126.0)
psspy.change_wnmod_icon(54,r"""2""",r"""REPCA1""",6,1)     #RefFlag (flag for V or Q control): 0: Q control 1: voltage control
psspy.change_wnmod_icon(54,r"""2""",r"""REPCA1""",7,0)     #Fflag (flag to disable frequency control): 1: Enable control 0: disable
psspy.change_wnmod_con(54,r"""2""",r"""REPCA1""",17, 0.0001)
##
##

#54, id=3 -->wind
#Type 4 WTG B - Fully inverter connected

psspy.machine_chng_4(54,r"""3""",[_i,_i,_i,_i,_i,3,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],_s)

psspy.add_wind_model(54,r"""3""",1,r"""REGCA1""",1,[0],[""],14,[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
psspy.change_wnmod_con(54,r"""3""",r"""REGCA1""",1, 0.02)
psspy.change_wnmod_con(54,r"""3""",r"""REGCA1""",2, 10.0)
psspy.change_wnmod_con(54,r"""3""",r"""REGCA1""",3, 0.9)
psspy.change_wnmod_con(54,r"""3""",r"""REGCA1""",4, 0.4)
psspy.change_wnmod_con(54,r"""3""",r"""REGCA1""",5, 1.22)
psspy.change_wnmod_con(54,r"""3""",r"""REGCA1""",6, 1.2)
psspy.change_wnmod_con(54,r"""3""",r"""REGCA1""",7, 0.8)
psspy.change_wnmod_con(54,r"""3""",r"""REGCA1""",8, 0.4)
psspy.change_wnmod_con(54,r"""3""",r"""REGCA1""",9,-1.3)
psspy.change_wnmod_con(54,r"""3""",r"""REGCA1""",10, 0.02)
psspy.change_wnmod_con(54,r"""3""",r"""REGCA1""",11, 0.7)
psspy.change_wnmod_con(54,r"""3""",r"""REGCA1""",12, 999.0)
psspy.change_wnmod_con(54,r"""3""",r"""REGCA1""",13,-999.0)
psspy.change_wnmod_con(54,r"""3""",r"""REGCA1""",14, 1.0)
psspy.add_wind_model(54,r"""3""",2,r"""REECA1""",6,[0,0,0,0,0,0],["","","","","",""],45,[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,
0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
psspy.change_wnmod_con(54,r"""3""",r"""REECA1""",1,-99.0)
psspy.change_wnmod_con(54,r"""3""",r"""REECA1""",2, 99.0)
psspy.change_wnmod_con(54,r"""3""",r"""REECA1""",4,-0.05)
psspy.change_wnmod_con(54,r"""3""",r"""REECA1""",5, 0.05)
psspy.change_wnmod_con(54,r"""3""",r"""REECA1""",7, 1.05)
psspy.change_wnmod_con(54,r"""3""",r"""REECA1""",8,-1.05)
psspy.change_wnmod_con(54,r"""3""",r"""REECA1""",10, 0.15)
psspy.change_wnmod_con(54,r"""3""",r"""REECA1""",13, 0.05)
psspy.change_wnmod_con(54,r"""3""",r"""REECA1""",14, 0.4)
psspy.change_wnmod_con(54,r"""3""",r"""REECA1""",15,-0.4)
psspy.change_wnmod_con(54,r"""3""",r"""REECA1""",16, 1.1)
psspy.change_wnmod_con(54,r"""3""",r"""REECA1""",17, 0.9)
psspy.change_wnmod_con(54,r"""3""",r"""REECA1""",19, 0.1)
psspy.change_wnmod_con(54,r"""3""",r"""REECA1""",21, 120.0)
psspy.change_wnmod_con(54,r"""3""",r"""REECA1""",23, 0.02)
psspy.change_wnmod_con(54,r"""3""",r"""REECA1""",24, 99.0)
psspy.change_wnmod_con(54,r"""3""",r"""REECA1""",25,-99.0)
psspy.change_wnmod_con(54,r"""3""",r"""REECA1""",26, 1.0)
psspy.change_wnmod_con(54,r"""3""",r"""REECA1""",28, 1.7)
psspy.change_wnmod_con(54,r"""3""",r"""REECA1""",29, 0.04)
psspy.change_wnmod_con(54,r"""3""",r"""REECA1""",30, 0.29)
psspy.change_wnmod_con(54,r"""3""",r"""REECA1""",31, 1.25)
psspy.change_wnmod_con(54,r"""3""",r"""REECA1""",32, 1.33)
psspy.change_wnmod_con(54,r"""3""",r"""REECA1""",39, 1.15)
psspy.change_wnmod_con(54,r"""3""",r"""REECA1""",40, 1.1)
psspy.change_wnmod_con(54,r"""3""",r"""REECA1""",41, 1.24)
psspy.change_wnmod_con(54,r"""3""",r"""REECA1""",42, 2.0)
psspy.change_wnmod_con(54,r"""3""",r"""REECA1""",43, 1.24)
psspy.change_wnmod_icon(54,r"""3""",r"""REECA1""",3,1)
psspy.change_wnmod_icon(54,r"""3""",r"""REECA1""",4,1)


psspy.add_wind_model(54,r"""3""",7,r"""REPCA1""",7,[0,0,0,0,0,0,0],["","","","","","",""],27,[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
psspy.change_wnmod_con(54,r"""3""",r"""REPCA1""",1, 0.02)
psspy.change_wnmod_con(54,r"""3""",r"""REPCA1""",2, 0.0008)     #Kp, Reactive power PI control proportional gain (pu)
psspy.change_wnmod_con(54,r"""3""",r"""REPCA1""",3, 0.008)      #Ki, Reactive power PI control integral gain (pu)
psspy.change_wnmod_con(54,r"""3""",r"""REPCA1""",5, 0.05)
psspy.change_wnmod_con(54,r"""3""",r"""REPCA1""",10, 0.1)
psspy.change_wnmod_con(54,r"""3""",r"""REPCA1""",11,-0.1)
psspy.change_wnmod_con(54,r"""3""",r"""REPCA1""",14, 0.75)
psspy.change_wnmod_con(54,r"""3""",r"""REPCA1""",15,-0.75)
psspy.change_wnmod_con(54,r"""3""",r"""REPCA1""",16, 1.0)
psspy.change_wnmod_con(54,r"""3""",r"""REPCA1""",18, 0.25)
psspy.change_wnmod_con(54,r"""3""",r"""REPCA1""",19,-0.00083)
psspy.change_wnmod_con(54,r"""3""",r"""REPCA1""",20, 0.00083)
psspy.change_wnmod_con(54,r"""3""",r"""REPCA1""",21, 99.0)
psspy.change_wnmod_con(54,r"""3""",r"""REPCA1""",22,-99.0)
psspy.change_wnmod_con(54,r"""3""",r"""REPCA1""",23, 1.0)
psspy.change_wnmod_con(54,r"""3""",r"""REPCA1""",24,-0.667)
psspy.change_wnmod_con(54,r"""3""",r"""REPCA1""",25, 0.1)
psspy.change_wnmod_con(54,r"""3""",r"""REPCA1""",26, 126.0)
psspy.change_wnmod_con(54,r"""3""",r"""REPCA1""",27, 126.0)
psspy.change_wnmod_icon(54,r"""3""",r"""REPCA1""",6,0)     #RefFlag (flag for V or Q control): 0: Q control 1: voltage control
psspy.change_wnmod_icon(54,r"""3""",r"""REPCA1""",7,0)     #Fflag (flag to disable frequency control): 1: Enable control 0: disable
psspy.change_wnmod_con(54,r"""3""",r"""REPCA1""",17, 0.0001)


##
##
#54, id=4 -->Battery

psspy.machine_chng_4(54,r"""4""",[_i,_i,_i,_i,_i,3,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],_s)

psspy.add_wind_model(54,r"""4""",1,r"""REGCA1""",1,[0],[""],14,[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
psspy.change_wnmod_con(54,r"""4""",r"""REGCA1""",1, 0.017)
psspy.change_wnmod_con(54,r"""4""",r"""REGCA1""",2, 10.0)
psspy.change_wnmod_con(54,r"""4""",r"""REGCA1""",3, 0.1)
psspy.change_wnmod_con(54,r"""4""",r"""REGCA1""",4, 0.05)
psspy.change_wnmod_con(54,r"""4""",r"""REGCA1""",5, 1.22)
psspy.change_wnmod_con(54,r"""4""",r"""REGCA1""",6, 1.2)
psspy.change_wnmod_con(54,r"""4""",r"""REGCA1""",7, 0.2)
psspy.change_wnmod_con(54,r"""4""",r"""REGCA1""",8, 0.05)
psspy.change_wnmod_con(54,r"""4""",r"""REGCA1""",9,-1.3)
psspy.change_wnmod_con(54,r"""4""",r"""REGCA1""",10, 0.02)
psspy.change_wnmod_con(54,r"""4""",r"""REGCA1""",12, 99.0)
psspy.change_wnmod_con(54,r"""4""",r"""REGCA1""",13,-99.0)
psspy.change_wnmod_con(54,r"""4""",r"""REGCA1""",14, 0.7)

psspy.add_wind_model(54,r"""4""",2,r"""REECC1""",5,[0,0,0,0,0],["","","","",""],45,[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,
0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",1,-99.0)
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",2, 99.0)
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",3, 0.01)
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",4,-0.05)
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",5, 0.05)
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",6, 15.0)
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",7, 0.75)
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",8,-0.75)
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",9, 1.0)
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",10, 0.05)
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",11, 0.75)
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",12,-0.75)
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",13, 1.1)
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",14, 0.9)
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",16, 1.0)
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",18, 1.0)
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",19, 0.017)
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",20, 99.0)
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",21,-99.0)
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",22, 1.1)       #PMAX (pu), Max. power limit
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",23,-0.567)     #PMIN (pu), Min. power limit
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",24, 1.11)
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",25, 0.017)
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",27, 0.75)
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",28, 0.2)
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",29, 0.75)
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",30, 0.5)
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",31, 0.75)
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",32, 1.0)
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",33, 0.75)
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",34, 0.2)
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",35, 1.11)
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",36, 0.5)
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",37, 1.11)
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",38, 0.75)
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",39, 1.11)
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",40, 1.0)
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",41, 1.11)
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",42, 999.0)     #T, battery discharge time (s)  (>0)
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",43, 0.5)       #SOCini (pu), Initial state of charge
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",44, 0.9)       #SOCmax (pu), Maximum allowable state of charge
psspy.change_wnmod_con(54,r"""4""",r"""REECC1""",45, 0.1)       #SOCmin (pu), Minimum allowable state of charge
psspy.change_wnmod_icon(54,r"""4""",r"""REECC1""",4,0)

psspy.add_wind_model(54,r"""4""",7,r"""REPCA1""",7,[0,0,0,0,0,0,0],["","","","","","",""],27,[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
psspy.change_wnmod_con(54,r"""4""",r"""REPCA1""",1, 0.02)
psspy.change_wnmod_con(54,r"""4""",r"""REPCA1""",2, 0.0008)     #Kp, Reactive power PI control proportional gain (pu)
psspy.change_wnmod_con(54,r"""4""",r"""REPCA1""",3, 0.008)      #Ki, Reactive power PI control integral gain (pu)
psspy.change_wnmod_con(54,r"""4""",r"""REPCA1""",5, 0.05)
psspy.change_wnmod_con(54,r"""4""",r"""REPCA1""",10, 0.1)
psspy.change_wnmod_con(54,r"""4""",r"""REPCA1""",11,-0.1)
psspy.change_wnmod_con(54,r"""4""",r"""REPCA1""",14, 0.75)
psspy.change_wnmod_con(54,r"""4""",r"""REPCA1""",15,-0.75)
psspy.change_wnmod_con(54,r"""4""",r"""REPCA1""",16, 1.0)
psspy.change_wnmod_con(54,r"""4""",r"""REPCA1""",18, 0.25)
psspy.change_wnmod_con(54,r"""4""",r"""REPCA1""",19,-0.00083)
psspy.change_wnmod_con(54,r"""4""",r"""REPCA1""",20, 0.00083)
psspy.change_wnmod_con(54,r"""4""",r"""REPCA1""",21, 99.0)
psspy.change_wnmod_con(54,r"""4""",r"""REPCA1""",22,-99.0)
psspy.change_wnmod_con(54,r"""4""",r"""REPCA1""",23, 1.0)
psspy.change_wnmod_con(54,r"""4""",r"""REPCA1""",24,-0.667)
psspy.change_wnmod_con(54,r"""4""",r"""REPCA1""",25, 0.1)
psspy.change_wnmod_con(54,r"""4""",r"""REPCA1""",26, 126.0)       #Ddn, reciprocal of droop for over-frequency conditions (pu)
psspy.change_wnmod_con(54,r"""4""",r"""REPCA1""",27, 126.0)       #Dup, reciprocal of droop for under-frequency conditions (pu)
psspy.change_wnmod_icon(54,r"""4""",r"""REPCA1""",6,0)            ##RefFlag (flag for V or Q control): 0: Q control 1: voltage control
psspy.change_wnmod_icon(54,r"""4""",r"""REPCA1""",7,1)            ##Fflag (flag to disable frequency control): 1: Enable control 0: disable
psspy.change_wnmod_con(54,r"""4""",r"""REPCA1""",17, 0.0001)



############################################################################################
psspy.plmod_remove(54,r"""1""",7)
psspy.add_plant_model(54,r"""1""",7,r"""IEEEG1""",0,"",0,[],[],20,[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
psspy.change_plmod_con(54,r"""1""",r"""IEEEG1""",1, 25.0)
psspy.change_plmod_con(54,r"""1""",r"""IEEEG1""",4, 0.1)
psspy.change_plmod_con(54,r"""1""",r"""IEEEG1""",5, 0.1)
psspy.change_plmod_con(54,r"""1""",r"""IEEEG1""",6,-0.1)
psspy.change_plmod_con(54,r"""1""",r"""IEEEG1""",7, 1.1759)
psspy.change_plmod_con(54,r"""1""",r"""IEEEG1""",9, 0.2614)
psspy.change_plmod_con(54,r"""1""",r"""IEEEG1""",10, 0.3452)
psspy.change_plmod_con(54,r"""1""",r"""IEEEG1""",12, 9.0)
psspy.change_plmod_con(54,r"""1""",r"""IEEEG1""",13, 0.4)
psspy.change_plmod_con(54,r"""1""",r"""IEEEG1""",15, 0.5)
psspy.change_plmod_con(54,r"""1""",r"""IEEEG1""",16, 0.3467)



psspy.add_plant_model(54,r"""5""",1,r"""GENTPJ1""",0,"",0,[],[],16,[ 4.8, 0.035, 1.5, 0.07, 3.2,0.0, 1.8, 1.75, 0.3, 0.47, 0.23, 0.23, 0.15, 0.1, 0.4, 0.1])
psspy.add_plant_model(54,r"""5""",6,r"""IEEET1""",0,"",0,[],[],14,[ 0.06, 20.0, 0.01, 5.0,-6.0, 1.0, 0.67, 0.1, 1.0,0.0, 3.0, 0.09, 4.0, 0.368])
psspy.add_plant_model(54,r"""5""",7,r"""TGOV1""",0,"",0,[],[],7,[ 0.04, 0.4, 1.05,0.0, 1.5, 5.0,0.0])
psspy.add_plant_model(54,r"""5""",3,r"""PSS2A""",0,"",6,[1,0,3,0,5,1],["","","","","",""],17,[ 2.0, 2.0, 0.02, 2.0, 4.0, 2.0, 0.333, 1.0, 0.5, 0.1, 30.0, 0.15, 0.03, 0.15, 0.03, 0.1,-0.1])




#111, id=2 -->PV
psspy.machine_chng_4(111,r"""2""",[_i,_i,_i,_i,_i,2,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],_s)

psspy.add_wind_model(111,r"""2""",1,r"""REGCA1""",1,[0],[""],14,[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
psspy.change_wnmod_con(111,r"""2""",r"""REGCA1""",1, 0.017)
psspy.change_wnmod_con(111,r"""2""",r"""REGCA1""",2, 10.0)
psspy.change_wnmod_con(111,r"""2""",r"""REGCA1""",3, 0.1)
psspy.change_wnmod_con(111,r"""2""",r"""REGCA1""",4, 0.05)
psspy.change_wnmod_con(111,r"""2""",r"""REGCA1""",5, 1.22)
psspy.change_wnmod_con(111,r"""2""",r"""REGCA1""",6, 1.2)
psspy.change_wnmod_con(111,r"""2""",r"""REGCA1""",7, 0.2)
psspy.change_wnmod_con(111,r"""2""",r"""REGCA1""",8, 0.05)
psspy.change_wnmod_con(111,r"""2""",r"""REGCA1""",9,-1.3)
psspy.change_wnmod_con(111,r"""2""",r"""REGCA1""",10, 0.02)
psspy.change_wnmod_con(111,r"""2""",r"""REGCA1""",12, 99.0)
psspy.change_wnmod_con(111,r"""2""",r"""REGCA1""",13,-99.0)
psspy.change_wnmod_con(111,r"""2""",r"""REGCA1""",14, 0.7)

psspy.add_wind_model(111,r"""2""",2,r"""REECB1""",5,[0,0,0,0,0],["","","","",""],25,[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
psspy.change_wnmod_con(111,r"""2""",r"""REECB1""",1, 0.5)
psspy.change_wnmod_con(111,r"""2""",r"""REECB1""",2, 1.1)
psspy.change_wnmod_con(111,r"""2""",r"""REECB1""",3, 0.01)
psspy.change_wnmod_con(111,r"""2""",r"""REECB1""",4,-0.1)
psspy.change_wnmod_con(111,r"""2""",r"""REECB1""",5, 0.1)
psspy.change_wnmod_con(111,r"""2""",r"""REECB1""",6, 2.0)
psspy.change_wnmod_con(111,r"""2""",r"""REECB1""",7, 1.0)
psspy.change_wnmod_con(111,r"""2""",r"""REECB1""",8,-1.0)
psspy.change_wnmod_con(111,r"""2""",r"""REECB1""",9, 1.0)
psspy.change_wnmod_con(111,r"""2""",r"""REECB1""",10, 0.01)
psspy.change_wnmod_con(111,r"""2""",r"""REECB1""",11, 0.6)
psspy.change_wnmod_con(111,r"""2""",r"""REECB1""",12,-0.6)
psspy.change_wnmod_con(111,r"""2""",r"""REECB1""",13, 1.2)
psspy.change_wnmod_con(111,r"""2""",r"""REECB1""",14, 0.8)
psspy.change_wnmod_con(111,r"""2""",r"""REECB1""",15, 1.0)
psspy.change_wnmod_con(111,r"""2""",r"""REECB1""",16, 1.0)
psspy.change_wnmod_con(111,r"""2""",r"""REECB1""",17, 1.0)
psspy.change_wnmod_con(111,r"""2""",r"""REECB1""",18, 1.0)
psspy.change_wnmod_con(111,r"""2""",r"""REECB1""",19, 0.01)
psspy.change_wnmod_con(111,r"""2""",r"""REECB1""",20, 1.0)
psspy.change_wnmod_con(111,r"""2""",r"""REECB1""",21,-1.0)
psspy.change_wnmod_con(111,r"""2""",r"""REECB1""",22, 1.0)
psspy.change_wnmod_con(111,r"""2""",r"""REECB1""",24, 1.0)
psspy.change_wnmod_con(111,r"""2""",r"""REECB1""",25, 0.01)
psspy.change_wnmod_icon(111,r"""2""",r"""REECB1""",3,1)
psspy.change_wnmod_icon(111,r"""2""",r"""REECB1""",4,1)

psspy.add_wind_model(111,r"""2""",7,r"""REPCA1""",7,[0,0,0,0,0,0,0],["","","","","","",""],27,[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
psspy.change_wnmod_con(111,r"""2""",r"""REPCA1""",1, 0.02)
psspy.change_wnmod_con(111,r"""2""",r"""REPCA1""",2, 0.0008)     #Kp, Reactive power PI control proportional gain (pu)
psspy.change_wnmod_con(111,r"""2""",r"""REPCA1""",3, 0.008)      #Ki, Reactive power PI control integral gain (pu)
psspy.change_wnmod_con(111,r"""2""",r"""REPCA1""",5, 0.05)
psspy.change_wnmod_con(111,r"""2""",r"""REPCA1""",10, 0.1)
psspy.change_wnmod_con(111,r"""2""",r"""REPCA1""",11,-0.1)
psspy.change_wnmod_con(111,r"""2""",r"""REPCA1""",14, 0.75)
psspy.change_wnmod_con(111,r"""2""",r"""REPCA1""",15,-0.75)
psspy.change_wnmod_con(111,r"""2""",r"""REPCA1""",16, 1.0)
psspy.change_wnmod_con(111,r"""2""",r"""REPCA1""",18, 0.25)
psspy.change_wnmod_con(111,r"""2""",r"""REPCA1""",19,-0.00083)
psspy.change_wnmod_con(111,r"""2""",r"""REPCA1""",20, 0.00083)
psspy.change_wnmod_con(111,r"""2""",r"""REPCA1""",21, 99.0)
psspy.change_wnmod_con(111,r"""2""",r"""REPCA1""",22,-99.0)
psspy.change_wnmod_con(111,r"""2""",r"""REPCA1""",23, 1.0)
psspy.change_wnmod_con(111,r"""2""",r"""REPCA1""",24,-0.667)
psspy.change_wnmod_con(111,r"""2""",r"""REPCA1""",25, 0.1)
psspy.change_wnmod_con(111,r"""2""",r"""REPCA1""",26, 126.0)
psspy.change_wnmod_con(111,r"""2""",r"""REPCA1""",27, 126.0)
psspy.change_wnmod_icon(111,r"""2""",r"""REPCA1""",6,1)     #RefFlag (flag for V or Q control): 0: Q control 1: voltage control
psspy.change_wnmod_icon(111,r"""2""",r"""REPCA1""",7,0)     #Fflag (flag to disable frequency control): 1: Enable control 0: disable
psspy.change_wnmod_con(111,r"""2""",r"""REPCA1""",17, 0.0001)
##
##

#111, id=3 -->wind
#Type 4 WTG B - Fully inverter connected

psspy.machine_chng_4(111,r"""3""",[_i,_i,_i,_i,_i,3,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],_s)

psspy.add_wind_model(111,r"""3""",1,r"""REGCA1""",1,[0],[""],14,[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
psspy.change_wnmod_con(111,r"""3""",r"""REGCA1""",1, 0.02)
psspy.change_wnmod_con(111,r"""3""",r"""REGCA1""",2, 10.0)
psspy.change_wnmod_con(111,r"""3""",r"""REGCA1""",3, 0.9)
psspy.change_wnmod_con(111,r"""3""",r"""REGCA1""",4, 0.4)
psspy.change_wnmod_con(111,r"""3""",r"""REGCA1""",5, 1.22)
psspy.change_wnmod_con(111,r"""3""",r"""REGCA1""",6, 1.2)
psspy.change_wnmod_con(111,r"""3""",r"""REGCA1""",7, 0.8)
psspy.change_wnmod_con(111,r"""3""",r"""REGCA1""",8, 0.4)
psspy.change_wnmod_con(111,r"""3""",r"""REGCA1""",9,-1.3)
psspy.change_wnmod_con(111,r"""3""",r"""REGCA1""",10, 0.02)
psspy.change_wnmod_con(111,r"""3""",r"""REGCA1""",11, 0.7)
psspy.change_wnmod_con(111,r"""3""",r"""REGCA1""",12, 999.0)
psspy.change_wnmod_con(111,r"""3""",r"""REGCA1""",13,-999.0)
psspy.change_wnmod_con(111,r"""3""",r"""REGCA1""",14, 1.0)
psspy.add_wind_model(111,r"""3""",2,r"""REECA1""",6,[0,0,0,0,0,0],["","","","","",""],45,[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,
0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
psspy.change_wnmod_con(111,r"""3""",r"""REECA1""",1,-99.0)
psspy.change_wnmod_con(111,r"""3""",r"""REECA1""",2, 99.0)
psspy.change_wnmod_con(111,r"""3""",r"""REECA1""",4,-0.05)
psspy.change_wnmod_con(111,r"""3""",r"""REECA1""",5, 0.05)
psspy.change_wnmod_con(111,r"""3""",r"""REECA1""",7, 1.05)
psspy.change_wnmod_con(111,r"""3""",r"""REECA1""",8,-1.05)
psspy.change_wnmod_con(111,r"""3""",r"""REECA1""",10, 0.15)
psspy.change_wnmod_con(111,r"""3""",r"""REECA1""",13, 0.05)
psspy.change_wnmod_con(111,r"""3""",r"""REECA1""",14, 0.4)
psspy.change_wnmod_con(111,r"""3""",r"""REECA1""",15,-0.4)
psspy.change_wnmod_con(111,r"""3""",r"""REECA1""",16, 1.1)
psspy.change_wnmod_con(111,r"""3""",r"""REECA1""",17, 0.9)
psspy.change_wnmod_con(111,r"""3""",r"""REECA1""",19, 0.1)
psspy.change_wnmod_con(111,r"""3""",r"""REECA1""",21, 120.0)
psspy.change_wnmod_con(111,r"""3""",r"""REECA1""",23, 0.02)
psspy.change_wnmod_con(111,r"""3""",r"""REECA1""",24, 99.0)
psspy.change_wnmod_con(111,r"""3""",r"""REECA1""",25,-99.0)
psspy.change_wnmod_con(111,r"""3""",r"""REECA1""",26, 1.0)
psspy.change_wnmod_con(111,r"""3""",r"""REECA1""",28, 1.7)
psspy.change_wnmod_con(111,r"""3""",r"""REECA1""",29, 0.04)
psspy.change_wnmod_con(111,r"""3""",r"""REECA1""",30, 0.29)
psspy.change_wnmod_con(111,r"""3""",r"""REECA1""",31, 1.25)
psspy.change_wnmod_con(111,r"""3""",r"""REECA1""",32, 1.33)
psspy.change_wnmod_con(111,r"""3""",r"""REECA1""",39, 1.15)
psspy.change_wnmod_con(111,r"""3""",r"""REECA1""",40, 1.1)
psspy.change_wnmod_con(111,r"""3""",r"""REECA1""",41, 1.24)
psspy.change_wnmod_con(111,r"""3""",r"""REECA1""",42, 2.0)
psspy.change_wnmod_con(111,r"""3""",r"""REECA1""",43, 1.24)
psspy.change_wnmod_icon(111,r"""3""",r"""REECA1""",3,1)
psspy.change_wnmod_icon(111,r"""3""",r"""REECA1""",4,1)


psspy.add_wind_model(111,r"""3""",7,r"""REPCA1""",7,[0,0,0,0,0,0,0],["","","","","","",""],27,[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
psspy.change_wnmod_con(111,r"""3""",r"""REPCA1""",1, 0.02)
psspy.change_wnmod_con(111,r"""3""",r"""REPCA1""",2, 0.0008)     #Kp, Reactive power PI control proportional gain (pu)
psspy.change_wnmod_con(111,r"""3""",r"""REPCA1""",3, 0.008)      #Ki, Reactive power PI control integral gain (pu)
psspy.change_wnmod_con(111,r"""3""",r"""REPCA1""",5, 0.05)
psspy.change_wnmod_con(111,r"""3""",r"""REPCA1""",10, 0.1)
psspy.change_wnmod_con(111,r"""3""",r"""REPCA1""",11,-0.1)
psspy.change_wnmod_con(111,r"""3""",r"""REPCA1""",14, 0.75)
psspy.change_wnmod_con(111,r"""3""",r"""REPCA1""",15,-0.75)
psspy.change_wnmod_con(111,r"""3""",r"""REPCA1""",16, 1.0)
psspy.change_wnmod_con(111,r"""3""",r"""REPCA1""",18, 0.25)
psspy.change_wnmod_con(111,r"""3""",r"""REPCA1""",19,-0.00083)
psspy.change_wnmod_con(111,r"""3""",r"""REPCA1""",20, 0.00083)
psspy.change_wnmod_con(111,r"""3""",r"""REPCA1""",21, 99.0)
psspy.change_wnmod_con(111,r"""3""",r"""REPCA1""",22,-99.0)
psspy.change_wnmod_con(111,r"""3""",r"""REPCA1""",23, 1.0)
psspy.change_wnmod_con(111,r"""3""",r"""REPCA1""",24,-0.667)
psspy.change_wnmod_con(111,r"""3""",r"""REPCA1""",25, 0.1)
psspy.change_wnmod_con(111,r"""3""",r"""REPCA1""",26, 126.0)
psspy.change_wnmod_con(111,r"""3""",r"""REPCA1""",27, 126.0)
psspy.change_wnmod_icon(111,r"""3""",r"""REPCA1""",6,0)     #RefFlag (flag for V or Q control): 0: Q control 1: voltage control
psspy.change_wnmod_icon(111,r"""3""",r"""REPCA1""",7,0)     #Fflag (flag to disable frequency control): 1: Enable control 0: disable
psspy.change_wnmod_con(111,r"""3""",r"""REPCA1""",17, 0.0001)



##
##
#111, id=4 -->Battery

psspy.machine_chng_4(111,r"""4""",[_i,_i,_i,_i,_i,3,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],_s)

psspy.add_wind_model(111,r"""4""",1,r"""REGCA1""",1,[0],[""],14,[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
psspy.change_wnmod_con(111,r"""4""",r"""REGCA1""",1, 0.017)
psspy.change_wnmod_con(111,r"""4""",r"""REGCA1""",2, 10.0)
psspy.change_wnmod_con(111,r"""4""",r"""REGCA1""",3, 0.1)
psspy.change_wnmod_con(111,r"""4""",r"""REGCA1""",4, 0.05)
psspy.change_wnmod_con(111,r"""4""",r"""REGCA1""",5, 1.22)
psspy.change_wnmod_con(111,r"""4""",r"""REGCA1""",6, 1.2)
psspy.change_wnmod_con(111,r"""4""",r"""REGCA1""",7, 0.2)
psspy.change_wnmod_con(111,r"""4""",r"""REGCA1""",8, 0.05)
psspy.change_wnmod_con(111,r"""4""",r"""REGCA1""",9,-1.3)
psspy.change_wnmod_con(111,r"""4""",r"""REGCA1""",10, 0.02)
psspy.change_wnmod_con(111,r"""4""",r"""REGCA1""",12, 99.0)
psspy.change_wnmod_con(111,r"""4""",r"""REGCA1""",13,-99.0)
psspy.change_wnmod_con(111,r"""4""",r"""REGCA1""",14, 0.7)

psspy.add_wind_model(111,r"""4""",2,r"""REECC1""",5,[0,0,0,0,0],["","","","",""],45,[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,
0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",1,-99.0)
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",2, 99.0)
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",3, 0.01)
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",4,-0.05)
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",5, 0.05)
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",6, 15.0)
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",7, 0.75)
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",8,-0.75)
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",9, 1.0)
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",10, 0.05)
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",11, 0.75)
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",12,-0.75)
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",13, 1.1)
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",14, 0.9)
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",16, 1.0)
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",18, 1.0)
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",19, 0.017)
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",20, 99.0)
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",21,-99.0)
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",22, 1.1)       #PMAX (pu), Max. power limit
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",23,-0.567)     #PMIN (pu), Min. power limit
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",24, 1.11)
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",25, 0.017)
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",27, 0.75)
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",28, 0.2)
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",29, 0.75)
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",30, 0.5)
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",31, 0.75)
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",32, 1.0)
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",33, 0.75)
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",34, 0.2)
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",35, 1.11)
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",36, 0.5)
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",37, 1.11)
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",38, 0.75)
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",39, 1.11)
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",40, 1.0)
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",41, 1.11)
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",42, 999.0)     #T, battery discharge time (s)  (>0)
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",43, 0.5)       #SOCini (pu), Initial state of charge
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",44, 0.9)       #SOCmax (pu), Maximum allowable state of charge
psspy.change_wnmod_con(111,r"""4""",r"""REECC1""",45, 0.1)       #SOCmin (pu), Minimum allowable state of charge
psspy.change_wnmod_icon(111,r"""4""",r"""REECC1""",4,0)

psspy.add_wind_model(111,r"""4""",7,r"""REPCA1""",7,[0,0,0,0,0,0,0],["","","","","","",""],27,[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
psspy.change_wnmod_con(111,r"""4""",r"""REPCA1""",1, 0.02)
psspy.change_wnmod_con(111,r"""4""",r"""REPCA1""",2, 0.0008)     #Kp, Reactive power PI control proportional gain (pu)
psspy.change_wnmod_con(111,r"""4""",r"""REPCA1""",3, 0.008)      #Ki, Reactive power PI control integral gain (pu)
psspy.change_wnmod_con(111,r"""4""",r"""REPCA1""",5, 0.05)
psspy.change_wnmod_con(111,r"""4""",r"""REPCA1""",10, 0.1)
psspy.change_wnmod_con(111,r"""4""",r"""REPCA1""",11,-0.1)
psspy.change_wnmod_con(111,r"""4""",r"""REPCA1""",14, 0.75)
psspy.change_wnmod_con(111,r"""4""",r"""REPCA1""",15,-0.75)
psspy.change_wnmod_con(111,r"""4""",r"""REPCA1""",16, 1.0)
psspy.change_wnmod_con(111,r"""4""",r"""REPCA1""",18, 0.25)
psspy.change_wnmod_con(111,r"""4""",r"""REPCA1""",19,-0.00083)
psspy.change_wnmod_con(111,r"""4""",r"""REPCA1""",20, 0.00083)
psspy.change_wnmod_con(111,r"""4""",r"""REPCA1""",21, 99.0)
psspy.change_wnmod_con(111,r"""4""",r"""REPCA1""",22,-99.0)
psspy.change_wnmod_con(111,r"""4""",r"""REPCA1""",23, 1.0)
psspy.change_wnmod_con(111,r"""4""",r"""REPCA1""",24,-0.667)
psspy.change_wnmod_con(111,r"""4""",r"""REPCA1""",25, 0.1)
psspy.change_wnmod_con(111,r"""4""",r"""REPCA1""",26, 126.0)       #Ddn, reciprocal of droop for over-frequency conditions (pu)
psspy.change_wnmod_con(111,r"""4""",r"""REPCA1""",27, 126.0)       #Dup, reciprocal of droop for under-frequency conditions (pu)
psspy.change_wnmod_icon(111,r"""4""",r"""REPCA1""",6,0)            ##RefFlag (flag for V or Q control): 0: Q control 1: voltage control
psspy.change_wnmod_icon(111,r"""4""",r"""REPCA1""",7,1)            ##Fflag (flag to disable frequency control): 1: Enable control 0: disable
psspy.change_wnmod_con(111,r"""4""",r"""REPCA1""",17, 0.0001)



############################################################################################
psspy.plmod_remove(111,r"""1""",7)
psspy.add_plant_model(111,r"""1""",7,r"""IEEEG1""",0,"",0,[],[],20,[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
psspy.change_plmod_con(111,r"""1""",r"""IEEEG1""",1, 25.0)
psspy.change_plmod_con(111,r"""1""",r"""IEEEG1""",4, 0.1)
psspy.change_plmod_con(111,r"""1""",r"""IEEEG1""",5, 0.1)
psspy.change_plmod_con(111,r"""1""",r"""IEEEG1""",6,-0.1)
psspy.change_plmod_con(111,r"""1""",r"""IEEEG1""",7, 1.1759)
psspy.change_plmod_con(111,r"""1""",r"""IEEEG1""",9, 0.2614)
psspy.change_plmod_con(111,r"""1""",r"""IEEEG1""",10, 0.3452)
psspy.change_plmod_con(111,r"""1""",r"""IEEEG1""",12, 9.0)
psspy.change_plmod_con(111,r"""1""",r"""IEEEG1""",13, 0.4)
psspy.change_plmod_con(111,r"""1""",r"""IEEEG1""",15, 0.5)
psspy.change_plmod_con(111,r"""1""",r"""IEEEG1""",16, 0.3467)



psspy.add_plant_model(111,r"""5""",1,r"""GENTPJ1""",0,"",0,[],[],16,[ 4.8, 0.035, 1.5, 0.07, 3.2,0.0, 1.8, 1.75, 0.3, 0.47, 0.23, 0.23, 0.15, 0.1, 0.4, 0.1])
psspy.add_plant_model(111,r"""5""",6,r"""IEEET1""",0,"",0,[],[],14,[ 0.06, 20.0, 0.01, 5.0,-6.0, 1.0, 0.67, 0.1, 1.0,0.0, 3.0, 0.09, 4.0, 0.368])
psspy.add_plant_model(111,r"""5""",7,r"""TGOV1""",0,"",0,[],[],7,[ 0.04, 0.4, 1.05,0.0, 1.5, 5.0,0.0])
psspy.add_plant_model(111,r"""5""",3,r"""PSS2A""",0,"",6,[1,0,3,0,5,1],["","","","","",""],17,[ 2.0, 2.0, 0.02, 2.0, 4.0, 2.0, 0.333, 1.0, 0.5, 0.1, 30.0, 0.15, 0.03, 0.15, 0.03, 0.1,-0.1])



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

psspy.chsb(0,1,[-1,-1,-1,1,1,0])
psspy.chsb(0,1,[-1,-1,-1,1,2,0])
psspy.chsb(0,1,[-1,-1,-1,1,3,0])
psspy.chsb(0,1,[-1,-1,-1,1,4,0])
psspy.chsb(0,1,[-1,-1,-1,1,5,0])
psspy.chsb(0,1,[-1,-1,-1,1,6,0])
psspy.chsb(0,1,[-1,-1,-1,1,7,0])
psspy.chsb(0,1,[-1,-1,-1,1,12,0])
psspy.chsb(0,1,[-1,-1,-1,1,13,0])
psspy.chsb(0,1,[-1,-1,-1,1,14,0])
psspy.chsb(0,1,[-1,-1,-1,1,16,0])
psspy.cong(0)
psspy.conl(0,1,1,[0,0],[0.0,0.0,0.0,0.0])
psspy.conl(0,1,2,[0,0],[0.0,0.0,0.0,0.0])
psspy.conl(0,1,3,[0,0],[0.0,0.0,0.0,0.0])

# Start the simulation
psspy.strt_2([0, 0], r"C:\dyntestGAN")


psspy.run(1, 13.0,0,0,0)



    # Randomly select two lines to disable
lines_to_disable = random.sample(line_list, 1)


for index, line in enumerate(lines_to_disable):

    # Generate a random bus number between 1 and 118
    random_bus_number = random.randint(1, 118)


    #random_bus_number = random.randint(1, 118)
    lines_to_disable3 = random.sample(line_list, 1)
    # Disable the selected lines
    for line3 in lines_to_disable3:
        #psspy.dist_branch_trip(line3[0], line3[1], r"""1""")
        psspy.dist_branch_fault(line3[0],line3[1],r"""1""",1, 138.0,[0.0,-0.2E+10])


    

    # Apply bus fault
    #psspy.dist_3phase_bus_fault(random_bus_number, 0, 1)
    
    psspy.run(1, 13.6, 0, 0, 0)
    psspy.dist_clear_fault(1)
    psspy.run(1, 26.7, 0, 0, 0)


    
    
    outfile = r"""C:\dyntestGAN.out"""
    chnfobj = dyntools.CHNF(outfile)
    short_title, chanid, chandata = chnfobj.get_data()



    t = chandata['time']


    # Define channel identifier ranges  [100]+[103]+[111]
    channel_idsGA = (45, 46, 51, 52)      # Channel identifier range for angle of generators
    channel_idsGP = (84, 85, 86, 87, 88, 117, 118, 119, 120, 121)    # Channel identifier range for power of generators
    channel_idsV = (606, 663)    # Channel identifier range for voltage of buses
    channel_idsF = (516, 509, 517)    # Channel identifier range frequency of the buses

    # Create a dictionary to map channel identifier ranges to output folder names
    channel_folders = {
        channel_idsGA: "Rotor Angle",
        channel_idsGP: "Gen Power",
        channel_idsV: "Voltage",
        channel_idsF: "Frequency Deviation"
    }


for channel_ids, folder_name in channel_folders.items():
    output_folder = os.path.join(os.getcwd(), folder_name)
        
    for channel_id in channel_ids:
        channel_data = chandata[channel_id]

        # Create a DataFrame to hold the data
        df = pd.DataFrame({'Time': t, f'Channel_{channel_id}': channel_data})

        # Create a unique filename
        filename = os.path.join(output_folder, f'Channel_{channel_id}_Outage{outage_num + 1}.csv')

        # Save the data as a CSV file
        df.to_csv(filename, index=False)

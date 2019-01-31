#!/usr/bin/python3
""" plots AS-CustomerConeSize data:
        X-Axis: Minimum Customer Cone Size
        Y-Axis: Number of ASes matching
"""
import matplotlib.pyplot as plt
import numpy as np
# ------ SETUP DATA -------
# list of ASes that have VP for a measurement platform
# generating list of ASes that contain a VP for RIPE Atlas
# ========================================================
RIPE_LIST = []
with open('RIPE_LIST.txt') as fd:
    for string in fd:
        if string != 'None\n':
            RIPE_LIST.append(int(string.rstrip('\n')))
# ========================================================
SPEEDCHECKER_LIST = []
with open('speechecker_as_list.txt') as fd0:
    for num in fd0:
        SPEEDCHECKER_LIST.append(int(num.rstrip('\n')))
# ========================================================
RR_RESPONSIVE_LIST = []
with open('responsive_as_list.txt') as fd2:
    for num in fd2:
        RR_RESPONSIVE_LIST.append(int(num.rstrip('\n')))
# ========================================================
RR_REACHABLE_LIST = []
with open('reachable_as_list.txt') as fd3:
    for num in fd3:
        RR_REACHABLE_LIST.append(int(num.rstrip('\n')))
# ========================================================
RIPE_RESPONSIVE_LIST = RIPE_LIST + RR_RESPONSIVE_LIST
RIPE_REACHABLE_LIST = RIPE_LIST + RR_REACHABLE_LIST
CC_RIPE_RESPONSIVE = {}
CC_RIPE_REACHABLE = {}
TS_LIST = []

# dictionary to store AS-CustomerCone data
# key = customer cone size
# value = [number of ASes with customer cone size of the key,
#          number of ASes with a VP in the customer cone]
CC_RIPE = {}
CC_SPEEDCHECKER = {}
CC_RR_RESPONSIVE = {}
CC_RR_REACHABLE = {}
CC_TS = {}

CC_LIST = []

def generate_cc_data():
    """ generates list of CC_Data """
    with open('20190101ASData.txt') as f:
        f.readline()
        f.readline()
        for line in f:
            curr_line = line.split()
            CC_LIST.append(curr_line)
    for i in range(len(CC_LIST)):
        for j in range(len(CC_LIST[i])):
            CC_LIST[i][j] = int(CC_LIST[i][j])

# opens up Customer Cone Data and creates
# data points associated with the given
# list and dictionary
def generate_data(as_list, as_dictionary):
    """ generates data to plot """
    # last seen CC_SIZE
    prev_cc_size = 0
    for i in range(len(CC_LIST)):
        AS = CC_LIST[i][0]
        # subtract 1 from the length of a customer cone because
        # the AS of the customer cone is included in the list
        length = len(CC_LIST[i]) - 1
        # checks to see if the length
        # is in the given dictionary
        # covers all cases where there is already a customer cone size
        # in the dictionary
        if length == prev_cc_size:
            if AS in as_list:
                # if the AS is in the list of ASes to check for
                # increment necessary values
                as_dictionary[length][0] = as_dictionary[length][0] + 1
                as_dictionary[length][1] = as_dictionary[length][1] + 1
            else:
                # else just increment the size of the set
                as_dictionary[length][1] = as_dictionary[length][1] + 1
        # if the length key needs to be added to the dictionary
        # covers all cases where customer cone size is max or less
        else:
            if prev_cc_size == 0:
                if AS in as_list:
                    as_dictionary[length] = [1, 1]
                else:
                    as_dictionary[length] = [0, 1]
            else:
                as_dictionary[length] = [0, 0]
                if AS in as_list:
                    as_dictionary[length][0] = as_dictionary[prev_cc_size][0]+1
                    as_dictionary[length][1] = as_dictionary[prev_cc_size][1]+1
                else:
                    as_dictionary[length][0] = as_dictionary[prev_cc_size][0]+1
        prev_cc_size = length
generate_cc_data()
generate_data(RIPE_LIST, CC_RIPE)
generate_data(RR_RESPONSIVE_LIST, CC_RR_RESPONSIVE)
generate_data(RR_REACHABLE_LIST, CC_RR_REACHABLE)
generate_data(RIPE_REACHABLE_LIST, CC_RIPE_REACHABLE)
generate_data(RIPE_RESPONSIVE_LIST, CC_RIPE_RESPONSIVE)
generate_data(SPEEDCHECKER_LIST, CC_SPEEDCHECKER)
# ------- CLEAN UP DATA ---------
# ========================================================
RIPE_X_VALUES = list(CC_RIPE.keys())
RIPE_Y_VALUES = []
for key in RIPE_X_VALUES:
    RIPE_Y_VALUES.append(CC_RIPE[key][0])
# ========================================================
RESPONSIVE_X_VALUES = list(CC_RR_RESPONSIVE.keys())
RESPONSIVE_Y_VALUES = []
for key in RESPONSIVE_X_VALUES:
    RESPONSIVE_Y_VALUES.append(CC_RR_RESPONSIVE[key][0])
# ========================================================
REACHABLE_X_VALUES = list(CC_RR_REACHABLE.keys())
REACHABLE_Y_VALUES = []
for key in REACHABLE_X_VALUES:
    REACHABLE_Y_VALUES.append(CC_RR_REACHABLE[key][0])

RIPE_REACHABLE_X_VALUES = list(CC_RIPE_REACHABLE.keys())
RIPE_REACHABLE_Y_VALUES = []
for key in RIPE_REACHABLE_X_VALUES:
    RIPE_REACHABLE_Y_VALUES.append(CC_RIPE_REACHABLE[key][0])

# ========================================================
RIPE_RESPONSIVE_X_VALUES = list(CC_RIPE_RESPONSIVE.keys())
RIPE_RESPONSIVE_Y_VALUES = []
for key in RIPE_RESPONSIVE_X_VALUES:
    RIPE_RESPONSIVE_Y_VALUES.append(CC_RIPE_RESPONSIVE[key][0])

# ------- PLOT DATA -------
#plt.ylim(bottom=0)
#plt.ylim(top=32000)
#plt.xlim(left=0)
#plt.xlim(right=len(list(REACHABLE_X_VALUES))+10)
#print(REACHABLE_Y_VALUES)
# PLOTTING RIPE VALUES ===================================
plt.semilogx(RIPE_X_VALUES, RIPE_Y_VALUES, label="RIPE")
plt.semilogx(RESPONSIVE_X_VALUES, RESPONSIVE_Y_VALUES, label="RR-RESPONSIVE")
plt.semilogx(REACHABLE_X_VALUES, REACHABLE_Y_VALUES, label="RR-REACHABLE")
plt.semilogx(RIPE_REACHABLE_X_VALUES, RIPE_REACHABLE_Y_VALUES,
             label="RIPE-REACHABLE")
plt.semilogx(RIPE_RESPONSIVE_X_VALUES, RIPE_RESPONSIVE_Y_VALUES,
             label="RIPE-RESPONSIVE")
#plt.bar(REACHABLE_X_VALUES, REACHABLE_Y_VALUES, width=1, color='g')
# PLOTTING RESPONSIVE VALUES =============================
#ax.bar(RESPONSIVE_X_VALUES, RESPONSIVE_Y_VALUES, width=w, color='g', label="RR-RESPONSIVE")
# PLOTTING REACHABLE VALUES =============================-
#ax.bar(REACHABLE_X_VALUES, REACHABLE_Y_VALUES, width=w, color='r', label="RR-REACHABLE")
# PLOT INFORMATION =======================================
#plt.xticks([i for i in range(len(REACHABLE_X_VALUES))], REACHABLE_X_VALUES, rotation='90')
#plt.xlabel('Minimum Customer Cone Size')
#plt.ylabel('Number of ASes Intersecting')

#plt.show()
plt.xlabel('Minimum Customer Cone Size')
plt.ylabel('# of ASes Hosting Vantage Points')
#plt.ylim(top=4000)
#plt.ylim(bottom=0)
#plt.yticks(np.arange(0, 4000, 500))
plt.legend()
plt.show()

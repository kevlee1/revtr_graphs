#!/usr/bin/python3
""" plots AS-CustomerConeSize data:
        X-Axis: Minimum Customer Cone Size
        Y-Axis: Percentage of ASes Hosting Vantage Points
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
with open('speedchecker_as_list.txt') as fd0:
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
TS_LIST = []
RIPE_RESPONSIVE_LIST = RIPE_LIST + RR_RESPONSIVE_LIST
RIPE_REACHABLE_LIST = RIPE_LIST + RR_REACHABLE_LIST
CC_RIPE_RESPONSIVE = {}
CC_RIPE_REACHABLE = {}
ALL_LIST = RIPE_LIST + RR_RESPONSIVE_LIST + RR_REACHABLE_LIST + SPEEDCHECKER_LIST
CC_ALL = {}
RIPE_SPEEDCHECKER_LIST = SPEEDCHECKER_LIST + RIPE_LIST
CC_RIPE_SPEEDCHECKER = {}

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
            as_dictionary[length][0].append(AS)
            if AS in as_list:
                # if the AS is in the list of ASes to check for
                # increment necessary values
                as_dictionary[length][1] = as_dictionary[length][1] + 1
                as_dictionary[length][2] = as_dictionary[length][2] + 1
            else:
                # else just increment the size of the set
                as_dictionary[length][2] = as_dictionary[length][2] + 1
        # if the length key needs to be added to the dictionary
        # covers all cases where customer cone size is max or less
        else:
            if prev_cc_size == 0:
                intersection = len(set([AS]) & set(as_list))
                as_dictionary[length] = [[AS], intersection, 1]
            else:
                # check which keys (their as_set) needed to appended
                # to this length (as_set)
                # finished creating list of ASes
                # for this minimum customer cone size
                as_dictionary[length] = [[], 0, 0]
                as_set = as_dictionary[prev_cc_size][0].copy()
                as_dictionary[length][0] = as_set
                as_dictionary[length][0].append(AS)
                # count number of intersections between set of ASes
                # for this minimum customer cone size and
                # ASes of VPs in a certain platform
                intersection_count = len(set(as_set) & set(as_list))
                as_dictionary[length][1] = intersection_count
                as_dictionary[length][2] = len(as_dictionary[length][0])
        prev_cc_size = length
generate_cc_data()
generate_data(RIPE_LIST, CC_RIPE)
generate_data(RR_RESPONSIVE_LIST, CC_RR_RESPONSIVE)
generate_data(RR_REACHABLE_LIST, CC_RR_REACHABLE)
generate_data(RIPE_REACHABLE_LIST, CC_RIPE_REACHABLE)
generate_data(RIPE_RESPONSIVE_LIST, CC_RIPE_RESPONSIVE)
generate_data(ALL_LIST, CC_ALL)
generate_data(SPEEDCHECKER_LIST, CC_SPEEDCHECKER)
generate_data(RIPE_SPEEDCHECKER_LIST, CC_RIPE_SPEEDCHECKER)
# ------- CLEAN UP DATA ---------
# ========================================================
RIPE_PLOT = {}
for key in CC_RIPE:
    RIPE_PLOT[key] = round(100 * CC_RIPE[key][1] / CC_RIPE[key][2], 2)
RIPE_X_VALUES = list(RIPE_PLOT.keys())
RIPE_Y_VALUES = []
for key in RIPE_X_VALUES:
    RIPE_Y_VALUES.append(RIPE_PLOT[key])
# ========================================================
RESPONSIVE_PLOT = {}
for key in CC_RR_RESPONSIVE:
    RESPONSIVE_PLOT[key] = round(100 * CC_RR_RESPONSIVE[key][1] /
                                 CC_RR_RESPONSIVE[key][2], 2)
RESPONSIVE_X_VALUES = list(RESPONSIVE_PLOT.keys())
RESPONSIVE_Y_VALUES = []
for key in RESPONSIVE_X_VALUES:
    RESPONSIVE_Y_VALUES.append(RESPONSIVE_PLOT[key])
# ========================================================
REACHABLE_PLOT = {}
for key in CC_RR_REACHABLE:
    REACHABLE_PLOT[key] = round(100 * CC_RR_REACHABLE[key][1] /
                                CC_RR_REACHABLE[key][2], 2)
REACHABLE_X_VALUES = list(REACHABLE_PLOT.keys())
REACHABLE_Y_VALUES = []
for key in REACHABLE_X_VALUES:
    REACHABLE_Y_VALUES.append(REACHABLE_PLOT[key])
# ================================================================
RIPE_RESPONSIVE_PLOT = {}
for key in CC_RIPE_RESPONSIVE:
    RIPE_RESPONSIVE_PLOT[key] = round(100 * CC_RIPE_RESPONSIVE[key][1] /
                                 CC_RIPE_RESPONSIVE[key][2], 2)
RIPE_RESPONSIVE_X_VALUES = list(RIPE_RESPONSIVE_PLOT.keys())
RIPE_RESPONSIVE_Y_VALUES = []
for key in RIPE_RESPONSIVE_X_VALUES:
    RIPE_RESPONSIVE_Y_VALUES.append(RIPE_RESPONSIVE_PLOT[key])
# ========================================================
RIPE_REACHABLE_PLOT = {}
for key in CC_RIPE_REACHABLE:
    RIPE_REACHABLE_PLOT[key] = round(100 * CC_RIPE_REACHABLE[key][1] /
                                CC_RIPE_REACHABLE[key][2], 2)
RIPE_REACHABLE_X_VALUES = list(RIPE_REACHABLE_PLOT.keys())
RIPE_REACHABLE_Y_VALUES = []
for key in RIPE_REACHABLE_X_VALUES:
    RIPE_REACHABLE_Y_VALUES.append(RIPE_REACHABLE_PLOT[key])
# =========================================================
ALL_PLOT = {}
for key in CC_ALL:
    ALL_PLOT[key] = round(100 * CC_ALL[key][1] / CC_ALL[key][2], 2)
ALL_X_VALUES = list(ALL_PLOT.keys())
ALL_Y_VALUES = []
for key in ALL_X_VALUES:
    ALL_Y_VALUES.append(ALL_PLOT[key])
# =========================================================
SPEEDCHECKER_PLOT = {}
for key in CC_SPEEDCHECKER:
    SPEEDCHECKER_PLOT[key] = round(100 * CC_SPEEDCHECKER[key][1] /
                                   CC_SPEEDCHECKER[key][2], 2)
SPEEDCHECKER_X_VALUES = list(SPEEDCHECKER_PLOT.keys())
SPEEDCHECKER_Y_VALUES = []
for key in SPEEDCHECKER_X_VALUES:
    SPEEDCHECKER_Y_VALUES.append(SPEEDCHECKER_PLOT[key])
# =========================================================
RIPE_SPEEDCHECKER_PLOT = {}
for key in CC_RIPE_SPEEDCHECKER:
    RIPE_SPEEDCHECKER_PLOT[key] = round(100 * CC_RIPE_SPEEDCHECKER[key][1] /
                                        CC_RIPE_SPEEDCHECKER[key][2], 2)
RIPE_SPEEDCHECKER_X_VALUES = list(RIPE_SPEEDCHECKER_PLOT.keys())
RIPE_SPEEDCHECKER_Y_VALUES = []
for key in RIPE_SPEEDCHECKER_X_VALUES:
    RIPE_SPEEDCHECKER_Y_VALUES.append(RIPE_SPEEDCHECKER_PLOT[key])
# ------- PLOT DATA -------
plt.semilogx(ALL_X_VALUES, ALL_Y_VALUES, label="ALL PLATFORMS")
plt.semilogx(RIPE_RESPONSIVE_X_VALUES, RIPE_RESPONSIVE_Y_VALUES, label="RIPE + RR-RESPONSIVE")
# PLOTTING RESPONSIVE VALUES =============================
plt.semilogx(RESPONSIVE_X_VALUES, RESPONSIVE_Y_VALUES, label="RR-RESPONSIVE")
plt.semilogx(RIPE_REACHABLE_X_VALUES, RIPE_REACHABLE_Y_VALUES,
             label="RIPE + RR-REACHABLE")
# PLOTTING REACHABLE VALUES =============================-
plt.semilogx(REACHABLE_X_VALUES, REACHABLE_Y_VALUES, label="RR-REACHABLE")
# PLOTTING RIPE_SPEEDCHECKER VALUES ======================
plt.semilogx(RIPE_SPEEDCHECKER_X_VALUES, RIPE_SPEEDCHECKER_Y_VALUES,
             label="RIPE + SPEEDCHECKER")
# PLOTTING SPEEDCHECKER VALUES ===========================
plt.semilogx(SPEEDCHECKER_X_VALUES, SPEEDCHECKER_Y_VALUES, label="SPEEDCHECKER")
# PLOTTING RIPE VALUES ===================================
plt.semilogx(RIPE_X_VALUES, RIPE_Y_VALUES, label="RIPE")
# PLOT INFORMATION =======================================
plt.xlabel('Minimum Customer Cone Size')
plt.ylabel('% of ASes Hosting Vantage Points')
plt.ylim(top=100)
plt.ylim(bottom=0)
plt.yticks(np.arange(0, 101, 20))
plt.legend()
plt.show()

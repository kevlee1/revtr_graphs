#!/usr/bin/python3
""" plots AS-CustomerConeSize data """
import matplotlib.pyplot as plt
from ripe.atlas.cousteau import ProbeRequest
# ------ SETUP DATA -------
# list of ASes that have VP for a measurement platform
# generating list of ASes that contain a VP for RIPE Atlas
RIPE_LIST = []
with open('RIPE_LIST.txt') as fd:
    for string in fd:
        if string != 'None\n':
            RIPE_LIST.append(string.rstrip('\n'))

SPEEDCHECKER_LIST = []
RR_RESPONSIVE_LIST = []
RR_REACHABLE_LIST = []
TS_LIST = []

# dictionary to store AS-CustomerCone data
# key = customer cone size
# value = [number of ASes with customer cone size of the key,
#          number of ASes with a VP in the customer cone]
CC_AS_RIPE = {}
CC_AS_SPEEDCHECKER = {}
CC_AS_RR_RESPONSIVE = {}
CC_AS_RR_REACHABLE = {}
CC_AS_TS = {}

# opens up Customer Cone Data and creates
# data points associated with the given
# list and dictionary
def generate_data(as_list, as_dictionary):
    """ generates data to plot """
    # opening up Customer Cone data
    with open('20190101ASData.txt') as f:
        # have to skip the first two lines
        f.readline()
        f.readline()
        # for loop to iterate through the file
        for line in f:
            # splits the line into a list
            curr_line = line.split()
            # skips the first element because
            # it is included in the list
            curr_line.pop(0)
            length = len(curr_line)
            # checks to see if the length
            # is in the given dictionary
            if length in as_dictionary:
                # check to see if there is any overlap between
                # the two lists
                if set(curr_line) & set(as_list):
                    # if there is, update counters
                    as_dictionary[length][0] = as_dictionary[length][0] + 1
                    as_dictionary[length][1] = as_dictionary[length][1] + 1
                # if there isn't, just increment the seen total
                else:
                    as_dictionary[length][0] = as_dictionary[length][0] + 1
            # if the length key needs to be added to the dictionary
            else:
                if set(curr_line) & set(as_list):
                    as_dictionary[length] = [1, 1]
                else:
                    as_dictionary[length] = [1, 0]

generate_data(RIPE_LIST, CC_AS_RIPE)
# ------- CLEAN UP DATA ---------
PLOT_RIPE = {}
for key in CC_AS_RIPE:
    PLOT_RIPE[key] = round(100 * float(CC_AS_RIPE[key][1]) /
                           float(CC_AS_RIPE[key][0]), 2)
print(PLOT_RIPE)
# ------- PLOT DATA -------

""" translates file of ip addresses into ASNs """

# initialize module and load IP to ASN database
SPEED_LIST = []
with open('speedCheckerData.txt') as f:
    f.readline()
    for line in f:
        SPEED_LIST.append(line.split(',')[2])
print(SPEED_LIST)
with open('speedchecker_as_list.txt', "w") as fd:
    for asn in SPEED_LIST:
        if asn != "" or asn:
            fd.write("%d\n" % int(asn))

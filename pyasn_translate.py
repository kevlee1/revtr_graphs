""" translates file of ip addresses into ASNs """
import pyasn

# initialize module and load IP to ASN database
asndb = pyasn.pyasn('ipasn_db_file')
ASN_LIST = []
with open('global_reach.txt') as f:
    for line in f:
        ASN_LIST.append(asndb.lookup(line.rstrip('\n'))[0])
print(len(ASN_LIST))
with open('reachable_as_list.txt', "w") as fd:
    for asn in ASN_LIST:
        if asn:
            fd.write("%d\n" % asn)

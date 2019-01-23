#!/usr/bin/python3
""" generates list of VPs from a platform """
from ripe.atlas.cousteau import ProbeRequest
RIPE_LIST = []
FILTERS = {"status": "1"}
PROBES = ProbeRequest(**FILTERS)
for probe in PROBES:
    RIPE_LIST.append(str(probe["asn_v4"]))
print(PROBES.total_count)
with open('RIPE_LIST.txt', 'w') as f:
    for item in RIPE_LIST:
        f.write("%s\n" % item)

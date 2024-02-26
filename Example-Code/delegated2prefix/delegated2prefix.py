#!/usr/bin/env python3

import sys
import ipaddress

# convert delegated file inputs to prefix/len

for i in sys.stdin:
    if i == None:
        continue
    elif i == "":
        continue
    elif i.startswith("#"):
        continue
    elif i.startswith("2"):
        continue
    elif "nro" in i:
        continue
    elif "summary" in i:
        continue

    a = i.rstrip().split("|")

    if "asn" in i:
        asn = int(a[3])
        cnt = int(a[4])
        for j in range(asn, asn + cnt):
            print(j)
    elif "ipv4" in i:
        st = int.from_bytes(ipaddress.IPv4Address(a[3]).packed, byteorder='big')
        ed = st + int(a[4]) - 1
        for j in ipaddress.summarize_address_range(
            ipaddress.IPv4Address(st), ipaddress.IPv4Address(ed)
        ):
            print(j)
    elif "ipv6" in i:
        pfx = a[3]
        len = a[4]
        print("/".join([pfx, len]))
    else:
        print("unknown type", i)
        sys.exit(1)

# Converting delegated file format to a prefix/len

the RIR Delegated files consist of "|" separated fields, so basically CSV.

normally prefixes are shown as prefix/len where len is the number of set bits
in the prefix so ```192.168.0.0/16``` has the first 16 bits of the 32 bit address
set to ```192.168```

as well as prefixes, IPv4 address ranges can be shown as the pair start-end so
```192.168.0.0/16``` is the same as ```192.168.0.0 - 192.168.255.255```

Because some IPv4 was given out as ranges which are not a single prefix, but
were recorded as a start-end sequence historically as a single transaction, the
format for IPv4 in a delegated file is ```IPv4 Prefix base|Host Count``` ie the range
can be calculated as (IPv4 Prefix base) - (IPv4 Prefix base) + (Host Count) -where the second field
is re-presented as the IPv4 address it represents. so 192.168.0.0 - (192.168.0.0 + 65535)

for AS numbers, the record format is ```Base AS|count``` which means all the AS numbers from the base AS
in sequence. So ```12345|4``` would mean ASNs ```12345, 12346, 12347, 12348```.

Because prefixes are innately more useful these days calculating things about IP addresses this python
script reads the delegated file and emits the list of ASN and IPv4 and IPv6 in their natural prefix
form. It converts the start|count format into the set of prefixes which are equivalent.

## Dependencies

This script depends only on packages distributed inside the normal Python3 release.

 * ```import sys```
 * ```import ipaddress```

## Logic

The script skips comments (denoted by ```#``` at the start of the line) and the summary and version information
in the delegated file.

## risks of running it on unfiltered data.

the un-filtered delegated file includes undelegated resources retained by IANA.

For the ASN, it will enumerate ALL 32 bit numbers from 0 to 4,294,967,296.

For IPv4 and IPv6 it's safer because the unallocated spaces represent by a small number of prefixes.

To avoid this problem, ```egrep -v "^iana"``` as a filter removes the blocks which are named as existing
solely in IANA which usefully includes all the unallocated ASN, and removes this problem. The more general
```grep -v iana``` will find other resources, which are not meant to be excluded.

from scapy.all import *

i = IPv6()
# 適宜変更が必要
i.dst = "2401:2500:102:2213:133:242:206:60"
q = ICMPv6EchoRequest()
p = (i/q)
sr1(p)

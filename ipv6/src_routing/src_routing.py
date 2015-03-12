from scapy.all import *

ip = IPv6()
ip.dst = "2401:2500:102:2213:133:242:206:60"
ip.nh = 43

header = IPv6ExtHdrRouting(addresses=['7::7'])
header.nh = 17

udp = UDP()
udp.sport = 3939
udp.dport = 53
udp.len = 100
payload = ('x'*100)

packet = ip/header/udp/payload

packet.show()
send(packet, count=100)

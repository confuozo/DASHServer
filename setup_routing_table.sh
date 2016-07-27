#!/bin/zsh
# setup the LTE host.
# address of LTE = 192.168.42.110, interface = enp0s29u1u1, gateway = 192.168.42.129
# WiFi ip = 192.168.0.110
# NOTE: adjust the values in this script accordingly

# create a new routing table 'rt2' and add the default gateway
sudo ip route add 192.168.42.0/24 dev enp0s29u1u1 src 192.168.42.117 table rt2
sudo ip route add default via 192.168.42.129 dev enp0s29u1u1 table rt2

# add a rule to use rt2 for all packets sent to the LTE interface        
sudo ip rule add from 192.168.42.117/32 table rt2                     
sudo ip rule add to 192.168.42.117/32 table rt2

# delete LTE from the default routing table
sudo route del default dev enp0s29u1u1  

# Test
curl --interface "192.168.42.117" --header "Range: 0-1000" -vvv http://dash.edgesuite.net/dash264/TestCasesHD/1a/qualcomm/1/BBB_1080_8M_video_init.mp4
curl --interface "192.168.0.110" --header "Range: 0-1000" -vvv http://dash.edgesuite.net/dash264/TestCasesHD/1a/qualcomm/1/BBB_1080_8M_video_init.mp4
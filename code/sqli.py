from scapy.all import *
import pandas as pd

# Read the PCAP file
packets = rdpcap("C://Users//Asus//Desktop//fyp_azfar//attack//sqli//sqli.pcapng")

# Define the columns you want to extract
columns = ['duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes', 'land', 'wrong_fragment', 'urgent',
           'hot', 'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell', 'su_attempted', 'num_root',
           'num_file_creations', 'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_host_login',
           'is_guest_login', 'count', 'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate',
           'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count',
           'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',
           'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'dst_host_rerror_rate',
           'dst_host_srv_rerror_rate', 'attack', 'level']

# Create a list to store extracted data
extracted_data = []

# Iterate through each packet and extract the desired fields
for packet in packets:
    packet_data = {}
    for col in columns:
        if hasattr(packet, 'payload'):
            ip_layer = packet.payload
            if hasattr(ip_layer, 'payload'):
                tcp_layer = ip_layer.payload
                if hasattr(tcp_layer, 'dport') and hasattr(tcp_layer, 'sport'):
                    # Considering TCP packets only for this example
                    if tcp_layer.dport == 80 or tcp_layer.sport == 80:  # Assuming HTTP traffic
                        packet_data[col] = tcp_layer.getfieldval(col)
    extracted_data.append(packet_data)

# Convert extracted data to DataFrame
df = pd.DataFrame(extracted_data)

# Print the DataFrame
print(df)

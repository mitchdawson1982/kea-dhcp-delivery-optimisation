import json
import uuid
import os

KEA_DHCP_INPUT_FILE_PATH = os.path.join(os.getcwd(), 'config', 'kea_dhcp_input.json')
KEA_DHCP_OUTPUT_FILE_PATH = os.path.join('config', 'kea_dhcp_output.json')
SITE_ID_GUID_MAP_PATH = os.path.join('config', 'fits_id_guid_map.json')

# Define the dhcp option data structure.
option_data = [
    {
        "name": "delivery-optimisation",
        "space": "dhcp4",
        "code": 234,
        "data": "",
    }
]

# Open the kea dhcp config fie, load the json into a python dictionary and close the input file.
kea_config_file = open(KEA_DHCP_INPUT_FILE_PATH, 'r')
kea_data = json.load(kea_config_file)
kea_config_file.close()

# Open the fits id guid map config fie, load the json into a python dictionary and close the input file.
fits_id_guid_map_file = open(SITE_ID_GUID_MAP_PATH, 'r')
fits_id_guid_map_data = json.load(kea_config_file)
fits_id_guid_map_file.close()


# Break out the shared networks element from the kea config.
shared_nets = kea_data['Dhcp4']['shared-networks']

# Iterate through the shared networks.
for shared_net in shared_nets:
    subnets = shared_net['subnet4']
    if not subnets:
        continue
    for subnet in subnets:
        site_id = subnet['user-context']['site-id']
        if site_id not in fits_id_guid_map_data:
            fits_id_guid_map_data[site_id] = str(uuid.uuid4())

        if 'option-data' in subnet:
            continue

        # option_data[0]['data'] = fits_id_guid_map[site_id]
        # subnet["option-data"] = option_data


site_id_map_json = open(SITE_ID_GUID_MAP_PATH, 'w')
site_id_map_json.write(json.dumps(fits_id_guid_map_data))

# new_json = open('new_kea_dhcp.json', 'w')
# new_json.write(json.dumps(kea_data))
# new_json.close()




# pprint(kea_data['Dhcp4']['option-data'])


# for subnet in subnets:
#     pass
import json

# helping function to check if key exists in a portal
def check_key(key : str, portal : dict) -> bool:
    for dict_element in portal:
        if key == dict_element["key"]:
            return True
    return False

# opening JSON file
f = open('TKeys.json')

# returns JSON object as a dictionary
data = json.load(f)

# creating map_final.txt
with open("map_final.txt", "w") as f_target:
    for id, entry in enumerate(data['map_final'], 1):
        map= '1' if check_key(entry["key"], data['map_final']) else '0'
        avk= '1' if check_key(entry["key"], data['avk_final']) else '0'
        hr= '1' if check_key(entry["key"], data['hr_final']) else '0'
        f_target.write(f'CALL i18N_insertOrUpdate({entry["key"]}, {entry["de"]}, {entry["en"]}, {map}, {avk}, {hr}, @{id});\n')

# creating avk_final.txt
with open("avk_final.txt", "w") as f_target:
    for id, entry in enumerate(data['avk_final'], 1):
        map= '1' if check_key(entry["key"], data['map_final']) else '0'
        avk= '1' if check_key(entry["key"], data['avk_final']) else '0'
        hr= '1' if check_key(entry["key"], data['hr_final']) else '0'
        f_target.write(f'CALL i18N_insertOrUpdate({entry["key"]}, {entry["de"]}, {entry["en"]}, {map}, {avk}, {hr}, @{id});\n')

# creating hr_final.txt
with open("hr_final.txt", "w") as f_target:
    for id, entry in enumerate(data['hr_final'], 1):
        map= '1' if check_key(entry["key"], data['map_final']) else '0'
        avk= '1' if check_key(entry["key"], data['avk_final']) else '0'
        hr= '1' if check_key(entry["key"], data['hr_final']) else '0'
        f_target.write(f'CALL i18N_insertOrUpdate({entry["key"]}, {entry["de"]}, {map}, {avk}, {hr}, @{id});\n')

# creating final_texts.txt
with open("final_texts.txt", "w") as f_target:
    for id, entry in enumerate(data['final_texts'], 1):
        if 'en' not in entry:
            entry["en"] = 'None'
        map= '1' if check_key(entry["key"], data['map_final']) else '0'
        avk= '1' if check_key(entry["key"], data['avk_final']) else '0'
        hr= '1' if check_key(entry["key"], data['hr_final']) else '0'
        f_target.write(f'CALL i18N_insertOrUpdate({entry["key"]}, {entry["de"]}, {entry["en"]}, {map}, {avk}, {hr}, @{id});\n')

# closing file
f.close()

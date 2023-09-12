from dm_control import mjcf
from dm_control.mjcf import export_with_assets
import json


# Specify the path to your JSON file
json_file_path = 'output_vertices_CE3_test2.json'
json_data = None
try:
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)
        # 'data' now contains the parsed JSON content    
except FileNotFoundError:
    print(f"The file '{json_file_path}' was not found.")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")

#print(type(json_data["vertices"][-1][0]))

mjcf_model = mjcf.RootElement()

for i, data in enumerate(json_data["vertices"]):
    print(data)
    my_masses = mjcf_model.worldbody.add('geom', name=f'point_mass_{i}',
                                    type='sphere', pos=data , size=".1", mass="0.01")
#print(my_masses)  
#print(mjcf_model)  # MJCF Element: <mujoco/>
#print("asdd")

xml_filename = 'my_masses.xml'

#mjcf_model.to_xml_string(xml_filename)


export_with_assets(mjcf_model, out_dir='/home/kumyew/Desktop/FYP/tetgen', out_file_name=xml_filename)

print(f'MJCF model saved to {xml_filename}')
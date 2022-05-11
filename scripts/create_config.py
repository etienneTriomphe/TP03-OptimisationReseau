from jinja2 import Template, Environment, FileSystemLoader
import json

def load_json_data_from_file(file_path):
    try:
        with open(file_path) as f:
            data = json.load(f)
            f.close()
    
    except IOError:
        print("Could not read file:", file_path)

    return data

def render_network_config(template_name, data):
    template = env.get_template(template_name) 
    return template.render(data) 

def save_built_config(file_name, data):
    try:
        with open(file_name, "w") as f:
            f.write(data)
            f.close()
    
    except IOError:
        print("Could not read file:", file_name)

def create_config_cpe_lyon_batA():    
    r1 = render_network_config("vlan_router.j2",load_json_data_from_file("./data/R1_CPE_LYON_BAT_A.json"))
    r1 += render_network_config("vrrp_router.j2",load_json_data_from_file("./data/R1_CPE_LYON_BAT_A.json"))

    r2 = render_network_config("vlan_router.j2",load_json_data_from_file("./data/R2_CPE_LYON_BAT_A.json"))
    r2 += render_network_config("vrrp_router.j2",load_json_data_from_file("./data/R2_CPE_LYON_BAT_A.json"))

    esw1 = render_network_config("vlan_switch.j2",load_json_data_from_file("./data/ESW1_CPE_LYON_BAT_A.json"))

    return r1, r2, esw1

def create_config_cpe_lyon_batB():
    r1 = render_network_config("vlan_router.j2",load_json_data_from_file("./data/R1_CPE_LYON_BAT_B.json"))
    r1 += render_network_config("vrrp_router.j2",load_json_data_from_file("./data/R1_CPE_LYON_BAT_B.json"))

    r2 = render_network_config("vlan_router.j2",load_json_data_from_file("./data/R2_CPE_LYON_BAT_B.json"))
    r2 += render_network_config("vrrp_router.j2",load_json_data_from_file("./data/R2_CPE_LYON_BAT_B.json"))

    esw1 = render_network_config("vlan_switch.j2",load_json_data_from_file("./data/ESW1_CPE_LYON_BAT_B.json"))

    return r1, r2, esw1
    
if __name__ == "__main__":

    env = Environment(loader=FileSystemLoader("templates"))

    """
        process question 3 to 5:
    """
    #question 3:
    r1_config, r2_config, esw1_config = create_config_cpe_lyon_batA()
    #print(config)
    #question 4:
    save_built_config('config/R1_CPE_LYON_BAT_A.conf', r1_config)
    save_built_config('config/R2_CPE_LYON_BAT_A.conf', r2_config)
    save_built_config('config/ESW1_CPE_LYON_BAT_A.conf', esw1_config)

    #question 5:
    r1_config, r2_config, esw1_config = create_config_cpe_lyon_batB()
    save_built_config('config/R1_CPE_LYON_BAT_B.conf', r1_config)
    save_built_config('config/R2_CPE_LYON_BAT_B.conf', r2_config)
    save_built_config('config/ESW1_CPE_LYON_BAT_B.conf', esw1_config)
    
    
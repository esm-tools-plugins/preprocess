import os

def preprocess(config):
    pp_method = pp_type = None
    for model in config["general"]["valid_model_names"]:
        if "preprocess" in config[model]:
            for name in config[model]["preprocess"]:
                if "method" in config[model]["preprocess"][name]:
                    pp_method = config[model]["preprocess"][name]["method"]
                if "type" in config[model]["preprocess"][name]:
                    pp_type = config[model]["preprocess"][name]["type"]
                if pp_type == "shell" and pp_method:
                    try:
                        os.command(pp_method)
                    except:
                        print("Shell execution of command: '" + pp_method + "' failed, please check...")
    return config
                

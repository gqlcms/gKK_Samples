import json
import os

def build_card(**kwargs):
    templete_card_default = {
        "path":"Config/templete_card/",
        "customize" : "templete_customizecards.dat",
        "process" : "templete_proc_card.dat",
        "run" : "templete_run_card.dat",
        "extramodels" : "templete_extramodels.dat",
    }
    templete_card = kwargs.get("templete_card",templete_card_default)
    
    card_parameters = kwargs.get("card_parameters",{})
    
    file_outdir = card_parameters["output"]["output_dir"]+card_parameters["process"]["output_dir"]+"/"
    file_outdir_relative_path = card_parameters["output"]["output_dir_relative_path"]+card_parameters["process"]["output_dir"]+"/"
    
    if not os.path.isfile(file_outdir):
        os.system("mkdir "+file_outdir)
    
    runcommands_default = "./gridpack_generation.sh {name_of_process_card_without _proc_card} {folder_containing_cards_relative_to_current_location} >{name_of_process_card_without _proc_card}.debug 2>&1 &"
    runcommands = kwargs.get("runcommands",runcommands_default)
    runcommands_par = {
        "name_of_process_card_without _proc_card" :  card_parameters["process"]["output_dir"] ,
        "folder_containing_cards_relative_to_current_location" :  file_outdir_relative_path ,
    }
    
    run_scripts = card_parameters["output"]["run_scripts"]
    with open(run_scripts, "w") as f:
        f.write(runcommands.format(**runcommands_par))
    
    for key in templete_card:
        if key!= "path":
            output_card_name = templete_card[key].replace( "templete",card_parameters["process"]["output_dir"] )
            templete = "{path}/{filename}".format( path = templete_card["path"], filename = templete_card[key])
            fin = open(templete,"r")
            cardin = fin.read()
            fileout = file_outdir+templete_card[key].replace( "templete", card_parameters["process"]["output_dir"] )
            with open(fileout,"w") as f:
                f.write(cardin.format(**(card_parameters.get(key,{}))))
            fin.close()

config = "Config/Card/3000_1500.json"
with open(config,"r") as f:
    card_parameters = json.load(f)

build_card(card_parameters = card_parameters)
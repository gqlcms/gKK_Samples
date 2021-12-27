import json

def process_output_dir(**kwargs):
    customize = kwargs.get("customize",{})
    # default_output_dir_templete = "Res1ToRes2GluToGluVV_M1-{KKGluon_mass}_R-{ratio} -nojpeg" # ratio is not good for case : (3000,1000)
    default_output_dir_templete = "Res1ToRes2GluToGluVV_M1-{KKGluon_mass}_R-{KKRadion_mass}"
    output_dir_templete = kwargs.get("output_dir_templete",{})
    
    ratio = str(float(customize["KKRadion_mass"])/float(customize["KKGluon_mass"])).replace(".","p")
    customize["ratio"] = ratio
    output_dir = default_output_dir_templete.format(**customize)
    
    return output_dir

card_parameters = {}

card_parameters["customize"] = {
    "gravity_coupling" : "5" ,
    "KKphoton_coupling" : "2.65" ,
    "KKW_coupling" : "3" ,
    "KKgluon_coupling" : "6" ,
    "KKGluon_mass" : "3000" ,
    "KKRadion_mass" : "1500" ,
}

card_parameters["process"] = {
    "output_dir" : "",
    "Radion_Decay" : "R > v v",
}
card_parameters["process"]["output_dir"] = process_output_dir( customize = card_parameters["customize"] )

card_parameters["output"] = {
    "output_dir" : "/eos/user/q/qiguo/gen/genproductions/bin/MadGraph5_aMCatNLO/cards/gKK/UL2016/V1/",
    "run_scripts" : "gKK_21_12_26.sh",
}

card_parameters["output"]["output_dir_relative_path"] = card_parameters["output"]["output_dir"].split("MadGraph5_aMCatNLO/")[-1]
card_parameters["output"]["run_scripts"] = card_parameters["output"]["output_dir"].replace(card_parameters["output"]["output_dir_relative_path"],"")+card_parameters["output"]["run_scripts"]



config = "/home/gql/tutorial/lib/gKK/signal_sample_produciotn/Code/V1/Config/Card/3000_1500.json"

with open(config,"w") as f:
    json.dump(card_parameters,f,indent = 4)

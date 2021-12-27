# download mg

MG_EXT=".tar.gz"
MG=MG5_aMC_v2.6.5$MG_EXT
MGSOURCE=https://cms-project-generators.web.cern.ch/cms-project-generators/$MG
wget --no-check-certificate ${MGSOURCE}
tar xzf ${MG}

# down load the model
model=Radion_GKK_UFO.zip
cd MG5_aMC_v2_6_5/models/
wget --no-check-certificate https://cms-project-generators.web.cern.ch/cms-project-generators/$model
unzip $model

# run mg scripts
cd 
./mg5_aMC /eos/user/q/qiguo/gKK/SignalSample/PrivateSample/V1/scripts/Mg_Scripts >debug 2>&1 
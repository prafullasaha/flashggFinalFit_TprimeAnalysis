# Python script to hold replacement model mapping for different analyses
from collections import OrderedDict as od

# Add analyses to globalReplacementMap. See "STXS" as an example
globalReplacementMap = od()

# Example analysis which with cats Untagged_Tag0,VBF_Tag0
globalReplacementMap['example'] = od()
# For WRONG VERTEX SCENARIO:
#  * single proc x cat for wrong vertex since for dZ > 1cm shape independent of proc x cat
#  * use proc x cat with highest number of WV events
globalReplacementMap['example']['procWV'] = "GG2H"
globalReplacementMap['example']['catWV'] = "Untagged_Tag0"
# For RIGHT VERTEX SCENARIO:
#  * default you should add is diagonal process from given category 
#  * if few events in diagonal process then may need to change the category aswell (see catRVMap)
#  * map must contain entry for all cats being processed (for replacement proc and cat)
globalReplacementMap['example']['procRVMap'] = od()
globalReplacementMap["example"]["procRVMap"]["Untagged_Tag0"] = "GG2H"
globalReplacementMap["example"]["procRVMap"]["VBF_Tag0"] = "VBF"
# Replacement category for RV fit
globalReplacementMap["example"]["catRVMap"] = od()
globalReplacementMap["example"]["catRVMap"]["Untagged_Tag0"] = "Untagged_Tag0"
globalReplacementMap["example"]["catRVMap"]["VBF_Tag0"] = "VBF_Tag0"

#Tprime Analysis
#globalReplacementMap['Tprime_600'] = od()
#globalReplacementMap['Tprime_600']['procWV'] = "THQ"
#globalReplacementMap['Tprime_600']['catWV'] = "THQLeptonicTag"
#globalReplacementMap['Tprime_600']['procRVMap'] = od()
#globalReplacementMap["Tprime_600"]["procRVMap"]["THQLeptonicTag"] = "THQ"
#globalReplacementMap["Tprime_600"]["catRVMap"] = od()
#globalReplacementMap["Tprime_600"]["catRVMap"]["THQLeptonicTag"] = "THQ"
#globalReplacementMap['Tprime_600']['procRVMap'] = od()
#globalReplacementMap["Tprime_600"]["procRVMap"]["THQHadronicTag"] = "THQ"
#globalReplacementMap["Tprime_600"]["catRVMap"] = od()
#globalReplacementMap["Tprime_600"]["catRVMap"]["THQHadronicTag"] = "THQ"
'''
globalReplacementMap['Tprime_600'] = od()
globalReplacementMap['Tprime_600']['procWV'] = "Tprime600"
globalReplacementMap['Tprime_600']['catWV'] = "THQLeptonicTag"
globalReplacementMap['Tprime_600']['procRVMap'] = od()
globalReplacementMap["Tprime_600"]["procRVMap"]["THQLeptonicTag"] = "Tprime600"
globalReplacementMap["Tprime_600"]["procRVMap"]["THQHadronicTag"] = "Tprime600"
globalReplacementMap["Tprime_600"]["catRVMap"] = od()
globalReplacementMap["Tprime_600"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["Tprime_600"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"
'''
globalReplacementMap['Tprime_600'] = od()
globalReplacementMap['Tprime_600']['procWV'] = "THQ"
globalReplacementMap['Tprime_600']['catWV'] = "THQLeptonicTag"
globalReplacementMap['Tprime_600']['procRVMap'] = od()
globalReplacementMap["Tprime_600"]["procRVMap"]["THQLeptonicTag"] = "THQ"
globalReplacementMap["Tprime_600"]["procRVMap"]["THQHadronicTag"] = "THQ"
globalReplacementMap["Tprime_600"]["catRVMap"] = od()
globalReplacementMap["Tprime_600"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["Tprime_600"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap['Tprime_625'] = od()
globalReplacementMap['Tprime_625']['procWV'] = "Tprime625"
globalReplacementMap['Tprime_625']['catWV'] = "THQLeptonicTag"
globalReplacementMap['Tprime_625']['procRVMap'] = od()
globalReplacementMap["Tprime_625"]["procRVMap"]["THQLeptonicTag"] = "Tprime625"
globalReplacementMap["Tprime_625"]["catRVMap"] = od()
globalReplacementMap["Tprime_625"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["Tprime_625"]["procRVMap"]["THQHadronicTag"] = "Tprime625"
globalReplacementMap["Tprime_625"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap['Tprime_650'] = od()
globalReplacementMap['Tprime_650']['procWV'] = "Tprime650"
globalReplacementMap['Tprime_650']['catWV'] = "THQLeptonicTag"
globalReplacementMap['Tprime_650']['procRVMap'] = od()
globalReplacementMap["Tprime_650"]["procRVMap"]["THQLeptonicTag"] = "Tprime650"
globalReplacementMap["Tprime_650"]["catRVMap"] = od()
globalReplacementMap["Tprime_650"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["Tprime_650"]["procRVMap"]["THQHadronicTag"] = "Tprime650"
globalReplacementMap["Tprime_650"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap['Tprime_675'] = od()
globalReplacementMap['Tprime_675']['procWV'] = "Tprime675"
globalReplacementMap['Tprime_675']['catWV'] = "THQLeptonicTag"
globalReplacementMap['Tprime_675']['procRVMap'] = od()
globalReplacementMap["Tprime_675"]["procRVMap"]["THQLeptonicTag"] = "Tprime675"
globalReplacementMap["Tprime_675"]["catRVMap"] = od()
globalReplacementMap["Tprime_675"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["Tprime_675"]["procRVMap"]["THQHadronicTag"] = "Tprime675"
globalReplacementMap["Tprime_675"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap['Tprime_700'] = od()
globalReplacementMap['Tprime_700']['procWV'] = "Tprime700"
globalReplacementMap['Tprime_700']['catWV'] = "THQLeptonicTag"
globalReplacementMap['Tprime_700']['procRVMap'] = od()
globalReplacementMap["Tprime_700"]["procRVMap"]["THQLeptonicTag"] = "Tprime700"
globalReplacementMap["Tprime_700"]["catRVMap"] = od()
globalReplacementMap["Tprime_700"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["Tprime_700"]["procRVMap"]["THQHadronicTag"] = "Tprime700"
globalReplacementMap["Tprime_700"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap['Tprime_800'] = od()
globalReplacementMap['Tprime_800']['procWV'] = "Tprime800"
globalReplacementMap['Tprime_800']['catWV'] = "THQLeptonicTag"
globalReplacementMap['Tprime_800']['procRVMap'] = od()
globalReplacementMap["Tprime_800"]["procRVMap"]["THQLeptonicTag"] = "Tprime800"
globalReplacementMap["Tprime_800"]["catRVMap"] = od()
globalReplacementMap["Tprime_800"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["Tprime_800"]["procRVMap"]["THQHadronicTag"] = "Tprime800"
globalReplacementMap["Tprime_800"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap['Tprime_900'] = od()
globalReplacementMap['Tprime_900']['procWV'] = "Tprime900"
globalReplacementMap['Tprime_900']['catWV'] = "THQLeptonicTag"
globalReplacementMap['Tprime_900']['procRVMap'] = od()
globalReplacementMap["Tprime_900"]["procRVMap"]["THQLeptonicTag"] = "Tprime900"
globalReplacementMap["Tprime_900"]["catRVMap"] = od()
globalReplacementMap["Tprime_900"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["Tprime_900"]["procRVMap"]["THQHadronicTag"] = "Tprime900"
globalReplacementMap["Tprime_900"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap['Tprime_1000'] = od()
globalReplacementMap['Tprime_1000']['procWV'] = "Tprime1000"
globalReplacementMap['Tprime_1000']['catWV'] = "THQLeptonicTag"
globalReplacementMap['Tprime_1000']['procRVMap'] = od()
globalReplacementMap["Tprime_1000"]["procRVMap"]["THQLeptonicTag"] = "Tprime1000"
globalReplacementMap["Tprime_1000"]["catRVMap"] = od()
globalReplacementMap["Tprime_1000"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["Tprime_1000"]["procRVMap"]["THQHadronicTag"] = "Tprime1000"
globalReplacementMap["Tprime_1000"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap['Tprime_1100'] = od()
globalReplacementMap['Tprime_1100']['procWV'] = "Tprime1100"
globalReplacementMap['Tprime_1100']['catWV'] = "THQLeptonicTag"
globalReplacementMap['Tprime_1100']['procRVMap'] = od()
globalReplacementMap["Tprime_1100"]["procRVMap"]["THQLeptonicTag"] = "Tprime1100"
globalReplacementMap["Tprime_1100"]["catRVMap"] = od()
globalReplacementMap["Tprime_1100"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["Tprime_1100"]["procRVMap"]["THQHadronicTag"] = "Tprime1100"
globalReplacementMap["Tprime_1100"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"

globalReplacementMap['Tprime_1200'] = od()
globalReplacementMap['Tprime_1200']['procWV'] = "Tprime1200"
globalReplacementMap['Tprime_1200']['catWV'] = "THQLeptonicTag"
globalReplacementMap['Tprime_1200']['procRVMap'] = od()
globalReplacementMap["Tprime_1200"]["procRVMap"]["THQLeptonicTag"] = "Tprime1200"
globalReplacementMap["Tprime_1200"]["catRVMap"] = od()
globalReplacementMap["Tprime_1200"]["catRVMap"]["THQLeptonicTag"] = "THQLeptonicTag"
globalReplacementMap["Tprime_1200"]["procRVMap"]["THQHadronicTag"] = "Tprime1200"
globalReplacementMap["Tprime_1200"]["catRVMap"]["THQHadronicTag"] = "THQHadronicTag"
# STXS analysis
globalReplacementMap['STXS'] = od()
# For WRONG VERTEX SCENARIO:
#  * single proc x cat for wrong vertex since for dZ > 1cm shape independent of proc x cat
#  * use proc x cat with highest number of WV events
globalReplacementMap['STXS']['procWV'] = "GG2H_0J_PTH_GT10"
globalReplacementMap['STXS']['catWV'] = "RECO_0J_PTH_GT10_Tag1"
# For RIGHT VERTEX SCENARIO:
#  * default mapping is to use diagonal process from given category 
#  * if few events in diagonal process then may need to change the category aswell (see catRVMap)
#  * map must contain entry for all cats being processed (for replacement proc and cat)
globalReplacementMap['STXS']['procRVMap'] = od()
globalReplacementMap["STXS"]["procRVMap"]["RECO_0J_PTH_0_10_Tag0"] = "GG2H_0J_PTH_0_10"
globalReplacementMap["STXS"]["procRVMap"]["RECO_0J_PTH_0_10_Tag1"] = "GG2H_0J_PTH_0_10"
globalReplacementMap["STXS"]["procRVMap"]["RECO_0J_PTH_0_10_Tag2"] = "GG2H_0J_PTH_0_10"
globalReplacementMap["STXS"]["procRVMap"]["RECO_0J_PTH_GT10_Tag0"] = "GG2H_0J_PTH_GT10"
globalReplacementMap["STXS"]["procRVMap"]["RECO_0J_PTH_GT10_Tag1"] = "GG2H_0J_PTH_GT10"
globalReplacementMap["STXS"]["procRVMap"]["RECO_0J_PTH_GT10_Tag2"] = "GG2H_0J_PTH_GT10"
globalReplacementMap["STXS"]["procRVMap"]["RECO_1J_PTH_0_60_Tag0"] = "GG2H_1J_PTH_0_60"
globalReplacementMap["STXS"]["procRVMap"]["RECO_1J_PTH_0_60_Tag1"] = "GG2H_1J_PTH_0_60"
globalReplacementMap["STXS"]["procRVMap"]["RECO_1J_PTH_0_60_Tag2"] = "GG2H_1J_PTH_0_60"
globalReplacementMap["STXS"]["procRVMap"]["RECO_1J_PTH_120_200_Tag0"] = "GG2H_1J_PTH_120_200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_1J_PTH_120_200_Tag1"] = "GG2H_1J_PTH_120_200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_1J_PTH_120_200_Tag2"] = "GG2H_1J_PTH_120_200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_1J_PTH_60_120_Tag0"] = "GG2H_1J_PTH_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_1J_PTH_60_120_Tag1"] = "GG2H_1J_PTH_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_1J_PTH_60_120_Tag2"] = "GG2H_1J_PTH_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_GE2J_PTH_0_60_Tag0"] = "GG2H_GE2J_MJJ_0_350_PTH_0_60"
globalReplacementMap["STXS"]["procRVMap"]["RECO_GE2J_PTH_0_60_Tag1"] = "GG2H_GE2J_MJJ_0_350_PTH_0_60"
globalReplacementMap["STXS"]["procRVMap"]["RECO_GE2J_PTH_0_60_Tag2"] = "GG2H_GE2J_MJJ_0_350_PTH_0_60"
globalReplacementMap["STXS"]["procRVMap"]["RECO_GE2J_PTH_120_200_Tag0"] = "GG2H_GE2J_MJJ_0_350_PTH_120_200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_GE2J_PTH_120_200_Tag1"] = "GG2H_GE2J_MJJ_0_350_PTH_120_200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_GE2J_PTH_120_200_Tag2"] = "GG2H_GE2J_MJJ_0_350_PTH_120_200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_GE2J_PTH_60_120_Tag0"] = "GG2H_GE2J_MJJ_0_350_PTH_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_GE2J_PTH_60_120_Tag1"] = "GG2H_GE2J_MJJ_0_350_PTH_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_GE2J_PTH_60_120_Tag2"] = "GG2H_GE2J_MJJ_0_350_PTH_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_PTH_200_300_Tag0"] = "GG2H_PTH_200_300"
globalReplacementMap["STXS"]["procRVMap"]["RECO_PTH_200_300_Tag1"] = "GG2H_PTH_200_300"
globalReplacementMap["STXS"]["procRVMap"]["RECO_PTH_300_450_Tag0"] = "GG2H_PTH_300_450"
globalReplacementMap["STXS"]["procRVMap"]["RECO_PTH_300_450_Tag1"] = "GG2H_PTH_300_450"
globalReplacementMap["STXS"]["procRVMap"]["RECO_PTH_450_650_Tag0"] = "GG2H_PTH_450_650"
globalReplacementMap["STXS"]["procRVMap"]["RECO_PTH_GT650_Tag0"] = "GG2H_PTH_GT650"
globalReplacementMap["STXS"]["procRVMap"]["RECO_THQ_LEP"] = "THQ"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_0_60_Tag0"] = "TTH_PTH_0_60"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_0_60_Tag1"] = "TTH_PTH_0_60"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_0_60_Tag2"] = "TTH_PTH_0_60"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_0_60_Tag3"] = "TTH_PTH_0_60"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_120_200_Tag0"] = "TTH_PTH_120_200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_120_200_Tag1"] = "TTH_PTH_120_200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_120_200_Tag2"] = "TTH_PTH_120_200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_120_200_Tag3"] = "TTH_PTH_120_200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_60_120_Tag0"] = "TTH_PTH_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_60_120_Tag1"] = "TTH_PTH_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_60_120_Tag2"] = "TTH_PTH_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_60_120_Tag3"] = "TTH_PTH_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_GT200_Tag0"] = "TTH_PTH_200_300"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_GT200_Tag1"] = "TTH_PTH_200_300"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_GT200_Tag2"] = "TTH_PTH_200_300"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_GT200_Tag3"] = "TTH_PTH_200_300"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_0_60_Tag0"] = "TTH_PTH_0_60"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_0_60_Tag1"] = "TTH_PTH_0_60"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_0_60_Tag2"] = "TTH_PTH_0_60"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_0_60_Tag3"] = "TTH_PTH_0_60"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_120_200_Tag0"] = "TTH_PTH_120_200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_120_200_Tag1"] = "TTH_PTH_120_200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_60_120_Tag0"] = "TTH_PTH_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_60_120_Tag1"] = "TTH_PTH_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_GT200_Tag0"] = "TTH_PTH_200_300"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_GT200_Tag1"] = "TTH_PTH_200_300"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFLIKEGGH_Tag0"] = "GG2H_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFLIKEGGH_Tag1"] = "GG2H_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_BSM_Tag0"] = "VBF_GE2J_MJJ_GT350_PTH_GT200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_BSM_Tag1"] = "VBF_GE2J_MJJ_GT350_PTH_GT200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_JET3VETO_HIGHMJJ_Tag0"] = "VBF_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_JET3VETO_HIGHMJJ_Tag1"] = "VBF_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_JET3VETO_LOWMJJ_Tag0"] = "VBF_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_JET3VETO_LOWMJJ_Tag1"] = "VBF_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_JET3_HIGHMJJ_Tag0"] = "VBF_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_JET3_HIGHMJJ_Tag1"] = "VBF_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_JET3_LOWMJJ_Tag0"] = "VBF_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_JET3_LOWMJJ_Tag1"] = "VBF_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_VHHAD_Tag0"] = "WH2HQQ_GE2J_MJJ_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_VHHAD_Tag1"] = "WH2HQQ_GE2J_MJJ_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VH_MET_Tag0"] = "QQ2HLL_PTV_150_250_0J"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VH_MET_Tag1"] = "QQ2HLL_PTV_75_150"
globalReplacementMap["STXS"]["procRVMap"]["RECO_WH_LEP_HIGH_Tag0"] = "QQ2HLNU_PTV_75_150"
globalReplacementMap["STXS"]["procRVMap"]["RECO_WH_LEP_HIGH_Tag1"] = "QQ2HLNU_PTV_75_150"
globalReplacementMap["STXS"]["procRVMap"]["RECO_WH_LEP_HIGH_Tag2"] = "QQ2HLNU_PTV_75_150"
globalReplacementMap["STXS"]["procRVMap"]["RECO_WH_LEP_LOW_Tag0"] = "QQ2HLNU_PTV_0_75"
globalReplacementMap["STXS"]["procRVMap"]["RECO_WH_LEP_LOW_Tag1"] = "QQ2HLNU_PTV_0_75"
globalReplacementMap["STXS"]["procRVMap"]["RECO_WH_LEP_LOW_Tag2"] = "QQ2HLNU_PTV_0_75"
globalReplacementMap["STXS"]["procRVMap"]["RECO_ZH_LEP_Tag0"] = "QQ2HLL_PTV_75_150"
globalReplacementMap["STXS"]["procRVMap"]["RECO_ZH_LEP_Tag1"] = "QQ2HLL_PTV_75_150"
# Replacement category for RV fit
globalReplacementMap["STXS"]["catRVMap"] = od()
globalReplacementMap["STXS"]["catRVMap"]["RECO_0J_PTH_0_10_Tag0"] = "RECO_0J_PTH_0_10_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_0J_PTH_0_10_Tag1"] = "RECO_0J_PTH_0_10_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_0J_PTH_0_10_Tag2"] = "RECO_0J_PTH_0_10_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_0J_PTH_GT10_Tag0"] = "RECO_0J_PTH_GT10_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_0J_PTH_GT10_Tag1"] = "RECO_0J_PTH_GT10_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_0J_PTH_GT10_Tag2"] = "RECO_0J_PTH_GT10_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_1J_PTH_0_60_Tag0"] = "RECO_1J_PTH_0_60_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_1J_PTH_0_60_Tag1"] = "RECO_1J_PTH_0_60_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_1J_PTH_0_60_Tag2"] = "RECO_1J_PTH_0_60_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_1J_PTH_120_200_Tag0"] = "RECO_1J_PTH_120_200_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_1J_PTH_120_200_Tag1"] = "RECO_1J_PTH_120_200_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_1J_PTH_120_200_Tag2"] = "RECO_1J_PTH_120_200_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_1J_PTH_60_120_Tag0"] = "RECO_1J_PTH_60_120_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_1J_PTH_60_120_Tag1"] = "RECO_1J_PTH_60_120_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_1J_PTH_60_120_Tag2"] = "RECO_1J_PTH_60_120_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_GE2J_PTH_0_60_Tag0"] = "RECO_GE2J_PTH_0_60_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_GE2J_PTH_0_60_Tag1"] = "RECO_GE2J_PTH_0_60_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_GE2J_PTH_0_60_Tag2"] = "RECO_GE2J_PTH_0_60_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_GE2J_PTH_120_200_Tag0"] = "RECO_GE2J_PTH_120_200_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_GE2J_PTH_120_200_Tag1"] = "RECO_GE2J_PTH_120_200_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_GE2J_PTH_120_200_Tag2"] = "RECO_GE2J_PTH_120_200_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_GE2J_PTH_60_120_Tag0"] = "RECO_GE2J_PTH_60_120_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_GE2J_PTH_60_120_Tag1"] = "RECO_GE2J_PTH_60_120_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_GE2J_PTH_60_120_Tag2"] = "RECO_GE2J_PTH_60_120_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_PTH_200_300_Tag0"] = "RECO_PTH_200_300_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_PTH_200_300_Tag1"] = "RECO_PTH_200_300_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_PTH_300_450_Tag0"] = "RECO_PTH_300_450_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_PTH_300_450_Tag1"] = "RECO_PTH_300_450_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_PTH_450_650_Tag0"] = "RECO_PTH_450_650_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_PTH_GT650_Tag0"] = "RECO_PTH_GT650_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_THQ_LEP"] = "RECO_THQ_LEP"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_0_60_Tag0"] = "RECO_TTH_HAD_PTH_0_60_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_0_60_Tag1"] = "RECO_TTH_HAD_PTH_0_60_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_0_60_Tag2"] = "RECO_TTH_HAD_PTH_0_60_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_0_60_Tag3"] = "RECO_TTH_HAD_PTH_0_60_Tag3"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_120_200_Tag0"] = "RECO_TTH_HAD_PTH_120_200_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_120_200_Tag1"] = "RECO_TTH_HAD_PTH_120_200_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_120_200_Tag2"] = "RECO_TTH_HAD_PTH_120_200_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_120_200_Tag3"] = "RECO_TTH_HAD_PTH_120_200_Tag3"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_60_120_Tag0"] = "RECO_TTH_HAD_PTH_60_120_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_60_120_Tag1"] = "RECO_TTH_HAD_PTH_60_120_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_60_120_Tag2"] = "RECO_TTH_HAD_PTH_60_120_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_60_120_Tag3"] = "RECO_TTH_HAD_PTH_60_120_Tag3"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_GT200_Tag0"] = "RECO_TTH_HAD_PTH_GT200_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_GT200_Tag1"] = "RECO_TTH_HAD_PTH_GT200_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_GT200_Tag2"] = "RECO_TTH_HAD_PTH_GT200_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_GT200_Tag3"] = "RECO_TTH_HAD_PTH_GT200_Tag3"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_0_60_Tag0"] = "RECO_TTH_LEP_PTH_0_60_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_0_60_Tag1"] = "RECO_TTH_LEP_PTH_0_60_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_0_60_Tag2"] = "RECO_TTH_LEP_PTH_0_60_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_0_60_Tag3"] = "RECO_TTH_LEP_PTH_0_60_Tag3"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_120_200_Tag0"] = "RECO_TTH_LEP_PTH_120_200_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_120_200_Tag1"] = "RECO_TTH_LEP_PTH_120_200_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_60_120_Tag0"] = "RECO_TTH_LEP_PTH_60_120_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_60_120_Tag1"] = "RECO_TTH_LEP_PTH_60_120_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_GT200_Tag0"] = "RECO_TTH_LEP_PTH_GT200_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_GT200_Tag1"] = "RECO_TTH_LEP_PTH_GT200_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFLIKEGGH_Tag0"] = "RECO_VBFLIKEGGH_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFLIKEGGH_Tag1"] = "RECO_VBFLIKEGGH_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_BSM_Tag0"] = "RECO_VBFTOPO_BSM_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_BSM_Tag1"] = "RECO_VBFTOPO_BSM_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_JET3VETO_HIGHMJJ_Tag0"] = "RECO_VBFTOPO_JET3VETO_HIGHMJJ_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_JET3VETO_HIGHMJJ_Tag1"] = "RECO_VBFTOPO_JET3VETO_HIGHMJJ_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_JET3VETO_LOWMJJ_Tag0"] = "RECO_VBFTOPO_JET3VETO_LOWMJJ_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_JET3VETO_LOWMJJ_Tag1"] = "RECO_VBFTOPO_JET3VETO_LOWMJJ_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_JET3_HIGHMJJ_Tag0"] = "RECO_VBFTOPO_JET3_HIGHMJJ_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_JET3_HIGHMJJ_Tag1"] = "RECO_VBFTOPO_JET3_HIGHMJJ_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_JET3_LOWMJJ_Tag0"] = "RECO_VBFTOPO_JET3_LOWMJJ_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_JET3_LOWMJJ_Tag1"] = "RECO_VBFTOPO_JET3_LOWMJJ_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_VHHAD_Tag0"] = "RECO_VBFTOPO_VHHAD_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_VHHAD_Tag1"] = "RECO_VBFTOPO_VHHAD_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VH_MET_Tag0"] = "RECO_VH_MET_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VH_MET_Tag1"] = "RECO_VH_MET_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_WH_LEP_HIGH_Tag0"] = "RECO_WH_LEP_HIGH_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_WH_LEP_HIGH_Tag1"] = "RECO_WH_LEP_HIGH_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_WH_LEP_HIGH_Tag2"] = "RECO_WH_LEP_HIGH_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_WH_LEP_LOW_Tag0"] = "RECO_WH_LEP_LOW_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_WH_LEP_LOW_Tag1"] = "RECO_WH_LEP_LOW_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_WH_LEP_LOW_Tag2"] = "RECO_WH_LEP_LOW_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_ZH_LEP_Tag0"] = "RECO_ZH_LEP_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_ZH_LEP_Tag1"] = "RECO_ZH_LEP_Tag1"

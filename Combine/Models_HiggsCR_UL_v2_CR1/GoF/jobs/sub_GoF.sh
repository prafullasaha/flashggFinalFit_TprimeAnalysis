#!/bin/bash
ulimit -s unlimited
set -e
cd /afs/cern.ch/work/p/prsaha/public/FinalFit_lite/CMSSW_10_2_13/src/flashggFinalFit/Combine/Models_HiggsCR_UL_v2_CR1/GoF
source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`

#Generate command
combine -M GoodnessOfFit -d /afs/cern.ch/work/p/prsaha/public/FinalFit_lite/CMSSW_10_2_13/src/flashggFinalFit/Combine/Models_HiggsCR_UL_v2_CR1/Datacard_HiggsCR_mu_inclusive.root --algo=saturated --saveWorkspace --toysFrequentist --bypassFrequentistFit -t 500 --expectSignal 1 -m 125 --freezeParameter MH -n _GoFtest_For500toys

combine -M GoodnessOfFit --algo=saturated -d /afs/cern.ch/work/p/prsaha/public/FinalFit_lite/CMSSW_10_2_13/src/flashggFinalFit/Combine/Models_HiggsCR_UL_v2_CR1/Datacard_HiggsCR_mu_inclusive.root -m 125 --freezeParameter MH -n _GoFtest_ForData

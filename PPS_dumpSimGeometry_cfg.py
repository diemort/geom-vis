from __future__ import print_function
import FWCore.ParameterSet.Config as cms
import sys, os
import FWCore.ParameterSet.VarParsing as VarParsing
from FWCore.Utilities.Enumerate import Enumerate
from Configuration.Geometry.dict2026Geometry import detectorVersionDict

varType = Enumerate ("Run1 2015 2015dev 2017 2017Muon 2021 2026 PPS-Timing PPS-Diamond PPS-Sunanda")
defaultVersion=str();

def help():
   print("Usage: cmsRun dumpSimGeometry_cfg.py  tag=TAG version=VERSION ")
   print("   tag=tagname")
   print("       identify geometry scenario ")
   print("      ", varType.keys())
   print("")
   print("   version=versionNumber")
   print("       scenario version from 2026 dictionary")
   print("")
   print("   out=outputFileName")
   print("       default is cmsSimGeom<tag><version>.root")
   print() 
   os._exit(1);

def versionCheck(ver):
   if ver == "":
      print("Please, specify 2026 scenario version\n")
      print(sorted([x[1] for x in detectorVersionDict.items()]))
      print("")
      help()

def simGeoLoad(score):
    print("Loading configuration for scenario", options.tag , options.version ,"...\n")
    if score == "2021-simu": # Full CMS geometry with PPS
       process.load("Geometry.CMSCommonData.cmsExtendedGeometry2021XML_cfi")

    elif score == "PPSrun2": # only PPS geometry of both arms for Run2
       process.load("Geometry.VeryForwardGeometry.PPS_geometryRPFromDD_2018_cfi")

    elif score == "PPSrun3": # only PPS geometry of both arms for Run3
       process.load("Geometry.VeryForwardGeometry.PPS_geometryRPFromDD_2021_cfi")

    elif score == "PPSrun3_LeftArm": # only PPS geometry Left Arm for Run3
       process.load("Geometry.VeryForwardGeometry.PPS_geometryRPFromDD_2021_LeftArm_cfi")

    elif score == "PPSrun3_Pixels": # Pixel sensors
       process.load("Geometry.VeryForwardGeometry.PPS_geometryRPFromDD_2021_Pixels_cfi")

    elif score == "PPS-Timing": # only PPS timing detector in cylindrical pot
       process.load("Geometry.VeryForwardGeometry.PPS_geometryRPFromDD_2021_Timing_cfi")

    else:
       help()

options = VarParsing.VarParsing ()

defaultTag=str(2017);
defaultLevel=100;
defaultOutputFileName="cmsSimGeom-"+ defaultTag +".root"

options.register ('tag',
                  defaultTag, # default value
                  VarParsing.VarParsing.multiplicity.singleton,
                  VarParsing.VarParsing.varType.string,
                  "info about geometry scenario")
options.register ('version',
                  defaultVersion, # default value
                  VarParsing.VarParsing.multiplicity.singleton,
                  VarParsing.VarParsing.varType.string,
                  "info about 2026 geometry scenario version")
options.register ('out',
                  defaultOutputFileName, # default value
                  VarParsing.VarParsing.multiplicity.singleton,
                  VarParsing.VarParsing.varType.string,
                  "Output file name")

options.parseArguments()

if (options.out == defaultOutputFileName ):
   options.out = "cmsSimGeom-" + str(options.tag) + str(options.version) + ".root"

process = cms.Process("SIMDUMP")
simGeoLoad(options.tag)

process.source = cms.Source("EmptySource")

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1))

process.add_(cms.ESProducer("TGeoMgrFromDdd",
                            verbose = cms.untracked.bool(True),
                            level = cms.untracked.int32(defaultLevel)
                           )              
            )

process.dump = cms.EDAnalyzer("DumpSimGeometry", 
                              tag = cms.untracked.string(options.tag),
                              outputFileName = cms.untracked.string(options.out)
                             )

process.p = cms.Path(process.dump)

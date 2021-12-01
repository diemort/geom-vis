#!/bin/bash

# add needed packages:
git cms-addpkg Geometry/VeryForwardData
git cms-addpkg Geometry/VeryForwardGeometry

# copy customised files to the geometry data:
cp data/cmsextend.xml ../Geometry/VeryForwardData/data
cp data/RP_Box_123_OCMS.xml ../Geometry/VeryForwardData/data/RP_Box/v3/
cp data/RP_Stations_Assembly_OCMS.xml ../Geometry/VeryForwardData/data/CTPPS_2021/Stations/Reco/v1/
cp data/CTPPS_Timing_Stations_Assembly_OCMS.xml ../Geometry/VeryForwardData/data/CTPPS_Diamond_2021/Reco/v1/
cp data/CTPPS_Timing_Negative_Station_OCMS.xml ../Geometry/VeryForwardData/data/CTPPS_Timing_Negative_Station/v1/

# copy customised descriptors to the package:
cp descriptors/* ../Geometry/VeryForwardGeometry/python

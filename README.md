# geom-vis
Visualisation for the PPS geometry

THe dumped geometry shows the geometry meant for reconstruction. Some cases are showing the geometry for simulation, and will carry a label "simu".

To dump the geometry, run the following command in a CMSSW area:

`cmsRun PPS_dumpSimGeometry_cfg.py tag=<your tag>`

The tags available are related to some components of the PPS geometry:

`2021-simu`
`PPSrun2`
`PPSrun3`
`PPSrun3_LeftArm`
`PPSrun3_FixPixels`
`PPS-Timing_Cylindrical`
`PPS-Timing_Box-simu`

To visualise the geometry dumped with cmsShow, run the following script:

`./show-geom.sh <file> <tag>`

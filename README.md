# geom-vis
Visualisation for the PPS geometry

THe dumped geometry shows the geometry meant for reconstruction. Some cases are showing the geometry for simulation, and will carry a label "simu".

To dump the geometry, run the following command in a CMSSW area:

`cmsRun PPS_dumpSimGeometry_cfg.py tag=<your tag>`

The tags available are related to some components of the PPS geometry:

:white_check_mark: `2021-simu`

:white_check_mark: `PPSrun2`

:white_check_mark: `PPSrun3`

:x: `PPSrun3_LeftArm`

:x: `PPSrun3_FixPixels`

:x: `PPS-Timing_Cylindrical`

:x: `PPS-Timing_Box-simu`

To visualise the geometry dumped with cmsShow, run the following script:

`./show-geom.sh <file> <tag>`

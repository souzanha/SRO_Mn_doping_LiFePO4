#!/bin/bash

for T in {100..1000..100}; do
    (
        cd "$T"
        sed 's/mctrials               2000000/mctrials               2020000/g' res.bak | sed 's/mcsample \*\*\*\*\* gulp.gmc/mcsample 1 gulp.gmc/' > gin.prod
        /home/jolla/bin/gulp_improved_MC_v3 < gin.prod > gout.prod
    )
    
    (
        cd "$T"
        ../GMC2XYZ gulp.gmc > MC.xyz
        grep Step gulp.gmc > steps.dat
    )
done

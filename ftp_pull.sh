#!/bin/bash

file='ftp://ftpe.rrc.texas.gov/dp_pend/dp_drilling_permit_pending_20200803110805.txt'
dest='/root/files/permit_pending.txt'

#download our file
curl $file -o $dest

unset file
unset dest

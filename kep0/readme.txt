

to compile:
make changes to probName_Config.sh as needed
./compileScript.sh probName id

to run:
make edits to probName.params 
generate probName_ics.hdf5 with probName_make_IC.py or copy over from another run or snapshot
generate outputs.txt (list of output times) with "outputListGen.sh maxInteger e-1" 
make edits to submit.sh
submit with "sbatch submit.sh"



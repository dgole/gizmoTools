module load TACC intel impi hdf5 gsl fftw2
cp $1_Config.sh ../gizmo-public/Config.sh
cd ../gizmo-public/
make clean
make
mv ./GIZMO ../$1$2/
cd ../$1$2/

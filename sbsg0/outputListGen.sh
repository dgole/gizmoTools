rm outputList.txt
touch outputList.txt
for i in `seq 0 $1`;
do
	echo ${i}.$2 >> outputList.txt
done

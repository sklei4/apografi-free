cat export.csv | grep Mac
number=$(cat export.csv | grep Mac | wc -l)
#number=$(echo $number + 1 | bc -l)
echo ---
echo Macbooks on campus: $number
echo $number*2200 | bc -l
echo '[Numbers founded by estimating cost of Macbooks to be 2200 per unit.]'

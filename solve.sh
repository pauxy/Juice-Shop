folders=(*)
echo "--- Folders detected ---"
printf "%s\n" "${folders[@]}"
for i in ${folders[@]}
do
    echo "---Files in $i---"
    if [[ -f "$i/solve.py" ]]
    then
        cd $i
        echo "solve.py found"
        echo "solving . . ."
        python3 solve.py 2>/dev/null
        cd ..
    else
        echo "no solve.py found"
    fi
done 

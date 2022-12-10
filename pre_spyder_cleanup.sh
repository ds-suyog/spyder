start=`date +%s`
clean_up_log=./logs/clean_up.log
touch $clean_up_log
echo -e "\n\n==================== Running pre run cleanup.sh Timestamp: " $(date) >> $clean_up_log

# truncate if log file size is beyond threshold
treat_fsize_beyond_threshold(){
    fpath=$1
    fsize=`stat -c "%s" $fpath`
    threshold=1000000 #1GB
    if [ $fsize -gt $threshold ]
    then
        echo 'truncating files beyond 1 GB threshold: ' $1 >> $clean_up_log
        # code to zip gecko log  #log rotate
        truncate -s 0 fpath
    else
        echo 'file under 1 GB threshold: ' $1 >> $clean_up_log
    fi
}

for f in `find ./logs/ -name "*.log" -type f`; do
    treat_fsize_beyond_threshold $f
done

# kill all firefox processes
# sudo killall firefox

end=`date +%s`
runtime=$((end-start))
echo "completed! runtime = " $((runtime)) " seconds" >> $clean_up_log

# set crontab to trigger data acquition (spyder + parser) on schedule

start=`date +%s`
auto_webscrap_log=./logs/auto_webscrap.log
touch $auto_webscrap_log
echo -e "\n==================== Triggering data acquition workflow Timestamp: " $(date) >> $auto_webscrap_log

echo "checking default python version = " `python -V` "." >> $auto_webscrap_log
source /home/sks/workspace/venvs/spyder/bin/activate
echo "activated venv3.10! python version = " `python -V` "." >> $auto_webscrap_log

# sleep 1
# echo "status openvpn: " `sudo service /usr/sbin/openvpn status` >> $auto_webscrap_log
# cd $openvpn_dir
# echo "starting openvpn!" >> $auto_webscrap_log
# sudo /usr/sbin/openvpn --config /config.ovpn &
# echo "waiting for openvpn to be ready..." >> $auto_webscrap_log
# sleep 12
# echo "openvpn ready!" >> $auto_webscrap_log
# cd $main_dir

python trigger.py
deactivate

# #echo "checking openvpn processes: " `ps -ef | grep "open"` >> $auto_webscrap_log
# sudo killall /usr/sbin/openvpn
# #echo "checking openvpn processes after killall: " `ps -ef | grep "open"` >> $auto_webscrap_log
# echo "status openvpn: " `sudo service /usr/sbin/openvpn status` >> $auto_webscrap_log

end=`date +%s`
runtime=$((end-start))
echo "shell script completed! runtime = " $((runtime)) " seconds" >> $auto_webscrap_log


# echo -e "running rclone! Timestamp: " $(date) >> $auto_webscrap_log
# rclone copy ./uploadfiles/ Remote:stocks/daily
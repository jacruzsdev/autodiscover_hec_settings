# Autodiscover HEC settings for Splunk
This script is usage for autodiscover HEC port and protocol to insert events via HEC in splunk local.

the `get_hec_endpoint` function get HTTP event collector port and sslConf from HTTP Event Collector Global Configuration.

This function dont required any parameter

This function was created in <strong>Splunk 7.2.6</strong> with <strong>Splunk Add-On Builder 2.2.0</strong> and running  in el <strong>RHEL 7.6 O.S</strong> 

Put this script in `$SPLUNK_HOME/etc/apps/$app_name$/bin` and call in your main script


# encoding = utf-8
import ConfigParser
import os
import re


def get_hec_endpoint():
    path = os.path.dirname(os.path.realpath(__file__))
    base_path = re.search("^.+?(?=splunk)[^\/]+\/", path)
    config = ConfigParser.ConfigParser()
    hec_conf_file = os.path.join(base_path.group(0), "etc/apps/splunk_httpinput/local/inputs.conf")
    config.readfp(open(hec_conf_file))
    hec_port = config.get('http', 'port')
    is_ssl = int(config.get('http', 'enableSSL'))
    protocol = "http" if is_ssl == 0 else "https"
    dns_server = "127.0.0.1"
    splunk_url = "%s://%s:%s/services/collector/event" % (protocol, dns_server, hec_port)
    return splunk_url

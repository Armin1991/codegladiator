import os
dir_path = os.path.dirname(os.path.realpath(__file__))
log_dir = dir_path.replace('config','logs')

application_host= '0.0.0.0'
consul_services = "http://127.0.0.1:8500/v1/agent/services"

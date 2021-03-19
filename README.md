# W106-config
config w106 power analyzer with flask web interface

# Setup for auta start service
1: cp w106-config.service to /etc/systemd/system
2: systemctl daemon-reload
3: systemctl start w106-config.service
FROM netboxcommunity/netbox:v4.0-2.9.1

COPY ./launch-netbox-dev.sh /opt/netbox/launch-netbox-dev.sh



# add you dev plugin here
COPY ./plugins /opt/netbox/netbox/plugins
RUN /opt/netbox/venv/bin/pip install -e /opt/netbox/netbox/plugins/*



COPY plugins_requirements.txt /opt/netbox/
RUN /opt/netbox/venv/bin/pip install --no-warn-script-location -r /opt/netbox/plugins_requirements.txt

# These lines are only required if your plugin has its own static files.
COPY configuration/configuration.py /etc/netbox/config/configuration.py
COPY configuration/plugins.py /etc/netbox/config/plugins.py
RUN SECRET_KEY="dummydummydummydummydummydummydummydummydummydummy" /opt/netbox/venv/bin/python /opt/netbox/netbox/manage.py collectstatic --no-input


CMD [ "/opt/netbox/docker-entrypoint.sh", "/opt/netbox/launch-netbox-dev.sh" ]


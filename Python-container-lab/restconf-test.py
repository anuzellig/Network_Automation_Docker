import lxml.etree as etree
from ncclient import manager
from jinja2 import Template


CREATE_INTERFACE = """
<config>
    <interface xmlns="urn:ios">
      <Loopback>
        <name>{{ interface }}</name>
        <description>{{ description }}</description>
        <ip>
           <address>
              <primary>
                 <address>{{ ip }}</address>
                 <mask>{{ netmask }}</mask>
              </primary>
           </address>
        </ip>
      </Loopback>
    </interface>
</config>
"""


def pretty_xml(xml: str) -> str:
    xml = etree.fromstring(xml.encode())
    return etree.tostring(xml, pretty_print=True).decode()


def configure_loopback(connection: manager.Manager, interface: str, description: str, ip: str, netmask: str) -> str:
    template = Template(CREATE_INTERFACE)
    config = template.render(
        interface=interface, description=description, ip=ip, netmask=netmask
    )
    return connection.edit_config(target="running", config=config).xml


if __name__ == "__main__":
    # Configure a loopback interface using NETCONF
    with manager.connect(
        # "host.docker.internal" is a special DNS name created by docker that points to the host
        host="host.docker.internal",
        port=12022,
        username="admin",
        password="admin",
        hostkey_verify=False,
        allow_agent=False,
        look_for_keys=False,
        device_params={"name": "default"},
    ) as m:
        response = configure_loopback(
            connection=m,
            interface="1",
            description="New loopback interface",
            ip="192.168.0.1",
            netmask="255.255.255.0",
        )
        print("Response:\n", pretty_xml(response))

        # Collect and display the running config
        config = m.get_config(source="running")
        print("Updated config:\n", pretty_xml(config.xml))

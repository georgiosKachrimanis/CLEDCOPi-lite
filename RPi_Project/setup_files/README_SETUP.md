# Start Here

When you execute the `setup.py`, all the necessary files and parameters will be created to run the RPis in a cluster using one of them as Coordinator. 
The initial installation process needs to be done on every RPi in the cluster.

**Important note:** The **Coordinator** is the Raspberry Pi that acts as an Access Point and processes some of the data collected by the rest of the devices in the cluster during operation.

**Agents** are the devices connected to the Coordinator's WLAN.

## How it works?

Using Raspberry Pi documentation on how to create a [Routed Access Point](https://www.raspberrypi.com/documentation/computers/configuration.html#setting-up-a-routed-wireless-access-point), we've created functions that streamline the setup and creation of the necessary configuration files.

The basic idea is to back up the existing configuration files of the Wi-Fi network 
("/etc/dhcpcd.conf", "/etc/wpa_supplicant/wpa_supplicant.conf", "/etc/dnsmasq.conf") and 
then create new configuration files that the device will use when acting as the Coordinator. 
However, this process is not just about creating a Coordinator; it also involves an automated way to switch between the roles of Coordinator and Agents.



## What are the changes?

- Installs [hostapd](https://wiki.gentoo.org/wiki/Hostapd) and [Flask Server](https://flask.palletsprojects.com/en/2.3.x/) if not already installed.
- Creates new configuration files for [dnsmasq](https://thekelleys.org.uk/dnsmasq/doc.html), [dhcpcd](https://wiki.archlinux.org/title/dhcpcd), and [hostapd](https://wiki.gentoo.org/wiki/Hostapd).
- Creates a new [wpa_supplicant](https://wiki.archlinux.org/title/wpa_supplicant) file with allowed/known WAN networks.
- Adjusts the [rc.local](https://linuxhint.com/use-etc-rc-local-boot/) file to restart some processes after booting.

## Hostapd (create_hostapd())

After the successful installation of hostapd, the function `create_hostapd()` will create a new configuration file ("/etc/hostapd/hostapd.conf"). This file contains the details of the Wi-Fi network created by each Raspberry Pi in the cluster. The WLAN SSID that each RPi creates is identified by the device and user's name. For example, if the device name is pi10, the WLAN SSID created by this device will be named pi10.

If you want to change any of the WLAN's parameters, such as country, Wi-Fi channel, or WPA passphrase, you can adjust the code in the `create_hostapd` function.

## Dnsmasq (create_dnsmasq())

`create_dnsmasq()` is responsible for creating the range of network addresses that the DHCP server will use to configure the WLAN of the current device. The range typically spans from 192.168.xxx.2 to 192.168.xxx.200 (with xxx being the unique number of each RPi in the cluster).

For example, if you use the device name pi10, the range will be 192.168.10.2 to 192.168.10.200. You can adjust the range, the first, second, and fourth octets, but it's recommended not to change the third octet. The subnet of the network is 255.255.255.0 or 192.168.xxx.0/24.

You can also add devices with static IP addresses in this configuration.

## Dhcpcd (create_dhcpcd())

The configuration file of the DHCP server is created in this step by `create_dhcpcd`. The static IP address of the Coordinator 
is determined based on the [Naming Conventions](naming-conventions). 
The first address is 192.168.xxx.1, with xxx being the unique Pi number of the device. 
For example, for pi10, the static IP of the Coordinator is 192.168.10.1.

If you want to change the IP of the network, you should adjust only the first, second, fourth octets, and the subnet mask.

## WPA (adjust_wpa_range())

With this function, we create the `wpa_supplicant` file that contains login and credentials for the possible networks of the cluster. 
You should change the country depending on your location, and make sure it matches the setting in `create_hostapd`. 
Also, update your preferred password (matching the one used in `create_hostapd`).

## Naming Conventions

Don't forget the naming convention when installing the OS. User and device names should follow the format "pi" + a unique device number 
(each device should have a unique number). For example, pi14@pi14. 


## Extra info
You can also use this setup file to configure your Raspberry Pi as an Access Point connected to your ethernet port! You will have a new Access Point for your home-office network.
If this is the case just change the password in `create_hostapd()` and that's all. Still, you need to adhere to the [Naming Conventions](naming-conventios) though.

For more information, please contact the owner of this repository at please contact me at [georgios.kachrimanis@icloud.com](mailto:georgios.kachrimanis@icloud.com), 
or check the documentation on the main Readme.md


## Future additions

- Changing the configuration in order to have a safe and secure password (MD5, SHA etc). 
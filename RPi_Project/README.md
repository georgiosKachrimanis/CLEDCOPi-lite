# Rpi-mDNS-DeviceManager for emergencies.

This project explores the exciting field of the cloud-edge continuum and leverages Raspberry Pi devices to achieve its objectives. 
It was initiated as part of my undergraduate thesis for the [Hellenic Open University (EAP)](https://www.eap.gr/en/) 
during the 2022-2023 academic year, under the guidance of Mr. Dimitriou Nikolaos(MsC).

## About

This project provides an intuitive device management system optimized for Raspberry Pi clusters. 
Utilizing mDNS (Multicast Domain Name System), devices within the network are easily identifiable by user-friendly names like pi2, pi3, pi4, etc.,
rather than by IP addresses. 
Such naming conventions allow for straightforward command syntax, for example: ssh pi2@pi2.local, making IP address knowledge redundant.

A significant feature is the flexibility in device communication regardless of the active Coordinator (or access point). 
With this system, frequent and unpredictable Coordinator changes don't obstruct message communication between devices. 
This approach fosters easy device-to-device interactions within a local network, replacing the need to know IP addresses 
with simple device names.

In essence, Rpi-mDNS-DeviceManager greatly simplifies tasks like sending commands to turn a camera on or off via a web browser, 
irrespective of the device's current IP. 
The project promotes scalable code, evident in its design patterns, and showcases the potential for effortless control of 
our Raspberry Pi device framework.

### Software capabilities.
The primary aim of our software development was to create a robust and adaptive framework tailored for Raspberry Pi devices. 
Recognizing the paramount importance of unbroken communication, especially during emergencies, we designed our system 
to function as a communication platform for first responders. 
In scenarios where critical infrastructure is compromised, it's crucial for rescue and relief teams to maintain coordination. 
Our software ensures that this communication remains unhindered, even in the most challenging conditions.

Additionally, we've integrated functionalities that allow our framework to play a pivotal role in the realm of the 
Internet of Things (IoT). As an IoT Edge device, it possesses the capability to ensure uninterrupted operations even 
when cloud communications face disruptions. By leveraging features like mDNS, which eliminates the need for 
knowledge of IP addresses and allows easy communication within the local network using device names, 
the framework simplifies tasks. For example, commands such as "pi.local:5000/stop_camera" can easily be 
executed without the need for extensive technical knowledge.

Through practical examples, such as effortlessly controlling the camera function with simple commands, 
we highlight the user-friendly nature of our system. This balance of advanced functionality 
and user accessibility makes it an invaluable tool, not only for emergency response scenarios but also for maintaining 
IoT operations when conventional systems might falter.

Our aim is to expand the capabilities of the framework, by using already made tools and libraries 
without losing the simplicity of design and use. 
In essence, we want to make the job of first responders as easy as possible and also to eliminate the need of specialized 
personel who can run and/or update the software. 


## Start here

### Initial Setup
For now (Version 1.0) you must keep the files on the desktop folder of your Raspberry Pi device. 
Before you clone the repo you should be finished with step 1.

 In case you just want to create an AP(Wlan network) for your home/Office network, then you should run steps 1, 2, 3 and on step 4 choose Coordinator. 
 After you connect the ethernet cable from your router to the Raspberry PI, you will have a new Wlan with the name you used during the setup.

1. Each device that takes part in the cluster must have a clean installation of the latest [Raspberry Pi OS](https://www.raspberrypi.com/software/) 
and should follow the [naming conventions](naming-conventios) when creating the user and device name. *Please keep in mind not to name 2 devices with the same name.* 
2. You have to run the file `setup.py` with elevated status (root privileges). The file is located inside the setup_files folder. 
You can get some more information about the setup.py from the dedicated readme_setup.md file that's also inside the folder.
3. After the installation is complete, the system will restart. 
4. By running the file `change_mode.py` you can choose if you want to change mode of the device (the default mode will be Agent). 

There is no more need for extra installation. Now the device is ready to be used in the cluster of Raspberry Pis. 
You can follow the rest of the guide.

## Running the application Software

WIP (Code needs to be cleaned)


# Naming Conventions
- Each device within our Raspberry Pi network is uniquely named following the format pixxx, where xxx is a number ranging from 2 to 254. 
- This naming convention aligns with the 
third octet of the IP addressing scheme we utilize to create individual WLAN networks for each device. 
Examples include pi12, pi46, and pi254.

- The primary user with administrative privileges on each device will have the same name as the device itself. 
For instance, the device pi34 is managed and controlled by the user named pi34.

This consistent naming strategy is more than just a naming convention. 
As evident in our codebase, it provides a seamless way to communicate with each device in the cluster, 
eliminating the need for a dedicated DNS database, thanks to the capabilities of mDNS.

One simple example is the device we named pi34. If it is Coordinator(more about it on a special chapter that needs to be created) of the Cluster, 
will create a Wlan with IP 192.168.34.0 and the range of available IPs will be 192.168.34.2 - 192.168.34.33 
and 192.168.34.35-192.168.34.254(We do not use the ip 192.168.34.34 to avoid confusions)

## Project Continuation 

Following the successful defense of my thesis, which received a top grade of "Arista" (10), the project's 
development continues as part of my part-time internship in collaboration with 
Mr. Dimitriou(MsC) at the [National Center for Scientific Research "Demokritos"](https://www.demokritos.gr/). 
More specifically, the project is being pursued within the [Institute of Telecommunications](https://www.iit.demokritos.gr/about-the-institute/).
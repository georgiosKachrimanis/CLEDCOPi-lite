import subprocess, os
from pathlib import Path


def revert_to_coordinator():
    """
        Reverts the system to Coordinator.

        This function performs the following operations:
        1. Enables the hostapd service.
        2. Back up the original dhcpcd.conf, hostapd.conf, and dnsmasq.conf files.
        3. Updates the dhcpcd.conf, hostapd.conf, and dnsmasq.conf files with new configurations if available.
        4. Start the hostapd service.
        5. Enables IPv4 forwarding.
        6. Configure the firewall for NAT and saves the rules.
        7. Restart the hostapd, dnsmasq, and dhcpcd services.
        8. Print the status of the operations to the console.

        Note: The function assumes that the new configuration files are named with a '.setup' extension
        and the original files are backed up with a '.orig' extension.

        Requires:
        - sudo privileges for executing system commands.
        - The existence of the '.setup' files for configuration.

        Returns:
            None
        """
    # Enable hostapd service
    subprocess.run(['sudo', 'systemctl', 'unmask', 'hostapd'], check=True)
    subprocess.run(['sudo', 'systemctl', 'enable', 'hostapd'], check=True)

    # Backup the original dhcpcd.conf file and configure the static IP
    if Path('/etc/dhcpcd.conf').exists():
        subprocess.run(['sudo', 'cp', '/etc/dhcpcd.conf', '/etc/dhcpcd.conf.orig'])
        print('dhcpcd.conf has been backed up successfully.')

    if Path('/etc/dhcpcd.conf.setup').exists():
        subprocess.run(['sudo', 'cp', '/etc/dhcpcd.conf.setup', '/etc/dhcpcd.conf'])
        print('dhcpcd.conf has been updated with the new file successfully.')

    # Backup the original hostapd.conf file and configure the access point
    if Path('/etc/hostapd/hostapd.conf').exists():
        subprocess.run(['sudo', 'cp', '/etc/hostapd/hostapd.conf', '/etc/hostapd/hostapd.conf.orig'])
        print('hostapd.conf has been backed up successfully.')

    if Path('/etc/hostapd/hostapd.conf.setup').exists():
        subprocess.run(['sudo', 'cp', '/etc/hostapd/hostapd.conf.setup', '/etc/hostapd/hostapd.conf'])
        print('hostapd.conf has been updated with the new file successfully.')

    # Start hostapd service
    subprocess.run(['sudo', 'systemctl', 'start', 'hostapd'], check=True)

    # Backup the original dnsmasq.conf file and configure the DHCP and DNS settings
    if Path('/etc/dnsmasq.conf').exists():
        subprocess.run(['sudo', 'cp', '/etc/dnsmasq.conf', '/etc/dnsmasq.conf.orig'])
        print('dnsmasq.conf has been backed up successfully.')

    if Path('/etc/dnsmasq.conf.setup').exists():
        subprocess.run(['sudo', 'cp', '/etc/dnsmasq.conf.setup', '/etc/dnsmasq.conf'])
        print('dnsmasq.conf has been updated with the new file successfully.')

    # Enable IPv4 forwarding
    if not Path('/etc/sysctl.d/routed-ap.conf').exists():
        subprocess.run(['sudo', 'sh', '-c', 'echo "# Enable IPv4 routing" > /etc/sysctl.d/routed-ap.conf'])
        subprocess.run(['sudo', 'sh', '-c', 'echo "net.ipv4.ip_forward=1" >> /etc/sysctl.d/routed-ap.conf'])

    subprocess.run(['sudo', 'sysctl', '-p', '/etc/sysctl.d/routed-ap.conf'])

    # Configure the firewall
    subprocess.run(['sudo', 'iptables', '-t', 'nat', '-A', 'POSTROUTING', '-o', 'eth0', '-j', 'MASQUERADE'])
    # Save the firewall rules to the netfilter-persistent configuration file
    subprocess.run(['sudo', 'netfilter-persistent', 'save'])

    # Restart the hostapd, dnsmasq and dhcpcd services

    subprocess.run(['sudo', 'systemctl', 'restart', 'dnsmasq'])
    subprocess.run(['sudo', 'systemctl', 'restart', 'dhcpcd'])
    subprocess.run(['sudo', 'systemctl', 'restart', 'hostapd'])
    print("AP setup complete.")
    print('dhcpcd, hostapd and dnsmasq have been restarted!')


def revert_to_agent():
    """
        Reverts the system to Agent mode from Coordinator mode.

        This function performs the following operations:
        1. Stops and disables the hostapd and dnsmasq services.
        2. Restore the original dhcpcd.conf, hostapd.conf, and dnsmasq.conf files from their '.orig' backups.
        3. Restarts the dhcpcd service.
        4. Print the status of the operations to the console.

        Note: The function assumes that the original configuration files are backed up with a '.orig' extension.

        Requires:
        - sudo privileges for executing system commands.
        - The existence of the '.orig' backup files for restoration.

        Returns:
            None
        """

    # Stop and disable hostapd and dnsmasq services
    os.system("sudo systemctl stop hostapd")
    os.system("sudo systemctl disable hostapd")
    os.system("sudo systemctl stop dnsmasq")
    os.system("sudo systemctl disable dnsmasq")

    # Restore original dhcpcd.conf file
    os.system("sudo cp /etc/dhcpcd.conf.orig /etc/dhcpcd.conf")
    print("Original dhcpcd.conf has been restored.")

    # Restore original hostapd.conf file
    os.system("sudo cp /etc/hostapd/hostapd.conf.orig /etc/hostapd/hostapd.conf")
    print("Original hostapd.conf has been restored.")

    # Restore original dnsmasq.conf file
    os.system("sudo cp /etc/dnsmasq.conf.orig /etc/dnsmasq.conf")
    print("Original dnsmasq.conf has been restored.")

    # Restart the dhcpcd service
    os.system("sudo systemctl restart dhcpcd")
    print("dhcpcd service has been restarted.")
    # Restore original hostapd.conf file


# I am not sure If I need this function anymore!
def revert_to_coordinator_process(hostname):
    """
    Separate process for reverting the device to Coordinator mode.
    """
    try:
        revert_to_coordinator()
        print(f'{hostname} successfully reverted to AP mode.')
    except Exception as e:
        print(f'Error during revert to AP mode: {str(e)}')

def main():
    # Get user input
    user_input = input("Enter 'coordinator' or 'agent' to choose a function: ")

    if user_input.lower() == 'coordinator':
        revert_to_coordinator()
    elif user_input.lower() == 'agent':
        revert_to_agent()
    else:
        print("Invalid input. Please enter 'coordinator' or 'agent'.")


if __name__ == "__main__":
    main()
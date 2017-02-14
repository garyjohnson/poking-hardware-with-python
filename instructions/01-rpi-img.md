`sudo diskutil list`
`sudo diskutil unmountDisk /dev/<disk>`
`sudo dd if=<img> of=/dev/r<disk> bs=1m`

#Enable SSH
create `/Volumes/boot/ssh` as an empty file and save

#Enable OTG modes
open `/Volumes/boot/config.txt` add line `dtoverlay=dwc2` to end
open `/Volumes/boot/cmdline.txt` add `modules-load=dwc2,g_ether` directly after `rootwait` (separated by spaces)
 - will look like this: `dwc_otg.lpm_enable=0 console=serial0,115200 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait modules-load=dwc2,g_ether quiet init=/usr/lib/raspi-config/init_resize.sh`

`sudo diskutil unmountDisk /dev/<disk>`

# Next
insert sd, plug in pi with micro usb cable (to USB, not power)

# Enable network sharing on macos
Open `Sharing` preferences pane
Under `Internet Sharing`, share connection from Wifi, to computers using `RNDIS/Ethernet Gadget`
Check `Internet Sharing`, click `Start`

# Find Pi IP address
Install arp-scan if needed (homebrew: `brew install arp-scan`)
`ifconfig` to find your bridge interface -- usually bridge1, bridge100
`sudo arp-scan --localnet --interface=bridge100`

# ssh into pi
`ssh pi@<ip>`

# sudo raspi-config
- expand filesystem
- change password
- change hostname
- reboot

# ssh into pi
`ssh pi@<hostname>.local`

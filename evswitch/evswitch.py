#!/usr/bin/env python3
import argparse
import subprocess as sbp
import shutil
import os
import sys

evman_dir = "/opt/evman/"

parseargs = argparse.ArgumentParser(
    description="Tool to chroot into a rootfs set up by evinstall",
    usage="evswitch [chroot]",
    epilog="Made with <3, never vibecoded.")
parseargs.add_argument(
    "chroot",
    nargs="?",
    help="Installed chroot name")

args = parseargs.parse_args()

if args.chroot is None:
    parseargs.print_help()
    sys.exit(0)

if not os.path.isdir(evman_dir + args.chroot):
    print(f"ERROR: Fatal: chroot '{args.chroot}' does not exist in '{evman_dir}'!",file=sys.stderr)
    sys.exit(1)
#Work In Progress
if os.path.isdir(evman_dir + args.chroot):
    chroot_dir = evman_dir + args.chroot + "/"
    chroot_dev = chroot_dir + "dev"
    chroot_proc = chroot_dir + "proc"
    chroot_sysfs = chroot_dir + "sys"
    print(f"Chrooting to {chroot_dir}")

    try:
        sbp.run(f"mount --bind /dev {chroot_dev}",shell=True)
        sbp.run(f"mount --bind /dev/pts {chroot_dev}/pts",shell=True)
        sbp.run(f"mount --bind /proc {chroot_proc}",shell=True)
        sbp.run(f"mount --bind /sys {chroot_sysfs}",shell=True)
        sbp.run(["chroot", chroot_dir, "/bin/bash"])
    finally:
        sbp.run(f"umount -l {chroot_sysfs}",shell=True)
        sbp.run(f"umount -l {chroot_proc}",shell=True)
        sbp.run(f"umount -l {chroot_dev}/pts",shell=True)
        sbp.run(f"umount -l {chroot_dev}",shell=True)




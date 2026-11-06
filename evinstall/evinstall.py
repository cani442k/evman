#!/usr/bin/env python3
import argparse
import sys
import os
evman_dir = "/opt/evman"

if sys.platform != "linux":
    print("ERROR: Fatal: evinstall is a Linux utility. Please run it on Linux.")
    sys.exit(1)
if os.geteuid() != 0:
    print("ERROR: Fatal: evinstall needs root privileges to run. Please run with sudo/doas.", file=sys.stderr)
    sys.exit(1)
subprocess.run("mkdir -p /opt/evswitch/chroots", shell=True)

parseargs = argparse.ArgumentParser(
    description="Experimental tool to automatically configure chroots",
    usage="evinstall [rootfs tarball] [chroot]",
    epilog="Made with <3, never vibecoded.")
parseargs.add_argument(
    "chroot",
    nargs="?",
    help="Chroot name to install to")
parseargs.add_argument(
    "rootfs_tar",
    nargs="?",
    help="Location of rootfs tarball to install"
)

args = parseargs.parse_args()


if args.chroot and args.rootfs_tar is None:
    parseargs.print_help()
    sys.exit(0)
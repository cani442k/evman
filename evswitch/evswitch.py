#!/usr/bin/env python3
import argparse
import subprocess
import shutil
import os
import sys

parseargs = argparse.ArgumentParser(
    description="Experimental tool to automatically configure chroots",
    usage="evswitch [chroot]",
    nargs=2,
    epilog="Made with <3\nNever vibecoded.")
parseargs.add_argument(
    "chroot",
    nargs="?",
    help="Installed chroot name")

args = parseargs.parse_args()

if os.geteuid() != 0:
    print("ERROR: Fatal: evswitch needs root privileges to run. Please run with sudo/doas.", file=sys.stderr)
    sys.exit(1)
subprocess.run("mkdir -p /opt/evswitch/chroots", shell=True)
#WIP
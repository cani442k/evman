#!/usr/bin/env python3
import argparse
import subprocess
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
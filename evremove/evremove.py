#!/usr/bin/env python3
import argparse
import sys
import os
evman_dir = "/opt/evman"
if sys.platform != "linux":
    print("ERROR: Fatal: evremove is a Linux utility. Please run it on Linux.")
    sys.exit(1)
if os.geteuid() != 0:
    print("ERROR: Fatal: evremove needs root privileges to run. Please run with sudo/doas.", file=sys.stderr)
    sys.exit(1)
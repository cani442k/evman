#!/usr/bin/env python3
if sys.platform != "linux":
    print("ERROR: Fatal: evswitch is a Linux utility. Please run it on Linux.")
    sys.exit(1)
if os.geteuid() != 0:
    print("ERROR: Fatal: evswitch needs root privileges to run. Please run with sudo/doas.", file=sys.stderr)
    sys.exit(1)
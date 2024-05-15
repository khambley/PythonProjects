#!/usr/bin/python3
# MapIt.py
# by Katherine Hambley
# Automatically launch the Google map in your browser using the copied address from your clipboard

import webbrowser, sys
if len(sys.argv) > 1:
    # Get address from command line
    address = ' '.join(sys.argv[1:])
    print(address)


# TODO: Get address from clipboard

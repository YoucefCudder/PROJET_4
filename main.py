#!/usr/bin/python3
# coding: utf8
from controllers.Controller import Controller
import sys


if __name__ == "__main__":
    try:
        Controller().start()
    except KeyboardInterrupt:
        print("Interrupted")
        sys.exit(0)

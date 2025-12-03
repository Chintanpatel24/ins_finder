import sys
import colorama
import time
import argparse
import json
import httpx
import hmac
import hashlib
import urllib
import requests
from httpx import get
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style, init


colorama.init(autoreset=True)


def banner():
    print("                _ _   _                ")
    print("  _  _ ___ ___ (_) |_( )___  _ __  ___ ")
    print(" | || / -_|_-< | |  _|/(_-< | '  \/ -_)")
    print("  \_, \___/__/ |_|\__| /__/ |_|_|_\___|")
    print("  |__/                                 ")
    print("\n\tTwitter: " + Fore.MAGENTA + "@blackeko5")


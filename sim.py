import os
import argparse
import urllib3
import requests

banner = """
███████╗██╗███╗   ███╗     █████╗ ██████╗ ██╗
██╔════╝██║████╗ ████║    ██╔══██╗██╔══██╗██║
███████╗██║██╔████╔██║    ███████║██████╔╝██║
╚════██║██║██║╚██╔╝██║    ██╔══██║██╔═══╝ ██║
███████║██║██║ ╚═╝ ██║    ██║  ██║██║     ██║
╚══════╝╚═╝╚═╝     ╚═╝    ╚═╝  ╚═╝╚═╝     ╚═╝
           Developed by @mkdirlove
  API by: https://www.facebook.com/joshg101 
  
"""

os.system("clear")
print(banner)
urllib3.disable_warnings()
parser = argparse.ArgumentParser(description='Generate a Facebook cover using SIM API.')
parser.add_argument('-n', '--name', required=True, help='Firstname')
parser.add_argument('-c', '--color', required=True, help='Color')
parser.add_argument('-a', '--address', required=True, help='Address')
parser.add_argument('-e', '--email', required=True, help='Email Address')
parser.add_argument('-s', '--subname', required=True, help='Lastname')
parser.add_argument('--sdt', required=True, help='Contact Number')
parser.add_argument('-o', '--output', required=True, help='Output PNG file')
args = parser.parse_args()

if not any(vars(args).values()):
    parser.print_help()
else:
    params = {
        'name': args.name,
        'color': args.color,
        'address': args.address,
        'email': args.email,
        'subname': args.subname,
        'sdt': args.sdt,
        'uid': '4',
    }
    headers = {
        'Host': 'sim.ainz-project.repl.co',
        'Sec-Ch-Ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.50 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'close',
    }

    response = requests.get('https://sim.ainz-project.repl.co/canvas/fbcover', headers=headers, params=params, verify=False)

    if args.output:
        with open(args.output, 'wb') as f:
            f.write(response.content)
    else:
        print(response.text)

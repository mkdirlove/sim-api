<h1 align="center">
  <br>
  <a href="https://github.com/mkdirlove/sim-api"><img src="https://github.com/mkdirlove/sim-api/blob/main/output.png" alt="sim-api"></a>
  <br>
  A simple Facebook cover photo generator using SIM API by https://www.facebook.com/joshg101
  <br>
</h1>

#### Installation

Copy-paste this into your terminal:

```
git clone https://github.com/mkdirlove/sim-api.git
```
```
cd sim-api
```
```
python3 sim.py -h
```

#### Usage
```
███████╗██╗███╗   ███╗     █████╗ ██████╗ ██╗
██╔════╝██║████╗ ████║    ██╔══██╗██╔══██╗██║
███████╗██║██╔████╔██║    ███████║██████╔╝██║
╚════██║██║██║╚██╔╝██║    ██╔══██║██╔═══╝ ██║
███████║██║██║ ╚═╝ ██║    ██║  ██║██║     ██║
╚══════╝╚═╝╚═╝     ╚═╝    ╚═╝  ╚═╝╚═╝     ╚═╝
           Developed by @mkdirlove
  API by: https://www.facebook.com/joshg101 
  

usage: sim.py [-h] -n NAME -c COLOR -a ADDRESS -e EMAIL -s SUBNAME --sdt SDT -o OUTPUT

Generate a Facebook cover using SIM API.

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Firstname
  -c COLOR, --color COLOR
                        Color
  -a ADDRESS, --address ADDRESS
                        Address
  -e EMAIL, --email EMAIL
                        Email Address
  -s SUBNAME, --subname SUBNAME
                        Lastname
  --sdt SDT             Contact Number
  -o OUTPUT, --output OUTPUT
                        Output PNG file
```
#### Sample Usage #1
```
python3 sim.py -n Jayson -c yellow -a Philippines -e mkdirlove@lspu.edu.ph -s "San Buenaventura" --sdt +639657032133 -o output.png
```

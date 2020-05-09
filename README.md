# forver
A quick and dirty way to perform forward and reverse DNS look-ups.

# Installation
python3 setup.py install

# Usage
```
usage: forver.py [-h] [-d DOMAINS] [-i IPS] [-t THREADS] [-o O] [-f]

optional arguments:
  -h, --help            show this help message and exit
  -d DOMAINS, --domains DOMAINS
                        Specify file with list of hostnames.
  -i IPS, --ips IPS     Specify file with list of IPs.
  -t THREADS, --threads THREADS
                        Number of threads to use.
  -o O, -out O          Specify output file to send results to.
  -f, --force           Use this flag to force --domains or --ips flag if
                        forver suspected wrong file or flag usage
```

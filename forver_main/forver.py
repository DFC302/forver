#!/usr/bin/env python3

import socket
import sys
import argparse
import concurrent.futures

def options():
	parser = argparse.ArgumentParser()

	# hostnames
	parser.add_argument(
		"-d", "--domains",
		help="Specify file with list of hostnames.",
		action="store",
	)

	parser.add_argument(
		"-i", "--ips",
		help="Specify file with list of IPs.",
		action="store",
	)

	parser.add_argument(
		"-t", "--threads",
		help="Number of threads to use.",
		action="store",
		type=int,
	)

	parser.add_argument(
		"-o", "-out",
		help="Specify output file to send results to.",
		action="store",
	)

	parser.add_argument(
		"-f", "--force",
		help="Use this flag to force --domains or --ips flag if forver suspected wrong file or flag usage.",
		action="store_true",
	)

	parser.add_argument(
		"-s", "--single",
		help="Use this flag with the --ips or --domains flag to search a single IP or domain.",
		action="store_true",
	)

	# if not arguments are given, print usage message
	if len(sys.argv[1:]) == 0:
		parser.print_help()
		parser.exit()

	args = parser.parse_args()

	return args

def single_search():
	if options().domains:
		host = options().domains.replace("http://", "").replace("https://", "").strip("\n")

		IP = socket.gethostbyname(host)
		print(f"HOSTNAME: {host} | IP: {IP}")

	elif options().ips:
		hostname = socket.gethostbyaddr(options().ips)[0]
		print(f"IP {options().ips} | HOSTNAME: {hostname}")


def threadExecution():
	if options().threads:
		threads = options().threads

	else:
		threads = 20

	domains = []

	if options().domains:
		with open(options().domains, "r") as hostfile:
			for host in hostfile:
				if host == "":
					pass

				if host[0:1].isdigit():
					print("Are you sure you are opening a file full of domains?")
					print("Or did you mean to use the --ips flag instead?")
					print("If so, run again using the --force flag.")

					if options().force:
						host = host.replace("http://", "").replace("https://", "").strip("\n")
						domains.append(host)

					else:
						sys.exit(1)

				else:
					host = host.replace("http://", "").replace("https://", "").strip("\n")
					domains.append(host)

		with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
			executor.map(domainNameSearch, domains)

	elif options().ips:
		with open(options().ips, "r") as ipfile:
			for ip in ipfile:
				if ip == "":
					pass

				elif ip.startswith("http"):
					print("Are you sure you are opening a file full of IPs??")
					print("Or did you mean to use the --domains flag instead??")
					print("If so, run again using the --force flag.")

					if options().force:
						domains.append(ip)

					else:
						sys.exit(1)

				else:
					domains.append(ip)

		with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
			executor.map(ipSearch, domains)

	# Just in case
	else:
		print("Unknown option!")
		sys.exit(1)

def domainNameSearch(host):
	try:
		IP = socket.gethostbyname(host)
		print(f"HOSTNAME: {host} | IP: {IP}")

		if options().out:
			with open(options().out, "a") as wf:
				wf.write(f"HOSTNAME: {host} | IP: {IP}\n")

	except Exception as e:
		print(f"HOSTNAME: {host} | IP: {e}")

		if options().out:
			with open(options().out, "a") as wf:
				wf.write(f"HOSTNAME: {host} | IP: {e}\n")

def ipSearch(ip):
	try:
		hostname = socket.gethostbyaddr(ip)[0]
		print(f"IP {ip} | HOSTNAME: {hostname}")

		if options().out:
			with open(options().out, "a") as wf:
				wf.write(f"IP {ip} | HOSTNAME: {hostname}\n")

	except Exception as e:
		print(f"IP {ip} | HOSTNAME: {e}")
		pass

		if options().out:
			with open(options().out, "a") as wf:
				wf.write(f"IP {ip} | HOSTNAME: {e}\n")

def main():
	if options().single:
		single_search()

	else:
		threadExecution()

if __name__ == "__main__":
	main()

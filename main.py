from argparse import ArgumentParser
from dotenv import dotenv_values
from pythonosc import udp_client

CAMERAS = ['General', 'Tiny', 'Tail', 'Meet']
CONFIG_VALUES = ['host', 'port', 'camera']

COMMANDS = {
	"WakeSleep" : {
		"address" : "/OBSBOT/WebCam/General/WakeSleep",
		"value" : 1,
		"options" : [0, 1],
		"type" : "simple"
	},
	"ResetGimbal" : {
		"address" : "/OBSBOT/WebCam/General/ResetGimbal",
		"value" : 0,
		"type" : "simple"
	}
}

Config = {
	"host" : "127.0.0.1",
	"port" : 16284,
	"camera"  : "General"
}

def update_config (args, env) :
	"""Updates Config object preferencing command line arguments"""
	for val in CONFIG_VALUES :
		if val.upper() in env :
			Config[val] = env[val.upper()]
		if getattr(args, val) is not None :
			Config[val] = getattr(args, val)

	#print(Config)

def list () :
	keys = COMMANDS.keys()

	print(f"Command\t\tAddress")
	for key in keys :
		print(f"{key}\t{COMMANDS[key]['address']}")

def send_osc_command_simple(address, value):
	"""Sends an OSC message with a single integer argument."""
	try:
		client = udp_client.SimpleUDPClient(Config["host"], Config["port"])
		client.send_message(address, value)
		print(f"Sent OSC message: {address}, value: {value}")
	except Exception as e:
		print(f"Error sending OSC message: {e}")

def command (args, parser) :
	if getattr(args, "command") is None :
		print(f"Please provide a command")
		parser.print_help()
		exit(1)

	if args.command in COMMANDS :
		cmd = COMMANDS[args.command]["address"]
		val = COMMANDS[args.command]["value"]

		if getattr(args, "value") is not None :
			if "options" in COMMANDS[args.command]:
				if int(args.value) not in COMMANDS[args.command]["options"] :
					print(f"Value {int(args.value)} not a valid value for command {cmd}")
					exit(3)
				else :
					val = int(args.value)
			elif "range" in COMMANDS[args.command]: 
				if args.value < COMMANDS[args.command]["range"][0] or args.value > COMMANDS[args.command]["range"][1] :
					print(f"Value {args.value} is not in range {COMMANDS[args.command]['range'][0]}->{COMMANDS[args.command]['range'][1]} for command {args.command}")
					exit(4)
				else : 
					val = args.value

		if COMMANDS[args.command]["type"] == "simple" :
			send_osc_command_simple(cmd, val)
		# getter
		# 
	else :
		print(f"Command {args.command} is not valid")
		parser.print_help()
		exit(2)

def main () :
	parser = ArgumentParser(description="Unofficial command line utility for sending OSC commands to OBSBOT cameras")
	parser.add_argument("-e", "--env", type=str, help="Choose an ENV file to use (default: .env)", default=".env")
	parser.add_argument("-H", "--host", type=str, help=f"Host to connect to OSC server (default: {Config['host']})")
	parser.add_argument("-P", "--port", type=int, help=f"Port of OSC server (default: {Config['port']})")
	parser.add_argument("-c", "--camera", choices=CAMERAS, help=f"OBSBOT camera type to send commands for [General/Tiny/Meet/Tail] (default: {Config['camera']})")
	parser.add_argument("-l", "--list", action="store_true", help="List all available commands for camera type")
	parser.add_argument("command", type=str, nargs="?", help="Command to issue to OBSBOT camera over OSC")
	parser.add_argument("value", type=float, nargs="?", help="Optional value to send with command")
	args = parser.parse_args()
	
	env = dotenv_values(args.env)

	update_config(args, env)

	if args.list :
		list()
	else :
		command(args, parser)

if __name__ == "__main__":
	main()
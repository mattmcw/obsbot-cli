from argparse import ArgumentParser
from dotenv import dotenv_values
from pythonosc import udp_client

CAMERAS = ['General', 'Tiny', 'Tail', 'Meet']
CONFIG_VALUES = ['host', 'port', 'camera']

COMMANDS = {
	"WakeSleep" : {
		"address" : "/OBSBOT/WebCam/General/WakeSleep",
		"value" : 1,
		"options_int" : [0, 1], #sleep/wake
		"type" : "set"
	},
	"ResetGimbal" : {
		"address" : "/OBSBOT/WebCam/General/ResetGimbal",
		"value" : 0,
		"type" : "set"
	},
	"SetMirror" : {
		"address" : "/OBSBOT/WebCam/General/SetMirror",
		"value" : 1,
		"options_int" : [0, 1], #regular/mirrored
		"type" : "set"
	},
	"SetAutoFocus" : {
		"address" : "/OBSBOT/WebCam/General/SetAutoFocus",
		"value" : 1,
		"options_int" : [0, 1], #manual/auto
		"type" : "set",
		"cameras" : ["Tiny", "Meet"]
	},
	"SetManualFocus" : {
		"address" : "/OBSBOT/WebCam/General/SetManualFocus",
		"value" : 1,
		"range_int" : [0, 100], #
		"type" : "set",
		"cameras" : ["Tiny", "Meet"]
	},
	"SetAutoExposure" : {
		"address" : "/OBSBOT/WebCam/General/SetAutoExposure",
		"value" : 1,
		"options_int" : [0, 1], #manual/auto
		"type" : "set"
	},
	"SetExposureCompensate" : {
		"address" : "/OBSBOT/WebCam/General/SetExposureCompensate",
		"value" : 0,
		"options_int" : [-30, -27, -23, -20, -17, -13, -10, -7, -3, 0, 3, 7, 10, 13, 17, 20, 23, 27, 30],
		"type" : "set"
	},
	"SetShutterSpeed" : {
		"address" : "/OBSBOT/WebCam/General/SetShutterSpeed",
		"value" : 80,
		"options_int" : [6400, 5000, 3200, 2500, 2000, 1600, 1250, 1000, 800, 640, 500, 400, 320, 240, 200, 160, 120, 100, 80, 60, 50, 40, 30, 25, 20, 15, 10, 8, 5, 4, 3], # floats?? 12.5, 6.25, 2.5
		"type" : "set"
	},
	"SetISO" : {
		"address" : "/OBSBOT/WebCam/General/SetISO",
		"value" : 1,
		"range_int" : [100, 6400], #snaps to nearest 100
		"type" : "set"
	},
	"SetAutoWhiteBalance" : {
		"address" : "/OBSBOT/WebCam/General/SetAutoWhiteBalance",
		"value" : 1,
		"options_int" : [0, 1], #manual/auto
		"type" : "set"
	},
	"SetColorTemperature" : {
		"address" : "/OBSBOT/WebCam/General/SetColorTemperature",
		"value" : 1,
		"range_int" : [2800, 6500], #snaps to nearest 100
		"type" : "set"
	}
}

'''

'''

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

	print(f"Command\t\tAddress\t\t\t\t\tOptions\tCameras")
	for key in keys :
		range_str = ""
		cameras_str = "*"
		if "options_int" in COMMANDS[key] :
			range_str = "/".join(map(str, COMMANDS[key]["options_int"]))
		elif "range_int" in COMMANDS[key] :
			range_str = "->".join(map(str,COMMANDS[key]["range_int"]))
		elif "range_float" in COMMANDS[key] :
			range_str = "->".join(map(str,COMMANDS[key]["range_float"]))
		else :
			range_str = COMMANDS[key]["value"]
		print(f"{key}\t{COMMANDS[key]['address']}\t[{range_str}]\t{cameras_str}")

def send_osc_command_set(address, value):
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

		if "cameras" in COMMANDS[args.command] and Config["camera"] not in COMMANDS[args.command]["cameras"] :
			print(f"Command {args.command} is not available to camera type {Config['camera']}")
			exit(5)

		if getattr(args, "value") is not None :
			if "options_int" in COMMANDS[args.command]:
				if int(args.value) not in COMMANDS[args.command]["options_int"] :
					print(f"Value {int(args.value)} not a valid value for command {cmd}")
					exit(3)
				else :
					val = int(args.value)
			elif "range_float" in COMMANDS[args.command]: 
				if float(args.value) < COMMANDS[args.command]["range_float"][0] or float(args.value) > COMMANDS[args.command]["range_float"][1] :
					print(f"Value {float(args.value)} is not in range {COMMANDS[args.command]['range_float'][0]}->{COMMANDS[args.command]['range_float'][1]} for command {args.command}")
					exit(4)
				else : 
					val = float(args.value)
			elif "range_int" in COMMANDS[args.command]: 
				if int(args.value) < COMMANDS[args.command]["range_int"][0] or int(args.value) > COMMANDS[args.command]["range_int"][1] :
					print(f"Value {int(args.value)} is not in range {COMMANDS[args.command]['range_int'][0]}->{COMMANDS[args.command]['range_int'][1]} for command {args.command}")
					exit(4)
				else : 
					val = int(args.value)
			else : 
				print(f"Ignoring value {args.value} for default {COMMANDS[args.command]['value']}...")

		if COMMANDS[args.command]["type"] == "set" :
			send_osc_command_set(cmd, val)
		# getter
		# adjuster
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
	parser.add_argument("value", type=str, nargs="?", help="Optional value to send with command")
	
	args = parser.parse_args()
	env = dotenv_values(args.env)
	update_config(args, env)

	if args.list :
		list()
	else :
		command(args, parser)

if __name__ == "__main__":
	main()
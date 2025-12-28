from argparse import ArgumentParser
from dotenv import dotenv_values
from pythonosc import udp_client

"""
/OBSBOT/WebCam/General/Connected
/OBSBOT/WebCam/General/ConnectedResp
/OBSBOT/WebCam/General/Disconnected
/OBSBOT/WebCam/General/SelectDevice
* /OBSBOT/WebCam/General/WakeSleep
/OBSBOT/WebCam/General/ResetGimbal
/OBSBOT/WebCam/General/SetZoom
/OBSBOT/WebCam/General/SetZoomSpeed
/OBSBOT/WebCam/General/SetZoomMax
/OBSBOT/WebCam/General/SetZoomMin
/OBSBOT/WebCam/General/SetGimbalUp
/OBSBOT/WebCam/General/SetGimbalDown
/OBSBOT/WebCam/General/SetGimbalLeft
/OBSBOT/WebCam/General/SetGimbalRight
/OBSBOT/WebCam/General/SetView
/OBSBOT/WebCam/General/SetGimMotorDegree
/OBSBOT/WebCam/General/SetGimMotorDegreeEx
/OBSBOT/WebCam/General/SetMirror
/OBSBOT/WebCam/General/SetPCRecording
/OBSBOT/WebCam/General/PCSnapshot

/OBSBOT/WebCam/General/SetAutoFocus
/OBSBOT/WebCam/General/SetManualFocus

/OBSBOT/WebCam/General/SetAutoExposure
/OBSBOT/WebCam/General/SetExposureCompensate
/OBSBOT/WebCam/General/SetShutterSpeed
/OBSBOT/WebCam/General/SetISO
/OBSBOT/WebCam/General/SetAutoWhiteBalance
/OBSBOT/WebCam/General/SetColorTemperature

/OBSBOT/WebCam/General/GetDeviceInfo
/OBSBOT/WebCam/General/DeviceInfo
/OBSBOT/WebCam/General/GetZoomInfo
/OBSBOT/WebCam/General/ZoomInfo
/OBSBOT/WebCam/General/GetGimbalPosInfo
/OBSBOT/WebCam/General/GetGimbalPosInfoResp

/OBSBOT/Camera/Tail/SetFocusMode
/OBSBOT/Camera/Tail/SetAiMode
/OBSBOT/Camera/Tail/SetTrackingSpeed
/OBSBOT/Camera/Tail/SetPanTrackingSpeed
/OBSBOT/Camera/Tail/SetTiltTrackingSpeed
/OBSBOT/Camera/Tail/SetPanAxisLock
/OBSBOT/Camera/Tail/SetTiltAxisLock
/OBSBOT/Camera/Tail/SetRecording
/OBSBOT/Camera/Tail/Snapshot
/OBSBOT/Camera/Tail/TriggerPreset

/OBSBOT/WebCam/Tiny/ToggleAILock
/OBSBOT/WebCam/Tiny/TriggerPreset
/OBSBOT/WebCam/Tiny/SetAiMode
/OBSBOT/WebCam/Tiny/SetTrackingMode
/OBSBOT/WebCam/Tiny/GetAiTrackingInfo
/OBSBOT/WebCam/Tiny/AiTrackingInfo
/OBSBOT/WebCam/Tiny/GetPresetPositionInfo
/OBSBOT/WebCam/Tiny/PresetPositionInfo

/OBSBOT/WebCam/Meet/SetVirtualBackground
/OBSBOT/WebCam/Meet/SetAutoFraming
/OBSBOT/WebCam/Meet/SetStandardMode
/OBSBOT/WebCam/Meet/GetVirtualBackgroundInfo
/OBSBOT/WebCam/Meet/VirtualBackgroundInfo
/OBSBOT/WebCam/Meet/GetAutoFramingInfo
/OBSBOT/WebCam/Meet/AutoFramingInfo
"""

CAMERAS = ['General', 'Tiny', 'Tail', 'Meet']
CONFIG_VALUES = ['host', 'port', 'camera']
COMMANDS = {
	"WakeSleep" : {
		"address" : "/OBSBOT/WebCam/General/WakeSleep",
		"value" : 1
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

def send_osc_command (address, value):
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
		if getattr(args, 'value') is not None :
			val = getattr(args, 'value')
		send_osc_command(cmd, val)
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
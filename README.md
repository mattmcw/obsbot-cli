# obsbot-cli

Unofficial command line utility for sending OSC commands to OBSBOT cameras

## Usage

```bash
python main.py --host 127.0.0.1 --port 16284 
```

## Commands

```bash
python main.py --list

Command		Address
WakeSleep	/OBSBOT/WebCam/General/WakeSleep
ResetGimbal	/OBSBOT/WebCam/General/ResetGimbal
```
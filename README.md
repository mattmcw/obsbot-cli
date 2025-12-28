# obsbot-cli

Unofficial command line utility for sending OSC commands to OBSBOT cameras

## Usage

```bash
python main.py --host 127.0.0.1 --port 16284 
```

## Commands

```bash
python main.py --list

Command		Address					Options	Cameras
WakeSleep	/OBSBOT/WebCam/General/WakeSleep	[0/1]	*
ResetGimbal	/OBSBOT/WebCam/General/ResetGimbal	[0]	*
SetMirror	/OBSBOT/WebCam/General/SetMirror	[0/1]	*
SetAutoFocus	/OBSBOT/WebCam/General/SetAutoFocus	[0/1]	*
SetManualFocus	/OBSBOT/WebCam/General/SetManualFocus	[0->100]	*
SetAutoExposure	/OBSBOT/WebCam/General/SetAutoExposure	[0/1]	*
SetExposureCompensate	/OBSBOT/WebCam/General/SetExposureCompensate	[-30->30]	*
SetShutterSpeed	/OBSBOT/WebCam/General/SetShutterSpeed	[3->6400]	*
SetISO	/OBSBOT/WebCam/General/SetISO	[100->6400]	*
SetAutoWhiteBalance	/OBSBOT/WebCam/General/SetAutoWhiteBalance	[0/1]	*
SetColorTemperature	/OBSBOT/WebCam/General/SetColorTemperature	[2800->6500]	*
```

## Coverage

```
/OBSBOT/WebCam/General/Connected
/OBSBOT/WebCam/General/ConnectedResp
/OBSBOT/WebCam/General/Disconnected
/OBSBOT/WebCam/General/SelectDevice
* /OBSBOT/WebCam/General/WakeSleep [0,1]
* /OBSBOT/WebCam/General/ResetGimbal [0]
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
* /OBSBOT/WebCam/General/SetMirror [0, 1]
/OBSBOT/WebCam/General/SetPCRecording
/OBSBOT/WebCam/General/PCSnapshot

* /OBSBOT/WebCam/General/SetAutoFocus
* /OBSBOT/WebCam/General/SetManualFocus
* /OBSBOT/WebCam/General/SetAutoExposure
* /OBSBOT/WebCam/General/SetExposureCompensate
* /OBSBOT/WebCam/General/SetShutterSpeed
* /OBSBOT/WebCam/General/SetISO
* /OBSBOT/WebCam/General/SetAutoWhiteBalance
* /OBSBOT/WebCam/General/SetColorTemperature

GETTERS

/OBSBOT/WebCam/General/GetDeviceInfo
/OBSBOT/WebCam/General/DeviceInfo
/OBSBOT/WebCam/General/GetZoomInfo
/OBSBOT/WebCam/General/ZoomInfo
/OBSBOT/WebCam/General/GetGimbalPosInfo
/OBSBOT/WebCam/General/GetGimbalPosInfoResp

TAIL

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

TINY

/OBSBOT/WebCam/Tiny/ToggleAILock
/OBSBOT/WebCam/Tiny/TriggerPreset
/OBSBOT/WebCam/Tiny/SetAiMode
/OBSBOT/WebCam/Tiny/SetTrackingMode
/OBSBOT/WebCam/Tiny/GetAiTrackingInfo
/OBSBOT/WebCam/Tiny/AiTrackingInfo
/OBSBOT/WebCam/Tiny/GetPresetPositionInfo
/OBSBOT/WebCam/Tiny/PresetPositionInfo

MEET

/OBSBOT/WebCam/Meet/SetVirtualBackground
/OBSBOT/WebCam/Meet/SetAutoFraming
/OBSBOT/WebCam/Meet/SetStandardMode
/OBSBOT/WebCam/Meet/GetVirtualBackgroundInfo
/OBSBOT/WebCam/Meet/VirtualBackgroundInfo
/OBSBOT/WebCam/Meet/GetAutoFramingInfo
/OBSBOT/WebCam/Meet/AutoFramingInfo
```
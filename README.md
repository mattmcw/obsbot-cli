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

## Coverage

```
/OBSBOT/WebCam/General/Connected
/OBSBOT/WebCam/General/ConnectedResp
/OBSBOT/WebCam/General/Disconnected
/OBSBOT/WebCam/General/SelectDevice
* /OBSBOT/WebCam/General/WakeSleep
# /OBSBOT/WebCam/General/ResetGimbal
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
/OBSBOT/WebCam/General/SetAutoExposure

/OBSBOT/WebCam/General/SetManualFocus
/OBSBOT/WebCam/General/SetExposureCompensate
/OBSBOT/WebCam/General/SetShutterSpeed
/OBSBOT/WebCam/General/SetISO
/OBSBOT/WebCam/General/SetAutoWhiteBalance
/OBSBOT/WebCam/General/SetColorTemperature

GETTERS

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
```
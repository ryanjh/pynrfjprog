from pynrfjprog import JLink
import ctypes
import sys

jlink = JLink.find_latest_dll()

if jlink:
    print("jlink found")
else:
    print("jlink not found!")

print(jlink)

lib = ctypes.cdll.LoadLibrary(jlink)
print(lib.JLINKARM_EMU_GetNumDevices())

# jlink.open(ip_addr="0.0.0.0:19020")
addr = sys.argv[1]
port = sys.argv[2]
result = lib.JLINKARM_SelectIP(addr.encode(), int(port))
if result == 1:
    print("Could not connect to emulator")
else:
    print("connect to emulator")

log_handler = None
error_handler = None

result = lib.JLINKARM_OpenEx(log_handler, error_handler)
result = ctypes.cast(result, ctypes.c_char_p).value
if result is not None:
    raise errors.JLinkException(result.decode())

print(log_handler, error_handler)

# jlink.opened()
if bool(lib.JLINKARM_IsOpen()):
    print("jlink.opened")

# jlink.connected()
if bool(lib.JLINKARM_EMU_IsConnected()):
    print("jlink.connected")

# jlink.set_tif(pylink.enums.JLinkInterfaces.SWD)
SWD = 1
res = lib.JLINKARM_TIF_Select(SWD)
if res != 0:
    print("JLINKARM_TIF_Select fail")

# jlink.connect("NRF52840_XXAA", 'auto', True)

MAX_BUF_SIZE = 336
chip_name = "NRF52840_XXAA"
err_buf = (ctypes.c_char * MAX_BUF_SIZE)()
cmd = 'Device = %s' % chip_name
print(cmd)
res = lib.JLINKARM_ExecCommand(cmd.encode(), err_buf, MAX_BUF_SIZE)
err_buf = ctypes.string_at(err_buf).decode()


AUTO_JTAG_SPEED = 0x0
lib.JLINKARM_SetSpeed(AUTO_JTAG_SPEED)

result = lib.JLINKARM_Connect()
if result < 0:
    print("JLINKARM_Connect fail")
else:
    print("JLINKARM_Connect ok")

# print(jlink.core_id())
print(lib.JLINKARM_GetId())

# print(jlink.device_family())
print(lib.JLINKARM_GetDeviceFamily())

# jlink.target_connected()
if bool(lib.JLINKARM_IsConnected()):
    print("jlink.target_connected")

# jlink.reset()
ms = 0
halt = True
lib.JLINKARM_SetResetDelay(ms)

res = lib.JLINKARM_Reset()
if res < 0:
    raise errors.JLinkException(res)
elif not halt:
    lib.JLINKARM_Go()

print('reset:', res)

# jlink.erase()
res = lib.JLINK_EraseChip()
if res < 0:
    raise errors.JLinkEraseException(res)

print('erase:', res)

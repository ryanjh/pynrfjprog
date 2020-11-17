from pynrfjprog import API
import sys

api = API.API('NRF52')
api.open()

# Note: It requires new libnrfjprogdll.so and libjlinkarm_nrf52_nrfjprogdll.so
# (e.g. pynrfjprog/lib_x64)
addr = sys.argv[1]
port = sys.argv[2]
api.select_ip(addr.encode(), int(port))

print(api.enum_emu_snr())
if len(sys.argv) > 3:
    api.connect_to_emu_with_snr(int(sys.argv[3]))
else:
    api.connect_to_emu_without_snr()
api.pin_reset()
api.erase_all()
#api.write_u32(ADDRESS, DATA, IS_FLASH)
api.disconnect_from_emu()
api.close()

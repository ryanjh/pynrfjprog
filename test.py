from pynrfjprog import API

api = API.API('NRF52')
api.open()
print(api.enum_emu_snr())
api.connect_to_emu_without_snr()
api.erase_all()
#api.write_u32(ADDRESS, DATA, IS_FLASH)
api.disconnect_from_emu()
api.close()

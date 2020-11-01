from pynrfjprog import HighLevel

api = HighLevel.API()
api.open()

print(api.get_connected_probes())

# # To program J-Link probe at snr <snr>:
# probe = HighLevel.DebugProbe(api, <snr>)
# probe.program(<hex_file>)
# probe.close()

# # To program MCUBoot target at serial port <serial>:
# probe = HighLevel.MCUBootDFUProbe(api, <serial>)
# probe.program(<hex_file>)
# probe.close()

# # To update LTE modem connected to J-Link prbe at snr <snr>:
# probe = HighLevel.IPCDFUProbe(api, <snr>)
# probe.program(<hex_file>)
# probe.close()

api.close()

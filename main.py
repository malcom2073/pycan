from __future__ import print_function

import can
can.rc['interface'] = 'pcan'
can.rc['channel'] = 'PCAN_USBBUS1'

def main():
  bus = can.interface.Bus()
  msg = can.Message(arbitration_id=0xc0ffee,
                      data=[0, 25, 0, 1, 3, 1, 4, 1],
                      extended_id=True)
  while True:
    msg = bus.recv()
    print("{:02x}".format(msg.arbitration_id) + "-" + ":".join("{:02x}".format(c) for c in msg.data))
    priority = (msg.arbitration_id >> 26) & 0x7
    EDP = (msg.arbitration_id >> 25) & 0x1
    DP = (msg.arbitration_id >> 24) & 0x1
    PF = ((msg.arbitration_id >> 16) & 0xFF)
    PF2 = ((msg.arbitration_id >> 8) & 0xFF)
    SA = (msg.arbitration_id) & 0xFF
    print("Priority: " + str(priority))
    print("EDP: " + str(EDP))
    print("DP: " + str(DP))
    print("PF: " + str(PF))
    print("PF2: " + str(PF2))
    print("SA: " + str(SA))

if __name__ == "__main__":
  main()

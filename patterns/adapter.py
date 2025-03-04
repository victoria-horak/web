class MicroUSBCharger:
    def charge_with_micro_usb(self):
        return "Заряджається через micro-USB"


class USB_CDevice:
    def charge_with_usb_c(self):
        return "Заряджається через USB-C"


class MicroUSBToUSB_CAdapter(USB_CDevice):
    def __init__(self, micro_usb_charger):
        self.micro_usb_charger = micro_usb_charger

    def charge_with_usb_c(self):
        return self.micro_usb_charger.charge_with_micro_usb() + " (через адаптер)"


old_charger = MicroUSBCharger()
adapter = MicroUSBToUSB_CAdapter(old_charger)

print(adapter.charge_with_usb_c())


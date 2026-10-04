from abc import ABC, abstractmethod
class SmartDevice(ABC):
    @abstractmethod
    def operate(self):
        pass
class SmartLight(SmartDevice):
    def operate(self):
        print("Turning on the smart light.")
class SmartSpeaker(SmartDevice):   
    def operate(self):
            print("Playing music on the smart speaker.")
class SmartAC(SmartDevice):
    def operate(self):
        print("Turning on the smart air conditioner.")      
devices = [SmartLight(), SmartSpeaker(), SmartAC()]
for device in devices:
    device.operate()                       

    
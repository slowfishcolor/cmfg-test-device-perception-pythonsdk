class Option:
    def __init__(self):
        self.qos = 0
        self.username = ""
        self.password = ""
        self.url = ""
        self.subscribe = 0
        self.publish = 1
        self.will = ""


class Data:
    def __init__(self, type):
        self.type = type


class AnalogSampleData(Data):
    def __init__(self):
        super(AnalogSampleData, self).__init__("AnalogSampleData")
        self.port = ""
        self.method = ""
        self.frequency = 0.0
        self.sampleCount = 1
        self.timestamp = 0
        self.value = []


class ControlData(Data):
    def __init__(self):
        super(ControlData, self).__init__("ControlData")
        self.commandCount = 0
        self.command = "null"
        self.commands = []
        self.commandMap = {}


class Instruction:
    def __init__(self):
        self.name = ""
        self.instruction = ""
        self.value = 0.0
        self.values = []
        self.minValue = 0.0
        self.maxValue = 0.0
        self.status = 0
        self.interval = 0
        self.timestamp = 0
        self.remark = ""


class InstructionData(Data):
    def __init__(self):
        super(InstructionData, self).__init__("InstructionData")
        self.instructionCount = 1
        self.instruction = 0
        self.instructions = []
        self.instructionMap = {}


class Payload:
    def __init__(self, option, data):
        self.type = data.type
        self.messageId = 0
        self.destination = ""
        self.deviceId = ""
        self.physicalDeviceId = ""
        self.timestamp = 0
        self.userId = 0
        self.code = 0
        self.option = option
        self.data = data
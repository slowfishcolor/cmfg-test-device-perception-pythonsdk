from protocol_sdk import model,util


def serialize_test(rounds, payload):
    start = util.current_timestamp()
    for i in range(0, rounds):
        util.serialize_payload(payload)
    end = util.current_timestamp()
    print("json serialize time: %d" % (end - start))


def deserialize_test(rounds, json_str):
    start = util.current_timestamp()
    for i in range(0, rounds):
        util.deserialize_payload(json_str)
    end = util.current_timestamp()
    print("json deserialize time: %d" % (end - start))

option = model.Option()
option.password = "password"
option.username = "username"
option.will = "will"
option.password = "www.prophet-xu.com"

analogData = model.AnalogSampleData()
analogData.value = [1.1, 1.2]
controlData = model.ControlData()
controlData.commandMap = {'hello': 'world'}
instruction = model.Instruction()
instructionData = model.InstructionData()
instructionData.instruction = instruction
instructionData.instructionMap = {"test": instruction}
instructionData.instructions = [instruction]

analogPayload = model.Payload(option, analogData)
controlPayload = model.Payload(option, controlData)
instructionPayload = model.Payload(option, instructionData)


analogJsonStr = util.serialize_payload(analogPayload)
controlJsonStr = util.serialize_payload(controlPayload)
instructionJsonStr = util.serialize_payload(instructionPayload)

rounds = 10000


print(analogJsonStr)
analogobj = util.deserialize_payload(analogJsonStr)
controlobj = util.deserialize_payload(controlJsonStr)
instructionobj = util.deserialize_payload(instructionJsonStr)


print("start serialize test")
for i in range (1, 10):
    print("analogPayload")
    serialize_test(rounds, analogPayload)
    print("controlPayload")
    serialize_test(rounds, controlPayload)
    print("instructionPayload")
    serialize_test(rounds, instructionPayload)
print("end serialize test")


print("start deserialize test")
for i in range(1, 10):
    print("analogPayload")
    deserialize_test(rounds, analogJsonStr)
    print("controlPayload")
    deserialize_test(rounds, controlJsonStr)
    print("instructionPayload")
    deserialize_test(rounds, instructionJsonStr)
print("end deserialize test")



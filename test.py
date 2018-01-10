from protocol_sdk import model,util


def serialize_test(rounds, payload):
    start = util.current_timestamp()
    for i in range(0, rounds):
        util.serialize_payload(payload)
    end = util.current_timestamp()
    print("json serialize time: %d" % (end - start))
    return end - start


def deserialize_test(rounds, json_str):
    start = util.current_timestamp()
    for i in range(0, rounds):
        util.deserialize_payload(json_str)
    end = util.current_timestamp()
    print("json deserialize time: %d" % (end - start))
    return end - start

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

rounds = 100000


print(analogJsonStr)
analogobj = util.deserialize_payload(analogJsonStr)
controlobj = util.deserialize_payload(controlJsonStr)
instructionobj = util.deserialize_payload(instructionJsonStr)


seControlAvg = 0
seAnalogAvg = 0
seInsAvg = 0

deControlAvg = 0
deAnalogAvg = 0
deInsAvg = 0

serializeAvg = 0
deserializeAvg = 0

print("start serialize test")
for i in range (1, 10):
    print("analogPayload")
    seAnalogAvg += serialize_test(rounds, analogPayload)
    print("controlPayload")
    seControlAvg += serialize_test(rounds, controlPayload)
    print("instructionPayload")
    seInsAvg += serialize_test(rounds, instructionPayload)
print("end serialize test")


print("start deserialize test")
for i in range(1, 10):
    print("analogPayload")
    deAnalogAvg += deserialize_test(rounds, analogJsonStr)
    print("controlPayload")
    deControlAvg += deserialize_test(rounds, controlJsonStr)
    print("instructionPayload")
    deInsAvg += deserialize_test(rounds, instructionJsonStr)
print("end deserialize test")


seAnalogAvg /= 10
seControlAvg /= 10
seInsAvg /= 10

deAnalogAvg /= 10
deControlAvg /= 10
deInsAvg /= 10

serializeAvg = (seAnalogAvg + seControlAvg + seInsAvg) / 3
deserializeAvg = (deAnalogAvg + deControlAvg + deInsAvg) / 3

print("")
print("seAnalogAvg: ", seAnalogAvg)
print("seControlAvg: ", seControlAvg)
print("seInsAvg: ", seInsAvg)
print("")
print("deAnalogAvg: ", deAnalogAvg)
print("deControlAvg: ", deControlAvg)
print("deInsAvg: ", deInsAvg)
print("")
print("serializeAvg: ", serializeAvg)
print("deserializeAvg: ", deserializeAvg)
print("")
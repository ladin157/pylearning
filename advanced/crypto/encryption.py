import base64
def stringToBase64(s):
    return base64.b64encode(s.encode('utf-8'))

def base64ToString(b):
    return base64.b64decode(b).decode('utf-8')

encoded = stringToBase64("{'system': {'branch_exited_reason': 'completed', 'branch_exited': True, 'dialog_stack': [{'dialog_node': 'root'}], 'dialog_request_counter': 1, '_node_output_map': {'Start And Initialize Context': [0, 0]}, 'dialog_turn_counter': 1}, 'AConoff': 'off', 'musiconoff': 'off', 'conversation_id': 'a0b1da76-73c3-4968-b8bb-48e746710688', 'default_counter': 0, 'volumeonoff': 'off', 'heateronoff': 'off', 'wipersonoff': 'off', 'lightonoff': 'off', 'appl_action': ''}")
print(encoded)
decoded = base64ToString(encoded)
print(decoded)
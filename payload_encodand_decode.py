import base64

def encode_payload(payload, salt_key, salt_index):
    # Add salt key to the payload
    salted_payload = salt_key + payload
    
    # Encode the salted payload to base64
    encoded_payload = base64.b64encode(salted_payload.encode()).decode()
    
    # Add salt index to the encoded payload
    encoded_payload_with_index = str(salt_index) + encoded_payload
    
    return encoded_payload_with_index

def decode_payload(encoded_payload_with_index, salt_key, salt_index):
    # Extract salt index from the beginning of the encoded payload
    encoded_payload = encoded_payload_with_index[len(str(salt_index)):]
    
    # Decode the encoded payload from base64
    decoded_payload = base64.b64decode(encoded_payload.encode()).decode()
    
    # Remove salt key from the decoded payload
    original_payload = decoded_payload[len(salt_key):]
    
    return original_payload

# Get user input for encoding
payload = input("Enter the payload to encode: ")
salt_key = input("Enter the salt key: ")
salt_index = int(input("Enter the salt index: "))

# Encode the payload with salt key and salt index
encoded_payload = encode_payload(payload, salt_key, salt_index)
print("Encoded payload:", encoded_payload)

# Get user input for decoding
decode_option = input("Do you want to decode this payload? (yes/no): ")
if decode_option.lower() == "yes":
    decode_salt_key = input("Enter the salt key for decoding: ")
    decode_salt_index = int(input("Enter the salt index for decoding: "))
    
    try:
        decoded_payload = decode_payload(encoded_payload, decode_salt_key, decode_salt_index)
        print("Decoded payload:", decoded_payload)
    except:
        print("Decoding failed with invalid salt key or salt index")
else:
    print("No decoding requested")

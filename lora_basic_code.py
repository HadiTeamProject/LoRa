import serial

# Configure the serial port
lora = serial.Serial(
    port='/dev/serial0',  # Raspberry Pi UART port
    baudrate=9600,         # Match baudrate with your LoRa module
    timeout=1              # Timeout for serial communication
)
while True:
    # Send data to LoRa module
    at_command= input('Enter your AT command:   ')
    #AT msg should end with \r\n or enter
    msg = f'{at_command}\r\n'
    #AT msg should be in byte formate
    msg = msg.encode('utf-8')
    lora.write(msg)
    # Wait for a response
    response = lora.readline().decode().strip()
    print("Received:", response)


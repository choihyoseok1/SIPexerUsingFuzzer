import socket

# 1. 서버 설정
HOST = "127.0.0.1"  # "나 자신" (localhost)
PORT = 5060         # SIP 기본 포트

SIP_RESPONSE = (
    "SIP/2.0 200 OK\r\n"
    "Via: SIP/2.0/UDP 127.0.0.1:5060;branch=z9hG4bK-sipexer\r\n" 
    "From: <sip:sipexer@localhost>\r\n"
    "To: <sip:server@localhost>;tag=12345\r\n"
    "Call-ID: default-call-id\r\n"
    "CSeq: 1 INVITE\r\n"
    "Content-Length: 0\r\n"
    "\r\n"
).encode('utf-8') 

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

print(f"--- 🐍 Python Mini SIP Server (UAS) ---")
print(f"--- Listening on udp://{HOST}:{PORT} ---")
print("--- (중지하려면 Ctrl+C) ---")

try:
    while True:
        data, addr = sock.recvfrom(4096) 
        
        print(f"\n--- 📞 Request Received from {addr} ---")
        print(data.decode('utf-8')) 
        
        print(f"--- ✉️ Sending 200 OK to {addr} ---")
        sock.sendto(SIP_RESPONSE, addr)

except KeyboardInterrupt:
    print("\n--- 🐍 Server shutting down. ---")
    sock.close()
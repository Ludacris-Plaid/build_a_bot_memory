# Simple listener
    import socket, threading

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("", 4444))
    server.listen(5)
    print("Listening for malware connection...")
    conn, addr = server.accept()
    print(f"Connected by {addr}")
    print(conn.recv(1024)) # Print the received data

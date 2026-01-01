import ssl
import socket

hostname = "google.com"
port = 443
context = ssl.create_default_context()

with socket.create_connection((hostname, port)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as secure_sock:
        print("TLS handshake berhasil")
        print("Versi TLS      :", secure_sock.version())
        print("Cipher Suite   :", secure_sock.cipher())
        print("Sertifikat TLS :", secure_sock.getpeercert())

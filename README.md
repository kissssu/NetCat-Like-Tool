# NetCat-Like Tool (Python Edition)

This is a simple Python-based implementation of a `netcat`-like tool, comprising a client-server architecture. The server can send commands to a connected client, which executes them and returns the output.

## Features
- Command execution on the client system via the server.
- Lightweight and straightforward implementation.
- Example of socket programming in Python.

---

## Files
### `server.py`
- Acts as the controller.
- Sends commands to the client.
- Displays output from the client.

### `client.py`
- Connects to the server.
- Executes received commands.
- Sends the output back to the server.

---

## Requirements
- **Python 3.x**
- A local or network connection between the server and client.

---

## Usage
1. **Run the server**:
   ```bash
   python3 server.py
   ```
- The server will start listening on 127.0.0.1:9999.

2. **Run the client:**
```bash
python3 client.py
```
- The client will attempt to connect to 127.0.0.1:9999.

3. Send commands:

- From the server terminal, type a command (e.g., ls, dir, whoami).\
- The client will execute the command and return the result.\
- To terminate the connection, type exit.\

## Example
### Server
```bash
$ python3 server.py
Listening.....!
address are: ('127.0.0.1', 12345)
Connected.
$ ls
Desktop
Documents
Downloads
```

### Client
```bash
Connecting....
Connected.
```

## Notes
- **Security Warning**: This tool is for educational purposes only. Executing arbitrary commands over a network is highly insecure and should not be used in production environments.
- Modify the IP address and port in the scripts to fit your network setup if needed.

## License
This project is provided under the MIT License.

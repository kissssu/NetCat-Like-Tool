# NetCat-Like Tool (Python Edition)

This is a simple Python-based implementation of a `netcat`-like tool, comprising a client-server architecture. The server can send commands to a connected client, which executes them and returns the output.

## Features

- Command execution on the client system via the server.
- Lightweight and straightforward implementation.
- Example of socket programming in Python.
- Robust handling of client and server disconnections.
- User-friendly connection retry mechanism.

---

## Files

### `server.py`

- Acts as the controller.
- Sends commands to the client.
- Displays output from the client.
- Handles client disconnections gracefully.

### `client.py`

- Connects to the server.
- Executes received commands.
- Sends the output back to the server.
- Implements connection retry with informative messages.
- Handles server disconnections gracefully.

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

2. Run the client:
    ```Bash
    python3 client.py
    ```
- The client will attempt to connect to 127.0.0.1:9999 and will retry if the connection is refused, displaying informative messages.

3. Send commands:
- From the server terminal, type a command (e.g., ls, dir, whoami).
- The client will execute the command and return the result.
- To terminate the connection, type exit. Both the client and server will indicate the connection closure.

## Example

- Server
```Bash
$ python3 server.py
Listening.....!
address are: ('127.0.0.1', 12345)
Connected.
$ ls
Desktop
Documents
Downloads
$ exit
Connection ended.
```
- Client
```Bash
$ python3 client.py
Connecting....
Connected.
$ ls
Desktop
Documents
Downloads
$ exit
Connection closed.
```

## Notes

- **Security Warning**: This tool is for educational purposes only. Executing arbitrary commands over a network is highly insecure and should not be used in production environments.
- Modify the IP address and port in the scripts to fit your network setup if needed.

## Future Enhancements/Upcoming Updates

- **Command History**: Implement command history on the client-side, allowing users to easily access and re-execute previous commands.
- **Improved Output Formatting**: Enhance the output display on the client-side for better readability, potentially using colors or indentation.
- **File Transfer Capabilities**: Add functionality to upload and download files between the client and server.
- **Interactive Shell**: Develop a more interactive shell-like experience on the client, including features like tab completion.
- **Authentication**: Implement a basic authentication mechanism to secure the connection between the client and server.

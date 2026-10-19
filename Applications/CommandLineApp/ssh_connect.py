import paramiko
import time

# Define the SSH connection parameters
hostname = 'moped12.devsonas.de'
port = 22
username = 'root'
password = 'your_password'  # You can also use key-based authentication

# Create an SSH client
ssh = paramiko.SSHClient()

try:
    # Automatically add the server's host key (this is insecure and should be avoided in production)
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the remote machine
    ssh.connect(hostname, port, username)

    # Open an interactive shell
    shell = ssh.invoke_shell()

    # Send commands to the shell
    while True:
        command = input('Enter the command to execute on the remote machine (type "exit" to quit): ')
        if command.lower() == 'exit':
            break
        else:
            # Send the command to the shell
            shell.send(command + '\n')

            # Wait 50 ms and then check shell
            time.sleep(0.05)

            # Wait for the command to complete
            while not shell.recv_ready():
                pass

            # Print the output of the command
            output = shell.recv(1024).decode()
            print("Output:")
            print(output)
finally:
    # Close the SSH connection
    ssh.close()
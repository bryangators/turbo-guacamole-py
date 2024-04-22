import subprocess
import signal
import sys

# Define the command to start the application
command = "uvicorn server:app --reload"

# Run the command using subprocess
process = subprocess.Popen(command, shell=True, cwd="src")

# Define a signal handler to catch KeyboardInterrupt
def signal_handler(sig, frame):
    print("Shutting down the server...")
    process.terminate()  # Terminate the uvicorn process gracefully
    sys.exit(0)

# Register the signal handler for SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, signal_handler)

# Wait for the subprocess to finish
process.wait()

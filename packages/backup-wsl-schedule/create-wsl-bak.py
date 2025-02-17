import subprocess
import os

def run_powershell_command(command):
    """Executes a PowerShell command.

    Args:
        command: The PowerShell command to execute (as a string).

    Returns:
        A tuple containing the return code and the combined stdout/stderr output.
        Returns None if there's an issue with subprocess.
    """
    try:
        process = subprocess.Popen(
            ["powershell.exe", "-Command", command],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,  # Combine stdout and stderr
            text=True,  # Decode output as text
            creationflags=subprocess.CREATE_NO_WINDOW  # Prevents console window from briefly flashing
        )
        stdout, _ = process.communicate()  # Get output and wait for the process to finish
        return process.returncode, stdout
    except FileNotFoundError:
        print("Error: powershell.exe not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    # Example usage:
    # my_command = "Get-ChildItem -Path 'C:\\Users\\YourUser\\Desktop' | Where-Object {$_.Extension -eq '.txt'}"  # Example: List .txt files on Desktop
    # my_command = "New-Item -ItemType file -Path '$env:USERPROFILE\\Desktop\\test.txt' -Force"  # Example: Create a file on the Desktop
    my_command = "wsl --export Ubuntu-24.04 C:\\wsl-backups\\ubuntu24-bak.tar" # Replace with your actual command

    result = run_powershell_command(my_command)

    if result:
        return_code, output = result
        if return_code == 0:
            print("Command executed successfully.")
            # print("Output:\n", output)  # Uncomment to print the output
        else:
            print(f"Command failed with return code: {return_code}")
            print("Output:\n", output)  # Print the error output for debugging
    else:
        print("Failed to run the command.")
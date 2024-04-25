import shutil
import os
import paramiko
from datetime import datetime

def backup_directory(local_dir=None, remote_dir=None, remote_host=None, remote_port=22, remote_username=None, remote_password=None):
    # Check if any input is None, if yes, prompt the user for input
    if None in (local_dir, remote_dir, remote_host, remote_username, remote_password):
        local_dir = input("Enter the local directory path: ")
        remote_dir = input("Enter the remote directory path: ")
        remote_host = input("Enter the remote host IP address or hostname: ")
        remote_username = input("Enter the remote username: ")
        remote_password = input("Enter the remote password: ")

    # Create a timestamp for the backup
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Create a report file
    report_file = f"backup_report_{timestamp}.txt"
    with open(report_file, 'w') as report:
        try:
            # Create a zip file of the local directory
            backup_file = f"{local_dir}_backup_{timestamp}.zip"
            shutil.make_archive(backup_file, 'zip', local_dir)
            
            # Connect to the remote server
            transport = paramiko.Transport((remote_host, remote_port))
            transport.connect(username=remote_username, password=remote_password)
            sftp = paramiko.SFTPClient.from_transport(transport)
            
            # Upload the backup file to the remote server
            sftp.put(backup_file, os.path.join(remote_dir, os.path.basename(backup_file)))
            sftp.close()
            transport.close()
            
            # Write success message to the report file
            report.write(f"Backup successful: {backup_file} uploaded to {remote_dir}\n")
        except Exception as e:
            # Write error message to the report file
            report.write(f"Backup failed: {str(e)}\n")

# Example usage
backup_directory()

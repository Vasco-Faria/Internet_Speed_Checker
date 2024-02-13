import speedtest
import sys

def convert_bytes_to_human_readable(bytes, units=["B", "KB", "MB", "GB", "TB", "PB", "EB"]):
    i = 0
    while bytes >= 1024 and i < len(units) - 1:
        bytes /= 1024
        i += 1
    return f"{bytes:.2f} {units[i]}"

def print_progress_message(message):
    sys.stdout.write("\r" + message)
    sys.stdout.flush()

def print_message_after_completion(message):
    print("\n" + message)

print("Testing internet speed. Please wait...")
test = speedtest.Speedtest()

print("\n")
print_progress_message("Testing download speed...")
download_speed = test.download()
print_progress_message(" " * len("Testing download speed..."))  

print_progress_message("Testing upload speed...")
upload_speed = test.upload()

sys.stdout.write("\r" + " " * len("Testing upload speed...")+ "\r")
sys.stdout.flush()


download_speed_human_readable = convert_bytes_to_human_readable(download_speed)
upload_speed_human_readable = convert_bytes_to_human_readable(upload_speed)

print(f"Download Speed: {download_speed_human_readable}")
print(f"Upload Speed: {upload_speed_human_readable}")

print_message_after_completion("Speed test complete.")

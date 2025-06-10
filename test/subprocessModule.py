import subprocess

## Running a Simple Command...
subprocess.run(["ls", "-l"])

## Capturing Command Output...
result = subprocess.run(["echo", "Hello Samiran"], capture_output=True, text=True)
print(result.stdout)

## Getting Command Output Using subprocess.check_output...
output = subprocess.check_output(["echo", "Hello World!"], text=True)
print(output)

## Handling Errors (check=True)
try:
    subprocess.run(["ls", "non_existing_file"], check=True)
except subprocess.CalledProcessError:
    print("Command failed!")

## Running Commands in the Shell (shell=True)
subprocess.run("echo Shell Command Execution", shell=True)

## Running a Command and Redirecting Output to a File
with open("output.txt", "w") as file:
    subprocess.run(["echo", "Writing to a file"], stdout=file)

## Running Multiple Commands in Sequence
subprocess.run("mkdir test_dir && cd test_dir && touch test_file.txt", shell=True)


"""
    subprocess.run()	Runs a command and waits for it to finish
    subprocess.check_output()	Runs a command and returns the output
    subprocess.Popen()	Runs a command with more control
    shell=True	Runs the command in the system shell
    capture_output=True	Captures output of a command
    check=True	Raises an error if the command fails
"""
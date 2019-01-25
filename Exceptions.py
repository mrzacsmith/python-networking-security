__author__ = 'silverback'

# This is the file name you want to create
fileName = "someFile"

try:
    fhandle = open(fileName, "w")
    # write is the test to fill the test file
    fhandle.write("This is some data to dump into the file")
    print("Write some data to the file")

except IOError as e:
    print("Exception caught: Unable to write to " + fileName + " ", e)
except Exception as e:
    print("Another error occurred ", e)
else:
    print("File written to successful")
    fhandle.close()

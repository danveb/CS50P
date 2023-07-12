# Implement a Python program that promps the user for name of a file
# output the file's media type if file's name ends, case-insensitively, in any suffix
# .gif
# .jpg
# .jpeg
# .png
# .pdf
# .txt
# .zip
# if the file's name ends with other suffix or nothing at all, output "application/octet-stream" instead

def main():
    """Prompt user for name of file and output media type"""
    # prompt user for input
    user_input = input("File name: ")
    # return a new function checking user_input
    return check_mime(user_input)

# helper function check_mime
def check_mime(input):
    """Helper function to check MIME type on str"""
    # split the string on "." to return an array
    check = input.split(".")
    # use only last string from array and convert to lowercase, no spaces
    extension = check[-1].strip().lower()
    # print(extension) # gif
    # match "switch" statement for various outputs
    match extension:
        case "gif":
            print("image/gif")
        case "jpg":
            print("image/jpeg")
        case "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        # default case if no match?
        case _:
            print("application/octet-stream")

main()
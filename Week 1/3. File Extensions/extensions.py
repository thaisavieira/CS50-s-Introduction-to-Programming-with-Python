# a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes: .gif, .jpg, .jpeg, .png, .pdf, .txt, .zip.

def main():
    user_input = str(input('File name: ')).lower()
    file_media_types(user_input)

def file_media_types(user_input):
    if '.gif' in user_input:
        print('image/gif')
    elif '.jpg' in user_input:
        print('image/jpeg')
    elif '.jpeg' in user_input:
        print('image/jpeg')
    elif '.png' in user_input:
        print('image/png')
    elif '.pdf' in user_input:
        print('application/pdf')
    elif '.zip' in user_input:
         print('application/zip')
    elif '.txt' in user_input:
        print('text/plain')
    else:
        print ('application/octet-stream')
main()



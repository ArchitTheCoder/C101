import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    
    def upload_files(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from, "rb")
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = "3OIBRRyvLyIAAAAAAAAAAX3ujJwUfDLpbp9T4dEeL2P1Zc6ujAxEwVUvLSj5L4yJ"

    transferData = TransferData(access_token)
    file_from = "test.txt"
    file_to = "C:/Users/archi/Dropbox/Test/sample"
    
    transferData.upload_files(file_from, file_to)
    print("File has been moved")

main()
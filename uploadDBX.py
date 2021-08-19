import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self,access_token)

        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token='sl.A21R0DNNfJ00cPDnY1ZCGd24sOX1XYlQnd8_-6eAuhSpsIw82gYhUJ7fQtCBE7n_BPZYsGxcQyGQndvPm7rC7ROo8yjTu52GrCSV32HasnPMoiemA5qRBapQ-SaHQ8zgkbg6X6o'
    transferData=TransferData(access_token)

    file_from=input("Enter the file to be transferres: ")
    file_to=input("Enter the full path to upload to dropbox: ")

    transferData.upload_file(file_from,file_to)
    print("File has been removed")

main()
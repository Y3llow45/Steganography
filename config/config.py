# Window props
window_title = "Steganography"
# Window position
window_x = 500
window_y = 200
# Window dimesions
window_width = 500
window_height = 500

# Regex patterns - do not change file_pattern
file_pattern = r"^[a-zA-Z0-9][a-zA-Z0-9_\-. ]*\.(png)$"
# Do not allow symbols that are not here: `~!@#$%^&*()-_=+[{]}\|;:'",<.>/?
msg_pattern = r'^[A-Za-z0-9 !@#$?%^|&;:*()_=+\-`\'~"\\{}\[\]<>.,/]+$'
# don't match characters like: ╚╚Ї

# Needs to be changed in both pyqt.py and hideRead.py
READ_MODE = "R"
HIDE_MODE = "H"
IMAGE_DIRECTORY = 'img/'
# Can be changed but no recommended
LINK_STYLE = 'style/style.css'
# Errors and texts
SET_MODE_READ = "read"
SET_MODE_HIDE = "hide"
TXT_OPEN_IMAGE = "Open Image File"
TXT_OPEN_SECOND_IMAGE = "Open Second Image File"
ERR_UPLOAD = "Upload an image!"
ERR_OUTPUT_FILE = "Enter output file!"
ERR_EXIST = "File already exist!"
ERR_INVALID_FILE = "No symbols / only .png!"
ERR_MESSAGE = "Message is reqired!"
ERR_INVALID_MESSAGE = "Message contains illegal symbols!"
ERR_MESSAGE_LENGTH = "Message is too long!"

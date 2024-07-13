import os

# variables for files, images, videos and music
text_file_extensions_dict = {
    ".txt": "Plain text file",
    ".md": "Markdown file",
    ".rtf": "Rich Text Format",
    ".doc": "Microsoft Word document",
    ".docx": "Microsoft Word Open XML document",
    ".odt": "OpenDocument Text document",
    ".pdf": "Portable Document Format",
    ".tex": "LaTeX document",
    ".wpd": "WordPerfect document",
    ".wps": "Microsoft Works Word Processor document"
}

csv_excel_file_extensions_dict = {
    ".csv": "Comma-separated values file",
    ".xls": "Microsoft Excel spreadsheet (older format)",
    ".xlsx": "Microsoft Excel spreadsheet (Open XML format)",
    ".xlsm": "Microsoft Excel macro-enabled spreadsheet",
    ".ods": "OpenDocument Spreadsheet",
    ".xlt": "Microsoft Excel template (older format)",
    ".xltx": "Microsoft Excel template (Open XML format)",
    ".xltxm": "Microsoft Excel macro-enabled template",
    ".tsv": "Tab-separated values file"
}

image_file_extensions_dict = {
    ".jpg": "JPEG image",
    ".jpeg": "JPEG image",
    ".png": "Portable Network Graphics",
    ".gif": "Graphics Interchange Format",
    ".bmp": "Bitmap image",
    ".tiff": "Tagged Image File Format",
    ".tif": "Tagged Image File Format",
    ".svg": "Scalable Vector Graphics",
    ".webp": "WebP image",
    ".ico": "Icon file",
    ".raw": "RAW image data",
    ".heic": "High Efficiency Image Coding",
    ".heif": "High Efficiency Image File Format"
}

video_file_extensions_dict = {
    ".mp4": "MPEG-4 video file",
    ".avi": "Audio Video Interleave file",
    ".mov": "Apple QuickTime movie file",
    ".wmv": "Windows Media Video file",
    ".flv": "Flash Video file",
    ".mkv": "Matroska Video file",
    ".webm": "WebM video file",
    ".mpeg": "MPEG video file",
    ".mpg": "MPEG video file",
    ".m4v": "MPEG-4 video file",
    ".3gp": "3GPP multimedia file",
    ".3g2": "3GPP2 multimedia file",
    ".ogg": "Ogg video file",
    ".ogv": "Ogg video file",
    ".ts": "Video Transport Stream file",
    ".vob": "DVD Video Object file"
}

music_file_extensions_dict = {
    ".mp3": "MPEG Audio Layer III",
    ".wav": "Waveform Audio File Format",
    ".flac": "Free Lossless Audio Codec",
    ".aac": "Advanced Audio Coding",
    ".m4a": "MPEG-4 Audio",
    ".ogg": "Ogg Vorbis",
    ".wma": "Windows Media Audio",
    ".alac": "Apple Lossless Audio Codec",
    ".aiff": "Audio Interchange File Format",
    ".opus": "Opus audio",
    ".amr": "Adaptive Multi-Rate",
    ".mid": "MIDI audio file",
    ".midi": "MIDI audio file"
}


def count_dir(list_input, base_directory):  #takes a list of strings, and the base directory and counts the number of directories
    count = 0
    directories = []
    not_directories = []
    for each in list_input:
        if os.path.isdir(base_directory + each):
            directories.append(base_directory + each)
            count += 1
        else:
            not_directories.append(base_directory + each)

    print(f"\tDirectories ({count}):")
    for each in directories:
        print(f'\t\t{each}')
    # print(f"\tNOT Directories:")
    # for each in not_directories:
    #     print(f'\t\t{each}')
    return count, not_directories


def sort_files(list_input):
    # takes a list that contains the file names
    # and base directory and will sort it based on text,audio, video, data (Csv, excel), and other

    #initiate counter for stats
    count_text = 0
    count_data = 0
    count_video = 0
    count_image = 0
    count_audio = 0
    count_other = 0

    list_text_files = []
    list_data_files = []
    list_audio_files = []
    list_image_files = []
    list_video_files = []
    list_other_files = []

    for each in list_input:
        #find the index of the last period using rfind(), returns -1 if the '.' isn't found

        start_index = each.rfind(".")
        if start_index > 0:  #this means the index is found
            extension = each[start_index:].lower()  #this is a string that contains the extension of the file
            if text_file_extensions_dict.get(extension, 0) != 0:
                list_text_files.append(each)
                count_text += 1
            elif music_file_extensions_dict.get(extension, 0) != 0:
                list_audio_files.append(each)
                count_audio += 1
            elif video_file_extensions_dict.get(extension, 0) != 0:
                list_video_files.append(each)
                count_video += 1
            elif csv_excel_file_extensions_dict.get(extension, 0) != 0:
                list_data_files.append(each)
                count_data += 1
            elif image_file_extensions_dict.get(extension, 0) != 0:
                list_image_files.append(each)
                count_image += 1
            else:
                list_other_files.append(each)
                count_other += 1
        else:
            continue

    print(f"\tText Based Files ({count_text}):")
    for each in list_text_files:
        print(f'\t\t{each}')

    print(f"\tAudio Files ({count_audio}):")
    for each in list_audio_files:
        print(f'\t\t{each}')

    print(f"\tData Files ({count_data}):")
    for each in list_data_files:
        print(f'\t\t{each}')

    print(f"\tVideo Files ({count_video}):")
    for each in list_video_files:
        print(f'\t\t{each}')

    print(f"\tImage Files ({count_image}):")
    for each in list_image_files:
        print(f'\t\t{each}')

    print(f"\tOther Files ({count_other}):")
    for each in list_other_files:
        print(f'\t\t{each}')

    sorted_files = {
        "audio": {
            "count": count_audio,
            "content": list_audio_files
        },
        "video": {
            "count": count_video,
            "content": list_video_files
        },
        "text": {
            "count": count_text,
            "content": list_text_files
        },
        "image": {
            "count": count_image,
            "content": list_image_files
        },
        "data": {
            "count": count_data,
            "content": list_data_files
        },
        "other": {
            "count": count_other,
            "content": list_other_files
        }
    }

    return sorted_files

# def count_dat(list_input, base_directory):
#     count = 0
#     data_files = []
#     not_data_files = []
#     for each in list_input:
#         #find the index of the last period using rfind(), returns -1 if the '.' isn't found
#         start_index = each.rfind(".")
#         if start_index > 0:  #this means the index is found
#             extension = each[start_index:]  #this is a string that contains the extension of the file
#             if text_file_extensions_dict.get(extension, 0) != 0:
#                 text_files.append(base_directory + each)
#                 count += 1
#             else:
#                 not_text_files.append(base_directory + each)
#         else:
#             continue
#     print(f"\tText Based Files:")
#     for each in text_files:
#         print(f'\t\t{each}')
#     print(f"\tNOT Text Based Files:")
#     for each in not_text_files:
#         print(f'\t\t{each}')
#     return count, not_text_files

# def count_vid(list_input, base_directory):
#     pass
#
#
# def count_aud(list_input, base_directory):
#     pass

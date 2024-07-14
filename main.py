#Navigate a folder and it will sort out the files based on the line endings
import file_util
import os

tab = "-" * 4  #variable for showing hierarchy of the files


def main():
    #ask the user for input for the location of the directory they want to clean up
    dir_for_clean = input("Enter the directory that you'd like to be cleaned up: ")
    #dir_for_output = input("Enter the directory that you'd like to output the sorted files to: ")

    #check to see if the director is valid.
    while True:
        if not os.path.isdir(dir_for_clean):
            dir_for_clean = input(
                f"The directory to be cleaned,\"{dir_for_clean}\", is invalid. Please supply a correct directory: ")
        # elif not os.path.isdir(dir_for_output):
        #     dir_for_output = input(f"The directory for output,\"{dir_for_output}\" is invalid. Please supply a correct directory:")
        else:  #both directories are valid
            #preprocessing to add '\' if it's not there
            if dir_for_clean[-1] != "\\":
                dir_for_clean += "\\"

            # if dir_for_output[-1] != "\\":
            #     dir_for_output += "\\"
            print(f"Directory to be cleaned/sorted:\n{tab}{dir_for_clean}\n")
            #print(f"Directory for output: \t\t\t\t{dir_for_output}")
            break

    content_dir_clean = os.listdir(dir_for_clean)
    #content_dir_out = os.listdir(dir_for_output)

    #num_directories = the number of directories found in the folder
    #not_directories = the list of files in the directory to be cleaned (excluding directories)
    num_directories, directories, not_directories = file_util.count_dir(content_dir_clean, dir_for_clean)

    sorted_files = file_util.sort_files(not_directories)
    #sorted files returns a dictionary

    #list that contains all of the full paths of each of the file types
    list_audio_files = sorted_files["audio"]["content"]
    list_video_files = sorted_files["video"]["content"]
    list_text_files = sorted_files["text"]["content"]
    list_image_files = sorted_files["image"]["content"]
    list_data_files = sorted_files["data"]["content"]
    list_other_files = sorted_files["other"]["content"]

    #integer that tells the total number of each file type
    count_audio = sorted_files["audio"]["count"]
    count_video = sorted_files["video"]["count"]
    count_text = sorted_files["text"]["count"]
    count_image = sorted_files["image"]["count"]
    count_data = sorted_files["data"]["count"]
    count_other = sorted_files["other"]["count"]

    #get the sizes of the total files
    size_audio = file_util.get_total_file_size(list_audio_files)
    size_video = file_util.get_total_file_size(list_video_files)
    size_text = file_util.get_total_file_size(list_text_files)
    size_image = file_util.get_total_file_size(list_image_files)
    size_data = file_util.get_total_file_size(list_data_files)
    size_other = file_util.get_total_file_size(list_other_files)

    # print summary for all the types of files
    print(f"Summary for {dir_for_clean}:")
    print(f"{tab}Number of DIRECTORIES: {num_directories}")
    print(f"{tab}Number of TEXT files: {count_text}, total size: {size_text} MB")
    print(f"{tab}Number of AUDIO files: {count_audio}, total size: {size_audio} MB")
    print(f"{tab}Number of IMAGE files: {count_image}, total size: {size_image} MB")
    print(f"{tab}Number of VIDEO files: {count_video}, total size: {size_video} MB")
    print(f"{tab}Number of DATA (CSV, XLS, etc) files: {count_data}, total size: {size_data} MB")
    print(f"{tab}Number of other files: {count_other}, total size: {size_other} MB")
    print()

    #let the user choose which file type they want to clean up
    while True:  #keep this loop going until quit
        response = input(
    """Choose from the following options:
    - Type in the file type to see the files
    - Type 'clean' to move sort all these files and place them in their respective folders
    - Type 'summary' to view summary for all the file types
    - Type 'q' or 'quit' to exit the program
> """
        ).lower()

        if response in ['q', 'quit']:
            print("Exiting Program. Good Bye!")
            exit()
        elif response in ['dir', 'directory', 'directories']:
            choice = "Directory"  #normalize the response
            print(f"{tab}Directories ({num_directories}):")
            for each in directories:
                print(f'{tab * 2}{each}')
            print()
        elif response in ['txt', 'text']:
            choice = "Text"  # normalize the response
            print(f"{tab}Text Based Files ({sorted_files["text"]["count"]}):")
            for each in sorted_files["text"]["content"]:
                print(f'{tab * 2}{each}, {round((os.path.getsize(each) / 1000000), 2)} MB')
            print()
        elif response in ['vid', 'video']:
            choice = "Video"  # normalize the response
            print(f"{tab}Video Files ({sorted_files["video"]["count"]}):")
            for each in sorted_files["video"]["content"]:
                print(f'{tab * 2}{each}, {round(os.path.getsize(each) / 1000000, 2)} MB')
            print()
        elif response in ['aud', 'audio']:
            choice = "Audio"  # normalize the response
            print(f"{tab}Audio Files ({sorted_files["audio"]["count"]}):")
            for each in sorted_files["audio"]["content"]:
                print(f'{tab * 2}{each}, {round((os.path.getsize(each) / 1000000), 2)} MB')
            print()
        elif response in ['data', 'dat']:
            choice = "Data"  # normalize the response
            print(f"{tab}Data Files ({sorted_files["data"]["count"]}):")
            for each in sorted_files["data"]["content"]:
                print(f'{tab * 2}{each}, {round(os.path.getsize(each) / 1000000, 2)} MB')
            print()
        elif response in ['img', 'image']:
            choice = "Image"  # normalize the response
            print(f"{tab}Image Files ({sorted_files["image"]["count"]}):")
            for each in sorted_files["image"]["content"]:
                print(f'{tab * 2}{each}, {round(os.path.getsize(each) / 1000000, 2)} MB')
            print()
        elif response in ['other', 'otr']:
            choice = "Other"  # normalize the response
            print(f"{tab}Other Files ({sorted_files["other"]["count"]}):")
            for each in sorted_files["other"]["content"]:
                print(f'{tab * 2}{each}, {round(os.path.getsize(each) / 1000000, 2)} MB')
            print()
        elif response == 'summary':
            # print summary for all the types of files
            print(f"Summary for {dir_for_clean}:")
            print(f"{tab}Number of DIRECTORIES: {num_directories}")
            print(f"{tab}Number of TEXT files: {count_text}, total size: {size_text} MB")
            print(f"{tab}Number of AUDIO files: {count_audio}, total size: {size_audio} MB")
            print(f"{tab}Number of IMAGE files: {count_image}, total size: {size_image} MB")
            print(f"{tab}Number of VIDEO files: {count_video}, total size: {size_video} MB")
            print(f"{tab}Number of DATA (CSV, XLS, etc) files: {count_data}, total size: {size_data} MB")
            print(f"{tab}Number of other files: {count_other}, total size: {size_other} MB")
            print()
        elif response == 'clean':
            #make directories for each of the type of files that have sizes
            print(f"Work in progress...")
        else:
            print("Invalid response. Try again.\n")

main()

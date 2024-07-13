#Navigate a folder and it will sort out the files based on the line endings
import file_util
import os

def main():

    #ask the user for input for the location of the directory they want to clean up
    dir_for_clean = input("Enter the directory that you'd like to be cleaned up: ")
    #dir_for_output = input("Enter the directory that you'd like to output the sorted files to: ")

        #check to see if the director is valid.
    while True:
        if not os.path.isdir(dir_for_clean):
            dir_for_clean = input(f"The directory to be cleaned,\"{dir_for_clean}\", is invalid. Please supply a correct directory: ")
        # elif not os.path.isdir(dir_for_output):
        #     dir_for_output = input(f"The directory for output,\"{dir_for_output}\" is invalid. Please supply a correct directory:")
        else:#both directories are valid
            print()
            #preprocessing to add '\' if it's not there
            if dir_for_clean[-1] != "\\":
                dir_for_clean += "\\"

            # if dir_for_output[-1] != "\\":
            #     dir_for_output += "\\"
            print(f"Directory to be cleaned/sorted: \t\t{dir_for_clean}")
            #print(f"Directory for output: \t\t\t\t{dir_for_output}")
            break

    print("Continuing with the program....\n")
    content_dir_clean = os.listdir(dir_for_clean)
    #content_dir_out = os.listdir(dir_for_output)


    #show the contents of the directories
    print(f'Contents of the directory to be cleaned ({dir_for_clean}):')
    for each in content_dir_clean:
        print(f"\t{each}")
    print()
    # print(f'Contents of the directory for output ({dir_for_output}):')
    # for each in content_dir_out:
    #     print(f"\t{each}")
    # print()
    #num_directories = the number of directories found in the folder
    #not_directories = the list of files in the directory to be cleaned (excluding directories)
    num_directories, not_directories = file_util.count_dir(content_dir_clean, dir_for_clean)

    #call on the sorting function
    sorted_files = file_util.sort_files(not_directories)
    count_audio = sorted_files["audio"]["count"]
    count_video = sorted_files["video"]["count"]
    count_text = sorted_files["text"]["count"]
    count_image = sorted_files["image"]["count"]
    count_data = sorted_files["data"]["count"]
    count_other = sorted_files["other"]["count"]

    print()
    print(f"Summary for {dir_for_clean}:")
    print(f"\tNumber of directories: ", num_directories)
    print(f"\tNumber of text files: ", count_text)
    print(f"\tNumber of audio files: ", count_audio)
    print(f"\tNumber of video files: ", count_video)
    print(f"\tNumber of data files: ", count_data)
    print(f"\tNumber of other files: ", count_other)

    #function that takes a list of strings and will return an integer of the number of files

    #blue color for directories

    #copy the files and sort it first as beta testing
main()
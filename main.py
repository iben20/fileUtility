#Navigate a folder and it will sort out the files based on the line endings
import file_util
import os

tab = "-" * 4  #variable for showing hierarchy of the files


def main():
    #ask the user for input for the location of the directory they want to clean up
    dir_for_clean = input("Enter the directory that you'd like to be cleaned up: ")

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

    # let the user choose which file type they want to clean up
    while True:  # keep this loop going until quit
        content_dir_clean = os.listdir(dir_for_clean)
        # content_dir_out = os.listdir(dir_for_output)
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

        response = input(
            """Choose from the following options:
- Type 'summary' to view summary for all the file types
- Type in the file type (ex, 'AUDIO') to see the files
- Type 'clean' to move all these files and place them in their respective folders
- Type 'q' or 'quit' to exit the program
> """
        ).lower()
        # # print summary for all the types of files
        # print(f"Summary for {dir_for_clean}:")
        # print(f"{tab}Number of DIRECTORIES: {num_directories}")
        # print(f"{tab}Number of TEXT files: {count_text}, total size: {size_text} MB")
        # print(f"{tab}Number of AUDIO files: {count_audio}, total size: {size_audio} MB")
        # print(f"{tab}Number of IMAGE files: {count_image}, total size: {size_image} MB")
        # print(f"{tab}Number of VIDEO files: {count_video}, total size: {size_video} MB")
        # print(f"{tab}Number of DATA (CSV, XLS, etc) files: {count_data}, total size: {size_data} MB")
        # print(f"{tab}Number of other files: {count_other}, total size: {size_other} MB")
        # print()
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
            var_data = 'data'
            var_image = 'image'
            var_audio = 'audio'
            var_video = 'video'
            var_text = 'text'
            var_other = 'other'
            folder_iterator = 0  #use this to append to a folder

            #check and see which directories to make based on the count of the files
            if count_audio > 0:
                #check if the folder is already created using os.path.exists(dir_for_clean+var_audio)
                folder_append = 1  # this is to append to the folder if one is already created
                if os.path.exists(dir_for_clean + var_audio.upper()):
                    r = input(f'Folder {var_audio.upper()} exists.\nMove files into the existing {var_audio.upper()} or create a new folder (\'existing\'/\'new\')? ').lower()

                    if r in ['existing', 'e']:  #user would like to merge the folder
                        print(f'Moving {var_audio} files into current {var_audio.upper()} folder.')
                        for each_file in sorted_files[var_audio]["content"]:
                            insert_index = each_file.rfind("\\")
                            each_file_move = each_file[:insert_index] + "\\" + var_audio.upper() + each_file[
                                                                                                   insert_index:]
                            print(f"Moving {each_file} to {var_audio.upper()} folder...")
                            os.replace(each_file, each_file_move) #moving the actual files

                    elif r in ['new','n']:
                        while True:
                            if os.path.exists(dir_for_clean + var_audio.upper() + str(folder_append)):
                                #folder exists, so continue and up folder_append
                                folder_append += 1
                            else:
                                #at this point, the folder should not exist and can be created
                                print(f"Creating a new directory called {var_audio.upper() + str(folder_append)}...")
                                new_folder = dir_for_clean + var_audio.upper() + str(folder_append)
                                os.mkdir(new_folder)
                                break #exit the loop

                        for each_file in sorted_files[var_audio]["content"]:
                            insert_index = each_file.rfind("\\")
                            each_file_move = each_file[:insert_index] + "\\" + var_audio.upper() + str(folder_append) + each_file[
                                                                                                   insert_index:]
                            print(f"Moving {each_file} to {new_folder} folder...")
                            os.replace(each_file, each_file_move) #moving the actual files
                    else:
                        print(f"Invalid response. Try again. ")

                else:
                    print(f'Moving {var_audio} files into current {var_audio.upper()} folder.')
                    for each_file in sorted_files[var_audio]["content"]:
                        insert_index = each_file.rfind("\\")
                        each_file_move = each_file[:insert_index] + "\\" + var_audio.upper() + each_file[
                                                                                               insert_index:]
                        print(f"Moving {each_file} to {var_audio.upper} folder...")
                        os.replace(each_file, each_file_move)  # moving the actual files

            if count_data > 0:
                # check if the folder is already created using os.path.exists(dir_for_clean+var_data)
                folder_append = 1  # this is to append to the folder if one is already created
                if os.path.exists(dir_for_clean + var_data.upper()):
                    r = input(
                        f'Folder {var_data.upper()} exists.\nMove files into the existing {var_data.upper()} or create a new folder (\'existing\'/\'new\')? ').lower()

                    if r in ['existing', 'e']:  # user would like to merge the folder
                        print(f'Moving {var_data} files into current {var_data.upper()} folder.')
                        for each_file in sorted_files[var_data]["content"]:
                            insert_index = each_file.rfind("\\")
                            each_file_move = each_file[:insert_index] + "\\" + var_data.upper() + each_file[
                                                                                                   insert_index:]
                            print(f"Moving {each_file} to {var_data.upper()} folder...")
                            os.replace(each_file, each_file_move)  # moving the actual files

                    elif r in ['new', 'n']:
                        while True:
                            if os.path.exists(dir_for_clean + var_data.upper() + str(folder_append)):
                                # folder exists, so continue and up folder_append
                                folder_append += 1
                            else:
                                # at this point, the folder should not exist and can be created
                                print(f"Creating a new directory called {var_data.upper() + str(folder_append)}...")
                                new_folder = dir_for_clean + var_data.upper() + str(folder_append)
                                os.mkdir(new_folder)
                                break  # exit the loop

                        for each_file in sorted_files[var_data]["content"]:
                            insert_index = each_file.rfind("\\")
                            each_file_move = each_file[:insert_index] + "\\" + var_data.upper() + str(
                                folder_append) + each_file[
                                                 insert_index:]
                            print(f"Moving {each_file} to {new_folder} folder...")
                            os.replace(each_file, each_file_move)  # moving the actual files
                    else:
                        print(f"Invalid response. Try again. ")

                else:
                    print(f'Moving {var_data} files into current {var_data.upper()} folder.')
                    for each_file in sorted_files[var_data]["content"]:
                        insert_index = each_file.rfind("\\")
                        each_file_move = each_file[:insert_index] + "\\" + var_data.upper() + each_file[
                                                                                               insert_index:]
                        print(f"Moving {each_file} to {var_data.upper()} folder...")
                        os.replace(each_file, each_file_move)  # moving the actual files

            if count_video > 0:
                # check if the folder is already created using os.path.exists(dir_for_clean+var_video)
                folder_append = 1  # this is to append to the folder if one is already created
                if os.path.exists(dir_for_clean + var_video.upper()):
                    r = input(
                        f'Folder {var_video.upper()} exists.\nMove files into the existing {var_video.upper()} or create a new folder (\'existing\'/\'new\')? ').lower()

                    if r in ['existing', 'e']:  # user would like to merge the folder
                        print(f'Moving {var_video} files into current {var_video.upper()} folder.')
                        for each_file in sorted_files[var_video]["content"]:
                            insert_index = each_file.rfind("\\")
                            each_file_move = each_file[:insert_index] + "\\" + var_video.upper() + each_file[
                                                                                                   insert_index:]
                            print(f"Moving {each_file} to {var_video.upper()} folder...")
                            os.replace(each_file, each_file_move)  # moving the actual files

                    elif r in ['new', 'n']:
                        while True:
                            if os.path.exists(dir_for_clean + var_video.upper() + str(folder_append)):
                                # folder exists, so continue and up folder_append
                                folder_append += 1
                            else:
                                # at this point, the folder should not exist and can be created
                                print(f"Creating a new directory called {var_video.upper() + str(folder_append)}...")
                                new_folder = dir_for_clean + var_video.upper() + str(folder_append)
                                os.mkdir(new_folder)
                                break  # exit the loop

                        for each_file in sorted_files[var_video]["content"]:
                            insert_index = each_file.rfind("\\")
                            each_file_move = each_file[:insert_index] + "\\" + var_video.upper() + str(
                                folder_append) + each_file[
                                                 insert_index:]
                            print(f"Moving {each_file} to {new_folder} folder...")
                            os.replace(each_file, each_file_move)  # moving the actual files
                    else:
                        print(f"Invalid response. Try again. ")

                else:
                    print(f'Moving {var_video} files into current {var_video.upper()} folder.')
                    for each_file in sorted_files[var_video]["content"]:
                        insert_index = each_file.rfind("\\")
                        each_file_move = each_file[:insert_index] + "\\" + var_video.upper() + each_file[
                                                                                               insert_index:]
                        print(f"Moving {each_file} to {var_video.upper()} folder...")
                        os.replace(each_file, each_file_move)  # moving the actual files

            if count_text > 0:
                # check if the folder is already created using os.path.exists(dir_for_clean+var_text)
                folder_append = 1  # this is to append to the folder if one is already created
                if os.path.exists(dir_for_clean + var_text.upper()):
                    r = input(
                        f'Folder {var_text.upper()} exists.\nMove files into the existing {var_text.upper()} or create a new folder (\'existing\'/\'new\')? ').lower()

                    if r in ['existing', 'e']:  # user would like to merge the folder
                        print(f'Moving {var_text} files into current {var_text.upper()} folder.')
                        for each_file in sorted_files[var_text]["content"]:
                            insert_index = each_file.rfind("\\")
                            each_file_move = each_file[:insert_index] + "\\" + var_text.upper() + each_file[
                                                                                                   insert_index:]
                            print(f"Moving {each_file} to {var_text.upper()} folder...")
                            os.replace(each_file, each_file_move)  # moving the actual files

                    elif r in ['new', 'n']:
                        while True:
                            if os.path.exists(dir_for_clean + var_text.upper() + str(folder_append)):
                                # folder exists, so continue and up folder_append
                                folder_append += 1
                            else:
                                # at this point, the folder should not exist and can be created
                                print(f"Creating a new directory called {var_text.upper() + str(folder_append)}...")
                                new_folder = dir_for_clean + var_text.upper() + str(folder_append)
                                os.mkdir(new_folder)
                                break  # exit the loop

                        for each_file in sorted_files[var_text]["content"]:
                            insert_index = each_file.rfind("\\")
                            each_file_move = each_file[:insert_index] + "\\" + var_text.upper() + str(
                                folder_append) + each_file[
                                                 insert_index:]
                            print(f"Moving {each_file} to {new_folder} folder...")
                            os.replace(each_file, each_file_move)  # moving the actual files
                    else:
                        print(f"Invalid response. Try again. ")

                else:
                    print(f'Moving {var_text} files into current {var_text.upper()} folder.')
                    for each_file in sorted_files[var_text]["content"]:
                        insert_index = each_file.rfind("\\")
                        each_file_move = each_file[:insert_index] + "\\" + var_text.upper() + each_file[
                                                                                               insert_index:]
                        print(f"Moving {each_file} to {var_text.upper()} folder...")
                        os.replace(each_file, each_file_move)  # moving the actual files

            if count_other > 0:
                # check if the folder is already created using os.path.exists(dir_for_clean+var_other)
                folder_append = 1  # this is to append to the folder if one is already created
                if os.path.exists(dir_for_clean + var_other.upper()):
                    r = input(
                        f'Folder {var_other.upper()} exists.\nMove files into the existing {var_other.upper()} or create a new folder (\'existing\'/\'new\')? ').lower()

                    if r in ['existing', 'e']:  # user would like to merge the folder
                        print(f'Moving {var_other} files into current {var_other.upper()} folder.')
                        for each_file in sorted_files[var_other]["content"]:
                            insert_index = each_file.rfind("\\")
                            each_file_move = each_file[:insert_index] + "\\" + var_other.upper() + each_file[
                                                                                                   insert_index:]
                            print(f"Moving {each_file} to {var_other.upper()} folder...")
                            os.replace(each_file, each_file_move)  # moving the actual files

                    elif r in ['new', 'n']:
                        while True:
                            if os.path.exists(dir_for_clean + var_other.upper() + str(folder_append)):
                                # folder exists, so continue and up folder_append
                                folder_append += 1
                            else:
                                # at this point, the folder should not exist and can be created
                                print(f"Creating a new directory called {var_other.upper() + str(folder_append)}...")
                                new_folder = dir_for_clean + var_other.upper() + str(folder_append)
                                os.mkdir(new_folder)
                                break  # exit the loop

                        for each_file in sorted_files[var_other]["content"]:
                            insert_index = each_file.rfind("\\")
                            each_file_move = each_file[:insert_index] + "\\" + var_other.upper() + str(
                                folder_append) + each_file[
                                                 insert_index:]
                            print(f"Moving {each_file} to {new_folder} folder...")
                            os.replace(each_file, each_file_move)  # moving the actual files
                    else:
                        print(f"Invalid response. Try again. ")

                else:
                    print(f'Moving {var_other} files into current {var_other.upper()} folder.')
                    for each_file in sorted_files[var_other]["content"]:
                        insert_index = each_file.rfind("\\")
                        each_file_move = each_file[:insert_index] + "\\" + var_other.upper() + each_file[
                                                                                               insert_index:]
                        print(f"Moving {each_file} to {var_other.upper()} folder...")
                        os.replace(each_file, each_file_move)  # moving the actual files

            if count_image > 0:
                # check if the folder is already created using os.path.exists(dir_for_clean+var_image)
                folder_append = 1  # this is to append to the folder if one is already created
                if os.path.exists(dir_for_clean + var_image.upper()):
                    r = input(
                        f'Folder {var_image.upper()} exists.\nMove files into the existing {var_image.upper()} or create a new folder (\'existing\'/\'new\')? ').lower()

                    if r in ['existing', 'e']:  # user would like to merge the folder
                        print(f'Moving {var_image} files into current {var_image.upper()} folder.')
                        for each_file in sorted_files[var_image]["content"]:
                            insert_index = each_file.rfind("\\")
                            each_file_move = each_file[:insert_index] + "\\" + var_image.upper() + each_file[
                                                                                                   insert_index:]
                            print(f"Moving {each_file} to {var_image.upper()} folder...")
                            os.replace(each_file, each_file_move)  # moving the actual files

                    elif r in ['new', 'n']:
                        while True:
                            if os.path.exists(dir_for_clean + var_image.upper() + str(folder_append)):
                                # folder exists, so continue and up folder_append
                                folder_append += 1
                            else:
                                # at this point, the folder should not exist and can be created
                                print(f"Creating a new directory called {var_image.upper() + str(folder_append)}...")
                                new_folder = dir_for_clean + var_image.upper() + str(folder_append)
                                os.mkdir(new_folder)
                                break  # exit the loop

                        for each_file in sorted_files[var_image]["content"]:
                            insert_index = each_file.rfind("\\")
                            each_file_move = each_file[:insert_index] + "\\" + var_image.upper() + str(
                                folder_append) + each_file[
                                                 insert_index:]
                            print(f"Moving {each_file} to {new_folder} folder...")
                            os.replace(each_file, each_file_move)  # moving the actual files
                    else:
                        print(f"Invalid response. Try again. ")

                else:
                    print(f'Moving {var_image} files into current {var_image.upper()} folder.')
                    for each_file in sorted_files[var_image]["content"]:
                        insert_index = each_file.rfind("\\")
                        each_file_move = each_file[:insert_index] + "\\" + var_image.upper() + each_file[
                                                                                               insert_index:]
                        print(f"Moving {each_file} to {var_image.upper()} folder...")
                        os.replace(each_file, each_file_move)  # moving the actual files

            print("\nCleaning complete!\n")

        else:
            print("Invalid response. Try again.\n")


main()  #run program

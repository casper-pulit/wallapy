from PIL import Image
import os


def splitAndSave(path):
    with Image.open(path) as im:
        left_tuple = [0, 0, im.width / 2, im.height]
        right_tuple = [im.width / 2, 0, im.width, im.height]
        im.crop(box=left_tuple).save(f"l_{path}")
        im.crop(box=right_tuple).save(f"r_{path}")
        if delete_source :
            os.remove(path)

class InvalidInput(Exception) :
    pass

def main():
    dir_path = "/home/casper/Pictures/wallpapers/"
    print(dir_path)
    delete_source = True

    while True:
        if delete_source :
            try :
                confirm = input("You've selected to remove source files after processing, enter Y to proceed, N to cancel:\n\n")
                if confirm.lower() != "y" and confirm.lower() != "n" :
                    raise InvalidInput
            except InvalidInput:
                print(f"Invalid Input: {confirm}. Please enter Y or N to proceed.")
                continue
            else :
                if confirm.lower() == "n" :
                    print("Exiting...")
                    exit()
                elif confirm.lower() == "y" :
                    break

            


    for file in os.listdir(dir_path):
        print(dir_path + file)
        print(f"{dir_path}L_{file}")
        print(f"{dir_path}R_{file}")
        
        if delete_source :
            print(dir_path + file + " Deleted")
            #os.remove(dir_path + file)
        else :
            print(dir_path + file + " Not Deleted")

    #splitAndSave(path + file)

    print("Hello World")

if __name__ == "__main__":
    main()

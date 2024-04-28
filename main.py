import os
from tqdm import tqdm
import click
from src.Exceptions import InvalidInput
from src.Utils import splitAndSave


@click.command()
@click.argument("dir_path")
@click.option(
    "-v/-q",
    "--verbose/--quiet",
    default=False,
    help="""
        -v, --verbose: Prints additional information during script execution

        -q, --queit: Displays progress bar only

        default = -q, --quiet

        """,
)
@click.option(
    "-d/-k",
    "--delete/--keep",
    default=False,
    help=""""-d, --delete: Deletes source files after processing complete
    
    -k, --keep: Keeps source files
    
    default = -k, --keep""",
)
@click.option(
    "-o",
    "--output_dir",
    default=None,
    help="""
    -o, --output_dir: Specifies output directory for processed images.
    If the directory does not exist the script will try to create it.                 
    
    default: None, same as input directory""",
)
def wallapy(dir_path, verbose, delete, output_dir):
    while True:
        if delete:
            try:
                confirm = input(
                    "You've selected to remove source files after processing, enter Y to proceed, N to cancel:\n\n"
                )
                if confirm.lower() != "y" and confirm.lower() != "n":
                    raise InvalidInput
            except InvalidInput:
                print(f"Invalid Input: {confirm}. Please enter Y or N to proceed.")
                continue
            else:
                if confirm.lower() == "n":
                    print("Exiting...")
                    exit()
                elif confirm.lower() == "y":
                    break
        else:
            break

    # Clean this up later... 
    # Check if file passed

    if os.path.isdir(dir_path) :
    # Get dir information
        file_list = []
        for file in os.listdir(dir_path):
            if os.path.isfile(f"{dir_path}/{file}"):
                file_list.append(f"{dir_path}/{file}")

        for file in tqdm(os.listdir(dir_path)):
            if os.path.isfile(f"{dir_path}/{file}"):
                if verbose:
                    click.echo(f"Processing {dir_path}{file}")

                splitAndSave(filename=file, path=dir_path, output_dir=output_dir)

                if delete:
                    if verbose:
                        click.echo(f"{dir_path}/{file} Deleted")
                    os.remove(f"{dir_path}/{file}")
    else:
        click.echo("Please pass a directory")
        exit()


if __name__ == "__main__":
    wallapy()

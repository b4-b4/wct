#!/usr/bin/env python3

import time, argparse, os

from src.module.explorer import Explorer
from src.colors import bcolors


if __name__ == "__main__":

    # COMMAND MODEL: python /path/to/wct.py <path> (<pattern> | <regex>) [-d | --delete]

    # Parser
    parser = argparse.ArgumentParser(prog="wct", description="Search and Moderation Wizard for the Computer Tree")
    parser.add_argument("path", type=str, help="Corresponds to the path where the search should start")
    parser.add_argument("pattern", type=str, help="the pattern to search for")

    # Options group
    options_group = parser.add_mutually_exclusive_group()
    options_group.add_argument("-d","--delete", action="store_true", help="Allows deletion at the end of the search"
                                                                          "(after confirmation)")

    args = parser.parse_args()

    if args:
        path = args.path
        pattern = args.pattern
        explorer = Explorer()

        # starts count
        start_time = time.time()

        explorer.explorer(path, pattern)
        print(f"\n{explorer.get_statistics()}")
        
        for item in explorer.get_target_paths():
            sliced_item = item.split("/")
            last_elem = bcolors.GREEN + sliced_item[-1] + bcolors.RESET
            sliced_item[-1] = last_elem
            complete_item = '/'.join(sliced_item)

            if args.delete:
                target_paths = explorer.get_target_paths()
                print(f"{target_paths.index(item)} | {complete_item}")
            else:
                print(f"| {complete_item}")
        
        # displays the execution time
        print(f"\n[   {time.time() - start_time} seconds   ]")

        try:
            target_paths
        except:
            quit(bcolors.print_red("Nothing to delete."))

        if args.delete:
            saved = input(f"""{bcolors.YELLOW}
Using the index, write the individual items you do not want to delete separated by commas.
Otherwise, enter <DE> to delete everything or <Enter> to exit.
>  {bcolors.RESET}""")

            if saved == "":
                quit()

            else:
                try:
                    saved_list = [saved]
                    saved_list = saved_list[0]
                    sliced_saved_list = saved_list.split(",")

                    for i in sliced_saved_list:
                        if i == "":
                            sliced_saved_list.remove(i)

                    for i in target_paths:

                        if str(target_paths.index(i)) not in sliced_saved_list:
                            try:
                                if os.path.isdir(i):
                                    os.rmdir(i)
                                    print(f"'{i}' has been removed (dir)")

                                elif os.path.isfile(i):
                                    os.remove(i)
                                    print(f"'{i}' has been removed (file)")

                            except Exception as ex:
                                print(bcolors.print_yellow(ex))

                            except OSError as ose:
                                print(bcolors.print_yellow(ose))

                except Exception as ex:
                    quit(bcolors.print_red(ex))

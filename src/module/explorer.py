import pathlib


def explorer(target: str):
    target_path = []
    visited_path = []
    starting_path = pathlib.Path()
    current_folder = pathlib.Path()

    while True:

        for item in current_folder.iterdir():
            print(f"\n[ITEM] : {item}")

            if (current_folder / item).is_dir():
                print(f"[is folder] : {current_folder / item}")
                ending = "/"
            elif (current_folder / item).is_file():
                print(f"[is file] : {current_folder / item}")
                ending = ""
            else:
                print("[Error]")

            item_path = (current_folder / item).absolute()
            print(f"[ITEM PATH] : {item_path}")


            # DEBUG: Target Path
            print(f"[TARGET PATH] : {len(target_path)} ->")
            for i in target_path:
                print(f"    > {i}")
            
            # DEBUG: Visited Path
            print(f"[VISITED PATH] : {len(visited_path)} ->")
            for i in visited_path:
                print(f"    > {i}")
            print("\n")

            # The target is part of the item and has not yet been found
            if target in item and item_path not in target_path:
                target_path.append(item_path)
                print(f"[+GREAT] : {item_path}")
            

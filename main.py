from vid_splitter import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Enter file path : ")
    path = str(input())
    print("\nEnter length of the video(=2) : ")
    seconds = int(input())
    print("\nEnter type of movement : ")
    print("\n ========= Writhing Movements ==========")
    print("\n01. Normal writhing => normal_writhing")
    print("\n02. Poor Repertoire => poor_repertoire")
    print("\n03. Cramped Synchronised => cramped_synchronised")
    print("\n04. Chaotic GM's => chaotic_gm")
    print("\n ========= Fidgety Movements ==========")
    print("\n05. Normal Fidgety => normal_fidgety")
    print("\n06. Abnormal Fidgety => abnormal_fidgety")
    type_of_movements = str(input())
    print("\nEnter batch number : ")
    print("\nAnushanga => 100..")
    print("\nRumali => 200..")
    print("\nHansamal => 300..\n")
    batch = int(input())

    vid_splitter(path, seconds, type_of_movements, batch)


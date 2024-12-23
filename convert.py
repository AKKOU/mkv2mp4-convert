import ffmpeg
import os

folderpath = '../ue5_movie2/'

def convertfile(input_file):
    try:
        output_name = input_file.replace(".mkv",".mp4")
        ffmpeg.input(folderpath + input_file).output(folderpath + 'mp4/' + output_name,vcodec='copy',acodec='copy').run()
        print(f"轉換完畢 - {input_file}")
    except:
        print(f"轉換失敗 - {input_file}")

for i in os.listdir(folderpath):
    if(i.endswith('.mkv')):
        convertfile(i)

a = input("轉換完畢 輸入任何鍵結束....")
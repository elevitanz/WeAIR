from moviepy.editor import ImageSequenceClip
import os

def main():
    input_directory = 'plot/tot_multiframe/'
    output_directory = 'plot/tot_video/'
    days = ['22_01', '24_01', '25_01', '26_01', '28_01', '01_02', '04_02', '05_02', '07_02']
    #colonne = ['AMBH', 'AMBP', 'CO', 'NO2', 'CO2', 'MASS_PM10']
    #colonne = ['AMBT', 'AMBH', 'AMBP', 'CO', 'NO2', 'CO2', 'MASS_PM10']
    colonne = ['AMBP']
    frame_files = sorted(os.listdir(input_directory))[1:]

    for colonna in colonne:
        tot_frames = []
        for d in days:
            frames = []
            for filename in frame_files:
                if d in filename and colonna in filename:
                    filepath = os.path.join(input_directory, filename)
                    frames.append(filepath)
            tot_frames += frames
        output_video_path = os.path.join(output_directory, f'{colonna}_video.mp4')
        clip = ImageSequenceClip(tot_frames, fps=0.9)
        clip.write_videofile(output_video_path)

if __name__ == "__main__":
    main()

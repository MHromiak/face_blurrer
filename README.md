# Face blurrer


A short project to get myself familiar with basic computer vision models and techniques. Faces are recognized and blurred from
livestreamed video, prerecorded video, and single images. 

Included models are pretrained and provided from the opencv git repository at https://github.com/opencv/opencv/tree/master/data/haarcascades



## Example Command Prompts

- `python main.py`                
    runs livestream face blurring

- `python main.py -h`             
    prints usage help

- `python main.py -video $path`   
    blurs video at specified path

- `python main.py -image $path`   
    blurs image at specified path

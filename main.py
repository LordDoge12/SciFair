import cv2
from src.yolov3.detection import GunDetection, ClothesDetection
from src.yolov3.arduinoBoard import sendP
def find_guy(gun_detection,cameras):
        for i in gun_detection.run_detection(cameras):
            #print(f'{i}')
            if 1 in list(i.values()):
                for key, value in i.items():
                    if value == 1:
                        print(f'Gunman in {key}')
            else:
                print('No Gunman found')

            #sendP(i)
            #if type(i) != int:
            #   break
def main():
    weight_path_gun = 'model/darknetGun.weights'
    config_path_gun = 'gun.cfg'
    cam1 = cv2.VideoCapture(0)
    cam2 = cv2.VideoCapture(1)
    #cam3 = cv2.VideoCapture(2)
    cameras = [
        (cam1, "Zone 1"), (cam2, 'Zone 2')
    ]
    
    gun_detection = GunDetection(weight_path_gun, config_path_gun)
    find_guy(gun_detection,cameras)
    

    
    clothes_detection = ClothesDetection(len(cameras))
    clothes_detection.run_detection(cameras)
    next_gun_detection = GunDetection(weight_path_gun, config_path_gun)
    while True:
        find_guy(next_gun_detection,cameras)
if __name__ == "__main__":
    main()

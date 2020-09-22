# Automatic-Number-Plate-Recognition-Using-K-NN-Algorithm-on-Raspberry-Pi-4
Automatic number plate recognition for indonesian plate (white on black)

## Method:
Vehicle detection using the Viola-Jones Algorithm, determining the location of the number plate using the contour of the license plate and number plate recognition using the K-NN algorithm.

## Prerequest
- python==3.6
- opencv-python==4.1.1.26
- numpy==1.17.3<br>
or install using<br>
`pip install -r requirements.txt`

## How to run (Linux):
- Image<br>
  `python DETECT2.py
- Video<br>
  `python detectvd.py

## Retrain
Retrain process will update classifications.txt and flattened_images.txt files<br>
`python GenData.py -d = <train_image>`<br>
example : <br>
`python GenData.py -d = train_image/train2.png`<br>
note: *Just input base on marked object one by one and press esc to exit the training process*

### Check the model
`python TrainAndTestData.py -d = train_image/train2.png`

### Result
![vlcsnap-2020-09-10-10h12m08s321](https://user-images.githubusercontent.com/26915668/93845632-c0b6fd80-fccb-11ea-8275-08d1cc20fff6.png)

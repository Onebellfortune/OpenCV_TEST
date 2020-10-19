import cv2
import numpy as np

def cross_correlation_1d(img,kernel):
    row,column=img.shape # 이미지의 row column 크기 저장
    kernel_row,kernel_column=kernel.shape
    if kernel_row>kernel_column:
        big=kernel_row
    else:
        big=kernel_column
    filtered_img=np.array(img) # 필터링 저장 이미지 초기화
    imgarr=np.zeros((row+big-1,column+big-1),dtype=int)

    if kernel.shape[0]==1: # column 벡터일경우
        for i in range(0, int(kernel_column/2)):                                           # 위아래왼오 채우기
            imgarr[i, int(kernel_column / 2):column + int(kernel_column / 2)] = img[0,0:column]
        for j in range(0, int(kernel_column / 2)):
            imgarr[int(kernel_column / 2):row + int(kernel_column / 2), j] = img[0:row, 0]
        for i in range(0, int(kernel_column / 2)):
            imgarr[row + int(kernel_column / 2) + i, int(kernel_column / 2):column + int(kernel_column / 2)] = img[row - 1,0:column]
        for j in range(0, int(kernel_column / 2)):
            imgarr[int(kernel_column / 2):row + int(kernel_column / 2), column +int(kernel_column/2)+ j] = img[0:row, column - 1]

        for i in range(0,int(kernel_column/2)): #끝에 채우기
            imgarr[0:i+int(kernel_column/2),0:i+int(kernel_column/2)]=img[0,0]
        for i in range(0, int(kernel_column/2)):
            imgarr[0:i+int(kernel_column/2),column+int(kernel_column/2):column+kernel_column-1]=img[0,column-1]
        for i in range(0, int(kernel_column/2) ):
            imgarr[row+int(kernel_column/2):row+kernel_column-1,0:i+int(kernel_column/2)] = img[row-1, 0]
        for i in range(0, int(kernel_column/2)):
            imgarr[row+int(kernel_column/2):row+kernel_column-1,row+int(kernel_column/2):row+kernel_column-1] = img[row - 1, column-1]

        imgarr[int(kernel_column / 2):row + int(kernel_column / 2), int(kernel_column / 2):column + int(kernel_column / 2)] = img[0:row, 0:column] # 가운데 채우기


        for i in range (0,row):
            for j in range (0,column):
                filtered_img[i][j]=(imgarr[i+int(kernel_column/2),j:j+kernel_column]*kernel[0,0:kernel_column]).sum() # correlation

    elif kernel.shape[1]==1: # row 벡터일경우


        for i in range(0, int(kernel_row/ 2)): #위아래 왼오 채우기
            imgarr[i, int(kernel_row / 2):column + int(kernel_row / 2)] = img[0,0:column]
        for j in range(0, int(kernel_row / 2)):
            imgarr[int(kernel_row / 2):row + int(kernel_row / 2), j] = img[0:row, 0]
        for i in range(0, int(kernel_row / 2)):
            imgarr[row + int(kernel_row / 2) + i, int(kernel_row / 2):column + int(kernel_row / 2)] = img[row - 1,0:column]
        for j in range(0, int(kernel_row / 2)):
            imgarr[int(kernel_row / 2):row + int(kernel_row / 2), column +int(kernel_row/2)+ j] = img[0:row, column - 1]

        for i in range(0, int(kernel_row / 2)):  # 끝에 채우기
            imgarr[0:i + int(kernel_row / 2), 0:i + int(kernel_row / 2)] = img[0, 0]
        for i in range(0, int(kernel_row / 2)):
            imgarr[0:i + int(kernel_row / 2), column + int(kernel_row / 2):column + kernel_row - 1] = img[0, column - 1]
        for i in range(0, int(kernel_row / 2)):
            imgarr[row + int(kernel_row/2):row + kernel_row - 1, 0:i + int(kernel_row / 2)] = img[row - 1, 0]
        for i in range(0, int(kernel_row / 2)):
            imgarr[row + int(kernel_row/2):row + kernel_row - 1,column+int(kernel_row/2):column + kernel_row - 1] = img[row - 1, column - 1]

        imgarr[int(kernel_row / 2):row + int(kernel_row / 2), int(kernel_row / 2):column + int(kernel_row / 2)] = img[0:row, 0:column] #가운데 채우기

        for i in range (0,column):
            for j in range (0,row):
                filtered_img[j][i]=(imgarr[j:j+kernel_row,i+int(kernel_row/2)]*kernel[0:kernel_row,0]).sum() #correlation


    return filtered_img

def cross_correlation_2d(img,kernel):
    row,column=img.shape
    kernel_row, kernel_column = kernel.shape
    filtered_img = np.array(img)  # 필터링 저장 이미지 초기화
    imgarr = np.zeros((row + kernel_row - 1, column + kernel_column - 1), dtype=int)


    for i in range(0, int(kernel_row / 2)):
        imgarr[i, int(kernel_column / 2):column + int(kernel_column / 2)] = img[0, 0:column]
    for j in range(0, int(kernel_column / 2)):
        imgarr[int(kernel_row / 2):row + int(kernel_row / 2), j] = img[0:row, 0]
    for i in range(0, int(kernel_row / 2)):
        imgarr[row + int(kernel_row / 2) + i, int(kernel_column / 2):column + int(kernel_column / 2)] = img[row - 1,0:column]
    for j in range(0, int(kernel_column / 2)):
        imgarr[int(kernel_row / 2):row + int(kernel_row / 2), column+int(kernel_column/2) + j] = img[0:row, column - 1]

    for i in range(0, int(kernel_row / 2)):  # 끝에 채우기
        imgarr[0:i + int(kernel_row / 2), 0:i + int(kernel_row / 2)] = img[0, 0]
    for i in range(0, int(kernel_row / 2)):
        imgarr[0:i + int(kernel_row / 2), column + int(kernel_row / 2):column + kernel_row - 1] = img[0, column - 1]
    for i in range(0, int(kernel_row / 2)):
        imgarr[row + int(kernel_row / 2):row + row - 1, 0:i + int(kernel_row / 2)] = img[row - 1, 0]
    for i in range(0, int(kernel_row / 2)):
        imgarr[row + int(kernel_row / 2):row + kernel_row - 1, column + int(kernel_row / 2):column + kernel_row - 1] = img[row - 1, column - 1]

    imgarr[int(kernel_row / 2):row + int(kernel_row / 2), int(kernel_column / 2):column + int(kernel_column / 2)] = img[0:row,0:column]


    for i in range (0,row):
        for j in range(0,column):
            filtered_img[i][j]=(imgarr[i:i+kernel_row,j:j+kernel_column]*kernel[0:kernel_row,0:kernel_column]).sum()

    return filtered_img


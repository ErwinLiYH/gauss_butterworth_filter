import numpy as np
from cv2 import cv2
import argparse
from matplotlib import pyplot as plt
import sys
import warnings

warnings.filterwarnings('ignore')

def butterworthFilter(img,high_or_low,D0,n):
    # img=cv2.imread(input_file,0)

    fourier_img=np.fft.fft2(img)

    show_fourier1=np.log(np.abs(np.fft.fftshift(fourier_img)))

    D=distance_array(img.shape)

    if high_or_low=='high':
        H=1/(1 + (D0/D)**(2*n))
    elif high_or_low=='low':
        H=1/(1 + (D/D0)**(2*n))

    show_filter=np.fft.fftshift(H)

    show_fourier2=show_fourier1*show_filter
    
    result=np.real(np.fft.ifft2(fourier_img*H))

    return show_fourier1,show_filter,show_fourier2,result

def gaussFilter(img,high_or_low,D0):
    fourier_img=np.fft.fft2(img)

    show_fourier1=np.log(np.abs(np.fft.fftshift(fourier_img)))

    D=distance_array(img.shape)

    if high_or_low=='high':
        H=1-np.exp((-D**2)/((2*D0)**2))
    elif high_or_low=='low':
        H=np.exp((-D**2)/((2*D0)**2))

    show_filter=np.fft.fftshift(H)

    show_fourier2=show_fourier1*show_filter
    
    result=np.real(np.fft.ifft2(fourier_img*H))

    return show_fourier1,show_filter,show_fourier2,result

def distance_array(shape):
    a1=[i for i in range(0,shape[0])]
    for i in range(0,shape[0]):
        if i>=shape[0]/2:
            a1[i]=a1[i]-shape[0]+1
    a2=[i for i in range(0,shape[1])]
    for i in range(0,shape[1]):
        if i>=shape[1]/2:
            a2[i]=a2[i]-shape[1]+1
    aa1=[a1 for i in range(0,shape[1])]
    aa2=[a2 for i in range(0,shape[0])]
    aa1=np.array(aa1).T
    aa2=np.array(aa2)
    return (aa1**2+aa2**2)**0.5

def normalize(array_like):
    max_num=np.max(array_like)
    min_num=np.min(array_like)
    return (array_like-min_num)/(max_num-min_num)

def improcess(args):
    i=args.i
    o=args.o
    f=args.f
    hol=args.hol
    D=args.D
    n=args.n

    
    img=cv2.imread(i,0)
    # img=np.array([[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8]])
    if f=='butterworth':
        show_fourier1,show_filter,show_fourier2,result=butterworthFilter(img,hol,D,n)
    if f=='gauss':
        show_fourier1,show_filter,show_fourier2,result=gaussFilter(img,hol,D)
    else:
        print('the filter is not supported')
        return
    # print(show_fourier1)
    # print(show_filter)
    # print(show_fourier2)
    # print(result)
    result=normalize(result)*255
    plt.figure('fourier transfermation')
    plt.subplot('151')
    plt.xticks([])
    plt.yticks([])
    plt.imshow(img,'gray',)
    plt.subplot('152')
    plt.xticks([])
    plt.yticks([])
    plt.imshow(show_fourier1,'gray')
    plt.subplot('153')
    plt.xticks([])
    plt.yticks([])
    plt.imshow(show_filter,'gray')
    plt.subplot('154')
    plt.xticks([])
    plt.yticks([])
    plt.imshow(show_fourier2,'gray')
    plt.subplot('155')
    plt.xticks([])
    plt.yticks([])
    plt.imshow(result,'gray')
    plt.show()
    cv2.imwrite(o,result)



main_parser=argparse.ArgumentParser(description='a simple image processer base on fourier transfer')
main_parser.add_argument('f',metavar='filter',type=str,help='the filter you want to use, candidate:[butterworth,gauss]')
main_parser.add_argument('-i',metavar='input file',type=str,help='the path of input file',default='./input.png')
main_parser.add_argument('-o',metavar='output file',type=str,help='the path of output file',default='./output.png')
main_parser.add_argument('-hol',metavar='high or low',help='high pass filter or low pass filter',type=str,default='high')
main_parser.add_argument('-D',help='D0 parameter',type=int,default=50)
main_parser.add_argument('-n',help='n parameter',type=int,default=2)

args = main_parser.parse_args(sys.argv[1:])
improcess(args)
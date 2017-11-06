# Introduction to OpenCV
——————The openCV exercises in EC601 class
Exercise 1
1. How does a program read the cvMat object, in particular, what is the order of the pixel structure?
  cvMat is the most important function in OpenCV. The program reads the cvMat object by using CvMat* cvCreateMat ( int rows, int cols, int type ). The type could be any pre-define type used the contruction:CV_<bit_depth> (S|U|F)C<number_of_channels>. Then, the elements of matrix could be 32 bits float or CV_8UC3, or others. One element in cvMat may not be a single number. We could use simple input to represent multiple values, then we could describle multicolor channels in a RGB image.
This kind of matrix is made of width, height, type, step and a pointer which points to the data.
  Mat is used in C++. We could use:  
   Mat src;
    src = imread(argv[1], CV_LOAD_IMAGE_COLOR); This kind of instructions to access the image.
  The structure is as follows: 
   typedef struct CvMat
{
    int type;
    int step;
    int* refcount;/* for internal use only */
    int hdr_refcount;
    union
    {
        uchar* ptr;
        short* s;
        int* i;
        float* fl;
        double* db;
    } data;
    union
    {
        int rows;
        int height;
    };
    union
    {
        int cols;
        int width;
    };
} CvMat;
______________________________________________________________________________________________________________
Exercise 2
1. ColorImage.cpp is a program that takes a look at colorspace conversions in OpenCV. Run the code in ColorImage.cpp and comment on the outputs. Implement the same thing in Python and save each image.
 The results are in the exercise2 folder
2. Print out the values of the pixel at (20,25) in the RGB, YCbCr and HSV versions of the image. What are the ranges of pixel values in each channel of each of the above mentioned colorspaces?
the values of the pixel at (20,25)
('blue pixel value', 246)
('Green pixel value', 236)
('red pixel value', 236)
('H pixel value', 120)
('S pixel value', 10)
('V pixel value', 246)
('Y pixel value', 237)
('Cb pixel value', 127)
('Cr pixel value', 133)
The range of R,G,B are all 0-255.
For HSV, Hue range is 0-179, Saturation range is 0-255 and Value range is 0-255.
For YCbCr, 16 to 235 for Y, Cb and Cr are ranging from 16 to 240.
______________________________________________________________________________________________________________
Exercise3

1.Look at the code in Noise.cpp and implement the code in Python. Also, print the results for different noise values in the Gaussian case, mean = 0, 5, 10, 20 and sigma = 0, 20, 50, 100 and for the salt-and-pepper case, pa = 0.01, 0.03, 0.05, 0.4 and pb = 0.01, 0.03, 0.05, 0.4.
2. Change the kernel sizes for all the filters with all different values for noises and print the results for 3x3, 5x5 and 7x7 kernels. Comment on the results. Which filter seems to work ”better” for images with salt-and-pepper noise and gaussian noise?
   According to the result,median filter works better for salt and pepper images and gaussian filter works better for gassian noise images.If the size of kernel becomes bigger, the results of the image becomes more blurred.


	
                            



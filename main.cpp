#include <iostream>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include "opencv/cv.h"

using namespace std;
using namespace cv;

// Media aritimética
double mean(double*t,int size){
    double m = 0;
    for (int i=0;i<size;i++){
        m += t[i];
    }
    return m/size;
}

// Calculo da variancia baseado em http://en.wikipedia.org/wiki/Variance#Discrete_random_variable
double variance(double*t,int size){
    double v = 0;
    for (int i = 0; i < size; i++){
        for (int j = 0; j < size; j++){
            double diff = t[i] - t[j];
            diff *= diff;
            v += (diff)/2;
        }
    }
    return v/(size*size);
}

int main(){
	std::cout << "Main.cpp" << std::endl;

    // Carregando as imagens para calcular os histogramas
	Mat image1 = imread("images/wave_1.png",CV_LOAD_IMAGE_COLOR);
    Mat image2 = imread("images/wave_2.png",CV_LOAD_IMAGE_COLOR);
    Mat image3 = imread("images/wave_3.png",CV_LOAD_IMAGE_COLOR);
    Mat image4 = imread("images/wave_4.png",CV_LOAD_IMAGE_COLOR);
    Mat image5 = imread("images/wave_5.png",CV_LOAD_IMAGE_COLOR);

    Mat hsv1,hsv2,hsv3,hsv4,hsv5;
    MatND hist1,hist2,hist3,hist4,hist5;

	cvtColor(image1, hsv1, CV_BGR2HSV);
    cvtColor(image2, hsv2, CV_BGR2HSV);
    cvtColor(image3, hsv3, CV_BGR2HSV);
    cvtColor(image4, hsv4, CV_BGR2HSV);
    cvtColor(image5, hsv5, CV_BGR2HSV);


    // Esses valores são necessários para calcular o histograma, são basicamente os mesmos
    // do exemplo da documentação do OpenCV
	int hbins = 30, sbins = 32;
	int histSize[] = {hbins, sbins};
	float hranges[] = {0,180};
	float sranges[] = {0,256};
	const float* ranges[] = {hranges,sranges};
	int channels[] = {0,1};


    // Calculando os histogramas
    calcHist( &hsv1, 1, channels, Mat(), // do not use mask
         hist1, 2, histSize, ranges,
         true, // the histogram is uniform
         false );

    calcHist( &hsv2, 1, channels, Mat(), // do not use mask
         hist2, 2, histSize, ranges,
         true, // the histogram is uniform
         false );

    calcHist( &hsv3, 1, channels, Mat(), // do not use mask
         hist3, 2, histSize, ranges,
         true, // the histogram is uniform
         false );

    calcHist( &hsv4, 1, channels, Mat(), // do not use mask
         hist4, 2, histSize, ranges,
         true, // the histogram is uniform
         false );

    calcHist( &hsv5, 1, channels, Mat(), // do not use mask
         hist5, 2, histSize, ranges,
         true, // the histogram is uniform
         false );

    // Correlação do histograma 1 com o histograma 2
    double correlation12 = compareHist(hist1,hist2,CV_COMP_CORREL);

    // Correlação do histograma 1 com o histograma 3
    double correlation13 = compareHist(hist1,hist3,CV_COMP_CORREL);

    // Correlação do histograma 1 com o histograma 4
    double correlation14 = compareHist(hist1,hist4,CV_COMP_CORREL);

    // Correlação do histograma 1 com o histograma 5
    double correlation15 = compareHist(hist1,hist5,CV_COMP_CORREL);

    double correlation[] = {correlation12,correlation13,correlation14,correlation15};

    std::cout << "CORRELATION 1 2: " << correlation12 << std::endl;
    std::cout << "CORRELATION 1 3: " << correlation13 << std::endl;
    std::cout << "CORRELATION 1 4: " << correlation14 << std::endl;
    std::cout << "CORRELATION 1 5: " << correlation15 << std::endl;

    // Preparando os dados que serão exibidos na tela
    int width = 400, height = 400;
    Mat histImage( width, height, CV_8UC3, Scalar( 0,0,0) );

    int w1 = width/5;
    int w2 = w1*2;
    int w3 = w1*3;
    int w4 = w1*4;

    int h1 = (correlation12)*height;
    int h2 = (correlation13)*height;
    int h3 = (correlation14)*height;
    int h4 = (correlation15)*height;

    // Grafico da evolução da correlação
    line(histImage, Point(w1,h1), Point(w2,h2), Scalar(255,0,0), 2, 8, 0);
    line(histImage, Point(w2,h2), Point(w3,h3), Scalar(0,255,0), 2, 8, 0);
    line(histImage, Point(w3,h3), Point(w4,h4), Scalar(0,0,255), 2, 8, 0);

    namedWindow("calcHist Demo", CV_WINDOW_AUTOSIZE );
    imshow("calcHist Demo", histImage );


    // Calculando a media e variancia
    double m = mean(correlation,4);
    double v = variance(correlation,4);

    std::cout << "Media: " << m << std::endl;
    std::cout << "Variancia: " << v << std::endl;


	waitKey(0);

	return 0;
}
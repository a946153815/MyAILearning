#ifndef ADDPEOPLE_H
#define ADDPEOPLE_H
#include "opencv2/opencv.hpp"
#include "opencv2/core.hpp"
#include "opencv2/highgui.hpp"
#include "opencv2/imgproc.hpp"
#include "opencv2/face.hpp"
#include "opencv2/core/utility.hpp"
#include "file.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <map>
#include <QDialog>
#include <QDebug>
#include <QMessageBox>
using namespace cv;
using namespace cv::face;
using namespace std;
namespace Ui {
class addPeople;
}

class addPeople : public QDialog
{
    Q_OBJECT

public:
    explicit addPeople(QWidget *parent = 0);
    lhxFILE file;
    ~addPeople();
    void AddCSV();
    void TrainingModel();
    void disposePic();
private slots:
    void on_pushButton_clicked();

    void on_add_clicked();

private:
    Ui::addPeople *ui;
    cv::Mat frame;
    cv::VideoCapture *capture;

    int MaxNumAboutPeople;
    cv::Mat norm_0_255(cv::InputArray _src);
    void detectAndDisplay(QString source, QString target);

    void read_csv(const std::string& filename, std::vector<cv::Mat>& images, std::vector<int>& labels);
};

#endif // ADDPEOPLE_H

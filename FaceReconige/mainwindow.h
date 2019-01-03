#ifndef MAINWINDOW_H
#define MAINWINDOW_H
#include "addpeople.h"
#include <QMainWindow>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private slots:
    void on_pushButton_clicked();

    void on_pushButton_2_clicked();

    void on_pushButton_3_clicked();

    void on_pushButton_4_clicked();

    void on_pushButton_5_clicked();

    void on_pushButton_6_clicked();

    void on_btn_train_clicked();

private:
    Ui::MainWindow *ui;
    addPeople a;
};

#endif // MAINWINDOW_H

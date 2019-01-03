#-------------------------------------------------
#
# Project created by QtCreator 2018-07-09T00:46:23
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = FaceReconige
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp \
    addpeople.cpp \
    file.cpp

HEADERS  += mainwindow.h \
    addpeople.h \
    file.h

FORMS    += mainwindow.ui \
    addpeople.ui

INCLUDEPATH += /usr/local/include \
                /usr/local/include/opencv \
                /usr/local/include/opencv2

LIBS += /usr/local/lib/libopencv_*


#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QFileDialog>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class QStandartItemModel;

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_pushButton_clicked();
    QStandartItemModel *mModel;

    void on_actionAbrir_triggered();

    void on_actionOpen_triggered();

    void on_actionSave_triggered();

    void on_actionDelete_triggered();

private:
    Ui::MainWindow *ui;
};
#endif // MAINWINDOW_H

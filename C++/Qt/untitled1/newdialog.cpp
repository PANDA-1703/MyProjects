#include "newdialog.h"
#include "ui_newdialog.h"



newdialog::newdialog(QWidget *parent):
    QDialog(parent),
    ui(new Ui::newdialog)
{
    ui->setupUi(this);
}

newdialog::~newdialog()
{
    delete ui;
}

int newdialog::getRowCount() const
{

}

int newdialog::getColCount() const
{

}

void newdialog::on_buttonBox_accepted()
{

}

void newdialog::on_buttonBox_regected()
{

}

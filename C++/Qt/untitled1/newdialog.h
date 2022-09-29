#ifndef NEWDIALOG_H
#define NEWDIALOG_H

#include <QDialog>

namespace Ui
{
class newdialog;
}

class newdialog : public QDialog
{
    Q_OBJECT
public:
    explicit newdialog(QWidget *parent = nullptr);
    ~newdialog();
    int getRowCount() const;
    int getColCount() const;
private slots:
    void on_buttonBox_accepted();
    void on_buttonBox_regected();
private:
    Ui::newdialog *ui;
};



#endif // NEWDIALOG_H

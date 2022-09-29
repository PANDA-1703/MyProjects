using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO;
using System.Text.RegularExpressions;
using System.Collections;
using static System.Windows.Forms.AxHost;
using System.Reflection.Emit;
using System.Reflection;
using System.Timers;
using System.Diagnostics;
using static System.Windows.Forms.LinkLabel;
using System.Runtime.InteropServices;
using System.Xml.Linq;


namespace Citek_ver2._0_
{
    

    public partial class Form1 : Form
    {

        public Form1()
        {
            InitializeComponent();
            
        }

        Stopwatch stopwatch = new Stopwatch();
        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }


        private void button1_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Выберите файл с РКК!");
            DialogResult message1 = openFileDialog1.ShowDialog();
            if (message1 != DialogResult.OK)
            {
                MessageBox.Show("Error! Try again.");
                return;
            }

            stopwatch.Start();

            // Работа с файлом "РКК"
            //int counter1 = 0;
            List<string> nameRKK = new List<string>();
            string file1 = openFileDialog1.FileName;
            foreach (string line1 in File.ReadLines(file1)) //построчное считывание с файла
            {
                string str = "Климов Сергей Александрович";

                if (line1.IndexOf(str) > -1) //поиск вхождений "Климов Сергей Александрович" для поиска ответственного в строке
                {
                    if (line1.IndexOf(";") > -1)
                    {
                        if (line1.IndexOf("(Отв") > -1)
                        {
                            nameRKK.Add(line1.Substring(line1.LastIndexOf('\t') + 1, line1.IndexOf("(Отв") - line1.LastIndexOf('\t') - 2));
                        }
                        else
                        {
                            nameRKK.Add(line1.Substring(line1.LastIndexOf('\t') + 1, line1.IndexOf(";")-1 - line1.LastIndexOf('\t') - 1));
                        }

                    }
                    else
                    {
                        if (line1.IndexOf("Отв") > -1)
                        {
                            nameRKK.Add(line1.Substring(line1.LastIndexOf('\t') + 1, line1.LastIndexOf("(Отв") - line1.IndexOf("\t") - 2));
                        }
                        else
                        {
                            nameRKK.Add(line1.Substring(line1.LastIndexOf('\t') + 1, line1.LastIndexOf(".") - line1.IndexOf("\t")));
                        }

                    }
                }

                else //иначе берём руководителя
                {
                    // обрезаем имя, отчество до инициалов
                    string initc = line1.Substring(0, line1.IndexOf('\t'));

                    int index = initc.IndexOf(' '); // пробел после фамилии
                    string lastName = initc.Substring(0, index).Trim();
                    lastName = lastName.Substring(0, 1).ToUpper() + lastName.Substring(1).ToLower(); //записали фамилию
                    initc = initc.Substring(index).Trim(); // удалили из строки фамилию

                    index = initc.IndexOf(' '); // пробел после имени
                    string firstName = initc.Substring(0, index).Trim();
                    firstName = firstName.Substring(0, 1).ToUpper() + firstName.Substring(1).ToLower(); // записали имя
                    string fatherName = initc.Substring(index).Trim().Substring(0, 1).ToUpper() + initc.Substring(index).Trim().Substring(1).ToLower(); //записали отчество
                    nameRKK.Add(lastName + " " + firstName.Substring(0, 1) + "." + fatherName.Substring(0, 1) + ".");
                }
                //counter1++;
            }

            var result1 = nameRKK.GroupBy(x => x).Select(x => new { value = x.Key, count = x.Count() });

            //=============================================================================================================
            // Работа с файлом "Обращения"
            MessageBox.Show("Выберите файл с Обращениями!");
            DialogResult message2 = openFileDialog1.ShowDialog();
            if (message2 != DialogResult.OK)
            {
                MessageBox.Show("Error! Try again.");
                return;
            }


            //int counter2 = 0;
            List<string> nameApp = new List<string>();

            string file2 = openFileDialog1.FileName;
            foreach (string line2 in File.ReadLines(file2)) //построчное считывание с файла
            {

                string str = "Климов Сергей Александрович";

                if (line2.IndexOf(str) > -1) //поиск вхождений "Климов Сергей Александрович" для поиска ответственного в строке
                {
                    if (line2.IndexOf(";") > -1)
                    {
                        if (line2.IndexOf("(Отв") > -1)
                        {
                            nameRKK.Add(line2.Substring(line2.LastIndexOf('\t') + 1, line2.IndexOf("(Отв") - line2.LastIndexOf('\t') - 2));
                        }
                        else
                        {
                            nameRKK.Add(line2.Substring(line2.LastIndexOf('\t') + 1, line2.IndexOf(";") - line2.LastIndexOf('\t') - 1));
                        }
                    }
                    else
                    {
                        if (line2.IndexOf("Отв") > -1)
                        {
                            nameRKK.Add(line2.Substring(line2.LastIndexOf('\t') + 1, line2.LastIndexOf("(Отв") - line2.IndexOf("\t") - 2));
                        }
                        else
                        {
                            nameRKK.Add(line2.Substring(line2.LastIndexOf('\t') + 1, line2.LastIndexOf(".") - line2.IndexOf("\t")));
                        }
                    }
                }
                else //иначе берём руководителя
                {
                    string initc = line2.Substring(0, line2.IndexOf('\t'));

                    int index = initc.IndexOf(' '); // пробел после фамилии
                    string lastName = initc.Substring(0, index).Trim();
                    lastName = lastName.Substring(0, 1).ToUpper() + lastName.Substring(1).ToLower(); //записали фамилию
                    initc = initc.Substring(index).Trim(); // удалили из строки фамилию

                    index = initc.IndexOf(' '); // пробел после имени
                    string firstName = initc.Substring(0, index).Trim();
                    firstName = firstName.Substring(0, 1).ToUpper() + firstName.Substring(1).ToLower(); // записали имя
                    string fatherName = initc.Substring(index).Trim().Substring(0, 1).ToUpper() + initc.Substring(index).Trim().Substring(1).ToLower(); //записали отчество

                    nameApp.Add(lastName + " " + firstName.Substring(0, 1) + "." + fatherName.Substring(0, 1) + ".");
                }
                //counter2++;
            }

            var result2 = nameApp.GroupBy(x => x).Select(x => new { value = x.Key, count = x.Count() });

            List<MyObject> NewList = new List<MyObject>();

            foreach (var person1 in result1) //запись в NewList в 3 столбца исполнителей, присутствующих в обоих файлах
            {
                foreach (var person2 in result2)
                {
                    if (person1.value == person2.value)
                    {
                        MyObject TempObject = new MyObject();
                        TempObject.firstItem = person1.value;
                        TempObject.secondItem = person1.count;
                        TempObject.threeItem = person2.count;

                        NewList.Add(TempObject);
                    }
                }
            }

            foreach (var person in result1) //запись в NewList тех, кого нет в файле 2
            {
                if (result2.Where(c => c.value == person.value).Count() == 0)
                {
                    MyObject TempObject = new MyObject();
                    TempObject.firstItem = person.value;
                    TempObject.secondItem = person.count;
                    TempObject.threeItem = 0;
                    NewList.Add(TempObject);
                }
            }

            foreach (var person in result2) //запись в NewList тех, кого нет в файле 1
            {
                if (result1.Where(c => c.value == person.value).Count() == 0)
                {
                    MyObject TempObject = new MyObject();
                    TempObject.firstItem = person.value;
                    TempObject.secondItem = 0;
                    TempObject.threeItem = person.count;
                    NewList.Add(TempObject);
                }
            }

            int allCountRKK = 0;
            int allCountApp = 0;
            int allCount = 0;

            foreach (var person in NewList) //вывод NewList в таблицу формы && подсчёт общего кол-ва документов 
            {
                dataGridView1.Rows.Add(null, person.firstItem, person.secondItem, person.threeItem, person.secondItem + person.threeItem);
                allCountRKK = allCountRKK + person.secondItem;
                allCountApp = allCountApp + person.threeItem;
                allCount = allCountRKK + allCountApp;
            }

            dataGridView1.Sort(dataGridView1.Columns[2], ListSortDirection.Descending); // сортировка по кол-ву RKK
            dataGridView1.Sort(dataGridView1.Columns[3], ListSortDirection.Descending); // сортировка по кол-ву App
            dataGridView1.Sort(dataGridView1.Columns[4], ListSortDirection.Descending); // сортировка по общему кол-ву обращений

            NumerateCells1(); // функция нумерации столбца id

            label1.Text = Convert.ToString("Неисполнено в срок " + allCount + " документов, из них: \n " +
                "- количество неисполненных входящих документов: " + allCountRKK + ";\n" +
                "- количество неисполненных письменных обращений граждан: " + allCountApp + ".");
            label2.Text = Convert.ToString("Файл 1: " + file1);
            label3.Text = Convert.ToString("Файл 2: " + file2);
            label4.Text = DateTime.Now.ToString("Дата составления отчёта: " + "yyyy.MM.dd, HH.mm.ss");
            stopwatch.Stop(); // остановка таймера
            label5.Text = Convert.ToString("Время работы алгоритма: " + stopwatch.ElapsedMilliseconds + " ms");
        }


        public void NumerateCells1() // присвоение id для строк (она же нумерация строк)
        {
            dataGridView1.Columns["id"].DataPropertyName = "Value";
            int colIndex = 0; //индекс столбца
            for (int i = 0; i < dataGridView1.RowCount-1; i++)
                dataGridView1.Rows[i].Cells[colIndex].Value = i + 1;
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e) // кнопка экспорта в txt
        {
            DialogResult message3 = saveFileDialog1.ShowDialog(); // saveDialog создания файла для записи
            string file3 = saveFileDialog1.FileName;
            System.IO.StreamWriter file = new System.IO.StreamWriter(file3);
            try
            {
                file.WriteLine(label1.Text + "\n");

                string sLine = "";

                for (int r = 0; r <= dataGridView1.Rows.Count - 2; r++)
                {
                    for (int c = 0; c <= dataGridView1.Columns.Count - 1; c++)
                    {
                        sLine = sLine + dataGridView1.Rows[r].Cells[c].Value;
                        if (c != dataGridView1.Columns.Count - 1)
                        {
                            sLine = sLine + ", ";
                        }
                    }

                    file.WriteLine(sLine); //Запись по строке за раз
                    sLine = "";
                }

                file.WriteLine("\n" + label4.Text); //Запись даты в файл

                file.Close();
                System.Windows.Forms.MessageBox.Show("Export Complete.", "Program Info", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
            catch (System.Exception err) // вывод ошибки в случае неудачи
            {
                System.Windows.Forms.MessageBox.Show(err.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                file.Close();
            }
        }

        private void label5_Click(object sender, EventArgs e)
        {

        }
    }

    public class MyObject //конструктор для записи в NewList
    {
        public string firstItem { get; set; }
        public int secondItem { get; set; }
        public int threeItem { get; set; }
    }

    
}

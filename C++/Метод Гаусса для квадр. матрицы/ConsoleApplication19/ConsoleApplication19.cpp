#include "stdafx.h"
#include <iostream>
#include <cmath> 
#include <stdio.h>
#include <omp.h> 
#include "windows.h"
#include <iomanip> 

using namespace std;
int main() {
	int n, m = 0, x = 0, y = 0;
	setlocale(LC_ALL, "Rus");
	cout << "Введите количество строк и столбцов: ";
	cin >> n;
	int i, j, r;
	double b, c = 1;
	double** arr = new double*[n];
	for (i = 0; i < n; i++) arr[i] = new double[n];
	cout << "Введите элементы массива:" << endl;
	for (i = 0; i < n; i++)
		for (j = 0; j < n; j++) cin >> arr[i][j];
	for (i = 0; i < n; i++) {
		for (j = 0; j < n; j++) cout << std::setw(4) << arr[i][j] << " ";
		cout << endl;
	}

	if (arr[0][0] == 0)
	{
		for (j = 0; j < n; j++)
		{
			for (i = 0; i < n; i++)
			{
				if (arr[i][j] != 0 && arr[0][0] == 0)
				{
					for (j = 0; j < n; j++)
					{
						swap(arr[i][j], arr[0][j]);
					}
				}
			}
		}
	}
	for (int r = 1; r < n; r++)
	{
		for (i = r; i < n; i++)
		{
			for (int h = 0; h < n; h++)
			{
				for (int t = 0; t < n; t++)
				{
					if (h > t)
					{
						m += abs(arr[h][t]);
					}
				}
			}
			if (m == 0)
			{
				goto next;
			}
			m = 0;
			b = arr[i][r - 1];
			for (j = r - 1; j < n; j++)
			{
				arr[i][j] = arr[i][j] + arr[r - 1][j] * (-b / arr[r - 1][r - 1]);
			}
		}
	}
next:
	cout << "" << endl;
	cout << "" << endl;
	cout << "" << endl;
	for (i = 0; i < n; i++) {
		for (j = 0; j < n; j++) cout << std::setw(4) << arr[i][j] << " ";
		cout << endl;
	}
#pragma omp parallel  private(i, j) shared(arr)
	{
#pragma omp for 
		for (i = 0; i < n; i++)
		{
			r = omp_get_thread_num();
			for (j = 0; j < n; j++)
			{
				if (i == j)
				{
					c = c * arr[i][j];
					printf("Нить` -> %d выполнила операцию \n", r);
				}
				Sleep(1000);
			}
		}
	}
	cout << "" << endl;
	cout << "" << endl;
	cout << "" << endl;
	cout << c << endl;
	return 0;
}
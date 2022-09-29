#include "stdafx.h"
#include <iostream>
#include <cmath> 
#include <stdio.h>
#include <omp.h> 
#include "windows.h"


int main()
{
	setlocale(LC_ALL, "Russian");
	const double a = 1.2, b = 2; 
	double x, h, f, fxx = 0; 
	int n, i, n2, k, r;
	std::cout << "Введите чётное количество разбиений n ";
	std::cin >> n;
	while (n % 2 != 0)
	{
		std::cin >> n;
	}
	n2 = n + 1;
	h = (b - a) / n;
	double *x1 = new double[n2]; double *fx = new double[n2];
	x1[0] = a;
				for (i = 1; i < n2; i++)
				{
					x1[i] = x1[i - 1] + h;
				}

				for (i = 0; i < n2; i++)
				{
					x = x1[i];
					fx[i] = sqrt(1 + 2 * pow(x, 2) - pow(x, 3));
				}
#pragma omp parallel  private(i) shared(n2, fx) reduction(+:fxx)
				{
#pragma omp for 
					for (i = 0; i < n2; i++)
					{
						r = omp_get_thread_num();
						if (i == 0 || i == n2 - 1)
						{
							fx[i] = fx[i];
						}
						else if (i % 2 == 0)
						{
							fx[i] = 2 * fx[i];
						}
						else if (i % 2 != 0)
						{
							fx[i] = 4 * fx[i];
						}
						fxx = fxx + fx[i];
						printf("Нить` -> %d выполнила операцию \n", r);
					}
					Sleep(1000);
				}
	f = h / 3 * fxx;
	std::cout << "Интеграл = " << f;
	return 0;
}

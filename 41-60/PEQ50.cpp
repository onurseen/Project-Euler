#include <bits/stdc++.h>

#define N 1000000

using namespace std;

void print_vec(vector<unsigned int> x)
{
	for (auto i : x)
		cout << i << endl;
}

int main(int ac, char **av)
{
	vector<unsigned int> primes;
	vector<bool> p(N + 1, true);
	p[0] = p[1] = false;

	for (unsigned int i = 2; i <= N; i++)
		if (p[i])
		{
			primes.push_back(i);
			for (unsigned int j = i * i; j <= N; j += i)
				p[j] = false;
		}

	int maxSum = 0, maxRun = -1;

	for (int i = 0; i < primes.size(); i++)
	{
		int sum = 0;

		for (int j = i; j < primes.size(); j++)
		{
			sum += primes[j];

			if (sum > N)
				break;
			if (p[sum] && sum > maxSum && j - i > maxRun)
			{
				maxRun = j - i;
				maxSum = sum;
			}
		}
	}
	cout << maxSum << endl;
}
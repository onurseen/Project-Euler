#include <bits/stdc++.h>

#define getmin(a, b) (a < b ? a : b)
#define N 10000000

using namespace std;

vector<unsigned int> Nprimes;

vector<unsigned int> sieve(unsigned int n)
{
	vector<unsigned int> p;
	vector<bool> primes(n + 1, true);
	primes[0] = primes[1] = false;
	
	for (int i = 2; i <= n; i++)
		if (primes[i])
		{
			p.push_back(i);
			for (int j = i * i; j <= n ; j += i)
				primes[j] = false;
		}
	return (p);
}

int num_len(unsigned int x)
{
	int i = 1;

	while (x, x /= 10)
		i++;
	return (i);
}

int is_permutations(unsigned int x, unsigned int y)
{
	int arr1[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
	int arr2[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

	if (num_len(x) != num_len(y))
		return (0);

	while (x && y)
	{
		arr1[x % 10]++;
		arr2[y % 10]++;
		x /= 10;
		y /= 10;
	}
	for (int i = 0; i < 10; i++)
		if (arr1[i] != arr2[i])
			return (0);
	return (1);
}

unsigned int phi(unsigned int x, double minQuotient)
{
	// minQuotient < x / res = res * minQuotient < x
	auto res = x;
	auto temp = x;

	for (auto p : Nprimes)
	{
		if (p * p > temp)
			break;

		if (temp % p != 0)
			continue;
		
		do
		{
			temp /= p;
		}
		while (temp % p == 0);

		res -= res / p;

		if (res * minQuotient < x)
			return (res);
	}

	if (res == x)
		return (x - 1);

	if (temp > 1)
		return (res - res / temp);
	else
		return (res);
}

int main(int ac, char **av)
{
	Nprimes = sieve(N);
	
	unsigned int ans = 2;
	double minQuotient = 999999;

	for (unsigned int i = 3; i < N; i++)
	{
		auto temp_phi = phi(i, minQuotient);
		double quotient = i / double(temp_phi);
		
		if (minQuotient <= quotient)
			continue;

		if (is_permutations(temp_phi, i))
		{
			minQuotient = quotient;
			ans = i;
		}
	}

	cout << ans << endl;
	return (0);
}








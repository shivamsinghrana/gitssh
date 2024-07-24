#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main ()
{
  int arr[100];
  int length, i, j, oddlen, evenlen, temp, c, d;
  int odd[50], even[50];
  cout << "enter the length of array : ";
  cin >> length;
  for (i = 0; i < length; i++)
    {
      cout << "Enter element at " << i << " index : ";
      cin >> arr[i];
    }
  if (length % 2 == 0)
    {
      oddlen = length / 2;
      evenlen = length / 2;
    }
  else
    {
      oddlen = length / 2;
      evenlen = (length / 2) + 1;
    }
  for (i = 0; i < length; i++)	// seperation of even and odd array
    {
      if (i % 2 == 0)
	{
	  even[i / 2] = arr[i];
	}
      else
	{
	  odd[i / 2] = arr[i];
	}
    }
  for (i = 0; i < evenlen - 1; i++)	// sorting of even array 
    {
      for (j = i + 1; j < evenlen; j++)
	{
	  temp = 0;
	  if (even[i] > even[j])
	    {
	      temp = even[i];
	      even[i] = even[j];
	      even[j] = temp;
	    }
	}
    }
  for (i = 0; i < oddlen - 1; i++)	// sorting of odd array 
    {
      for (j = i + 1; j < oddlen; j++)
	{
	  temp = 0;
	  if (odd[i] > odd[j])
	    {
	      temp = odd[i];
	      odd[i] = odd[j];
	      odd[j] = temp;
	    }
	}
    }
  cout << "\nSorted even array : ";	// printing even array
  for (i = 0; i < evenlen; i++)
    {
      cout << even[i] << " ";
    }
  cout << "\n";
  cout << "Sorted odd array : ";	// printing odd array 
  for (i = 0; i < oddlen; i++)
    {
      cout << odd[i] << " ";
    }
  cout << endl;
  cout << even[evenlen - 2] + odd[oddlen - 2];	// printing final result 
}
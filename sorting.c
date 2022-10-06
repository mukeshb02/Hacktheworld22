/*  menu driven program
    - Selection sort
    - Bubble sort
    - Insertion sort
    - Merge sort  */

#include <stdio.h>

void print(int arr[], int n)
{
    for(int i=0;i<n;i++)
        printf("%d ",arr[i]);
    printf("\n"); 
}

void merge(int arr[], int low, int mid, int high)
{
	int i, j, k;
	int n1 = mid - low + 1;
	int n2 = high - mid;
	int a1[n1], a2[n2];
	for (i = 0; i < n1; i++)
		a1[i] = arr[low + i];
	for (j = 0; j < n2; j++)
		a2[j] = arr[mid + 1 + j];
	i = 0;
    j = 0; 
	k = low; 
	while (i < n1 && j < n2)
    {
		if (a1[i] <= a2[j]) 
        {
			arr[k] = a1[i];
			i++;
		}
		else 
        {
			arr[k] = a2[j];
			j++;
		}
		k++;
	}
	while (i < n1)
    {
		arr[k] = a1[i];
		i++;
		k++;
	}
    while (j < n2) {
		arr[k] = a2[j];
		j++;
		k++;
	}
}

void mergesort(int arr[], int low, int high)
{
	if (low < high)
    {
        int mid = (low + high - 1) / 2;
		mergesort(arr, low, mid);
		mergesort(arr, mid + 1, high);
		merge(arr, low, mid, high);
	}
}

void bubblesort(int arr[], int n)
{
    for(int i=0;i<n;i++)
    {
        int flag = 0;
        for(int j =0;j<n-i-1;j++)
            if(arr[j]>arr[j+1])
            {
                int temp=arr[j];
                arr[j] = arr[j+1];
                arr[j+1]=temp;
                flag++;
            }
        if(flag==0)
            break;
    }
    printf("The sorted array using bubble sort :\n");
    print(arr,n);
}

void insertionsort(int arr[], int n)
{
    int j,key;
    for(int i=1;i<n;i++)
    {
        key = arr[i];
        for(j =i-1;j>=0 && arr[j] > key;j--)
            arr[j+1]=arr[j];
        arr[j+1]=key;
    }
    printf("The sorted array using insertion sort :\n");
    print(arr,n);
}

void selectionsort(int arr[], int n)
{
    for(int i=0;i<n-1;i++)
    {
        int min=i;
        for(int j =i+1;j<n;j++)
            if(arr[min]>arr[j])
                min=j;
        int temp=arr[min];
        arr[min] = arr[i];
        arr[i]=temp;
    }
    printf("The sorted array using selection sort :\n");
    print(arr,n);
}

int main()
{
    int a[20],arr[20],n,choice,s1=1;
    printf("Enter the size of array : ");
    scanf("%d",&n);
    printf("Enter the values : ");
    for(int i=0;i<n;i++)
        scanf("%d",&a[i]);
    while(s1 == 1)
    {
        printf("Enter :\n1 for Selection Sort\n2 for Bubble Sort\n3 for Insertion Sort\n4 for Merge Sort\n");
        scanf("%d",&choice);
        for(int i =0;i<n;i++)
            arr[i]=a[i];
        printf("The original array : \n");
        print(arr,n);
        switch(choice)
        {
            case 1:
                selectionsort(arr,n);
                break;
            case 2:
                bubblesort(arr,n);
                break;
            case 3:
                insertionsort(arr,n);
                break;
            case 4:
                mergesort(arr, 0, n - 1);
                printf("The sorted array using merge sort :\n");
                print(arr,n);
                break;
            default:
                printf("Wrong Input\n");            
        } 
        printf("Press '1' to continue or '0' to terminate the program : ");
        scanf("%d",&s1);
    }    
}
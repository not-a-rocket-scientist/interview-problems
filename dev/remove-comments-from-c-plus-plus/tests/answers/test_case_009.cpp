


#include <iostream>

void PrintArray(int *array, int n) {
  for (int i = 0; i < n; ++i)
    std::cout << array[i] << " " << std::flush;
  std::cout << std::endl;
}

void Merger(int arr[], int lo, int  mi, int hi){
    int *temp = new int[hi-lo+1];
    int i = lo, j = mi + 1;
    int k = 0;
    while(i <= mi && j <=hi){
        if(arr[i] <= arr[j])
            temp[k++] = arr[i++];
        else
            temp[k++] = arr[j++];
    }

    while(i <= mi)
        temp[k++] = arr[i++];

    while(j <= hi)
        temp[k++] = arr[j++];

    for(k = 0, i = lo; i <= hi; ++i, ++k)
        arr[i] = temp[k];

    delete []temp;
}
void MergeSortHelper(int arr[], int lo, int hi){
    int mid;
    if(lo < hi){
        mid = (lo + hi) >> 1;
        MergeSortHelper(arr, lo, mid);
        MergeSortHelper(arr, mid+1, hi);
        Merger(arr, lo, mid, hi);
    }
}
void MergeSort(int arr[], int arr_size){
    MergeSortHelper(arr, 0, arr_size-1);
}

int main() {
  int array[] = {94, 42, 50, 95, 333, 65, 54, 456, 1, 1234};
  int n = sizeof(array)/sizeof(array[0]);

  std::cout << "Before Merge Sort :" << std::endl;
  PrintArray(array, n);

  MergeSort(array, n);

  std::cout << "After Merge Sort :" << std::endl;
  PrintArray(array, n);
  return (0);
}

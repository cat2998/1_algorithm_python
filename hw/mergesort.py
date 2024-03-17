def merge_sort(arr, first, last):
	if first >= last:
		return

	merge_sort(arr, first, (first+last)//2)
	merge_sort(arr, (first+last)//2+1, last)

	return sorting(arr, first, last)


def sorting(arr, first, last):
	mid = (first + last) // 2
	i, j = first, mid+1
	temp = []

	while i <= mid and j <= last:
		if arr[i] <= arr[j]:
			temp.append(arr[i])
			i += 1

		else:
			temp.append(arr[j])
			j += 1

	while i <= mid:
		temp.append(arr[i])
		i += 1

	while j <= last:
		temp.append(arr[j])
		j += 1

	for k in range(first, last+1):
		arr[k] = temp[k-first]

	return arr

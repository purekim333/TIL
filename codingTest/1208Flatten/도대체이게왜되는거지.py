for tc in range(1, 11) :
    dump = int(input())

    arr = list(map(int, input().split()))

    for atmpt in range(dump) :
        mx_number = 0
        mn_number = 0
        for i in range(100) :
            if arr[mx_number] < arr[i] :
                mx_number = i

            if arr[mn_number] > arr[i] :
                # mn_height = arr[i]
                mn_number = i
        
        if arr[mx_number] - arr[mn_number] <= 1:
            break

        # mx_height = arr[mx_number]
        # mn_height = arr[mn_number]

        arr[mx_number] -= 1
        arr[mn_number] += 1

    mx_height = arr[0]
    mn_height = arr[0]
    for i in range(1, 100) :
        if mx_height < arr[i] :
            mx_height = arr[i]
        if mn_height > arr[i] :
            mn_height = arr[i]
        # if mx_height - 1 - mn_height + 1 <= 1:
        #     break

    answer = mx_height - mn_height

    print(f'#{tc} {answer}')   
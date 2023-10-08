def main(n:int, sc_list:list):
    f_count_slime = sum([sc[1] for sc in sc_list])
    num_slime = sum([sc[1] for sc in sc_list])
    sorted_sc_list = sorted(sc_list, key=lambda x:x[0])
    # 方針→サイズが小さい順に並べて、小さいスライムから合体させていく。
    # 1. countが2以上かつ、 2倍のサイズがもともと0個の場合、そのサイズのカウントは0であるとsc_listに入れる
    # 2. 実際にスライムを合体させる。このとき、個数/2だけ合体させられるので、個数/2だけ2倍のサイズのカウントを増やす
    # 3. sc_list をまたサイズが小さい順に並べる
    size_list = [sc[0] for sc in sc_list]
    for i in range(f_count_slime):
        if len(sorted_sc_list) == 0:
            break
        size, count = sorted_sc_list[i]
        if count > 1 and 2*size not in size_list:
            sorted_sc_list.append((2*size, count//2))
            sorted_sc_list = sorted(sorted_sc_list, key=lambda x:x[0])
            size_list.append(2*size)
        else:
            # sc[0] == 2*size のところに size_list に count//2 を足す
            for i in range(len(sorted_sc_list)):
                if sorted_sc_list[i][0] == 2*size:
                    sorted_sc_list[i][1] += count//2
        num_slime -= count//2
    print(num_slime)

if __name__ == "__main__":
    n = int(input())
    sc_list = [list(map(int, input().split())) for _ in range(n)]
    main(n=n, sc_list=sc_list)
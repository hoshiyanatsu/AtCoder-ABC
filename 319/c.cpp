#include <array>
#include <iostream>
#include <vector>
#include <tuple>
#include <numeric>
#include <algorithm>

int main()
{
    using namespace std;
    array<int, 9> cells;
    array<int, 9> order; // i 個めのマスが何回目に開けられるか
    iota(begin(order), end(order), 0);
    for (int i = 0; i < order.size(); ++i) {
        std::cout << "order[" << i << "] = " << order[i] << std::endl;
    }

    return 0;
}
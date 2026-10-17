from pathlib import Path

ROOT = Path(".")
COURSE = ROOT / "courses" / "data-structures-and-algorithms"
LESSONS_DIR = COURSE / "lessons"
LESSONS_DIR.mkdir(parents=True, exist_ok=True)

LESSONS = [
    {
        "num": 1,
        "slug": "lesson-01",
        "title": "Tổng quan DSA và độ phức tạp thuật toán",
        "pdf": ["01_Do_Phuc_Tap_Thuat_Toan.pdf"],
        "intro": "Bài mở đầu giúp người mới hiểu DSA là gì, vì sao phải học độ phức tạp và cách đọc Big O khi phân tích thuật toán.",
        "focus": [
            "Độ phức tạp thời gian và không gian.",
            "Big O: O(1), O(log n), O(n), O(n log n), O(n^2), O(2^n), O(n!).",
            "Đếm vòng lặp, đệ quy và bộ nhớ phụ.",
            "Giới hạn thời gian trong bài chấm online.",
        ],
        "example_set": "complexity",
        "quiz_keyword": "độ phức tạp",
        "quiz_use": "so sánh thuật toán, ước lượng tốc độ chạy, chọn lời giải phù hợp",
    },
    {
        "num": 2,
        "slug": "lesson-02",
        "title": "Các hệ đếm phổ biến và hàm",
        "pdf": ["02_Cac_He_Dem_Pho_Bien.pdf", "03_Ham.pdf"],
        "intro": "Bài này ghép hai nền tảng quan trọng: hệ nhị phân, bát phân, thập lục phân và tư duy chia chương trình thành hàm nhỏ.",
        "focus": [
            "Đổi hệ 10 sang 2, 8, 16 và ngược lại.",
            "Ý nghĩa của bit và tiền tố 0x.",
            "Cú pháp hàm, prototype, tham trị và tham chiếu.",
            "Nạp chồng hàm và hàm toán học thường dùng.",
        ],
        "example_set": "numbers_functions",
        "quiz_keyword": "hệ đếm và hàm",
        "quiz_use": "đọc bit, viết hàm, chia nhỏ chương trình, tối ưu code",
    },
    {
        "num": 3,
        "slug": "lesson-03",
        "title": "Đệ quy",
        "pdf": ["04_De_Quy.pdf"],
        "intro": "Đệ quy là cách viết hàm gọi lại chính nó. Bài học này giúp bạn hiểu stack frame, điều kiện dừng và công thức truy hồi.",
        "focus": [
            "Stack và stack frame.",
            "Điều kiện dừng và bài toán con nhỏ nhất.",
            "Công thức truy hồi.",
            "Đệ quy trong tính tổng, Fibonacci, đổi hệ đếm.",
        ],
        "example_set": "recursion",
        "quiz_keyword": "đệ quy",
        "quiz_use": "chia nhỏ bài toán, duyệt cây, quay lui, công thức truy hồi",
    },
    {
        "num": 4,
        "slug": "lesson-04",
        "title": "Vector và mảng một chiều",
        "pdf": ["05_Vector.pdf", "06_Mang_1_Chieu.pdf"],
        "intro": "Bài này đi từ mảng một chiều đến vector để bạn thấy cách lưu danh sách số liệu, duyệt, tìm max/min và đếm tần suất.",
        "focus": [
            "Vector là mảng động của STL.",
            "Mảng một chiều lưu liên tiếp trong bộ nhớ.",
            "Chỉ số bắt đầu từ 0 và không có kiểm tra biên tự động.",
            "Bài toán max/min, tổng, đếm xuất hiện.",
        ],
        "example_set": "array_vector",
        "quiz_keyword": "vector và mảng",
        "quiz_use": "lưu danh sách số liệu, duyệt phần tử, thống kê cơ bản",
    },
    {
        "num": 5,
        "slug": "lesson-05",
        "title": "Mảng hai chiều, prefix sum và mảng hiệu",
        "pdf": ["07_Mang_2_Chieu.pdf", "08_Mang_Cong_Don_Hieu.pdf"],
        "intro": "Bài này mở rộng tư duy từ mảng 1D sang ma trận, rồi dùng prefix sum và mảng hiệu để tối ưu truy vấn và cập nhật đoạn.",
        "focus": [
            "Mảng hai chiều, hàng và cột.",
            "Prefix sum 1D và 2D.",
            "Mảng hiệu cho cập nhật đoạn.",
            "Tối ưu truy vấn nhiều lần.",
        ],
        "example_set": "matrix_prefix",
        "quiz_keyword": "mảng hai chiều và prefix",
        "quiz_use": "ma trận, tổng đoạn, cập nhật đoạn, tối ưu nhiều truy vấn",
    },
    {
        "num": 6,
        "slug": "lesson-06",
        "title": "String",
        "pdf": ["09_String.pdf"],
        "intro": "Chuỗi ký tự là kiểu dữ liệu xuất hiện khắp nơi: tên, câu, từ khóa, số lớn và xử lý input. Bài này dạy nhập xuất, hàm chuỗi và stringstream.",
        "focus": [
            "Nhập chuỗi có và không có dấu cách.",
            "Các hàm length, size, substr, find, erase, replace.",
            "Trôi lệnh khi dùng cin và getline.",
            "Tách từ bằng stringstream và xử lý số lớn.",
        ],
        "example_set": "string",
        "quiz_keyword": "string",
        "quiz_use": "xử lý văn bản, tên, câu, số lớn, tách từ",
    },
    {
        "num": 7,
        "slug": "lesson-07",
        "title": "Set và Map",
        "pdf": ["10_Set.pdf", "11_Map.pdf"],
        "intro": "Bài này ghép hai container rất mạnh của STL: set để loại trùng và map để lưu cặp key-value, đếm tần suất và gom nhóm dữ liệu.",
        "focus": [
            "Set, multiset, unordered_set.",
            "Map, multimap, unordered_map.",
            "insert, find, count, erase, begin, rbegin.",
            "Khi nào cần thứ tự và khi nào cần hash.",
        ],
        "example_set": "set_map",
        "quiz_keyword": "set và map",
        "quiz_use": "loại trùng, đếm tần suất, ánh xạ khóa-giá trị",
    },
    {
        "num": 8,
        "slug": "lesson-08",
        "title": "Stack, queue và priority_queue",
        "pdf": ["12_Ngan_Xep_Hang_Doi.pdf", "26_Ngan_Xep_Hang_Doi_CTDL.pdf"],
        "intro": "Bài này gộp stack, queue và priority_queue, giải thích LIFO, FIFO và cách lấy phần tử ưu tiên nhất trong C++ STL.",
        "focus": [
            "Stack cho ngoặc đúng và biểu thức.",
            "Queue cho hàng chờ và BFS.",
            "Priority_queue cho max-heap và min-heap.",
            "Các hàm push, pop, top, front, back, empty, size.",
        ],
        "example_set": "stack_queue",
        "quiz_keyword": "stack queue priority_queue",
        "quiz_use": "ngoặc đúng, mô phỏng hàng chờ, BFS, chọn phần tử ưu tiên",
    },
    {
        "num": 9,
        "slug": "lesson-09",
        "title": "Sắp xếp và tìm kiếm",
        "pdf": ["13_Thuat_Toan_Sap_Xep.pdf", "14_Thuat_Toan_Tim_Kiem.pdf"],
        "intro": "Bài này đi qua các thuật toán sắp xếp cơ bản và tìm kiếm tuyến tính, nhị phân, cùng lower_bound và upper_bound.",
        "focus": [
            "Selection, bubble, insertion, counting, merge, quick.",
            "sort và stable_sort trong STL.",
            "Linear search, binary search và các biến thể.",
            "Điều kiện phải sắp xếp trước khi dùng binary search.",
        ],
        "example_set": "sort_search",
        "quiz_keyword": "sắp xếp và tìm kiếm",
        "quiz_use": "chuẩn bị dữ liệu, tra cứu phần tử, lấy cận dưới/cận trên",
    },
    {
        "num": 10,
        "slug": "lesson-10",
        "title": "Thuật toán sinh",
        "pdf": ["15_Thuat_Toan_Sinh.pdf"],
        "intro": "Thuật toán sinh liệt kê có hệ thống các cấu hình như xâu nhị phân, tổ hợp, hoán vị, phân hoạch và tập con bằng bitmask.",
        "focus": [
            "Cấu hình đầu tiên, cấu hình cuối cùng, cấu hình kế tiếp.",
            "Sinh xâu nhị phân, tổ hợp, hoán vị.",
            "Sinh phân hoạch và tập con bằng bit.",
            "next_permutation và prev_permutation.",
        ],
        "example_set": "generation",
        "quiz_keyword": "thuật toán sinh",
        "quiz_use": "liệt kê cấu hình, tổ hợp, hoán vị, tập con",
    },
    {
        "num": 11,
        "slug": "lesson-11",
        "title": "Cây nhị phân và BST",
        "pdf": ["17_Cay_Nhi_Phan.pdf"],
        "intro": "Bài này giới thiệu cây nhị phân, các kiểu cây và cây tìm kiếm nhị phân BST cùng các thao tác duyệt, tìm, chèn, xóa.",
        "focus": [
            "Node gốc, cha, lá, mức, chiều sâu, chiều cao.",
            "Full, perfect, complete, balanced tree.",
            "Inorder, preorder, postorder, level order, spiral order.",
            "BST search, insert và delete.",
        ],
        "example_set": "tree",
        "quiz_keyword": "cây nhị phân",
        "quiz_use": "biểu diễn phân cấp, tìm kiếm, duyệt cây, BST",
    },
    {
        "num": 12,
        "slug": "lesson-12",
        "title": "Khái niệm và biểu diễn đồ thị",
        "pdf": ["18_Graph_01_Khai_Niem_Co_Ban.pdf", "19_Graph_02_Bieu_Dien_Do_Thi.pdf"],
        "intro": "Bài này đặt nền cho đồ thị: định nghĩa, bậc đỉnh, đường đi, chu trình, liên thông và cách lưu đồ thị bằng ma trận kề hoặc danh sách kề.",
        "focus": [
            "Đồ thị vô hướng, có hướng, đa đồ thị, giả đồ thị.",
            "Đỉnh kề, cạnh liên thuộc, bậc và bán bậc.",
            "Đường đi, chu trình, liên thông, SCC/weakly connected.",
            "Ma trận kề, danh sách cạnh, danh sách kề.",
        ],
        "example_set": "graph_basic",
        "quiz_keyword": "đồ thị",
        "quiz_use": "mô hình hóa quan hệ, lưu mạng lưới, chuẩn bị DFS/BFS",
    },
    {
        "num": 13,
        "slug": "lesson-13",
        "title": "DFS, BFS và ứng dụng",
        "pdf": ["20_Graph_03_DFS_BFS.pdf", "21_Graph_04_Ung_Dung_DFS_BFS.pdf"],
        "intro": "DFS và BFS là hai công cụ duyệt đồ thị cơ bản nhất, đồng thời là nền cho thành phần liên thông, đường đi, chu trình, đỉnh trụ và cạnh cầu.",
        "focus": [
            "DFS đi sâu, BFS đi rộng.",
            "Visited, queue, đệ quy và parent.",
            "Đếm thành phần liên thông, tìm đường đi.",
            "Duyệt mảng hai chiều như một đồ thị lưới.",
        ],
        "example_set": "dfs_bfs",
        "quiz_keyword": "dfs bfs",
        "quiz_use": "duyệt đồ thị, tìm đường, đếm thành phần, flood fill",
    },
    {
        "num": 14,
        "slug": "lesson-14",
        "title": "Topo, SCC và Tarjan cơ bản",
        "pdf": ["22_Graph_05_Thanh_Phan_Lien_Thong.pdf"],
        "intro": "Bài này đi vào đồ thị có hướng: sắp xếp topo, thành phần liên thông mạnh và ý tưởng Tarjan qua mảng disc, low.",
        "focus": [
            "Topo chỉ áp dụng cho DAG.",
            "Kahn và DFS cho topological sort.",
            "Kosaraju để tìm SCC.",
            "Disc, low và logic của Tarjan.",
        ],
        "example_set": "topo_tarjan",
        "quiz_keyword": "topo và SCC",
        "quiz_use": "xử lý phụ thuộc, DAG, tách thành phần liên thông mạnh",
    },
    {
        "num": 15,
        "slug": "lesson-15",
        "title": "DSU, Kruskal và Prim",
        "pdf": ["23_Graph_06_DSU.pdf", "24_Graph_07_Cay_Khung_Toi_Thieu.pdf"],
        "intro": "Bài này nối DSU với cây khung nhỏ nhất: biết Find/Union rồi dùng chúng trong Kruskal, sau đó so sánh với Prim.",
        "focus": [
            "DSU, Find, Union, path compression, union by size.",
            "MST trên đồ thị vô hướng liên thông.",
            "Kruskal chọn cạnh nhỏ nhất không tạo chu trình.",
            "Prim mở rộng cây bằng priority_queue.",
        ],
        "example_set": "dsu_mst",
        "quiz_keyword": "dsu mst",
        "quiz_use": "gộp nhóm, kiểm tra chu trình, nối mạng tối ưu",
    },
    {
        "num": 16,
        "slug": "lesson-16",
        "title": "Đường đi ngắn nhất và mini project",
        "pdf": ["25_Graph_08_Dang_Di_Ngan_Nhat.pdf", "Tổng hợp"],
        "intro": "Bài cuối tổng hợp Dijkstra, Bellman-Ford, Floyd-Warshall và một mini project ôn tập để nối các kỹ thuật đã học.",
        "focus": [
            "Dijkstra cho cạnh không âm.",
            "Bellman-Ford cho cạnh âm và chu trình âm.",
            "Floyd-Warshall cho mọi cặp đỉnh.",
            "Ôn tập vector, map, set, sort và graph.",
        ],
        "example_set": "shortest_review",
        "quiz_keyword": "đường đi ngắn nhất",
        "quiz_use": "bản đồ, định tuyến, khoảng cách giữa các đỉnh",
    },
]


def esc(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


EXAMPLES = {
    "complexity": [
        (
            "Ví dụ 1: Vòng lặp đơn",
            """#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    long long sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += i;
    }
    cout << sum << endl;
    return 0;
}""",
            "Tính tổng 1..n để minh họa một vòng lặp đơn.",
            ["Nhập n.", "In tổng 1..n.", "Biến: n, sum, i.", "Đọc n rồi cộng dồn.", "O(n), O(1)."],
        ),
        (
            "Ví dụ 2: Hai vòng lặp lồng nhau",
            """#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    int cnt = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cnt++;
        }
    }
    cout << cnt << endl;
    return 0;
}""",
            "Đếm số lần lặp của hai vòng lặp lồng nhau.",
            ["Nhập n.", "In n * n.", "Biến: n, cnt, i, j.", "Vòng ngoài và vòng trong chạy n lần.", "O(n^2), O(1)."],
        ),
    ],
    "numbers_functions": [
        (
            "Ví dụ 1: Đổi hệ 10 sang hệ 2",
            """#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    if (n == 0) {
        cout << 0 << endl;
        return 0;
    }
    string bin;
    while (n > 0) {
        bin.push_back(char('0' + (n % 2)));
        n /= 2;
    }
    reverse(bin.begin(), bin.end());
    cout << bin << endl;
    return 0;
}""",
            "Đổi số thập phân sang nhị phân.",
            ["Nhập n.", "In chuỗi nhị phân.", "Biến: n, bin.", "Chia liên tiếp cho 2 rồi đảo ngược.", "O(log n)."],
        ),
        (
            "Ví dụ 2: Hàm tìm số lớn nhất và truyền tham chiếu",
            """#include <iostream>
using namespace std;

int max3(int a, int b, int c) {
    int res = a;
    if (b > res) res = b;
    if (c > res) res = c;
    return res;
}

void swap2(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}

int main() {
    int x, y, z;
    cin >> x >> y >> z;
    cout << max3(x, y, z) << endl;
    swap2(x, y);
    cout << x << ' ' << y << endl;
    return 0;
}""",
            "Minh họa prototype, hàm max3 và swap bằng tham chiếu.",
            ["Nhập 3 số.", "In số lớn nhất rồi đổi chỗ x và y.", "Biến: x, y, z, res, temp.", "Gọi hàm riêng để xử lý rõ ràng.", "O(1)."],
        ),
    ],
    "recursion": [
        (
            "Ví dụ 1: Tính tổng từ 1 đến n",
            """#include <iostream>
using namespace std;

long long sumToN(int n) {
    if (n == 0) return 0;
    return n + sumToN(n - 1);
}

int main() {
    int n;
    cin >> n;
    cout << sumToN(n) << endl;
    return 0;
}""",
            "Đệ quy tính tổng 1..n.",
            ["Nhập n.", "In tổng.", "Biến: n.", "Base case là n = 0.", "O(n)."],
        ),
        (
            "Ví dụ 2: Tính tổng chữ số",
            """#include <iostream>
using namespace std;

int sumDigit(int n) {
    if (n < 10) return n;
    return n % 10 + sumDigit(n / 10);
}

int main() {
    int n;
    cin >> n;
    cout << sumDigit(n) << endl;
    return 0;
}""",
            "Đệ quy tính tổng các chữ số của một số.",
            ["Nhập n.", "In tổng chữ số.", "Biến: n.", "Tách chữ số cuối và phần còn lại.", "O(log n)."],
        ),
    ],
    "array_vector": [
        (
            "Ví dụ 1: Vector và thống kê điểm",
            """#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    int mx = a[0], mn = a[0];
    long long sum = 0;
    for (int x : a) {
        sum += x;
        if (x > mx) mx = x;
        if (x < mn) mn = x;
    }
    cout << mx << '\\n' << mn << '\\n' << sum << endl;
    return 0;
}""",
            "Dùng vector để lưu danh sách điểm và thống kê nhanh.",
            ["Nhập n và n điểm.", "In max, min, tổng.", "Biến: a, mx, mn, sum.", "Duyệt một lượt qua vector.", "O(n)."],
        ),
        (
            "Ví dụ 2: Mảng một chiều và đếm số lần xuất hiện",
            """#include <iostream>
using namespace std;

int main() {
    int n, x;
    cin >> n >> x;
    int a[1000];
    for (int i = 0; i < n; i++) cin >> a[i];
    int cnt = 0;
    for (int i = 0; i < n; i++) if (a[i] == x) cnt++;
    cout << cnt << endl;
    return 0;
}""",
            "Đếm số lần xuất hiện của x trong mảng.",
            ["Nhập n, x và dãy số.", "In số lần xuất hiện của x.", "Biến: a, x, cnt.", "Duyệt toàn bộ mảng.", "O(n)."],
        ),
    ],
    "matrix_prefix": [
        (
            "Ví dụ 1: Nhập và in ma trận",
            """#include <iostream>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    int a[100][100];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) cin >> a[i][j];
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) cout << a[i][j] << ' ';
        cout << endl;
    }
    return 0;
}""",
            "Nhập và in lại ma trận 2 chiều.",
            ["Nhập n, m và ma trận.", "In ma trận.", "Biến: a, i, j.", "Hai vòng lặp lồng nhau.", "O(nm)."],
        ),
        (
            "Ví dụ 2: Prefix sum và mảng hiệu",
            """#include <iostream>
using namespace std;

int main() {
    int n, q;
    cin >> n >> q;
    long long pre[1005] = {}, diff[1005] = {};
    for (int i = 1; i <= n; i++) {
        long long x;
        cin >> x;
        pre[i] = pre[i - 1] + x;
    }
    while (q--) {
        int l, r, val;
        cin >> l >> r >> val;
        diff[l] += val;
        diff[r + 1] -= val;
        cout << pre[r] - pre[l - 1] << endl;
    }
    return 0;
}""",
            "Minh họa tổng đoạn và cập nhật đoạn.",
            ["Nhập n, q và các truy vấn.", "In tổng đoạn rồi cập nhật đoạn.", "Biến: pre, diff, l, r, val.", "Prefix trả lời tổng, diff xử lý cập nhật.", "O(n + q)."],
        ),
    ],
    "string": [
        (
            "Ví dụ 1: Nhập chuỗi có dấu cách và đếm nguyên âm",
            """#include <iostream>
#include <string>
using namespace std;

int main() {
    cin.ignore();
    string s;
    getline(cin, s);
    int cnt = 0;
    for (char c : s) {
        c = tolower(c);
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') cnt++;
    }
    cout << cnt << endl;
    return 0;
}""",
            "Nhập một dòng và đếm nguyên âm.",
            ["Nhập cả dòng.", "In số nguyên âm.", "Biến: s, c, cnt.", "Dùng getline rồi duyệt từng ký tự.", "O(len(s))."],
        ),
        (
            "Ví dụ 2: Tách từ bằng stringstream",
            """#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main() {
    string s;
    getline(cin, s);
    stringstream ss(s);
    string word;
    int cnt = 0;
    while (ss >> word) cnt++;
    cout << cnt << endl;
    return 0;
}""",
            "Đếm số từ trong một câu.",
            ["Nhập một dòng văn bản.", "In số lượng từ.", "Biến: s, ss, word, cnt.", "Đưa chuỗi vào stringstream rồi đọc từng token.", "O(len(s))."],
        ),
    ],
    "set_map": [
        (
            "Ví dụ 1: Set loại trùng",
            """#include <iostream>
#include <set>
using namespace std;

int main() {
    int n;
    cin >> n;
    set<int> se;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        se.insert(x);
    }
    for (int x : se) cout << x << ' ';
    cout << endl;
    return 0;
}""",
            "Loại bỏ phần tử trùng và sắp xếp tăng dần.",
            ["Nhập n và n số.", "In các giá trị duy nhất.", "Biến: se, x.", "Chèn từng số vào set.", "O(n log n)."],
        ),
        (
            "Ví dụ 2: Map đếm tần suất",
            """#include <iostream>
#include <map>
using namespace std;

int main() {
    int n;
    cin >> n;
    map<int, int> mp;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        mp[x]++;
    }
    for (auto it : mp) cout << it.first << ' ' << it.second << '\\n';
    return 0;
}""",
            "Đếm tần suất bằng map.",
            ["Nhập n và dãy số.", "In cặp giá trị - tần suất.", "Biến: mp, x.", "Mỗi số tăng mp[x].", "O(n log n)."],
        ),
    ],
    "stack_queue": [
        (
            "Ví dụ 1: Kiểm tra ngoặc đúng bằng stack",
            """#include <iostream>
#include <stack>
#include <string>
using namespace std;

bool check(string s) {
    stack<char> st;
    for (char c : s) {
        if (c == '(') st.push(c);
        else if (c == ')') {
            if (st.empty()) return false;
            st.pop();
        }
    }
    return st.empty();
}

int main() {
    string s;
    cin >> s;
    cout << (check(s) ? "YES" : "NO") << endl;
    return 0;
}""",
            "Kiểm tra chuỗi ngoặc tròn có cân bằng không.",
            ["Nhập chuỗi ngoặc.", "In YES hoặc NO.", "Biến: s, st.", "Gặp '(' thì push, gặp ')' thì pop.", "O(n)."],
        ),
        (
            "Ví dụ 2: Queue và priority_queue",
            """#include <iostream>
#include <queue>
using namespace std;

int main() {
    queue<int> q;
    q.push(10);
    q.push(20);
    cout << q.front() << endl;
    q.pop();

    priority_queue<int> pq;
    pq.push(4);
    pq.push(9);
    cout << pq.top() << endl;
    return 0;
}""",
            "Minh họa queue FIFO và priority_queue max-heap.",
            ["Không cần input.", "In đầu queue và top của heap.", "Biến: q, pq.", "Push rồi lấy front/top.", "O(log n) với priority_queue."],
        ),
    ],
    "sort_search": [
        (
            "Ví dụ 1: Selection sort",
            """#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[1000];
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < n - 1; i++) {
        int pos = i;
        for (int j = i + 1; j < n; j++) if (a[j] < a[pos]) pos = j;
        swap(a[i], a[pos]);
    }
    for (int i = 0; i < n; i++) cout << a[i] << ' ';
    cout << endl;
    return 0;
}""",
            "Sắp xếp mảng bằng selection sort.",
            ["Nhập n và dãy số.", "In dãy đã sắp xếp.", "Biến: a, pos.", "Mỗi lượt chọn phần tử nhỏ nhất còn lại.", "O(n^2)."],
        ),
        (
            "Ví dụ 2: Binary search và lower_bound",
            """#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int a[] = {1, 2, 2, 4, 5, 7};
    auto it1 = lower_bound(a, a + 6, 2);
    auto it2 = upper_bound(a, a + 6, 2);
    cout << (it1 - a) << '\\n' << (it2 - a) << endl;
    return 0;
}""",
            "Dùng STL để tìm cận dưới và cận trên.",
            ["Không cần input.", "In hai vị trí cận.", "Biến: a, it1, it2.", "Dùng thuật toán nhị phân của STL.", "O(log n)."],
        ),
    ],
    "generation": [
        (
            "Ví dụ 1: Sinh xâu nhị phân",
            """#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    for (int mask = 0; mask < (1 << n); mask++) {
        for (int i = n - 1; i >= 0; i--) cout << ((mask >> i) & 1);
        cout << endl;
    }
    return 0;
}""",
            "Liệt kê mọi xâu nhị phân độ dài n bằng bitmask.",
            ["Nhập n.", "In tất cả cấu hình.", "Biến: n, mask.", "Đếm từ 0 đến 2^n - 1.", "O(n * 2^n)."],
        ),
        (
            "Ví dụ 2: Sinh hoán vị bằng next_permutation",
            """#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int a[4] = {1, 2, 3, 4};
    do {
        for (int i = 0; i < 4; i++) cout << a[i] << ' ';
        cout << endl;
    } while (next_permutation(a, a + 4));
    return 0;
}""",
            "Sinh các hoán vị của dãy 1..4.",
            ["Không cần input.", "In từng hoán vị.", "Biến: a.", "Lặp next_permutation đến khi hết.", "O(n * n!)."],
        ),
    ],
    "tree": [
        (
            "Ví dụ 1: Duyệt cây nhị phân",
            """#include <iostream>
using namespace std;

struct Node { int data; Node *left, *right; };

Node* makeNode(int x) {
    Node* p = new Node();
    p->data = x;
    p->left = p->right = nullptr;
    return p;
}

void inorder(Node* root) {
    if (!root) return;
    inorder(root->left);
    cout << root->data << ' ';
    inorder(root->right);
}

int main() {
    Node* root = makeNode(1);
    root->left = makeNode(2);
    root->right = makeNode(3);
    inorder(root);
    return 0;
}""",
            "Tạo cây mẫu và duyệt inorder.",
            ["Không cần input.", "In thứ tự inorder.", "Biến: root, left, right.", "Đệ quy trái - gốc - phải.", "O(n)."],
        ),
        (
            "Ví dụ 2: BST search và insert",
            """#include <iostream>
using namespace std;

struct Node { int data; Node *left, *right; };

Node* makeNode(int x) {
    Node* p = new Node();
    p->data = x;
    p->left = p->right = nullptr;
    return p;
}

Node* insert(Node* root, int x) {
    if (!root) return makeNode(x);
    if (x < root->data) root->left = insert(root->left, x);
    else if (x > root->data) root->right = insert(root->right, x);
    return root;
}

bool search(Node* root, int x) {
    if (!root) return false;
    if (root->data == x) return true;
    if (x < root->data) return search(root->left, x);
    return search(root->right, x);
}

int main() {
    Node* root = nullptr;
    root = insert(root, 5);
    root = insert(root, 3);
    root = insert(root, 7);
    cout << search(root, 7) << endl;
    return 0;
}""",
            "Chèn và tìm kiếm trong BST.",
            ["Không cần input.", "In 1 nếu tìm thấy 7.", "Biến: root, x.", "Đi theo nhánh trái/phải đúng quy tắc BST.", "Trung bình O(log n)."],
        ),
    ],
    "graph_basic": [
        (
            "Ví dụ 1: Ma trận kề",
            """#include <iostream>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    int a[105][105] = {};
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        a[u][v] = 1;
        a[v][u] = 1;
    }
    cout << a[1][2] << endl;
    return 0;
}""",
            "Lưu và kiểm tra cạnh bằng ma trận kề.",
            ["Nhập n, m và các cạnh.", "In 0 hoặc 1.", "Biến: a, u, v.", "Đánh dấu hai chiều trong đồ thị vô hướng.", "O(1) kiểm tra cạnh, O(n^2) bộ nhớ."],
        ),
        (
            "Ví dụ 2: Danh sách kề",
            """#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> adj[1005];
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    cout << adj[1].size() << endl;
    return 0;
}""",
            "Lưu đồ thị bằng danh sách kề.",
            ["Nhập n, m và các cạnh.", "In số đỉnh kề với 1.", "Biến: adj, u, v.", "Mỗi đỉnh giữ một vector đỉnh kề.", "O(n + m)."],
        ),
    ],
    "dfs_bfs": [
        (
            "Ví dụ 1: DFS và BFS",
            """#include <iostream>
#include <algorithm>
#include <functional>
#include <vector>
#include <queue>
using namespace std;

vector<int> adj[1005];
bool vis[1005];

void DFS(int u) {
    vis[u] = true;
    cout << u << ' ';
    for (int v : adj[u]) if (!vis[v]) DFS(v);
}

void BFS(int s) {
    queue<int> q;
    q.push(s);
    vis[s] = true;
    while (!q.empty()) {
        int u = q.front(); q.pop();
        cout << u << ' ';
        for (int v : adj[u]) if (!vis[v]) {
            vis[v] = true;
            q.push(v);
        }
    }
}

int main() {
    adj[1].push_back(2); adj[2].push_back(1);
    adj[2].push_back(3); adj[3].push_back(2);
    DFS(1);
    cout << '\\n';
    fill(vis, vis + 1005, false);
    BFS(1);
    return 0;
}""",
            "Minh họa DFS và BFS trên cùng một đồ thị nhỏ.",
            ["Không cần input.", "In thứ tự duyệt DFS và BFS.", "Biến: adj, vis, q.", "DFS dùng đệ quy, BFS dùng queue.", "O(V + E)."],
        ),
        (
            "Ví dụ 2: Tìm đường đi và flood fill trên grid",
            """#include <iostream>
#include <queue>
using namespace std;

int n = 3, m = 3;
int a[3][3] = {{1,1,0},{0,1,0},{0,0,1}};
bool vis[3][3];
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

void DFS(int i, int j) {
    vis[i][j] = true;
    for (int k = 0; k < 4; k++) {
        int ni = i + dx[k], nj = j + dy[k];
        if (ni >= 0 && ni < n && nj >= 0 && nj < m && !vis[ni][nj] && a[ni][nj] == 1) DFS(ni, nj);
    }
}

int main() {
    int comp = 0;
    for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) if (!vis[i][j] && a[i][j] == 1) {
        comp++;
        DFS(i, j);
    }
    cout << comp << endl;
    return 0;
}""",
            "Đếm số vùng liên thông trên ma trận.",
            ["Không cần input.", "In số vùng có giá trị 1.", "Biến: a, vis, dx, dy, comp.", "Mỗi ô mới kích hoạt một DFS.", "O(nm)."],
        ),
    ],
    "topo_tarjan": [
        (
            "Ví dụ 1: Topological sort bằng Kahn",
            """#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
    int n = 4;
    vector<int> adj[5];
    adj[1] = {2, 3};
    adj[2] = {4};
    adj[3] = {4};
    vector<int> indeg(n + 1, 0);
    for (int u = 1; u <= n; u++) for (int v : adj[u]) indeg[v]++;
    queue<int> q;
    for (int i = 1; i <= n; i++) if (indeg[i] == 0) q.push(i);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        cout << u << ' ';
        for (int v : adj[u]) if (--indeg[v] == 0) q.push(v);
    }
    return 0;
}""",
            "Sắp xếp topo bằng thuật toán Kahn.",
            ["Không cần input.", "In một thứ tự topo.", "Biến: adj, indeg, q.", "Lấy dần đỉnh indegree 0.", "O(V + E)."],
        ),
        (
            "Ví dụ 2: Tarjan cơ bản với disc và low",
            """#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

vector<int> adj[1005];
bool vis[1005];
int disc[1005], low[1005], timer = 0;

void DFS(int u, int p = -1) {
    vis[u] = true;
    disc[u] = low[u] = ++timer;
    for (int v : adj[u]) {
        if (v == p) continue;
        if (!vis[v]) {
            DFS(v, u);
            low[u] = min(low[u], low[v]);
        } else {
            low[u] = min(low[u], disc[v]);
        }
    }
}

int main() {
    adj[1].push_back(2); adj[2].push_back(1);
    adj[2].push_back(3); adj[3].push_back(2);
    DFS(1);
    cout << disc[1] << ' ' << low[1] << endl;
    return 0;
}""",
            "Minh họa ý tưởng disc và low.",
            ["Không cần input.", "In disc và low của đỉnh 1.", "Biến: adj, vis, disc, low, timer.", "DFS gán thời điểm thăm rồi cập nhật low.", "O(V + E)."],
        ),
    ],
    "dsu_mst": [
        (
            "Ví dụ 1: DSU cơ bản",
            """#include <iostream>
using namespace std;

const int MAXN = 1005;
int parent[MAXN], sz[MAXN];

int Find(int u) {
    if (u == parent[u]) return u;
    return parent[u] = Find(parent[u]);
}

bool Union(int u, int v) {
    u = Find(u); v = Find(v);
    if (u == v) return false;
    if (sz[u] < sz[v]) swap(u, v);
    parent[v] = u;
    sz[u] += sz[v];
    return true;
}

int main() {
    for (int i = 1; i <= 4; i++) parent[i] = i, sz[i] = 1;
    Union(1, 2);
    Union(2, 3);
    cout << (Find(1) == Find(3)) << endl;
    return 0;
}""",
            "Kiểm tra hai đỉnh có cùng tập hay không.",
            ["Không cần input.", "In 1 nếu cùng tập.", "Biến: parent, sz.", "Find nén đường đi, Union gộp theo size.", "Gần O(1) trung bình."],
        ),
        (
            "Ví dụ 2: Kruskal và Prim",
            """#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

struct Edge { int u, v, w; };

int main() {
    vector<Edge> edges = {{1,2,1}, {1,3,4}, {2,3,2}, {2,4,3}};
    sort(edges.begin(), edges.end(), [](Edge a, Edge b) { return a.w < b.w; });
    int cost = 0;
    for (auto e : edges) cost += e.w;
    cout << cost << endl;
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
    pq.push({0, 1});
    cout << pq.top().first << endl;
    return 0;
}""",
            "Gợi ý cách nghĩ Kruskal và Prim.",
            ["Không cần input.", "In tổng và phần tử đỉnh của heap.", "Biến: edges, cost, pq.", "Sort cạnh, rồi dùng heap lấy cạnh nhỏ nhất.", "O(E log E) và O(E log V)."],
        ),
    ],
    "shortest_review": [
        (
            "Ví dụ 1: Dijkstra",
            """#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int main() {
    vector<pair<int,int>> adj[5];
    adj[1].push_back({2, 2});
    adj[1].push_back({3, 5});
    adj[2].push_back({3, 1});
    adj[2].push_back({4, 4});
    const int INF = 1e9;
    vector<int> dist(5, INF);
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
    dist[1] = 0;
    pq.push({0, 1});
    while (!pq.empty()) {
        auto [du, u] = pq.top(); pq.pop();
        if (du != dist[u]) continue;
        for (auto [v, w] : adj[u]) if (dist[v] > dist[u] + w) {
            dist[v] = dist[u] + w;
            pq.push({dist[v], v});
        }
    }
    cout << dist[4] << endl;
    return 0;
}""",
            "Tìm đường đi ngắn nhất bằng Dijkstra.",
            ["Không cần input.", "In khoảng cách đến đỉnh 4.", "Biến: adj, dist, pq.", "Luôn relax cạnh từ đỉnh có dist nhỏ nhất hiện tại.", "O((V + E) log V)."],
        ),
        (
            "Ví dụ 2: Bellman-Ford",
            """#include <iostream>
#include <vector>
using namespace std;

struct Edge { int u, v, w; };

int main() {
    vector<Edge> edges = {{1,2,4}, {2,3,-2}, {1,3,5}};
    const int INF = 1e9;
    vector<int> dist(4, INF);
    dist[1] = 0;
    for (int i = 1; i <= 2; i++) {
        for (auto e : edges) if (dist[e.u] < INF && dist[e.v] > dist[e.u] + e.w) {
            dist[e.v] = dist[e.u] + e.w;
        }
    }
    cout << dist[3] << endl;
    return 0;
}""",
            "Tìm đường đi ngắn nhất khi có cạnh âm.",
            ["Không cần input.", "In khoảng cách đến đỉnh 3.", "Biến: edges, dist.", "Lặp n - 1 lần và relax toàn bộ cạnh.", "O(VE)."],
        ),
        (
            "Ví dụ 3: Floyd-Warshall",
            """#include <iostream>
#include <algorithm>
using namespace std;

const int INF = 1e9;
int d[4][4];

int main() {
    for (int i = 1; i <= 3; i++) for (int j = 1; j <= 3; j++) d[i][j] = (i == j ? 0 : INF);
    d[1][2] = 3;
    d[2][3] = 4;
    for (int k = 1; k <= 3; k++) {
        for (int i = 1; i <= 3; i++) {
            for (int j = 1; j <= 3; j++) {
                if (d[i][k] < INF && d[k][j] < INF) d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
            }
        }
    }
    cout << d[1][3] << endl;
    return 0;
}""",
            "Tính khoảng cách giữa mọi cặp đỉnh.",
            ["Không cần input.", "In khoảng cách từ 1 đến 3.", "Biến: d, k, i, j.", "Thử từng đỉnh trung gian.", "O(n^3)."],
        ),
    ],
}


def render_example(num, title, code, purpose, bullets):
    return f"""
<div class=\"card mb-3\">
  <div class=\"card-body\">
    <h3 class=\"h5 fw-bold\">{esc(title)}</h3>
    <pre><code>{esc(code)}</code></pre>
    <h4 class=\"h6 fw-bold\">Giải thích chương trình</h4>
    <ul>
      <li><strong>Chương trình làm gì:</strong> {esc(purpose)}</li>
      <li><strong>Input:</strong> {esc(bullets[0])}</li>
      <li><strong>Output:</strong> {esc(bullets[1])}</li>
      <li><strong>Biến chính:</strong> {esc(bullets[2])}</li>
      <li><strong>Luồng chạy:</strong> {esc(bullets[3])}</li>
      <li><strong>Độ phức tạp / kết quả kỳ vọng:</strong> {esc(bullets[4])}</li>
    </ul>
  </div>
</div>
"""


def render_examples(kind):
    return "\n".join(render_example(i + 1, title, code, purpose, bullets) for i, (title, code, purpose, bullets) in enumerate(EXAMPLES[kind]))


def render_theory(spec):
    return f"""
<section class=\"lesson-section\">
  <h2>1. Tài liệu lý thuyết</h2>
  <div class=\"alert alert-primary\">
    <strong>Nội dung chính từ PDF:</strong>
    <ul class=\"mb-0 mt-2\">
      {''.join(f'<li>{esc(item)}</li>' for item in spec['focus'])}
    </ul>
  </div>
  <p>{esc(spec['intro'])}</p>
  <p>Trong bài này, điều quan trọng nhất là không chỉ nhớ định nghĩa mà còn phải biết bài toán nào nên dùng kỹ thuật nào, vì sao nó chạy nhanh hơn và khi nào không nên áp dụng. Khi đọc PDF gốc, hãy để ý các ví dụ và công thức vì chúng thường là điểm quyết định để làm bài tập.</p>
  <p>Ở level của sinh viên năm nhất và người tự học, mục tiêu là hiểu thật rõ dữ liệu đang được lưu như thế nào, thao tác nào là O(1), thao tác nào là O(log n) hoặc O(n), rồi dùng kiến thức đó để chọn lời giải hợp lý hơn. Đây là tinh thần xuyên suốt toàn bộ khóa học.</p>
</section>
"""


def render_practice(spec):
    k = esc(spec['quiz_keyword'])
    return f"""
<section class=\"lesson-section\">
  <h2>Bài tập thực hành</h2>
  <div class=\"row g-3\">
    <div class=\"col-12 col-md-6\"><div class=\"p-3 border rounded-3 h-100\"><h3 class=\"h6 fw-bold\">Dễ 1</h3><p class=\"mb-0\">Viết chương trình nhỏ áp dụng {k} với input đơn giản.</p></div></div>
    <div class=\"col-12 col-md-6\"><div class=\"p-3 border rounded-3 h-100\"><h3 class=\"h6 fw-bold\">Dễ 2</h3><p class=\"mb-0\">Thêm comment tiếng Việt cho từng khối logic trong chương trình.</p></div></div>
    <div class=\"col-12 col-md-6\"><div class=\"p-3 border rounded-3 h-100\"><h3 class=\"h6 fw-bold\">Dễ 3</h3><p class=\"mb-0\">Thử đổi input biên để xem chương trình còn đúng không.</p></div></div>
    <div class=\"col-12 col-md-6\"><div class=\"p-3 border rounded-3 h-100\"><h3 class=\"h6 fw-bold\">Trung bình 1</h3><p class=\"mb-0\">Kết hợp {k} với một cấu trúc dữ liệu đã học để giải bài toán nhỏ.</p></div></div>
    <div class=\"col-12 col-md-6\"><div class=\"p-3 border rounded-3 h-100\"><h3 class=\"h6 fw-bold\">Trung bình 2</h3><p class=\"mb-0\">Tự thiết kế test case và phân tích độ phức tạp của lời giải.</p></div></div>
  </div>
</section>
"""


def render_quiz(spec):
    k = esc(spec['quiz_keyword'])
    u = esc(spec['quiz_use'])
    n = spec['num']
    return f"""
<section class=\"lesson-section\">
  <h2>Trắc nghiệm JavaScript</h2>
  <form id=\"quiz-form-{n}\" class=\"vstack gap-3\">
    <div><p class=\"fw-semibold mb-2\">1. Mục tiêu chính của {k} là gì?</p>
      <div class=\"form-check\"><input class=\"form-check-input\" type=\"radio\" name=\"q1\" id=\"q{n}1a\" value=\"a\"><label class=\"form-check-label\" for=\"q{n}1a\">Giúp giải quyết {u}</label></div>
      <div class=\"form-check\"><input class=\"form-check-input\" type=\"radio\" name=\"q1\" id=\"q{n}1b\" value=\"b\"><label class=\"form-check-label\" for=\"q{n}1b\">Chỉ để trang trí code</label></div>
      <div class=\"form-check\"><input class=\"form-check-input\" type=\"radio\" name=\"q1\" id=\"q{n}1c\" value=\"c\"><label class=\"form-check-label\" for=\"q{n}1c\">Thay thế mọi cú pháp C++</label></div>
    </div>
    <div><p class=\"fw-semibold mb-2\">2. Khi nào nên nghĩ đến {k}?</p>
      <div class=\"form-check\"><input class=\"form-check-input\" type=\"radio\" name=\"q2\" id=\"q{n}2a\" value=\"a\"><label class=\"form-check-label\" for=\"q{n}2a\">Khi bài toán có tính lặp lại, tra cứu hoặc tối ưu rõ ràng</label></div>
      <div class=\"form-check\"><input class=\"form-check-input\" type=\"radio\" name=\"q2\" id=\"q{n}2b\" value=\"b\"><label class=\"form-check-label\" for=\"q{n}2b\">Chỉ khi không có input</label></div>
      <div class=\"form-check\"><input class=\"form-check-input\" type=\"radio\" name=\"q2\" id=\"q{n}2c\" value=\"c\"><label class=\"form-check-label\" for=\"q{n}2c\">Chỉ khi cần giao diện đồ họa</label></div>
    </div>
    <div><p class=\"fw-semibold mb-2\">3. Điều nào đúng với code ví dụ?</p>
      <div class=\"form-check\"><input class=\"form-check-input\" type=\"radio\" name=\"q3\" id=\"q{n}3a\" value=\"a\"><label class=\"form-check-label\" for=\"q{n}3a\">Code có <code>main()</code> và comment tiếng Việt</label></div>
      <div class=\"form-check\"><input class=\"form-check-input\" type=\"radio\" name=\"q3\" id=\"q{n}3b\" value=\"b\"><label class=\"form-check-label\" for=\"q{n}3b\">Code không cần thư viện</label></div>
      <div class=\"form-check\"><input class=\"form-check-input\" type=\"radio\" name=\"q3\" id=\"q{n}3c\" value=\"c\"><label class=\"form-check-label\" for=\"q{n}3c\">Code luôn chỉ cần một dòng</label></div>
    </div>
    <div><p class=\"fw-semibold mb-2\">4. Lỗi nào hay gặp nhất?</p>
      <div class=\"form-check\"><input class=\"form-check-input\" type=\"radio\" name=\"q4\" id=\"q{n}4a\" value=\"a\"><label class=\"form-check-label\" for=\"q{n}4a\">Sai điều kiện biên hoặc chọn sai cấu trúc dữ liệu</label></div>
      <div class=\"form-check\"><input class=\"form-check-input\" type=\"radio\" name=\"q4\" id=\"q{n}4b\" value=\"b\"><label class=\"form-check-label\" for=\"q{n}4b\">Viết comment tiếng Việt</label></div>
      <div class=\"form-check\"><input class=\"form-check-input\" type=\"radio\" name=\"q4\" id=\"q{n}4c\" value=\"c\"><label class=\"form-check-label\" for=\"q{n}4c\">Dùng <code>cout</code> để in kết quả</label></div>
    </div>
    <div><p class=\"fw-semibold mb-2\">5. Ứng dụng nào phù hợp nhất?</p>
      <div class=\"form-check\"><input class=\"form-check-input\" type=\"radio\" name=\"q5\" id=\"q{n}5a\" value=\"a\"><label class=\"form-check-label\" for=\"q{n}5a\">{u}</label></div>
      <div class=\"form-check\"><input class=\"form-check-input\" type=\"radio\" name=\"q5\" id=\"q{n}5b\" value=\"b\"><label class=\"form-check-label\" for=\"q{n}5b\">Vẽ logo trang web</label></div>
      <div class=\"form-check\"><input class=\"form-check-input\" type=\"radio\" name=\"q5\" id=\"q{n}5c\" value=\"c\"><label class=\"form-check-label\" for=\"q{n}5c\">Tạo tài khoản đăng nhập</label></div>
    </div>
    <div class=\"d-flex flex-wrap gap-2\">
      <button type=\"button\" class=\"btn btn-primary\" onclick=\"checkQuiz('quiz-form-{n}', 'quiz-result-{n}', {{ q1: 'a', q2: 'a', q3: 'a', q4: 'a', q5: 'a' }})\">Nộp bài</button>
      <div id=\"quiz-result-{n}\" class=\"quiz-result\"></div>
    </div>
  </form>
</section>
"""


def render_essays(spec):
    n = spec["num"]
    k = esc(spec["quiz_keyword"])
    return f"""
<section class=\"lesson-section\">
  <h2>Câu hỏi tự luận tự ôn tập</h2>
  <div class=\"mb-4\">
    <p class=\"fw-semibold mb-2\">Câu 1. Vì sao bài {n} quan trọng trong khóa học?</p>
    <textarea id=\"essay-{n}-1\" class=\"form-control mb-3\" rows=\"5\" placeholder=\"Tự viết câu trả lời của bạn...\" oninput=\"saveEssayDraft('essay-{n}-1', 'dsa-lesson-{n}-1')\"></textarea>
    <button type=\"button\" class=\"btn btn-outline-primary\" onclick=\"toggleSuggestedAnswer('answer-{n}-1')\">Xem đáp án tham khảo</button>
    <div id=\"answer-{n}-1\" class=\"suggested-answer mt-3 card\"><div class=\"card-body\"><p class=\"mb-0\">Gợi ý: bài học này là nền để hiểu các chủ đề nâng cao hơn, vì nó cho bạn cách nhìn đúng về dữ liệu, độ phức tạp và kỹ thuật giải bài.</p></div></div>
  </div>
  <div>
    <p class=\"fw-semibold mb-2\">Câu 2. Khi nào bạn sẽ chọn {k} trong một bài toán thực tế?</p>
    <textarea id=\"essay-{n}-2\" class=\"form-control mb-3\" rows=\"5\" placeholder=\"Tự viết câu trả lời của bạn...\" oninput=\"saveEssayDraft('essay-{n}-2', 'dsa-lesson-{n}-2')\"></textarea>
    <button type=\"button\" class=\"btn btn-outline-primary\" onclick=\"toggleSuggestedAnswer('answer-{n}-2')\">Xem đáp án tham khảo</button>
    <div id=\"answer-{n}-2\" class=\"suggested-answer mt-3 card\"><div class=\"card-body\"><p class=\"mb-0\">Gợi ý: hãy mô tả input, output, ràng buộc, rồi so sánh với đặc tính của {k}. Nếu nó giúp chương trình rõ ràng hơn, nhanh hơn hoặc tiết kiệm bộ nhớ hơn thì đó là lựa chọn hợp lý.</p></div></div>
  </div>
</section>
"""


def render_summary(spec):
    return f"""
<section class=\"lesson-section\">
  <h2>Tóm tắt bài học</h2>
  <ul>
    <li>{esc(spec['focus'][0])}</li>
    <li>{esc(spec['focus'][1])}</li>
    <li>{esc(spec['focus'][2])}</li>
  </ul>
</section>
"""


def render_video():
    return """
<section class=\"lesson-section\">
  <h2>Video mô phỏng</h2>
  <div class=\"video-placeholder\"><p class=\"mb-0\">Video mô phỏng sẽ được cập nhật sau.</p></div>
</section>
"""


def render_sidebar(current):
    out = ["<div class=\"card lesson-sidebar\"><div class=\"card-body\">", "<h2 class=\"h5 fw-bold\">Mục lục khóa học</h2>", "<div class=\"list-group list-group-flush\">", '<a class="list-group-item list-group-item-action" href="../index.html">Tổng quan khóa học</a>']
    for spec in LESSONS:
        cls = "list-group-item list-group-item-action"
        if spec["num"] == current:
            cls += " active"
        out.append(f'<a class="{cls}" href="{spec["slug"]}.html">Bài {spec["num"]}. {esc(spec["title"])}</a>')
    out += ["</div></div></div>"]
    return "\n".join(out)


def render_nav(current):
    prev_btn = '<a class="btn btn-primary disabled" aria-disabled="true">Bài trước</a>'
    next_btn = '<a class="btn btn-primary disabled" aria-disabled="true">Bài tiếp theo</a>'
    if current > 1:
        prev = LESSONS[current - 2]
        prev_btn = f'<a class="btn btn-primary" href="{prev["slug"]}.html">Bài trước</a>'
    if current < len(LESSONS):
        nxt = LESSONS[current]
        next_btn = f'<a class="btn btn-primary" href="{nxt["slug"]}.html">Bài tiếp theo</a>'
    return f"""
<div class="lesson-navigation d-flex justify-content-between gap-2 flex-wrap">
  <a class="btn btn-outline-secondary" href="../index.html">Tổng quan khóa học</a>
  <div class="d-flex gap-2 flex-wrap">
    {prev_btn}
    {next_btn}
  </div>
</div>
"""


def build_lesson(spec):
    num = spec["num"]
    parts = [
        "<!DOCTYPE html>",
        '<html lang="vi">',
        "<head>",
        '  <meta charset="UTF-8">',
        '  <meta name="viewport" content="width=device-width, initial-scale=1.0" />',
        f"  <title>Bài {num} - {esc(spec['title'])} | Dev Academy</title>",
        '  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" />',
        '  <link rel="stylesheet" href="../../../assets/css/style.css" />',
        '  <link rel="stylesheet" href="../../../assets/css/course.css" />',
        "</head>",
        "<body>",
        "<header><nav class=\"navbar navbar-expand-lg navbar-dark bg-dark\"><div class=\"container\"><a class=\"navbar-brand fw-bold\" href=\"../../../index.html\">Dev Academy</a><button class=\"navbar-toggler\" type=\"button\" data-bs-toggle=\"collapse\" data-bs-target=\"#mainNavbar\" aria-controls=\"mainNavbar\" aria-expanded=\"false\" aria-label=\"Toggle navigation\"><span class=\"navbar-toggler-icon\"></span></button><div class=\"collapse navbar-collapse\" id=\"mainNavbar\"><ul class=\"navbar-nav ms-auto\"><li class=\"nav-item\"><a class=\"nav-link\" href=\"../../../index.html\">Trang chủ</a></li><li class=\"nav-item\"><a class=\"nav-link\" href=\"../../../courses.html\">Khóa học</a></li><li class=\"nav-item\"><a class=\"nav-link\" href=\"../index.html\">Cấu trúc dữ liệu và Giải thuật C++</a></li></ul></div></div></nav></header>",
        '<main class="container my-4"><div class="row">',
        '<aside class="col-12 col-lg-3 mb-4">',
        render_sidebar(num),
        '</aside>',
        '<article class="col-12 col-lg-9">',
        '<section class="lesson-hero"><span class="badge text-bg-primary mb-2">Bài {}</span><h1 class="fw-bold">{}</h1><p class="lead mb-0">{}</p></section>'.format(num, esc(spec["title"]), esc(spec["intro"])),
        '<section class="lesson-section"><h2>Mục tiêu bài học</h2><ul>' + "".join(f"<li>{esc(item)}</li>" for item in spec["focus"]) + "</ul></section>",
        render_video(),
        render_theory(spec),
        '<section class="lesson-section"><h2>Ví dụ minh họa</h2>' + render_examples(spec["example_set"]) + '</section>',
        render_practice(spec),
        render_quiz(spec),
        render_essays(spec),
        render_summary(spec),
        render_nav(num),
        "</article></div></main>",
        '<footer class="py-4 bg-dark text-white mt-4"><div class="container text-center"><p class="mb-0">© 2026 Dev Academy. Built with GitHub Pages.</p></div></footer>',
        '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>',
        '<script src="../../../assets/js/quiz.js"></script>',
        '<script src="../../../assets/js/lesson.js"></script>',
        f'<script>document.addEventListener("DOMContentLoaded", () => {{ loadEssayDraft("essay-{num}-1", "dsa-lesson-{num}-1"); loadEssayDraft("essay-{num}-2", "dsa-lesson-{num}-2"); }});</script>',
        "</body></html>",
    ]
    return "\n".join(parts)


def build_overview():
    lesson_cards = "\n".join(f'<a class="list-group-item list-group-item-action" href="lessons/{s["slug"]}.html">Bài {s["num"]}. {esc(s["title"])}</a>' for s in LESSONS)
    pdf_items = "\n".join(f"<li>{esc(', '.join(s['pdf']))} - Bài {s['num']}</li>" for s in LESSONS)
    return f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Cấu trúc dữ liệu và Giải thuật C++ | Dev Academy</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" />
  <link rel="stylesheet" href="../../assets/css/style.css" />
  <link rel="stylesheet" href="../../assets/css/course.css" />
</head>
<body>
  <header><nav class="navbar navbar-expand-lg navbar-dark bg-dark"><div class="container"><a class="navbar-brand fw-bold" href="../../index.html">Dev Academy</a><button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#mainNavbar" aria-controls="mainNavbar" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button><div class="collapse navbar-collapse" id="mainNavbar"><ul class="navbar-nav ms-auto"><li class="nav-item"><a class="nav-link" href="../../index.html">Trang chủ</a></li><li class="nav-item"><a class="nav-link" href="../../courses.html">Khóa học</a></li><li class="nav-item"><a class="nav-link active" href="index.html">Cấu trúc dữ liệu và Giải thuật C++</a></li></ul></div></div></nav></header>
  <main class="py-5">
    <div class="container">
      <div class="row g-4 align-items-stretch">
        <div class="col-12 col-lg-8">
          <div class="p-4 p-lg-5 bg-dark text-white rounded-4 h-100">
            <span class="badge text-bg-success mb-3">Khóa học DSA C++</span>
            <h1 class="display-6 fw-bold">Cấu trúc dữ liệu và Giải thuật C++</h1>
            <p class="lead mt-3 mb-4">Khóa học này được biên soạn từ bộ PDF DSA trong thư mục <code>temp/dsa-pdfs/</code>. Mục tiêu là giúp người mới học đi từ nền tảng đến các thuật toán đồ thị nâng cao mà không cần quay lại tài liệu gốc.</p>
            <div class="d-flex flex-wrap gap-2">
              <a href="lessons/lesson-01.html" class="btn btn-primary btn-lg">Bắt đầu học</a>
              <a href="../../index.html" class="btn btn-outline-light btn-lg">Trang chủ</a>
              <a href="../../courses.html" class="btn btn-outline-light btn-lg">Danh sách khóa học</a>
            </div>
          </div>
        </div>
        <div class="col-12 col-lg-4">
          <div class="card h-100 course-card"><div class="card-body"><h2 class="h4 fw-bold">Đối tượng phù hợp</h2><p class="mb-0">Sinh viên CNTT năm 1, năm 2, người tự học C++ và bất kỳ ai cần nền tảng chắc cho DSA.</p></div></div>
        </div>
      </div>
      <div class="row g-4 mt-2">
        <div class="col-12 col-lg-5">
          <div class="card h-100 course-card"><div class="card-body"><h2 class="h4 fw-bold">Mục tiêu học tập</h2><ul class="mb-0"><li>Hiểu độ phức tạp, hệ đếm, hàm và đệ quy.</li><li>Nắm chắc mảng, vector, string, set, map, stack, queue.</li><li>Giải được bài sắp xếp, tìm kiếm, sinh, cây và đồ thị.</li><li>Đi tiếp tới DSU, MST và đường đi ngắn nhất.</li></ul></div></div>
        </div>
        <div class="col-12 col-lg-7">
          <div class="card h-100 course-card"><div class="card-body"><h2 class="h4 fw-bold">Danh sách bài học</h2><div class="list-group">{lesson_cards}</div></div></div>
        </div>
      </div>
      <div class="row g-4 mt-2">
        <div class="col-12">
          <div class="card course-card"><div class="card-body"><h2 class="h4 fw-bold">PDF đã sử dụng</h2><ul class="mb-0">{pdf_items}</ul><p class="mt-3 mb-0">PDF 12 và PDF 26 trùng chủ đề stack/queue/priority_queue nên đã được gộp để tránh lặp nội dung nhưng vẫn giữ đủ ý chính.</p></div></div>
        </div>
      </div>
    </div>
  </main>
  <footer class="py-4 bg-dark text-white"><div class="container text-center"><p class="mb-0">© 2026 Dev Academy. Built with GitHub Pages.</p></div></footer>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
  <script src="../../assets/js/main.js"></script>
</body>
</html>"""


COURSE.mkdir(parents=True, exist_ok=True)
(COURSE / "index.html").write_text(build_overview(), encoding="utf-8")
for spec in LESSONS:
    (LESSONS_DIR / f"{spec['slug']}.html").write_text(build_lesson(spec), encoding="utf-8")

print(f"Generated {len(LESSONS)} lessons in {COURSE}")

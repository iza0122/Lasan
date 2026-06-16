graph TD
    %% Tác nhân
    TV[Thành viên]
    AD[Admin]
    PH[Phụ huynh]
    TQ[Thủ quỹ]

    %% Kho dữ liệu
    D1[(D1: Người dùng)]
    D2[(D2: Bài viết & Thông báo)]
    D3[(D3: Lịch & Sinh hoạt)]
    D4[(D4: Quỹ & Học phí)]

    subgraph Phân hệ 1: Quản lý Xã hội
        P1((1.0 Quy trình<br>Tương tác Xã hội))
    end

    subgraph Phân hệ 2: Quản lý Sinh hoạt
        P2((2.0 Quy trình<br>Điều hành Sinh hoạt))
    end

    subgraph Phân hệ 3: Quản lý Tài chính
        P3((3.0 Quy trình<br>Kế toán Tài chính))
    end

    %% Tương tác Phân hệ 1
    TV -->|Soạn bài viết| P1
    AD -->|Duyệt bài, Đăng thông báo| P1
    P1 ==>|Lưu tin, Trạng thái duyệt| D2
    D2 ==>|Hiển thị bảng tin công khai| TV

    %% Tương tác Phân hệ 2
    AD -->|Lên lịch trực, Thực đơn| P2
    TV -->|Xin phép, Chừa cơm, Chấm nước| P2
    P2 ==>|Cập nhật Đơn phép| D1
    P2 ==>|Ghi nhận Lịch / Cơm / Nước| D3
    D3 ==>|Đồng bộ lịch, Đếm suất cơm| TV
    P2 -->|Gửi link xác thực| PH
    PH -->|Xác nhận phép| P2

    %% Tương tác Phân hệ 3
    TQ -->|Nhập khoản chi, Duyệt đóng phí| P3
    TV -->|Gửi mã QR chuyển khoản| P3
    P3 ==>|Ghi nhật ký thu chi| D4
    D4 ==>|Vẽ biểu đồ, Xuất nhật ký công khai| TV
    D4 ==>|Báo cáo dòng tiền| TQ
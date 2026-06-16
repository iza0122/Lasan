graph TD
    %% Tác nhân bên ngoài
    TV[Thành viên]
    AD[Admin]
    PH[Phụ huynh]
    TQ[Thủ quỹ]
    K[Khách]

    %% Hệ thống trung tâm
    HT((Hệ thống Quản lý<br>Nhà chung))

    %% Luồng dữ liệu của Thành viên
    TV -->|1. Bài viết chữ+ảnh<br>2. Đơn xin phép<br>3. Yêu cầu chừa cơm<br>4. Tích chấm nước<br>5. Minh chứng đóng phí| HT
    HT -->|1. Bảng tin, Thông báo<br>2. Lịch trực nhật, Thực đơn<br>3. Danh sách phí cần đóng| TV

    %% Luồng dữ liệu của Admin
    AD -->|1. Lệnh duyệt bài<br>2. Thông báo mới<br>3. Lịch phân công<br>4. Lệnh duyệt đơn phép| HT
    HT -->|1. Bài viết chờ duyệt<br>2. Đơn phép chờ duyệt| AD

    %% Luồng dữ liệu của Phụ huynh
    HT -->|Link xác nhận qua SMS/Zalo| PH
    PH -->|Phản hồi Đồng ý/Từ chối| HT

    %% Luồng dữ liệu của Thủ quỹ
    TQ -->|1. Nhập thông tin chi tiêu<br>2. Xác nhận gạch nợ phí| HT
    HT -->|Dữ liệu thu chi, Biểu đồ thống kê| TQ

    %% Luồng dữ liệu của Khách
    K -->|Gửi form liên hệ/đăng ký ở| HT
    HT -->|Thông tin giới thiệu công khai| K

- Sử dụng python cho backend
- Sử dụng vercel để deploy
- Có cấu hình .env
- Sử dụng database postgresSQL (local dùng sqlite, cloud dùng Supbase)
- R2 cloudfare cho object storage
- Firebase cho đăng kí, đăng nhập
- Frontend tạm dùng nextjs
- cấu trúc thư mục tổng quan

homemanagement-root/
├── backend/                  # Mã nguồn phía Server (API, Database, Logic)
├── frontend/                 # Mã nguồn phía Client (Giao diện Web/Mobile)
├── docs/                     # Tài liệu thiết kế (ERD, DFD, API Spec)
├── .gitignore
└── README.md

Cấu trúc chi tiết Backend
backend/
├── src/
│   ├── config/               # Cấu hình hệ thống (Database, JWT, Zalo/SMS API)
│   │   ├── database.js
│   │   └── constants.js       # Lưu giờ khóa sổ: MEAL_LUNCH_LIMIT = '10:45'
│   ├── common/               # Các hàm dùng chung, Middleware, Guards
│   │   ├── middlewares/      # Kiểm tra quyền Admin, Thủ quỹ
│   │   ├── utils/            # Hàm gửi SMS, tạo mã Token bảo mật cho Phụ huynh
│   │   └── interceptors/
│   ├── modules/              # CHỨA CÁC PHÂN HỆ NGHIỆP VỤ CHÍNH
│   │   ├── auth/             # Đăng nhập, đăng ký tài khoản
│   │   ├── users/            # Quản lý thành viên, thông tin phụ huynh
│   │   ├── social/           # --- PHÂN HỆ XÃ HỘI ---
│   │   │   ├── controllers/  # Tiếp nhận request đăng bài, duyệt bài
│   │   │   ├── services/     # Logic hàng đợi "Chờ duyệt", bắn thông báo Home
│   │   │   └── models/       # Post.js, Announcement.js
│   │   ├── management/       # --- PHÂN HỆ QUẢN LÝ ---
│   │   │   ├── controllers/  # Request xin phép, chừa cơm, chấm nước
│   │   │   ├── services/     # Thuật toán khóa chừa cơm (>10:45, >18:15)
│   │   │   │                 # Logic sinh link token duyệt cho Phụ huynh
│   │   │   └── models/       # DutySchedule.js, LeaveRequest.js, Meal.js
│   │   └── finance/          # --- PHÂN HỆ TÀI CHÍNH ---
│   │   │   ├── controllers/  # Request đóng phí, chi tiêu
│   │   │   ├── services/     # Logic tính số dư quỹ, gom dữ liệu vẽ biểu đồ
│   │   │   └── models/       # UserFee.js, Expense.js
│   ├── app.js                # Khởi tạo ứng dụng
│   └── server.js             # Khởi chạy server
├── database/
│   ├── migrations/           # File khởi tạo và cập nhật cấu trúc bảng DB
│   └── seeders/              # Dữ liệu mẫu (Tạo tài khoản Admin mặc định)
├── .env                      # Lưu biến môi trường bí mật (DB_PASS, API_KEY)
├── package.json
└── README.md

Tham khảo cấu trúc sau, thay đổi theo công nghệ chọn
frontend/
├── public/                   # Tài sản tĩnh (Logo, hình ảnh cơ sở vật chất)
├── src/
│   ├── assets/               # CSS, SCSS, Icons toàn cục
│   ├── components/           # Các UI Component dùng chung cho toàn hệ thống
│   │   ├── ui/               # Button, Input, Modal, Table, Badge trạng thái
│   │   └── common/           # Sidebar, Navbar (Admin/Thành viên riêng), Footer
│   ├── core/                 # Cấu hình cốt lõi
│   │   ├── api/              # Cấu hình Axios/Fetch client (gắn Token tự động)
│   │   └── routes/           # Định tuyến trang (Public, Protected Routes)
│   ├── features/             # CHỨA GIAO DIỆN THEO PHÂN HỆ
│   │   ├── public-intro/     # Trang giới thiệu cho Khách (Lịch sử, Nội quy, Form liên hệ)
│   │   ├── social/           # Giao diện Bảng tin, Form đăng bài, Màn hình duyệt bài của Admin
│   │   ├── management/       # Giao diện Lịch tuần (Calendar View), Form xin phép,
│   │   │                     # Nút bấm chừa cơm (Ẩn/Hiện theo thời gian thực), Chấm nước
│   │   └── finance/          # Màn hình quét mã QR đóng phí, Nhật ký chi tiêu công khai,
│   │                         # Dashboard biểu đồ Tròn/Cột của Thủ quỹ
│   ├── hooks/                # Custom hooks dùng chung (useAuth, useNotification)
│   ├── store/                # Quản lý trạng thái toàn cục (Redux / Zustand / Context)
│   ├── app/                  # File gốc khởi chạy ứng dụng (hoặc pages/)
│   └── main.jsx
├── tailwind.config.js        # File cấu hình giao diện nếu dùng Tailwind CSS
├── package.json
└── README.md
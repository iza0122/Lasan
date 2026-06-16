erDiagram
    USERS ||--o{ POSTS : "viết / duyệt"
    USERS ||--o{ ANNOUNCEMENTS : "tạo"
    USERS ||--o{ LEAVE_REQUESTS : "tạo / duyệt"
    USERS ||--o{ MEAL_REGISTRATIONS : "đăng ký"
    USERS ||--o{ WATER_TRACKINGS : "ghi nhận"
    USERS ||--o{ DUTY_ASSIGNMENTS : "được phân công"
    USERS ||--o{ USER_FEES : "đóng / xác nhận"
    USERS ||--o{ EXPENSES : "chi tiêu"

    DUTY_SCHEDULES ||--o{ DUTY_ASSIGNMENTS : "bao gồm"
    MENUS ||--o{ MEAL_REGISTRATIONS : "áp dụng cho"

    USERS {
        int id PK
        string name
        string phone
        string email
        string password
        string role "Admin/Treasurer/Member"
        string parent_phone
        string status "Active/Inactive"
    }

    POSTS {
        int id PK
        int author_id FK
        string title
        text content
        string images
        string status "Pending/Approved/Rejected"
        int approved_by FK
        datetime created_at
    }

    ANNOUNCEMENTS {
        int id PK
        int creator_id FK
        string title
        text content
        datetime created_at
    }

    LEAVE_REQUESTS {
        int id PK
        int user_id FK
        string type "Late/Overnight/Home"
        datetime start_time
        datetime end_time
        text reason
        string parent_status "Pending/Approved/Rejected"
        string admin_status "Pending/Approved/Rejected"
        int approved_by_admin_id FK
        datetime created_at
    }

    MENUS {
        int id PK
        date menu_date
        string meal_type "Lunch/Dinner"
        text description
    }

    MEAL_REGISTRATIONS {
        int id PK
        int user_id FK
        int menu_id FK
        date registration_date
        string meal_type "Lunch/Dinner"
        boolean is_cancelled "True nếu chừa cơm"
        datetime updated_at
    }

    WATER_TRACKINGS {
        int id PK
        int user_id FK
        date tracking_date
        boolean is_taken
    }

    DUTY_SCHEDULES {
        int id PK
        date schedule_date
        string shift_type "Cooking/Cleaning"
        string location "Bếp/Nhà xe/Phòng học..."
        text description
    }

    DUTY_ASSIGNMENTS {
        int id PK
        int schedule_id FK
        int user_id FK
    }

    USER_FEES {
        int id PK
        int user_id FK
        string fee_name "Tiền phòng/Tiền quỹ..."
        decimal amount
        string month_year
        string status "Unpaid/Paid"
        string qr_proof_url
        int confirmed_by FK
        datetime paid_at
    }

    EXPENSES {
        int id PK
        int treasurer_id FK
        decimal amount
        string content
        string category
        string invoice_image_url
        datetime created_at
    }
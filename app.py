Bắt đầu

Nhập STV      // Số tiền muốn vay (triệu đồng)
Nhập TGV      // Thời gian vay (năm)
Nhập LSV      // Lãi suất vay (số thập phân)
Nhập TN       // Thu nhập hàng tháng (triệu đồng/tháng)
Nhập SNTGD    // Số người trong gia đình

Gán CPSH ← 5  // Chi phí sinh hoạt bình quân/người

Nhập PTMC     // Số tiền phải trả cho khoản vay cũ

PTMM ← (STV / (TGV × 12)) + (STV × (LSV / 12))

DTI ← (PTMC + PTMM) / (TN - SNTGD × CPSH)

Nhập GTTSDB   // Giá trị tài sản đảm bảo

LTV ← STV / GTTSDB

Nhập STKH     // Tuổi khách hàng

Xuất "Chỉ số DTI là:", DTI × 100, "%"

Xuất "Chỉ số LTV là:", LTV × 100, "%"

Nếu (DTI ≤ 0.7) và (LTV ≤ 0.7) và (18 ≤ STKH ≤ 70) thì
    Xuất "ĐƯỢC CHO VAY"
Ngược lại
    Xuất "KHÔNG ĐƯỢC CHO VAY"
Kết thúc nếu

Kết thúc

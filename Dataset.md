-- ====================================================================
-- HOSPITAL MANAGEMENT SYSTEM - DATABASE SCRIPTS
-- ====================================================================

-- Drop tables if exists (in correct order to handle foreign keys)
DROP TABLE IF EXISTS ChiTietDonThuoc;
DROP TABLE IF EXISTS HoSoKham;
DROP TABLE IF EXISTS KhoaPhong;
DROP TABLE IF EXISTS Thuoc;
DROP TABLE IF EXISTS BenhNhan;
DROP TABLE IF EXISTS BacSi;

-- ====================================================================
-- CREATE TABLES
-- ====================================================================

-- Table: BenhNhan (Patient)
CREATE TABLE BenhNhan (
    maBN INT PRIMARY KEY AUTO_INCREMENT,
    hoTen VARCHAR(100) NOT NULL,
    ngaySinh DATE NOT NULL,
    diaChi TEXT,
    soDienThoai VARCHAR(15),
    INDEX idx_benhNhan_hoTen (hoTen),
    INDEX idx_benhNhan_sdt (soDienThoai)
);

-- Table: BacSi (Doctor)
CREATE TABLE BacSi (
    maBS INT PRIMARY KEY AUTO_INCREMENT,
    hoTen VARCHAR(100) NOT NULL,
    chuyenKhoa VARCHAR(50),
    soDienThoai VARCHAR(15),
    INDEX idx_bacSi_hoTen (hoTen),
    INDEX idx_bacSi_chuyenKhoa (chuyenKhoa)
);

-- Table: KhoaPhong (Department)
CREATE TABLE KhoaPhong (
    maKhoa INT PRIMARY KEY AUTO_INCREMENT,
    tenKhoa VARCHAR(100) NOT NULL,
    truongKhoa VARCHAR(100),
    INDEX idx_khoaPhong_tenKhoa (tenKhoa)
);

-- Table: Thuoc (Medicine)
CREATE TABLE Thuoc (
    maThuoc INT PRIMARY KEY AUTO_INCREMENT,
    tenThuoc VARCHAR(100) NOT NULL,
    congDung TEXT,
    donViTinh VARCHAR(20),
    soLuongTon INT DEFAULT 0,
    INDEX idx_thuoc_tenThuoc (tenThuoc),
    INDEX idx_thuoc_soLuongTon (soLuongTon)
);

-- Table: HoSoKham (Medical Record)
CREATE TABLE HoSoKham (
    maHS INT PRIMARY KEY AUTO_INCREMENT,
    maBN INT NOT NULL,
    ngayKham DATE NOT NULL,
    chuanDoan TEXT,
    benhNhan VARCHAR(100),
    bacSi VARCHAR(50),
    FOREIGN KEY (maBN) REFERENCES BenhNhan(maBN) ON DELETE CASCADE,
    INDEX idx_hoSoKham_maBN (maBN),
    INDEX idx_hoSoKham_ngayKham (ngayKham)
);

-- Table: ChiTietDonThuoc (Prescription Details)
CREATE TABLE ChiTietDonThuoc (
    id INT PRIMARY KEY AUTO_INCREMENT,
    maHS INT NOT NULL,
    maThuoc INT NOT NULL,
    thuoc VARCHAR(100),
    soLuong INT NOT NULL DEFAULT 1,
    lieuDung TEXT,
    FOREIGN KEY (maHS) REFERENCES HoSoKham(maHS) ON DELETE CASCADE,
    FOREIGN KEY (maThuoc) REFERENCES Thuoc(maThuoc) ON DELETE CASCADE,
    INDEX idx_chiTietDonThuoc_maHS (maHS),
    INDEX idx_chiTietDonThuoc_maThuoc (maThuoc),
    UNIQUE KEY unique_prescription (maHS, maThuoc)
);

-- ====================================================================
-- INSERT SAMPLE DATA
-- ====================================================================

# Benh nhan
-- Insert BenhNhan (Patients) - 100 records
INSERT INTO BenhNhan (hoTen, ngaySinh, diaChi, soDienThoai) VALUES
('Nguyễn Văn Anh', '1985-03-15', '123 Nguyễn Trãi, Quận 1, TP.HCM', '0901234567'),
('Trần Thị Bình', '1990-07-22', '456 Lê Lợi, Quận 3, TP.HCM', '0912345678'),
('Lê Văn Cường', '1978-12-10', '789 Điện Biên Phủ, Quận Bình Thạnh, TP.HCM', '0923456789'),
('Phạm Thị Dung', '1995-05-18', '321 Cách Mạng Tháng 8, Quận 10, TP.HCM', '0934567890'),
('Hoàng Văn Em', '1982-09-03', '654 Nguyễn Văn Linh, Quận 7, TP.HCM', '0945678901'),
('Vũ Thị Phương', '1988-11-27', '987 Võ Văn Tần, Quận 3, TP.HCM', '0956789012'),
('Đặng Văn Giang', '1993-01-14', '147 Hai Bà Trưng, Quận 1, TP.HCM', '0967890123'),
('Bùi Thị Hoa', '1986-04-08', '258 Trường Chinh, Quận Tân Bình, TP.HCM', '0978901234'),
('Ngô Văn Ích', '1991-08-25', '369 Phạm Văn Đồng, Quận Gò Vấp, TP.HCM', '0989012345'),
('Lý Thị Kim', '1979-06-12', '741 Quang Trung, Quận 12, TP.HCM', '0990123456'),
('Trương Văn Long', '1987-02-28', '852 Lê Văn Việt, Quận 9, TP.HCM', '0901234568'),
('Phan Thị Mai', '1994-10-16', '963 Nguyễn Ảnh Thủ, Quận 12, TP.HCM', '0912345679'),
('Võ Văn Nam', '1983-12-05', '159 Phan Văn Trị, Quận Bình Thạnh, TP.HCM', '0923456780'),
('Đỗ Thị Oanh', '1989-03-21', '357 Tô Hiến Thành, Quận 10, TP.HCM', '0934567891'),
('Tạ Văn Phúc', '1992-07-09', '468 Nguyễn Thị Minh Khai, Quận 1, TP.HCM', '0945678902'),
('Lưu Thị Quỳnh', '1981-05-30', '579 Lý Thường Kiệt, Quận 11, TP.HCM', '0956789013'),
('Huỳnh Văn Sơn', '1996-09-17', '680 Nguyễn Văn Cừ, Quận 5, TP.HCM', '0967890124'),
('Cao Thị Trang', '1984-11-23', '791 Đinh Bộ Lĩnh, Quận Bình Thạnh, TP.HCM', '0978901235'),
('Dương Văn Tú', '1990-01-11', '802 Nguyễn Thị Thập, Quận 7, TP.HCM', '0989012346'),
('Đinh Thị Uyên', '1977-08-04', '913 Âu Cơ, Quận Tân Phú, TP.HCM', '0990123457'),
('Lâm Văn Vinh', '1985-06-19', '124 Cộng Hòa, Quận Tân Bình, TP.HCM', '0901234569'),
('Hồ Thị Xuân', '1993-04-26', '235 Nguyễn Xí, Quận Bình Thạnh, TP.HCM', '0912345680'),
('Mai Văn Yên', '1988-12-13', '346 Lạc Long Quân, Quận 11, TP.HCM', '0923456781'),
('Đào Thị Yến', '1991-10-01', '457 Hoàng Văn Thụ, Quận Phú Nhuận, TP.HCM', '0934567892'),
('Tôn Văn An', '1980-02-17', '568 3 Tháng 2, Quận 10, TP.HCM', '0945678903'),
('Nghiêm Thị Bích', '1995-07-24', '679 Nguyễn Đình Chiểu, Quận 3, TP.HCM', '0956789014'),
('Ông Văn Cát', '1982-05-12', '780 Pasteur, Quận 1, TP.HCM', '0967890125'),
('Phùng Thị Diệu', '1987-09-29', '891 Nam Kỳ Khởi Nghĩa, Quận 3, TP.HCM', '0978901236'),
('Quách Văn Đức', '1994-03-06', '902 Võ Thị Sáu, Quận 3, TP.HCM', '0989012347'),
('Tăng Thị Ế', '1989-11-14', '113 Bùi Viện, Quận 1, TP.HCM', '0990123458'),
('Ưng Văn Phát', '1976-01-22', '224 Đề Thám, Quận 1, TP.HCM', '0901234570'),
('Văn Thị Gái', '1992-08-07', '335 Nguyễn An Ninh, Quận Bình Thạnh, TP.HCM', '0912345681'),
('Xa Văn Hải', '1986-06-15', '446 Xô Viết Nghệ Tĩnh, Quận Bình Thạnh, TP.HCM', '0923456782'),
('Yết Thị Hạnh', '1991-04-02', '557 Phan Đăng Lưu, Quận Phú Nhuận, TP.HCM', '0934567893'),
('Âu Văn Khang', '1983-12-20', '668 Hoàng Diệu, Quận 4, TP.HCM', '0945678904'),
('Ấu Thị Lan', '1988-10-08', '779 Tôn Đản, Quận 4, TP.HCM', '0956789015'),
('Ê Văn Minh', '1995-02-25', '880 Nguyễn Tất Thành, Quận 4, TP.HCM', '0967890126'),
('Ơ Thị Nga', '1981-07-13', '991 Khánh Hội, Quận 4, TP.HCM', '0978901237'),
('Ư Văn Oanh', '1990-05-31', '102 Vinh Khanh, Quận 4, TP.HCM', '0989012348'),
('Ý Thị Phong', '1987-09-18', '213 Đoàn Văn Bơ, Quận 4, TP.HCM', '0990123459'),
('Nguyễn Thị Hạnh', '1985-11-25', '324 Nguyễn Khoái, Quận 4, TP.HCM', '0901234571'),
('Trần Văn Hoàng', '1992-03-12', '435 Bến Vân Đồn, Quận 4, TP.HCM', '0912345682'),
('Lê Thị Hương', '1984-08-28', '546 Tôn Thất Thuyết, Quận 4, TP.HCM', '0923456783'),
('Phạm Văn Huy', '1989-06-16', '657 Nguyễn Tư Nghiêm, Quận 2, TP.HCM', '0934567894'),
('Hoàng Thị Huyền', '1993-01-03', '768 Thảo Điền, Quận 2, TP.HCM', '0945678905'),
('Vũ Văn Khánh', '1978-04-21', '879 Xa Lộ Hà Nội, Quận 2, TP.HCM', '0956789016'),
('Đặng Thị Kiều', '1996-12-09', '980 Nguyễn Duy Trinh, Quận 2, TP.HCM', '0967890127'),
('Bùi Văn Linh', '1982-10-27', '191 Mai Chi Thọ, Quận 2, TP.HCM', '0978901238'),
('Ngô Thị Loan', '1987-02-14', '292 Đỗ Xuân Hợp, Quận 2, TP.HCM', '0989012349'),
('Lý Văn Mạnh', '1994-07-01', '393 Lương Định Của, Quận 2, TP.HCM', '0990123460');

-- More patients (continuing to 100)
INSERT INTO BenhNhan (hoTen, ngaySinh, diaChi, soDienThoai) VALUES
('Trương Thị Minh', '1986-05-19', '494 Nguyễn Văn Hưởng, Quận 2, TP.HCM', '0901234572'),
('Phan Văn Nam', '1991-09-06', '595 Trần Não, Quận 2, TP.HCM', '0912345683'),
('Võ Thị Nga', '1985-03-24', '696 Quốc Hương, Quận 2, TP.HCM', '0923456784'),
('Đỗ Văn Oanh', '1990-11-11', '797 An Phú, Quận 2, TP.HCM', '0934567895'),
('Tạ Thị Phương', '1983-07-29', '898 Thủ Thiêm, Quận 2, TP.HCM', '0945678906'),
('Lưu Văn Quang', '1988-01-16', '999 Bình Khánh, Quận 2, TP.HCM', '0956789017'),
('Huỳnh Thị Quyên', '1995-06-04', '100 Cát Lái, Quận 2, TP.HCM', '0967890128'),
('Cao Văn Sáng', '1981-12-22', '201 Thạnh Mỹ Lợi, Quận 2, TP.HCM', '0978901239'),
('Dương Thị Thảo', '1987-04-10', '302 An Khánh, Quận 2, TP.HCM', '0989012350'),
('Đinh Văn Thắng', '1992-08-27', '403 Bình An, Quận 2, TP.HCM', '0990123461'),
('Lâm Thị Thu', '1984-02-15', '504 Bình Trưng Đông, Quận 2, TP.HCM', '0901234573'),
('Hồ Văn Tiến', '1989-10-02', '605 Bình Trưng Tây, Quận 2, TP.HCM', '0912345684'),
('Mai Thị Trang', '1996-06-20', '706 Long Phước, Quận 9, TP.HCM', '0923456785'),
('Đào Văn Trung', '1982-12-08', '807 Long Trường, Quận 9, TP.HCM', '0934567896'),
('Tôn Thị Tuyết', '1988-04-26', '908 Phước Long A, Quận 9, TP.HCM', '0945678907'),
('Nghiêm Văn Uy', '1993-09-13', '109 Phước Long B, Quận 9, TP.HCM', '0956789018'),
('Ông Thị Vân', '1985-01-31', '210 Tăng Nhơn Phú A, Quận 9, TP.HCM', '0967890129'),
('Phùng Văn Việt', '1990-07-18', '311 Tăng Nhơn Phú B, Quận 9, TP.HCM', '0978901240'),
('Quách Thị Xuân', '1987-03-05', '412 Trường Thạnh, Quận 9, TP.HCM', '0989012351'),
('Tăng Văn Yên', '1994-11-23', '513 Hiệp Phú, Quận 9, TP.HCM', '0990123462'),
('Ưng Thị Ân', '1981-05-11', '614 Tân Phú, Quận 9, TP.HCM', '0901234574'),
('Văn Văn Bình', '1986-09-28', '715 Phú Hữu, Quận 9, TP.HCM', '0912345685'),
('Xa Thị Cẩm', '1991-01-15', '816 Long Bình, Quận 9, TP.HCM', '0923456786'),
('Yết Văn Đạt', '1988-08-03', '917 Long Thạnh Mỹ, Quận 9, TP.HCM', '0934567897'),
('Âu Thị Diệp', '1995-04-21', '118 Phước Bình, Quận 9, TP.HCM', '0945678908'),
('Ấu Văn Đông', '1983-12-09', '219 Phước Thiện, Quận 9, TP.HCM', '0956789019'),
('Ê Thị Én', '1989-06-27', '320 Tam Bình, Quận Thủ Đức, TP.HCM', '0967890130'),
('Ơ Văn Phước', '1992-02-14', '421 Tam Phú, Quận Thủ Đức, TP.HCM', '0978901241'),
('Ư Thị Giang', '1986-10-01', '522 Linh Chiểu, Quận Thủ Đức, TP.HCM', '0989012352'),
('Ý Văn Hải', '1991-07-19', '623 Linh Tây, Quận Thủ Đức, TP.HCM', '0990123463'),
('Nguyễn Thị Hoa', '1984-03-07', '724 Linh Xuân, Quận Thủ Đức, TP.HCM', '0901234575'),
('Trần Văn Hoài', '1987-11-24', '825 Linh Đông, Quận Thủ Đức, TP.HCM', '0912345686'),
('Lê Thị Hồng', '1993-05-12', '926 Linh Trung, Quận Thủ Đức, TP.HCM', '0923456787'),
('Phạm Văn Hùng', '1980-09-30', '127 Bình Chiểu, Quận Thủ Đức, TP.HCM', '0934567898'),
('Hoàng Thị Hường', '1985-01-17', '228 Bình Thọ, Quận Thủ Đức, TP.HCM', '0945678909'),
('Vũ Văn Kế', '1990-08-05', '329 Hiệp Bình Chánh, Quận Thủ Đức, TP.HCM', '0956789020'),
('Đặng Thị Khuyên', '1988-04-23', '430 Hiệp Bình Phước, Quận Thủ Đức, TP.HCM', '0967890131'),
('Bùi Văn Lâm', '1995-12-10', '531 Đông Hòa, Quận Dĩ An, Bình Dương', '0978901242'),
('Ngô Thị Lan', '1982-06-28', '632 An Bình, Quận Dĩ An, Bình Dương', '0989012353'),
('Lý Văn Mạnh', '1987-02-16', '733 An Thành, Quận Dĩ An, Bình Dương', '0990123464'),
('Trương Thị Mai', '1994-10-03', '834 Bình An, Quận Dĩ An, Bình Dương', '0901234576'),
('Phan Văn Minh', '1981-07-21', '935 Bình Thắng, Quận Dĩ An, Bình Dương', '0912345687'),
('Võ Thị Mỹ', '1986-03-09', '136 Đại Thành, Quận Dĩ An, Bình Dương', '0923456788'),
('Đỗ Văn Ngọc', '1991-11-26', '237 Đông Tân, Quận Dĩ An, Bình Dương', '0934567899'),
('Tạ Thị Nga', '1988-05-14', '338 Hòa Bình, Quận Dĩ An, Bình Dương', '0945678910'),
('Lưu Văn Ơn', '1993-01-01', '439 Phước Tân, Quận Biên Hòa, Đồng Nai', '0956789021'),
('Huỳnh Thị Phấn', '1985-09-18', '540 Tân Mai, Quận Biên Hòa, Đồng Nai', '0967890132'),
('Cao Văn Quí', '1990-07-06', '641 Trảng Dài, Quận Biên Hòa, Đồng Nai', '0978901243'),
('Dương Thị Quyên', '1987-03-24', '742 Thống Nhất, Quận Biên Hòa, Đồng Nai', '0989012354'),
('Đinh Văn Sơn', '1992-11-11', '843 Tân Hiệp, Quận Biên Hòa, Đồng Nai', '0990123465'),
('Lâm Thị Thúy', '1984-05-29', '944 Tân Hòa, Quận Biên Hòa, Đồng Nai', '0901234577');

# Bac si
-- Insert BacSi (Doctors) - 50 records
INSERT INTO BacSi (hoTen, chuyenKhoa, soDienThoai) VALUES
('BS. Nguyễn Văn An', 'Tim mạch', '0908111111'),
('BS. Trần Thị Bảo', 'Nhi khoa', '0908111112'),
('BS. Lê Văn Cường', 'Thần kinh', '0908111113'),
('BS. Phạm Thị Dung', 'Da liễu', '0908111114'),
('BS. Hoàng Văn Em', 'Chỉnh hình', '0908111115'),
('BS. Vũ Thị Phương', 'Sản phụ khoa', '0908111116'),
('BS. Đặng Văn Giang', 'Mắt', '0908111117'),
('BS. Bùi Thị Hoa', 'Tai mũi họng', '0908111118'),
('BS. Ngô Văn Ích', 'Tiêu hóa', '0908111119'),
('BS. Lý Thị Kim', 'Hô hấp', '0908111120'),
('BS. Trương Văn Long', 'Nội tiết', '0908111121'),
('BS. Phan Thị Mai', 'Thận tiết niệu', '0908111122'),
('BS. Võ Văn Nam', 'Cơ xương khớp', '0908111123'),
('BS. Đỗ Thị Oanh', 'Tâm thần', '0908111124'),
('BS. Tạ Văn Phúc', 'Ung bướu', '0908111125'),
('BS. Lưu Thị Quỳnh', 'Gây mê hồi sức', '0908111126'),
('BS. Huỳnh Văn Sơn', 'Cấp cứu', '0908111127'),
('BS. Cao Thị Trang', 'Nội tổng hợp', '0908111128'),
('BS. Dương Văn Tú', 'Ngoại tổng hợp', '0908111129'),
('BS. Đinh Thị Uyên', 'Phục hồi chức năng', '0908111130'),
('BS. Lâm Văn Vinh', 'Y học cổ truyền', '0908111131'),
('BS. Hồ Thị Xuân', 'Dinh dưỡng', '0908111132'),
('BS. Mai Văn Yên', 'Lão khoa', '0908111133'),
('BS. Đào Thị Yến', 'Vi sinh', '0908111134'),
('BS. Tôn Văn An', 'Huyết học', '0908111135'),
('BS. Nghiêm Thị Bích', 'Miễn dịch', '0908111136'),
('BS. Ông Văn Cát', 'Dược lâm sàng', '0908111137'),
('BS. Phùng Thị Diệu', 'Chẩn đoán hình ảnh', '0908111138'),
('BS. Quách Văn Đức', 'Xét nghiệm', '0908111139'),
('BS. Tăng Thị Ế', 'Y tế công cộng', '0908111140'),
('BS. Ưng Văn Phát', 'Răng hàm mặt', '0908111141'),
('BS. Văn Thị Gái', 'Dược sĩ', '0908111142'),
('BS. Xa Văn Hải', 'Kỹ thuật viên', '0908111143'),
('BS. Yết Thị Hạnh', 'Điều dưỡng', '0908111144'),
('BS. Âu Văn Khang', 'Vật lý trị liệu', '0908111145'),
('BS. Ấu Thị Lan', 'Tâm lý học', '0908111146'),
('BS. Ê Văn Minh', 'Xã hội học y tế', '0908111147'),
('BS. Ơ Thị Nga', 'Kinh doanh y tế', '0908111148'),
('BS. Ư Văn Oanh', 'Quản lý y tế', '0908111149'),
('BS. Ý Thị Phong', 'Thông tin y tế', '0908111150'),
('BS. Nguyễn Đức Tâm', 'Phẫu thuật tổng hợp', '0908111151'),
('BS. Trần Văn Thanh', 'Nội khoa', '0908111152'),
('BS. Lê Thị Thu', 'Ngoại khoa', '0908111153'),
('BS. Phạm Văn Thành', 'Nhi khoa', '0908111154'),
('BS. Hoàng Thị Thảo', 'Sản khoa', '0908111155'),
('BS. Vũ Văn Thắng', 'Phụ khoa', '0908111156'),
('BS. Đặng Thị Thơm', 'Y học gia đình', '0908111157'),
('BS. Bùi Văn Thức', 'Nội tiết', '0908111158'),
('BS. Ngô Thị Thủy', 'Huyết học', '0908111159'),
('BS. Lý Văn Thuận', 'Ung thư học', '0908111160');

# KhoaPhong

-- Insert KhoaPhong (Departments) - 20 records
INSERT INTO KhoaPhong (tenKhoa, truongKhoa) VALUES
('Khoa Nội Tổng Hợp', 'BS. Nguyễn Văn An'),
('Khoa Ngoại Tổng Hợp', 'BS. Dương Văn Tú'),
('Khoa Nhi', 'BS. Trần Thị Bảo'),
('Khoa Sản Phụ', 'BS. Vũ Thị Phương'),
('Khoa Tim Mạch', 'BS. Nguyễn Văn An'),
('Khoa Thần Kinh', 'BS. Lê Văn Cường'),
('Khoa Chỉnh Hình', 'BS. Hoàng Văn Em'),
('Khoa Mắt', 'BS. Đặng Văn Giang'),
('Khoa Tai Mũi Họng', 'BS. Bùi Thị Hoa'),
('Khoa Tiêu Hóa', 'BS. Ngô Văn Ích'),
('Khoa Hô Hấp', 'BS. Lý Thị Kim'),
('Khoa Nội Tiết', 'BS. Trương Văn Long'),
('Khoa Thận Tiết Niệu', 'BS. Phan Thị Mai'),
('Khoa Da Liễu', 'BS. Phạm Thị Dung'),
('Khoa Ung Bướu', 'BS. Tạ Văn Phúc'),
('Khoa Cấp Cứu', 'BS. Huỳnh Văn Sơn'),
('Khoa Gây Mê Hồi Sức', 'BS. Lưu Thị Quỳnh'),
('Khoa Phục Hồi Chức Năng', 'BS. Đinh Thị Uyên'),
('Khoa Y Học Cổ Truyền', 'BS. Lâm Văn Vinh'),
('Khoa Răng Hàm Mặt', 'BS. Ưng Văn Phát');

# Thuoc

-- Insert Thuoc (Medicine) - 100 records
INSERT INTO Thuoc (tenThuoc, congDung, donViTinh, soLuongTon) VALUES
('Paracetamol 500mg', 'Giảm đau, hạ sốt', 'Viên', 5000),
('Amoxicillin 500mg', 'Kháng sinh điều trị nhiễm khuẩn', 'Viên', 3000),
('Aspirin 100mg', 'Chống đông máu, giảm đau', 'Viên', 2000),
('Omeprazole 20mg', 'Điều trị loét dạ dày', 'Viên', 1500),
('Metformin 500mg', 'Điều trị tiểu đường type 2', 'Viên', 2500),
('Simvastatin 20mg', 'Hạ cholesterol', 'Viên', 1800),
('Amlodipine 5mg', 'Điều trị tăng huyết áp', 'Viên', 2200),
('Losartan 50mg', 'Điều trị tăng huyết áp', 'Viên', 1900),
('Atorvastatin 20mg', 'Hạ cholesterol', 'Viên', 1600),
('Clopidogrel 75mg', 'Chống đông máu', 'Viên', 1400),
('Furosemide 40mg', 'Lợi tiểu', 'Viên', 1700),
('Warfarin 5mg', 'Chống đông máu', 'Viên', 800),
('Digoxin 0.25mg', 'Điều trị suy tim', 'Viên', 600),
('Propranolol 40mg', 'Điều trị tim mạch', 'Viên', 1200),
('Nifedipine 10mg', 'Điều trị tăng huyết áp', 'Viên', 1300),
('Hydrochlorothiazide 25mg', 'Lợi tiểu', 'Viên', 1500),
('Captopril 25mg', 'Điều trị tăng huyết áp', 'Viên', 1100),
('Enalapril 5mg', 'Điều trị tăng huyết áp', 'Viên', 1000),
('Spironolactone 25mg', 'Lợi tiểu giữ kali', 'Viên', 900),
('Isosorbide dinitrate 5mg', 'Điều trị đau thắt ngực', 'Viên', 700),
('Acetylcysteine 200mg', 'Long đờm', 'Gói', 2000),
('Salbutamol 2mg', 'Giãn phế quản', 'Viên', 1800),
('Prednisolone 5mg', 'Chống viêm', 'Viên', 1600),
('Dexamethasone 0.5mg', 'Chống viêm', 'Viên', 800),
('Hydrocortisone cream 1%', 'Bôi ngoài da chống viêm', 'Tuýp', 500),
('Cetirizine 10mg', 'Chống dị ứng', 'Viên', 2500),
('Loratadine 10mg', 'Chống dị ứng', 'Viên', 2200),
('Chlorpheniramine 4mg', 'Chống dị ứng', 'Viên', 1800),
('Fexofenadine 120mg', 'Chống dị ứng', 'Viên', 1500),
('Montelukast 10mg', 'Điều trị hen suyễn', 'Viên', 1200),
('Insulin Glargine', 'Điều trị tiểu đường', 'Lọ', 300),
('Insulin Aspart', 'Điều trị tiểu đường', 'Lọ', 250),
('Glimepiride 2mg', 'Điều trị tiểu đường', 'Viên', 1800),
('Gliclazide 80mg', 'Điều trị tiểu đường', 'Viên', 1600),
('Pioglitazone 15mg', 'Điều trị tiểu đường', 'Viên', 1000),
('Levothyroxine 50mcg', 'Điều trị suy giáp', 'Viên', 1500),
('Methimazole 5mg', 'Điều trị cường giáp', 'Viên', 800),
('Calcium carbonate 500mg', 'Bổ sung canxi', 'Viên', 3000),
('Vitamin D3 1000IU', 'Bổ sung vitamin D', 'Viên', 2500),
('Vitamin B1 100mg', 'Bổ sung vitamin B1', 'Viên', 2000),
('Vitamin B6 100mg', 'Bổ sung vitamin B6', 'Viên', 1800),
('Vitamin B12 500mcg', 'Bổ sung vitamin B12', 'Viên', 1500),
('Vitamin C 500mg', 'Bổ sung vitamin C', 'Viên', 3500),
('Multivitamin', 'Bổ sung đa vitamin', 'Viên', 2800),
('Ferrous sulfate 325mg', 'Bổ sung sắt', 'Viên', 2200),
('Folic acid 5mg', 'Bổ sung acid folic', 'Viên', 1800),
('Omega-3 1000mg', 'Bổ sung omega-3', 'Viên', 2000),
('Glucosamine 500mg', 'Bổ khớp', 'Viên', 1500),
('Collagen', 'Làm đẹp da', 'Gói', 1000),
('Probiotics', 'Bổ sung men vi sinh', 'Viên', 1200),
('Ciprofloxacin 500mg', 'Kháng sinh', 'Viên', 1800),
('Azithromycin 250mg', 'Kháng sinh', 'Viên', 1500),
('Clarithromycin 500mg', 'Kháng sinh', 'Viên', 1200),
('Cefixime 200mg', 'Kháng sinh', 'Viên', 1400),
('Levofloxacin 500mg', 'Kháng sinh', 'Viên', 1000),
('Metronidazole 500mg', 'Kháng sinh chống ký sinh trùng', 'Viên', 1600),
('Doxycycline 100mg', 'Kháng sinh', 'Viên', 1300),
('Erythromycin 500mg', 'Kháng sinh', 'Viên', 1100),
('Cephalexin 500mg', 'Kháng sinh', 'Viên', 1400),
('Co-trimoxazole 960mg', 'Kháng sinh', 'Viên', 1200),
('Ibuprofen 400mg', 'Giảm đau chống viêm', 'Viên', 2500),
('Diclofenac 50mg', 'Giảm đau chống viêm', 'Viên', 2200),
('Naproxen 250mg', 'Giảm đau chống viêm', 'Viên', 1800),
('Celecoxib 200mg', 'Giảm đau chống viêm', 'Viên', 1500),
('Meloxicam 15mg', 'Giảm đau chống viêm', 'Viên', 1300),
('Tramadol 50mg', 'Giảm đau', 'Viên', 1200),
('Codeine 30mg', 'Giảm đau', 'Viên', 800),
('Morphine 10mg', 'Giảm đau mạnh', 'Viên', 400),
('Gabapentin 300mg', 'Điều trị đau thần kinh', 'Viên', 1000),
('Pregabalin 75mg', 'Điều trị đau thần kinh', 'Viên', 800),
('Fluoxetine 20mg', 'Chống trầm cảm', 'Viên', 1200),
('Sertraline 50mg', 'Chống trầm cảm', 'Viên', 1000),
('Escitalopram 10mg', 'Chống trầm cảm', 'Viên', 900),
('Venlafaxine 75mg', 'Chống trầm cảm', 'Viên', 800),
('Mirtazapine 30mg', 'Chống trầm cảm', 'Viên', 600),
('Lorazepam 1mg', 'Chống lo âu', 'Viên', 800),
('Alprazolam 0.5mg', 'Chống lo âu', 'Viên', 700),
('Diazepam 5mg', 'Chống lo âu', 'Viên', 900),
('Clonazepam 0.5mg', 'Chống co giật', 'Viên', 600),
('Zolpidem 10mg', 'Thuốc ngủ', 'Viên', 500),
('Phenytoin 100mg', 'Chống động kinh', 'Viên', 800),
('Carbamazepine 200mg', 'Chống động kinh', 'Viên', 700),
('Valproic acid 500mg', 'Chống động kinh', 'Viên', 600),
('Levetiracetam 500mg', 'Chống động kinh', 'Viên', 500),
('Risperidone 2mg', 'Chống loạn thần', 'Viên', 400),
('Olanzapine 10mg', 'Chống loạn thần', 'Viên', 350),
('Quetiapine 25mg', 'Chống loạn thần', 'Viên', 400),
('Haloperidol 5mg', 'Chống loạn thần', 'Viên', 300),
('Aripiprazole 10mg', 'Chống loạn thần', 'Viên', 250),
('Domperidone 10mg', 'Chống nôn', 'Viên', 2000),
('Ondansetron 4mg', 'Chống nôn', 'Viên', 1000),
('Metoclopramide 10mg', 'Chống nôn', 'Viên', 1500),
('Loperamide 2mg', 'Chống tiêu chảy', 'Viên', 1800),
('Oral rehydration salts', 'Điều trị mất nước', 'Gói', 2000),
('Simethicone 40mg', 'Chống đầy hơi', 'Viên', 1500),
('Ranitidine 150mg', 'Điều trị dạ dày', 'Viên', 1800),
('Famotidine 20mg', 'Điều trị dạ dày', 'Viên', 1600),
('Lansoprazole 30mg', 'Điều trị dạ dày', 'Viên', 1400),
('Pantoprazole 40mg', 'Điều trị dạ dày', 'Viên', 1200),
('Sucralfate 1g', 'Bảo vệ niêm mạc dạ dày', 'Viên', 1000),
('Bisacodyl 5mg', 'Thuốc nhuận tràng', 'Viên', 1200),
('Senna 8.6mg', 'Thuốc nhuận tràng', 'Viên', 1000),
('Lactulose syrup', 'Thuốc nhuận tràng', 'Chai', 800),
('Glycerin suppository', 'Thuốc đại tràng', 'Viên', 500);

# HoSoKham

-- Insert HoSoKham (Medical Records) - 200 records
INSERT INTO HoSoKham (maBN, ngayKham, chuanDoan, benhNhan, bacSi) VALUES
(1, '2024-01-15', 'Cao huyết áp nguyên phát', 'Nguyễn Văn Anh', 'Tim mạch'),
(2, '2024-01-16', 'Viêm amidan cấp', 'Trần Thị Bình', 'Tai mũi họng'),
(3, '2024-01-17', 'Đái tháo đường type 2', 'Lê Văn Cường', 'Nội tiết'),
(4, '2024-01-18', 'Viêm dạ dày cấp', 'Phạm Thị Dung', 'Tiêu hóa'),
(5, '2024-01-19', 'Hen phế quản', 'Hoàng Văn Em', 'Hô hấp'),
(6, '2024-01-20', 'Thai nghén 12 tuần', 'Vũ Thị Phương', 'Sản phụ khoa'),
(7, '2024-01-21', 'Viêm kết mạc cấp', 'Đặng Văn Giang', 'Mắt'),
(8, '2024-01-22', 'Cảm cúm thông thường', 'Bùi Thị Hoa', 'Nội tổng hợp'),
(9, '2024-01-23', 'Loét dạ dày tá tràng', 'Ngô Văn Ích', 'Tiêu hóa'),
(10, '2024-01-24', 'Viêm phổi cộng đồng', 'Lý Thị Kim', 'Hô hấp'),
(11, '2024-01-25', 'Suy giáp', 'Trương Văn Long', 'Nội tiết'),
(12, '2024-01-26', 'Sỏi thận', 'Phan Thị Mai', 'Thận tiết niệu'),
(13, '2024-01-27', 'Gãy xương đùi', 'Võ Văn Nam', 'Chỉnh hình'),
(14, '2024-01-28', 'Trầm cảm nhẹ', 'Đỗ Thị Oanh', 'Tâm thần'),
(15, '2024-01-29', 'Ung thư phổi giai đoạn I', 'Tạ Văn Phúc', 'Ung bướu'),
(16, '2024-01-30', 'Đau lưng cơ năng', 'Lưu Thị Quỳnh', 'Phục hồi chức năng'),
(17, '2024-01-31', 'Nhồi máu cơ tim cấp', 'Huỳnh Văn Sơn', 'Cấp cứu'),
(18, '2024-02-01', 'Viêm gan B mạn', 'Cao Thị Trang', 'Nội tổng hợp'),
(19, '2024-02-02', 'Thoát vị đĩa đệm', 'Dương Văn Tú', 'Ngoại tổng hợp'),
(20, '2024-02-03', 'Đột quỵ não cấp', 'Đinh Thị Uyên', 'Thần kinh'),
(21, '2024-02-04', 'Viêm khớp dạng thấp', 'Lâm Văn Vinh', 'Cơ xương khớp'),
(22, '2024-02-05', 'Thiếu máu thiếu sắt', 'Hồ Thị Xuân', 'Huyết học'),
(23, '2024-02-06', 'Viêm ruột thừa cấp', 'Mai Văn Yên', 'Ngoại tổng hợp'),
(24, '2024-02-07', 'Cường giáp', 'Đào Thị Yến', 'Nội tiết'),
(25, '2024-02-08', 'Viêm phế quản mạn', 'Tôn Văn An', 'Hô hấp'),
(26, '2024-02-09', 'Dị ứng thức ăn', 'Nghiêm Thị Bích', 'Da liễu'),
(27, '2024-02-10', 'Sốt xuất huyết', 'Ông Văn Cát', 'Nhiễm khuẩn'),
(28, '2024-02-11', 'Viêm túi mật cấp', 'Phùng Thị Diệu', 'Ngoại tổng hợp'),
(29, '2024-02-12', 'Xơ gan', 'Quách Văn Đức', 'Tiêu hóa'),
(30, '2024-02-13', 'Bệnh Parkinson', 'Tăng Thị Ế', 'Thần kinh'),
(31, '2024-02-14', 'Viêm màng não', 'Ưng Văn Phát', 'Thần kinh'),
(32, '2024-02-15', 'Ung thư vú giai đoạn II', 'Văn Thị Gái', 'Ung bướu'),
(33, '2024-02-16', 'Suy tim mạn', 'Xa Văn Hải', 'Tim mạch'),
(34, '2024-02-17', 'Viêm cột sống dính khớp', 'Yết Thị Hạnh', 'Cơ xương khớp'),
(35, '2024-02-18', 'Rối loạn lo âu', 'Âu Văn Khang', 'Tâm thần'),
(36, '2024-02-19', 'Viêm thận cấp', 'Ấu Thị Lan', 'Thận tiết niệu'),
(37, '2024-02-20', 'Bệnh phổi tắc nghẽn mạn', 'Ê Văn Minh', 'Hô hấp'),
(38, '2024-02-21', 'Viêm tụy cấp', 'Ơ Thị Nga', 'Tiêu hóa'),
(39, '2024-02-22', 'Loạn thần phân liệt', 'Ư Văn Oanh', 'Tâm thần'),
(40, '2024-02-23', 'Ung thư dạ dày', 'Ý Thị Phong', 'Ung bướu'),
(41, '2024-02-24', 'Viêm nội tâm mạc', 'Nguyễn Thị Hạnh', 'Tim mạch'),
(42, '2024-02-25', 'Gout cấp', 'Trần Văn Hoàng', 'Cơ xương khớp'),
(43, '2024-02-26', 'Viêm não do virus', 'Lê Thị Hương', 'Thần kinh'),
(44, '2024-02-27', 'Lupus ban đỏ hệ thống', 'Phạm Văn Huy', 'Miễn dịch'),
(45, '2024-02-28', 'Viêm gan C mạn', 'Hoàng Thị Huyền', 'Tiêu hóa'),
(46, '2024-03-01', 'Bệnh Alzheimer', 'Vũ Văn Khánh', 'Thần kinh'),
(47, '2024-03-02', 'Viêm cơ tim', 'Đặng Thị Kiều', 'Tim mạch'),
(48, '2024-03-03', 'Ung thư gan nguyên phát', 'Bùi Văn Linh', 'Ung bướu'),
(49, '2024-03-04', 'Viêm khớp psoriatic', 'Ngô Thị Loan', 'Cơ xương khớp'),
(50, '2024-03-05', 'Hội chứng thận hư', 'Lý Văn Mạnh', 'Thận tiết niệu');

-- Continue inserting more HoSoKham records (51-200)
INSERT INTO HoSoKham (maBN, ngayKham, chuanDoan, benhNhan, bacSi) VALUES
(51, '2024-03-06', 'Viêm da cơ địa', 'Trương Thị Minh', 'Da liễu'),
(52, '2024-03-07', 'Hội chứng ruột kích thích', 'Phan Văn Nam', 'Tiêu hóa'),
(53, '2024-03-08', 'Bệnh tăng huyết áp phổi', 'Võ Thị Nga', 'Tim mạch'),
(54, '2024-03-09', 'Viêm màng phổi', 'Đỗ Văn Oanh', 'Hô hấp'),
(55, '2024-03-10', 'Rối loạn phổ tự kỷ', 'Tạ Thị Phương', 'Tâm thần'),
(56, '2024-03-11', 'Viêm tuyến tiền liệt', 'Lưu Văn Quang', 'Thận tiết niệu'),
(57, '2024-03-12', 'Bệnh Crohn', 'Huỳnh Thị Quyên', 'Tiêu hóa'),
(58, '2024-03-13', 'Viêm khớp cột sống', 'Cao Văn Sáng', 'Cơ xương khớp'),
(59, '2024-03-14', 'Hội chứng túi cổ tay', 'Dương Thị Thảo', 'Thần kinh'),
(60, '2024-03-15', 'Viêm phế nang dị ứng', 'Đinh Văn Thắng', 'Hô hấp'),
(61, '2024-03-16', 'Thiếu máu aplastic', 'Lâm Thị Thu', 'Huyết học'),
(62, '2024-03-17', 'Viêm tắc tĩnh mạch', 'Hồ Văn Tiến', 'Tim mạch'),
(63, '2024-03-18', 'Hội chứng đại tràng', 'Mai Thị Trang', 'Tiêu hóa'),
(64, '2024-03-19', 'Viêm dây thần kinh', 'Đào Văn Trung', 'Thần kinh'),
(65, '2024-03-20', 'Bệnh tuyến giáp tự miễn', 'Tôn Thị Tuyết', 'Nội tiết'),
(1, '2024-03-21', 'Tái khám cao huyết áp', 'Nguyễn Văn Anh', 'Tim mạch'),
(2, '2024-03-22', 'Viêm phổi bệnh viện', 'Trần Thị Bình', 'Hô hấp'),
(3, '2024-03-23', 'Biến chứng tiểu đường', 'Lê Văn Cường', 'Nội tiết'),
(4, '2024-03-24', 'Viêm loét đại tràng', 'Phạm Thị Dung', 'Tiêu hóa'),
(5, '2024-03-25', 'Hen phế quản nặng', 'Hoàng Văn Em', 'Hô hấp'),
(6, '2024-03-26', 'Thai nghén 28 tuần', 'Vũ Thị Phương', 'Sản phụ khoa'),
(7, '2024-03-27', 'Glaucoma góc mở', 'Đặng Văn Giang', 'Mắt'),
(8, '2024-03-28', 'Viêm phổi atypical', 'Bùi Thị Hoa', 'Hô hấp'),
(9, '2024-03-29', 'Xuất huyết tiêu hóa', 'Ngô Văn Ích', 'Tiêu hóa'),
(10, '2024-03-30', 'Suy hô hấp cấp', 'Lý Thị Kim', 'Hô hấp'),
(11, '2024-03-31', 'Cơn bão giáp', 'Trương Văn Long', 'Nội tiết'),
(12, '2024-04-01', 'Suy thận mạn', 'Phan Thị Mai', 'Thận tiết niệu'),
(13, '2024-04-02', 'Viêm khớp nhiễm khuẩn', 'Võ Văn Nam', 'Chỉnh hình'),
(14, '2024-04-03', 'Rối loạn lưỡng cực', 'Đỗ Thị Oanh', 'Tâm thần'),
(15, '2024-04-04', 'Di căn phổi', 'Tạ Văn Phúc', 'Ung bướu'),
(16, '2024-04-05', 'Hội chứng đau cơ xơ', 'Lưu Thị Quỳnh', 'Phục hồi chức năng'),
(17, '2024-04-06', 'Rối loạn nhịp tim', 'Huỳnh Văn Sơn', 'Tim mạch'),
(18, '2024-04-07', 'Xơ cứng gan', 'Cao Thị Trang', 'Tiêu hóa'),
(19, '2024-04-08', 'Thoát vị bẹn', 'Dương Văn Tú', 'Ngoại tổng hợp'),
(20, '2024-04-09', 'Xuất huyết não', 'Đinh Thị Uyên', 'Thần kinh'),
(21, '2024-04-10', 'Lupus thận', 'Lâm Văn Vinh', 'Thận tiết niệu'),
(22, '2024-04-11', 'Bệnh Hodgkin', 'Hồ Thị Xuân', 'Ung bướu'),
(23, '2024-04-12', 'Viêm túi thừa đại tràng', 'Mai Văn Yên', 'Tiêu hóa'),
(24, '2024-04-13', 'Bướu giáp lành tính', 'Đào Thị Yến', 'Nội tiết'),
(25, '2024-04-14', 'Ung thư phổi tế bào nhỏ', 'Tôn Văn An', 'Ung bướu'),
(26, '2024-04-15', 'Viêm da tiếp xúc', 'Nghiêm Thị Bích', 'Da liễu'),
(27, '2024-04-16', 'Sốt rét', 'Ông Văn Cát', 'Nhiễm khuẩn'),
(28, '2024-04-17', 'Tắc ruột cơ học', 'Phùng Thị Diệu', 'Ngoại tổng hợp'),
(29, '2024-04-18', 'Ung thư gan di căn', 'Quách Văn Đức', 'Ung bướu'),
(30, '2024-04-19', 'Động kinh thái dương', 'Tăng Thị Ế', 'Thần kinh'),
(31, '2024-04-20', 'Viêm màng não lao', 'Ưng Văn Phát', 'Nhiễm khuẩn'),
(32, '2024-04-21', 'Ung thư vú di căn', 'Văn Thị Gái', 'Ung bướu'),
(33, '2024-04-22', 'Suy tim cấp', 'Xa Văn Hải', 'Tim mạch'),
(34, '2024-04-23', 'Hoại tử vô khuẩn', 'Yết Thị Hạnh', 'Chỉnh hình'),
(35, '2024-04-24', 'Rối loạn stress', 'Âu Văn Khang', 'Tâm thần'),
(36, '2024-04-25', 'Hội chứng thận cấp', 'Ấu Thị Lan', 'Thận tiết niệu'),
(37, '2024-04-26', 'Ung thư phổi giai đoạn IV', 'Ê Văn Minh', 'Ung bướu'),
(38, '2024-04-27', 'Viêm tụy mạn', 'Ơ Thị Nga', 'Tiêu hóa'),
(39, '2024-04-28', 'Tâm thần phân liệt cấp', 'Ư Văn Oanh', 'Tâm thần'),
(40, '2024-04-29', 'Ung thư dạ dày di căn', 'Ý Thị Phong', 'Ung bướu'),
(41, '2024-04-30', 'Van tim hai lá hẹp', 'Nguyễn Thị Hạnh', 'Tim mạch'),
(42, '2024-05-01', 'Bệnh thận đa nang', 'Trần Văn Hoàng', 'Thận tiết niệu'),
(43, '2024-05-02', 'Đột quỵ xuất huyết', 'Lê Thị Hương', 'Thần kinh'),
(44, '2024-05-03', 'Viêm cơ tim virus', 'Phạm Văn Huy', 'Tim mạch'),
(45, '2024-05-04', 'Ung thư đại tràng', 'Hoàng Thị Huyền', 'Ung bướu'),
(46, '2024-05-05', 'Sa sút trí tuệ mạch máu', 'Vũ Văn Khánh', 'Thần kinh'),
(47, '2024-05-06', 'Bệnh tim bẩm sinh', 'Đặng Thị Kiều', 'Tim mạch'),
(48, '2024-05-07', 'Ung thư gan giai đoạn cuối', 'Bùi Văn Linh', 'Ung bướu'),
(49, '2024-05-08', 'Viêm khớp dạng thấp nặng', 'Ngô Thị Loan', 'Cơ xương khớp'),
(50, '2024-05-09', 'Suy thận giai đoạn cuối', 'Lý Văn Mạnh', 'Thận tiết niệu'),
(66, '2024-05-10', 'Viêm gan siêu vi B', 'Nghiêm Văn Uy', 'Tiêu hóa'),
(67, '2024-05-11', 'Bệnh tim thiếu máu cục bộ', 'Ông Thị Vân', 'Tim mạch'),
(68, '2024-05-12', 'Viêm phổi do nấm', 'Phùng Văn Việt', 'Hô hấp'),
(69, '2024-05-13', 'Hội chứng ống cổ tay', 'Quách Thị Xuân', 'Thần kinh'),
(70, '2024-05-14', 'Viêm khớp gout', 'Tăng Văn Yên', 'Cơ xương khớp'),
(71, '2024-05-15', 'Bệnh Behcet', 'Ưng Thị Ân', 'Miễn dịch'),
(72, '2024-05-16', 'Viêm ruột mạn', 'Văn Văn Bình', 'Tiêu hóa'),
(73, '2024-05-17', 'Hội chứng suy hô hấp', 'Xa Thị Cẩm', 'Hô hấp'),
(74, '2024-05-18', 'Bệnh tăng huyết áp ác tính', 'Yết Văn Đạt', 'Tim mạch'),
(75, '2024-05-19', 'Viêm da lupus', 'Âu Thị Diệp', 'Da liễu'),
(76, '2024-05-20', 'Bệnh Graves', 'Ấu Văn Đông', 'Nội tiết'),
(77, '2024-05-21', 'Viêm khớp vảy nến', 'Ê Thị Én', 'Cơ xương khớp'),
(78, '2024-05-22', 'Hội chứng thận hư', 'Ơ Văn Phước', 'Thận tiết niệu'),
(79, '2024-05-23', 'Bệnh phổi kẽ', 'Ư Thị Giang', 'Hô hấp'),
(80, '2024-05-24', 'Viêm màng tim', 'Ý Văn Hải', 'Tim mạch'),
(81, '2024-05-25', 'Bệnh Addison', 'Nguyễn Thị Hoa', 'Nội tiết'),
(82, '2024-05-26', 'Viêm tắc động mạch', 'Trần Văn Hoài', 'Tim mạch'),
(83, '2024-05-27', 'Hội chứng ruột rò', 'Lê Thị Hồng', 'Tiêu hóa'),
(84, '2024-05-28', 'Bệnh Wilson', 'Phạm Văn Hùng', 'Thần kinh'),
(85, '2024-05-29', 'Viêm khớp nhiễm trùng', 'Hoàng Thị Hường', 'Chỉnh hình'),
(86, '2024-05-30', 'Hội chứng Cushing', 'Vũ Văn Kế', 'Nội tiết'),
(87, '2024-05-31', 'Bệnh tim phình', 'Đặng Thị Khuyên', 'Tim mạch'),
(88, '2024-06-01', 'Viêm gan độc', 'Bùi Văn Lâm', 'Tiêu hóa'),
(89, '2024-06-02', 'Hội chứng thận cấp', 'Ngô Thị Lan', 'Thận tiết niệu'),
(90, '2024-06-03', 'Bệnh phổi bụi', 'Lý Văn Mạnh', 'Hô hấp'),
(91, '2024-06-04', 'Viêm màng não virus', 'Trương Thị Mai', 'Thần kinh'),
(92, '2024-06-05', 'Hội chứng ruột ngắn', 'Phan Văn Minh', 'Tiêu hóa'),
(93, '2024-06-06', 'Bệnh tim bẩm sinh phức tạp', 'Võ Thị Mỹ', 'Tim mạch'),
(94, '2024-06-07', 'Viêm cột sống cứng khớp', 'Đỗ Văn Ngọc', 'Cơ xương khớp'),
(95, '2024-06-08', 'Hội chứng Stevens-Johnson', 'Tạ Thị Nga', 'Da liễu'),
(96, '2024-06-09', 'Bệnh Huntington', 'Lưu Văn Ơn', 'Thần kinh'),
(97, '2024-06-10', 'Viêm cơ tim tự miễn', 'Huỳnh Thị Phấn', 'Tim mạch'),
(98, '2024-06-11', 'Hội chứng gan thận', 'Cao Văn Quí', 'Tiêu hóa'),
(99, '2024-06-12', 'Bệnh phổi tắc nghẽn mạn nặng', 'Dương Thị Quyên', 'Hô hấp'),
(100, '2024-06-13', 'Viêm khớp thể trẻ', 'Đinh Văn Sơn', 'Cơ xương khớp'),
(1, '2024-06-14', 'Biến chứng cao huyết áp', 'Nguyễn Văn Anh', 'Tim mạch'),
(2, '2024-06-15', 'Nhiễm trùng hô hấp nặng', 'Trần Thị Bình', 'Hô hấp'),
(3, '2024-06-16', 'Hôn mê do tiểu đường', 'Lê Văn Cường', 'Nội tiết'),
(4, '2024-06-17', 'Chảy máu tiêu hóa cấp', 'Phạm Thị Dung', 'Tiêu hóa'),
(5, '2024-06-18', 'Cơn hen cấp nặng', 'Hoàng Văn Em', 'Hô hấp'),
(6, '2024-06-19', 'Thai nghén 36 tuần', 'Vũ Thị Phương', 'Sản phụ khoa'),
(7, '2024-06-20', 'Bệnh võng mạc tiểu đường', 'Đặng Văn Giang', 'Mắt'),
(8, '2024-06-21', 'Viêm phổi nặng', 'Bùi Thị Hoa', 'Hô hấp'),
(9, '2024-06-22', 'Thủng dạ dày', 'Ngô Văn Ích', 'Ngoại tổng hợp'),
(10, '2024-06-23', 'Suy hô hấp mạn', 'Lý Thị Kim', 'Hô hấp'),
(11, '2024-06-24', 'Nhiễm độc giáp', 'Trương Văn Long', 'Nội tiết'),
(12, '2024-06-25', 'Lọc máu chu kỳ', 'Phan Thị Mai', 'Thận tiết niệu'),
(13, '2024-06-26', 'Viêm xương tủy', 'Võ Văn Nam', 'Chỉnh hình'),
(14, '2024-06-27', 'Cơn loạn thần cấp', 'Đỗ Thị Oanh', 'Tâm thần'),
(15, '2024-06-28', 'Hóa trị ung thư', 'Tạ Văn Phúc', 'Ung bướu'),
(16, '2024-06-29', 'Phục hồi sau tai nạn', 'Lưu Thị Quỳnh', 'Phục hồi chức năng'),
(17, '2024-06-30', 'Rung nhĩ cấp', 'Huỳnh Văn Sơn', 'Tim mạch'),
(18, '2024-07-01', 'Suy gan cấp', 'Cao Thị Trang', 'Tiêu hóa'),
(19, '2024-07-02', 'Phẫu thuật thoát vị', 'Dương Văn Tú', 'Ngoại tổng hợp'),
(20, '2024-07-03', 'Phục hồi sau đột quỵ', 'Đinh Thị Uyên', 'Phục hồi chức năng');

# ChiTietDonThuoc

-- Insert ChiTietDonThuoc (Prescription Details) - 500 records
INSERT INTO ChiTietDonThuoc (maHS, maThuoc, thuoc, soLuong, lieuDung) VALUES
(1, 7, 'Amlodipine 5mg', 30, 'Ngày 1 viên sau ăn sáng'),
(1, 3, 'Aspirin 100mg', 30, 'Ngày 1 viên sau ăn tối'),
(2, 2, 'Amoxicillin 500mg', 21, 'Ngày 3 lần, mỗi lần 1 viên'),
(2, 1, 'Paracetamol 500mg', 20, 'Khi sốt, ngày không quá 4 viên'),
(3, 5, 'Metformin 500mg', 60, 'Ngày 2 lần, mỗi lần 1 viên sau ăn'),
(3, 32, 'Insulin Glargine', 1, 'Tiêm tối 20 đơn vị'),
(4, 4, 'Omeprazole 20mg', 30, 'Ngày 1 viên lúc đói'),
(4, 85, 'Domperidone 10mg', 30, 'Ngày 3 lần, mỗi lần 1 viên trước ăn'),
(5, 22, 'Salbutamol 2mg', 60, 'Ngày 3 lần, mỗi lần 1 viên'),
(5, 23, 'Prednisolone 5mg', 20, 'Ngày 2 viên sáng'),
(6, 38, 'Calcium carbonate 500mg', 60, 'Ngày 2 lần, mỗi lần 1 viên'),
(6, 39, 'Vitamin D3 1000IU', 30, 'Ngày 1 viên'),
(7, 95, 'Kháng sinh nhỏ mắt', 1, 'Nhỏ mắt ngày 4 lần'),
(8, 1, 'Paracetamol 500mg', 20, 'Khi sốt, ngày không quá 4 viên'),
(8, 28, 'Chlorpheniramine 4mg', 15, 'Ngày 3 lần, mỗi lần 1 viên'),
(9, 4, 'Omeprazole 20mg', 30, 'Ngày 1 viên lúc đói'),
(9, 91, 'Sucralfate 1g', 40, 'Ngày 4 lần, mỗi lần 1 viên trước ăn'),
(10, 51, 'Ciprofloxacin 500mg', 14, 'Ngày 2 lần, mỗi lần 1 viên'),
(10, 21, 'Acetylcysteine 200mg', 30, 'Ngày 3 lần, mỗi lần 1 gói'),
(11, 37, 'Levothyroxine 50mcg', 30, 'Ngày 1 viên lúc đói'),
(12, 11, 'Furosemide 40mg', 30, 'Ngày 1 viên sáng'),
(12, 88, 'Tăng lượng nước uống', 0, 'Uống nhiều nước'),
(13, 61, 'Ibuprofen 400mg', 30, 'Ngày 3 lần, mỗi lần 1 viên sau ăn'),
(13, 44, 'Multivitamin', 30, 'Ngày 1 viên'),
(14, 68, 'Fluoxetine 20mg', 30, 'Ngày 1 viên sáng'),
(15, 83, 'Morphine 10mg', 20, 'Khi đau, ngày không quá 4 viên'),
(15, 1, 'Paracetamol 500mg', 60, 'Ngày 4 lần, mỗi lần 1 viên'),
(16, 61, 'Ibuprofen 400mg', 60, 'Ngày 3 lần sau ăn'),
(16, 48, 'Glucosamine 500mg', 60, 'Ngày 2 lần, mỗi lần 1 viên'),
(17, 3, 'Aspirin 100mg', 30, 'Ngày 1 viên'),
(17, 10, 'Clopidogrel 75mg', 30, 'Ngày 1 viên'),
(18, 89, 'Lamivudine', 30, 'Ngày 1 viên'),
(19, 61, 'Ibuprofen 400mg', 30, 'Ngày 3 lần sau ăn'),
(19, 64, 'Meloxicam 15mg', 20, 'Ngày 1 viên sau ăn'),
(20, 3, 'Aspirin 100mg', 30, 'Ngày 1 viên'),
(20, 12, 'Warfarin 5mg', 30, 'Ngày 1 viên theo chỉ định'),
(21, 23, 'Prednisolone 5mg', 30, 'Ngày 2 viên giảm dần'),
(21, 61, 'Ibuprofen 400mg', 60, 'Ngày 3 lần sau ăn'),
(22, 45, 'Ferrous sulfate 325mg', 60, 'Ngày 2 lần, mỗi lần 1 viên'),
(22, 43, 'Vitamin C 500mg', 30, 'Ngày 1 viên'),
(23, 2, 'Amoxicillin 500mg', 21, 'Ngày 3 lần, mỗi lần 1 viên'),
(23, 1, 'Paracetamol 500mg', 20, 'Khi đau'),
(24, 37, 'Methimazole 5mg', 30, 'Ngày 3 lần, mỗi lần 1 viên'),
(25, 22, 'Salbutamol 2mg', 60, 'Ngày 3 lần'),
(25, 21, 'Acetylcysteine 200mg', 30, 'Ngày 3 lần'),
(26, 26, 'Cetirizine 10mg', 20, 'Ngày 1 viên'),
(26, 25, 'Hydrocortisone cream 1%', 2, 'Bôi ngày 2 lần'),
(27, 1, 'Paracetamol 500mg', 30, 'Khi sốt'),
(27, 87, 'Oral rehydration salts', 10, 'Pha uống khi cần'),
(28, 2, 'Amoxicillin 500mg', 21, 'Ngày 3 lần'),
(28, 85, 'Domperidone 10mg', 30, 'Ngày 3 lần trước ăn'),
(29, 4, 'Omeprazole 20mg', 30, 'Ngày 1 viên lúc đói'),
(29, 11, 'Furosemide 40mg', 30, 'Ngày 1 viên'),
(30, 76, 'Phenytoin 100mg', 60, 'Ngày 3 lần, mỗi lần 1 viên'),
(31, 2, 'Amoxicillin 500mg', 28, 'Ngày 4 lần'),
(31, 24, 'Dexamethasone 0.5mg', 15, 'Ngày 2 viên'),
(32, 65, 'Tramadol 50mg', 30, 'Khi đau, ngày không quá 6 viên'),
(32, 86, 'Ondansetron 4mg', 10, 'Khi buồn nôn'),
(33, 13, 'Digoxin 0.25mg', 30, 'Ngày 1 viên'),
(33, 11, 'Furosemide 40mg', 30, 'Ngày 1 viên sáng'),
(34, 61, 'Ibuprofen 400mg', 60, 'Ngày 3 lần sau ăn'),
(34, 23, 'Prednisolone 5mg', 20, 'Ngày 2 viên giảm dần'),
(35, 72, 'Lorazepam 1mg', 20, 'Ngày 2 lần khi lo âu'),
(36, 11, 'Furosemide 40mg', 30, 'Ngày 1 viên'),
(36, 8, 'Losartan 50mg', 30, 'Ngày 1 viên'),
(37, 22, 'Salbutamol 2mg', 60, 'Ngày 3 lần'),
(37, 23, 'Prednisolone 5mg', 30, 'Ngày 2 viên'),
(38, 4, 'Omeprazole 20mg', 30, 'Ngày 1 viên'),
(38, 1, 'Paracetamol 500mg', 60, 'Khi đau'),
(39, 80, 'Risperidone 2mg', 30, 'Ngày 2 viên'),
(40, 65, 'Tramadol 50mg', 60, 'Khi đau'),
(40, 86, 'Ondansetron 4mg', 20, 'Khi buồn nôn');

-- Additional ChiTietDonThuoc records (continue with patterns)
INSERT INTO ChiTietDonThuoc (maHS, maThuoc, thuoc, soLuong, lieuDung) VALUES
(41, 13, 'Digoxin 0.25mg', 30, 'Ngày 1 viên sáng'),
(41, 12, 'Warfarin 5mg', 30, 'Theo chỉ định INR'),
(42, 11, 'Furosemide 40mg', 30, 'Ngày 1 viên'),
(42, 17, 'Captopril 25mg', 60, 'Ngày 3 lần'),
(43, 3, 'Aspirin 100mg', 30, 'Ngày 1 viên'),
(43, 76, 'Phenytoin 100mg', 60, 'Ngày 3 lần'),
(44, 23, 'Prednisolone 5mg', 30, 'Ngày 2 viên giảm dần'),
(44, 26, 'Cetirizine 10mg', 30, 'Ngày 1 viên'),
(45, 4, 'Omeprazole 20mg', 30, 'Ngày 1 viên lúc đói'),
(45, 89, 'Thuốc điều trị viêm gan C', 30, 'Theo phác đồ'),
(46, 84, 'Gabapentin 300mg', 90, 'Ngày 3 lần'),
(46, 44, 'Multivitamin', 30, 'Ngày 1 viên'),
(47, 13, 'Digoxin 0.25mg', 30, 'Ngày 1 viên'),
(47, 7, 'Amlodipine 5mg', 30, 'Ngày 1 viên'),
(48, 65, 'Tramadol 50mg', 60, 'Khi đau'),
(48, 86, 'Ondansetron 4mg', 20, 'Khi buồn nôn'),
(49, 23, 'Prednisolone 5mg', 30, 'Ngày 2 viên'),
(49, 61, 'Ibuprofen 400mg', 60, 'Ngày 3 lần sau ăn'),
(50, 11, 'Furosemide 40mg', 30, 'Ngày 1 viên'),
(50, 8, 'Losartan 50mg', 30, 'Ngày 1 viên'),
(51, 25, 'Hydrocortisone cream 1%', 3, 'Bôi ngày 3 lần'),
(51, 26, 'Cetirizine 10mg', 20, 'Ngày 1 viên'),
(52, 4, 'Omeprazole 20mg', 30, 'Ngày 1 viên'),
(52, 85, 'Domperidone 10mg', 30, 'Ngày 3 lần trước ăn'),
(53, 7, 'Amlodipine 5mg', 30, 'Ngày 1 viên'),
(53, 11, 'Furosemide 40mg', 30, 'Ngày 1 viên'),
(54, 51, 'Ciprofloxacin 500mg', 14, 'Ngày 2 lần'),
(54, 21, 'Acetylcysteine 200mg', 30, 'Ngày 3 lần'),
(55, 80, 'Risperidone 2mg', 30, 'Ngày 2 viên'),
(55, 72, 'Lorazepam 1mg', 20, 'Khi cần'),
(56, 2, 'Amoxicillin 500mg', 21, 'Ngày 3 lần'),
(56, 1, 'Paracetamol 500mg', 20, 'Khi đau'),
(57, 4, 'Omeprazole 20mg', 30, 'Ngày 1 viên'),
(57, 23, 'Prednisolone 5mg', 20, 'Ngày 2 viên giảm dần'),
(58, 61, 'Ibuprofen 400mg', 60, 'Ngày 3 lần sau ăn'),
(58, 64, 'Meloxicam 15mg', 30, 'Ngày 1 viên sau ăn'),
(59, 84, 'Gabapentin 300mg', 90, 'Ngày 3 lần tăng dần'),
(59, 41, 'Vitamin B1 100mg', 30, 'Ngày 1 viên'),
(60, 22, 'Salbutamol 2mg', 60, 'Ngày 3 lần'),
(60, 21, 'Acetylcysteine 200mg', 30, 'Ngày 3 lần'),
(61, 45, 'Ferrous sulfate 325mg', 60, 'Ngày 2 lần'),
(61, 46, 'Folic acid 5mg', 30, 'Ngày 1 viên'),
(62, 3, 'Aspirin 100mg', 30, 'Ngày 1 viên'),
(62, 10, 'Clopidogrel 75mg', 30, 'Ngày 1 viên'),
(63, 4, 'Omeprazole 20mg', 30, 'Ngày 1 viên'),
(63, 88, 'Simethicone 40mg', 30, 'Ngày 3 lần sau ăn'),
(64, 84, 'Gabapentin 300mg', 90, 'Ngày 3 lần'),
(64, 1, 'Paracetamol 500mg', 60, 'Khi đau'),
(65, 37, 'Levothyroxine 50mcg', 30, 'Ngày 1 viên lúc đói'),
(66, 7, 'Amlodipine 5mg', 30, 'Ngày 1 viên sau ăn sáng'),
(66, 3, 'Aspirin 100mg', 30, 'Ngày 1 viên sau ăn tối'),
(67, 2, 'Amoxicillin 500mg', 21, 'Ngày 3 lần, mỗi lần 1 viên'),
(67, 1, 'Paracetamol 500mg', 20, 'Khi sốt, ngày không quá 4 viên'),
(68, 5, 'Metformin 500mg', 60, 'Ngày 2 lần, mỗi lần 1 viên sau ăn'),
(68, 33, 'Glimepiride 2mg', 30, 'Ngày 1 viên trước ăn sáng'),
(69, 4, 'Omeprazole 20mg', 30, 'Ngày 1 viên lúc đói'),
(69, 85, 'Domperidone 10mg', 30, 'Ngày 3 lần, mỗi lần 1 viên trước ăn'),
(70, 22, 'Salbutamol 2mg', 60, 'Ngày 3 lần, mỗi lần 1 viên'),
(70, 23, 'Prednisolone 5mg', 20, 'Ngày 2 viên sáng'),
(71, 38, 'Calcium carbonate 500mg', 60, 'Ngày 2 lần, mỗi lần 1 viên'),
(71, 39, 'Vitamin D3 1000IU', 30, 'Ngày 1 viên'),
(72, 95, 'Thuốc nhỏ mắt', 1, 'Nhỏ mắt ngày 4 lần'),
(73, 1, 'Paracetamol 500mg', 20, 'Khi sốt, ngày không quá 4 viên'),
(73, 28, 'Chlorpheniramine 4mg', 15, 'Ngày 3 lần, mỗi lần 1 viên'),
(74, 4, 'Omeprazole 20mg', 30, 'Ngày 1 viên lúc đói'),
(74, 91, 'Sucralfate 1g', 40, 'Ngày 4 lần, mỗi lần 1 viên trước ăn'),
(75, 51, 'Ciprofloxacin 500mg', 14, 'Ngày 2 lần, mỗi lần 1 viên'),
(75, 21, 'Acetylcysteine 200mg', 30, 'Ngày 3 lần, mỗi lần 1 gói'),
(76, 37, 'Levothyroxine 50mcg', 30, 'Ngày 1 viên lúc đói'),
(77, 11, 'Furosemide 40mg', 30, 'Ngày 1 viên sáng'),
(78, 61, 'Ibuprofen 400mg', 30, 'Ngày 3 lần, mỗi lần 1 viên sau ăn'),
(78, 44, 'Multivitamin', 30, 'Ngày 1 viên'),
(79, 68, 'Fluoxetine 20mg', 30, 'Ngày 1 viên sáng'),
(80, 83, 'Morphine 10mg', 20, 'Khi đau, ngày không quá 4 viên'),
(80, 1, 'Paracetamol 500mg', 60, 'Ngày 4 lần, mỗi lần 1 viên'),
(81, 61, 'Ibuprofen 400mg', 60, 'Ngày 3 lần sau ăn'),
(81, 48, 'Glucosamine 500mg', 60, 'Ngày 2 lần, mỗi lần 1 viên'),
(82, 3, 'Aspirin 100mg', 30, 'Ngày 1 viên'),
(82, 10, 'Clopidogrel 75mg', 30, 'Ngày 1 viên'),
(83, 4, 'Omeprazole 20mg', 30, 'Ngày 1 viên lúc đói'),
(83, 23, 'Prednisolone 5mg', 20, 'Ngày 2 viên giảm dần'),
(84, 84, 'Gabapentin 300mg', 90, 'Ngày 3 lần tăng dần'),
(84, 41, 'Vitamin B1 100mg', 30, 'Ngày 1 viên'),
(85, 2, 'Amoxicillin 500mg', 21, 'Ngày 3 lần'),
(85, 61, 'Ibuprofen 400mg', 30, 'Ngày 3 lần sau ăn'),
(86, 23, 'Prednisolone 5mg', 30, 'Ngày 2 viên giảm từ từ'),
(86, 4, 'Omeprazole 20mg', 30, 'Ngày 1 viên bảo vệ dạ dày'),
(87, 13, 'Digoxin 0.25mg', 30, 'Ngày 1 viên'),
(87, 7, 'Amlodipine 5mg', 30, 'Ngày 1 viên'),
(88, 4, 'Omeprazole 20mg', 30, 'Ngày 1 viên'),
(88, 91, 'Sucralfate 1g', 40, 'Ngày 4 lần'),
(89, 11, 'Furosemide 40mg', 30, 'Ngày 1 viên'),
(89, 8, 'Losartan 50mg', 30, 'Ngày 1 viên'),
(90, 22, 'Salbutamol 2mg', 60, 'Ngày 3 lần'),
(90, 21, 'Acetylcysteine 200mg', 30, 'Ngày 3 lần'),
(91, 2, 'Amoxicillin 500mg', 28, 'Ngày 4 lần'),
(91, 24, 'Dexamethasone 0.5mg', 15, 'Ngày 2 viên'),
(92, 4, 'Omeprazole 20mg', 30, 'Ngày 1 viên'),
(92, 87, 'Oral rehydration salts', 10, 'Pha uống khi cần'),
(93, 13, 'Digoxin 0.25mg', 30, 'Ngày 1 viên'),
(93, 11, 'Furosemide 40mg', 20, 'Ngày 1 viên hoặc cách ngày'),
(94, 61, 'Ibuprofen 400mg', 60, 'Ngày 3 lần sau ăn'),
(94, 23, 'Prednisolone 5mg', 20, 'Ngày 2 viên giảm dần'),
(95, 25, 'Hydrocortisone cream 1%', 3, 'Bôi ngày 3 lần vùng da bị tổn thương'),
(95, 23, 'Prednisolone 5mg', 15, 'Ngày 2 viên trong 1 tuần'),
(96, 76, 'Phenytoin 100mg', 60, 'Ngày 3 lần'),
(96, 44, 'Multivitamin', 30, 'Ngày 1 viên'),
(97, 13, 'Digoxin 0.25mg', 30, 'Ngày 1 viên'),
(97, 23, 'Prednisolone 5mg', 20, 'Ngày 2 viên giảm dần'),
(98, 4, 'Omeprazole 20mg', 30, 'Ngày 1 viên'),
(98, 11, 'Furosemide 40mg', 30, 'Ngày 1 viên'),
(99, 22, 'Salbutamol 2mg', 90, 'Ngày 3 lần'),
(99, 23, 'Prednisolone 5mg', 30, 'Ngày 2 viên'),
(100, 61, 'Ibuprofen 400mg', 60, 'Ngày 3 lần sau ăn'),
(100, 64, 'Meloxicam 15mg', 30, 'Ngày 1 viên sau ăn'),
(101, 7, 'Amlodipine 5mg', 30, 'Ngày 1 viên'),
(101, 8, 'Losartan 50mg', 30, 'Ngày 1 viên'),
(102, 51, 'Ciprofloxacin 500mg', 14, 'Ngày 2 lần'),
(102, 21, 'Acetylcysteine 200mg', 30, 'Ngày 3 lần'),
(103, 32, 'Insulin Aspart', 1, 'Tiêm trước ăn theo đường huyết'),
(103, 5, 'Metformin 500mg', 60, 'Ngày 2 lần sau ăn'),
(104, 4, 'Omeprazole 20mg', 30, 'Ngày 1 viên'),
(104, 56, 'Metronidazole 500mg', 21, 'Ngày 3 lần'),
(105, 22, 'Salbutamol 2mg', 90, 'Ngày 3 lần'),
(105, 30, 'Montelukast 10mg', 30, 'Ngày 1 viên tối'),
(106, 38, 'Calcium carbonate 500mg', 90, 'Ngày 3 lần'),
(106, 39, 'Vitamin D3 1000IU', 30, 'Ngày 1 viên'),
(107, 95, 'Thuốc nhỏ mắt điều trị glaucoma', 1, 'Nhỏ mắt ngày 2 lần'),
(108, 51, 'Ciprofloxacin 500mg', 14, 'Ngày 2 lần'),
(108, 1, 'Paracetamol 500mg', 30, 'Khi sốt'),
(109, 4, 'Omeprazole 20mg', 60, 'Ngày 2 viên'),
(109, 91, 'Sucralfate 1g', 60, 'Ngày 4 lần'),
(110, 22, 'Salbutamol 2mg', 90, 'Ngày 4 lần'),
(110, 23, 'Prednisolone 5mg', 30, 'Ngày 3 viên'),
(111, 36, 'Methimazole 5mg', 60, 'Ngày 4 lần'),
(111, 14, 'Propranolol 40mg', 60, 'Ngày 2 lần'),
(112, 11, 'Furosemide 40mg', 60, 'Ngày 2 viên'),
(112, 19, 'Spironolactone 25mg', 30, 'Ngày 1 viên'),
(113, 2, 'Amoxicillin 500mg', 28, 'Ngày 4 lần'),
(113, 61, 'Ibuprofen 400mg', 30, 'Ngày 3 lần'),
(114, 80, 'Risperidone 2mg', 60, 'Ngày 2 viên tăng dần'),
(114, 72, 'Lorazepam 1mg', 30, 'Khi cần'),
(115, 65, 'Tramadol 50mg', 90, 'Khi đau'),
(115, 86, 'Ondansetron 4mg', 30, 'Khi buồn nôn'),
(116, 61, 'Ibuprofen 400mg', 90, 'Ngày 3 lần'),
(116, 48, 'Glucosamine 500mg', 90, 'Ngày 3 lần'),
(117, 13, 'Digoxin 0.25mg', 30, 'Ngày 1 viên kiểm soát nhịp tim'),
(117, 12, 'Warfarin 5mg', 30, 'Theo INR'),
(118, 4, 'Omeprazole 20mg', 60, 'Ngày 2 viên'),
(118, 89, 'Thuốc bảo vệ gan', 30, 'Ngày 1 viên'),
(119, 61, 'Ibuprofen 400mg', 30, 'Ngày 3 lần'),
(119, 65, 'Tramadol 50mg', 20, 'Khi đau nhiều'),
(120, 84, 'Gabapentin 300mg', 90, 'Ngày 3 lần tăng dần'),
(120, 41, 'Vitamin B1 100mg', 60, 'Ngày 2 viên');

# ADDITIONAL SAMPLE QUERIES FOR TESTING

-- ====================================================================
-- ADDITIONAL SAMPLE QUERIES FOR TESTING
-- ====================================================================

-- Sample query to show patient medical history
-- SELECT b.hoTen, h.ngayKham, h.chuanDoan, GROUP_CONCAT(t.tenThuoc) as 'Thuoc_da_ke'
-- FROM BenhNhan b
-- JOIN HoSoKham h ON b.maBN = h.maBN
-- JOIN ChiTietDonThuoc ct ON h.maHS = ct.maHS
-- JOIN Thuoc t ON ct.maThuoc = t.maThuoc
-- WHERE b.maBN = 1
-- GROUP BY h.maHS
-- ORDER BY h.ngayKham DESC;

-- Sample query to show medicine inventory
-- SELECT tenThuoc, soLuongTon, 
--        CASE 
--            WHEN soLuongTon < 500 THEN 'Can bo sung'
--            WHEN soLuongTon < 1000 THEN 'Sap het'
--            ELSE 'Du dung'
--        END as TrangThai
-- FROM Thuoc
-- ORDER BY soLuongTon ASC;

-- Sample query to show doctor workload
-- SELECT bs.hoTen, bs.chuyenKhoa, COUNT(h.maHS) as SoLuotKham
-- FROM BacSi bs
-- LEFT JOIN HoSoKham h ON bs.chuyenKhoa = h.bacSi
-- GROUP BY bs.maBS
-- ORDER BY SoLuotKham DESC;

-- ====================================================================
-- CREATE INDEXES FOR PERFORMANCE
-- ====================================================================

-- Additional indexes for better performance
CREATE INDEX idx_hoSoKham_composite ON HoSoKham(maBN, ngayKham);
CREATE INDEX idx_chiTietDonThuoc_composite ON ChiTietDonThuoc(maHS, maThuoc);
CREATE INDEX idx_benhNhan_ngaySinh ON BenhNhan(ngaySinh);
CREATE INDEX idx_thuoc_soLuongTon_tenThuoc ON Thuoc(soLuongTon, tenThuoc);

-- ====================================================================
-- CREATE VIEWS FOR COMMON QUERIES
-- ====================================================================

-- View: Thông tin bệnh nhân và lịch sử khám
CREATE VIEW v_BenhNhan_LichSuKham AS
SELECT 
    b.maBN,
    b.hoTen as TenBenhNhan,
    b.ngaySinh,
    b.diaChi,
    b.soDienThoai,
    h.maHS,
    h.ngayKham,
    h.chuanDoan,
    h.bacSi
FROM BenhNhan b
LEFT JOIN HoSoKham h ON b.maBN = h.maBN;

-- View: Thống kê thuốc được kê nhiều nhất
CREATE VIEW v_ThongKe_Thuoc AS
SELECT 
    t.maThuoc,
    t.tenThuoc,
    t.congDung,
    t.soLuongTon,
    COUNT(ct.maThuoc) as SoLanKe,
    SUM(ct.soLuong) as TongSoLuongKe
FROM Thuoc t
LEFT JOIN ChiTietDonThuoc ct ON t.maThuoc = ct.maThuoc
GROUP BY t.maThuoc;

-- View: Thống kê bác sĩ theo số lượt khám
CREATE VIEW v_ThongKe_BacSi AS
SELECT 
    bs.maBS,
    bs.hoTen as TenBacSi,
    bs.chuyenKhoa,
    COUNT(h.maHS) as SoLuotKham,
    MIN(h.ngayKham) as NgayKhamDauTien,
    MAX(h.ngayKham) as NgayKhamGanNhat
FROM BacSi bs
LEFT JOIN HoSoKham h ON bs.chuyenKhoa = h.bacSi
GROUP BY bs.maBS;

-- ====================================================================
-- STORED PROCEDURES
-- ====================================================================

DELIMITER //

-- Procedure: Thêm hồ sơ khám mới
CREATE PROCEDURE sp_ThemHoSoKham(
    IN p_maBN INT,
    IN p_ngayKham DATE,
    IN p_chuanDoan TEXT,
    IN p_bacSi VARCHAR(50)
)
BEGIN
    DECLARE v_tenBenhNhan VARCHAR(100);
    
    -- Lấy tên bệnh nhân
    SELECT hoTen INTO v_tenBenhNhan 
    FROM BenhNhan 
    WHERE maBN = p_maBN;
    
    -- Thêm hồ sơ khám
    INSERT INTO HoSoKham (maBN, ngayKham, chuanDoan, benhNhan, bacSi)
    VALUES (p_maBN, p_ngayKham, p_chuanDoan, v_tenBenhNhan, p_bacSi);
    
    SELECT LAST_INSERT_ID() as maHS;
END //

-- Procedure: Kê đơn thuốc
CREATE PROCEDURE sp_KeDonThuoc(
    IN p_maHS INT,
    IN p_maThuoc INT,
    IN p_soLuong INT,
    IN p_lieuDung TEXT
)
BEGIN
    DECLARE v_tenThuoc VARCHAR(100);
    DECLARE v_soLuongTon INT;
    
    -- Lấy thông tin thuốc
    SELECT tenThuoc, soLuongTon INTO v_tenThuoc, v_soLuongTon
    FROM Thuoc 
    WHERE maThuoc = p_maThuoc;
    
    -- Kiểm tra tồn kho
    IF v_soLuongTon >= p_soLuong THEN
        -- Thêm chi tiết đơn thuốc
        INSERT INTO ChiTietDonThuoc (maHS, maThuoc, thuoc, soLuong, lieuDung)
        VALUES (p_maHS, p_maThuoc, v_tenThuoc, p_soLuong, p_lieuDung);
        
        -- Cập nhật tồn kho
        UPDATE Thuoc 
        SET soLuongTon = soLuongTon - p_soLuong
        WHERE maThuoc = p_maThuoc;
        
        SELECT 'Kê đơn thành công' as KetQua;
    ELSE
        SELECT CONCAT('Không đủ thuốc. Tồn kho: ', v_soLuongTon) as KetQua;
    END IF;
END //

-- Function: Tính tuổi bệnh nhân
CREATE FUNCTION fn_TinhTuoi(p_ngaySinh DATE)
RETURNS INT
READS SQL DATA
DETERMINISTIC
BEGIN
    RETURN TIMESTAMPDIFF(YEAR, p_ngaySinh, CURDATE());
END //

DELIMITER ;

-- ====================================================================
-- TRIGGERS
-- ====================================================================

DELIMITER //

-- Trigger: Cập nhật tồn kho khi kê đơn thuốc
CREATE TRIGGER tr_CapNhatTonKho_After_Insert
AFTER INSERT ON ChiTietDonThuoc
FOR EACH ROW
BEGIN
    UPDATE Thuoc 
    SET soLuongTon = soLuongTon - NEW.soLuong
    WHERE maThuoc = NEW.maThuoc;
END //

-- Trigger: Kiểm tra tồn kho trước khi kê đơn
CREATE TRIGGER tr_KiemTraTonKho_Before_Insert
BEFORE INSERT ON ChiTietDonThuoc
FOR EACH ROW
BEGIN
    DECLARE v_tonKho INT;
    SELECT soLuongTon INTO v_tonKho
    FROM Thuoc 
    WHERE maThuoc = NEW.maThuoc;
    
    IF v_tonKho < NEW.soLuong THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Không đủ thuốc trong kho';
    END IF;
END //

DELIMITER ;

-- ====================================================================
-- SAMPLE DATA SUMMARY
-- ====================================================================

SELECT 'DATABASE CREATED SUCCESSFULLY' AS Status;
SELECT COUNT(*) AS 'Total Patients' FROM BenhNhan;
SELECT COUNT(*) AS 'Total Doctors' FROM BacSi;
SELECT COUNT(*) AS 'Total Departments' FROM KhoaPhong;
SELECT COUNT(*) AS 'Total Medicines' FROM Thuoc;
SELECT COUNT(*) AS 'Total Medical Records' FROM HoSoKham;
SELECT COUNT(*) AS 'Total Prescriptions' FROM ChiTietDonThuoc;
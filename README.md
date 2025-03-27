# Course Management API

Bu proje GELECEĞİ YAZAN KADINLAR YAPAY ZEKA kapsamında verilmiş olan ödevin çözümüdür. Ödev aşağıdaki gibidir:

`//
Görev 2: Bu görev dosyasını benimle (En sevdiğiniz hocanız) paylaşınız.
Online Eğitim Sistemi – Analiz ve Modelleme Aşağıda, Category, Course, Lesson, Student ve Payment modüllerini içeren bir online eğitim sisteminin analizi ve modellemesi yer almaktadır.
Sistem Gereksinimleri
1 İşlevsel Gereksinimler Kategori Yönetimi: Kategorilerin eklenmesi, güncellenmesi ve silinmesi. Kurs Yönetimi: Kurs ekleme, düzenleme, kategorilere bağlama ve yayınlama. 
Ders Yönetimi: Kurslara bağlı dersler oluşturma, içerik ekleme. 
Öğrenci Yönetimi: Öğrenci kaydı, giriş yapma, kurslara kayıt olma. Ödeme Yönetimi: Kurs kayıtları için ödeme işlemlerinin yönetilmesi.
Varlık-İlişki Diyagramı (ERD) Aşağıdaki varlıklar ve ilişkiler üzerinden bir ER modeli oluşturulacaktır:
Category (Kategori)
id (PK) name (Kategori adı) description (Açıklama)
Course (Kurs) id (PK) title (Başlık) description (Açıklama) category_id (FK - Category) price (Ücret) created_at (Oluşturulma tarihi)
Lesson (Ders)
id (PK) title (Ders başlığı) content (Ders içeriği) video_url (Video linki) course_id (FK - Course) Student (Öğrenci)
id (PK) name (Ad Soyad) email (E-posta) password (Şifre - Hashlenmiş) Enrollment (Kayıt)
id (PK) student_id (FK - Student) course_id (FK - Course) status (Tamamlandı / Devam Ediyor / İptal Edildi) enrolled_at (Kayıt tarihi) Payment (Ödeme)
id (PK) student_id (FK - Student) course_id (FK - Course) amount (Tutar) status (Beklemede / Başarılı / Başarısız) transaction_id (Ödeme sağlayıcısından gelen işlem ID'si) paid_at (Ödeme tarihi)
*Veriler restful bir api ile sunulacak. (Json-server) *Python kullanarak ve verileri gereksinimlere göre tüketiniz. (GET,POST,PUT,Patch,DELETE)
Post işlemlerinde  örneğin kategori ismi tekrar edemez. Bu kural tüm name olan objeler için geçerli
Put ve patch işlemlerinde kategori ismi başka bir kategoride varsa tekrar edemez ama kendi datası için geçerli değil.
//POST { "id":1 "name":"Giyim", "description":"Çok güzel kıyafetler" }
//PUT/1 { "name":"Giyim", "description":"Çok güzel giysiler" }`


Bu proje, kurs yönetim sistemi için bir **RESTful API** sağlar. **Kategoriler, kurslar, dersler, öğrenciler, kayıtlar ve ödemeleri** yönetmek için geliştirilmiştir.

## 📌 Kullanılan Teknolojiler
- **Python**
- **Flask**
- **JSON Server** (Fake API için)
- **Requests** (HTTP istekleri için)

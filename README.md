# simple-ransomware

Bu kodları Python:Sıfırdan İleri Seviyeye - Etic Hacker örnekleriyle kursu ile beraber yazdım.

Bu kursta os paketini ve cryptography paketi içerisinde bulunan fernet şifreleme algoritmasını kullandım.

Ransomware içinde bulunduğu klasörde olan bütün dosyaları şifrelemek için kullanılır, Ransomdecrypter ise bu şifreyi çözmek için yazılmış koddur.

Fernet, simetrik bir şifreleme algoritmasıdır yani bu demek oluyorki tek anahtar ile hem şifreleme hemde çözme işlemi yapılabilir.

Fernet veri bütünlüğünü sağlamak için Hash-based Message Authentication Code kullanır.Bu verinin aynı kaldığının yani değiştirilmediğini doğrulamak için kullanılır.

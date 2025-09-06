
# ملف تشغيل للوحدة المشفرة MAYANew.cpython-312.so
import MAYANew

# تأكد أن الدالة الرئيسية موجودة داخل الملف الأصلي
if hasattr(MAYANew, 'main'):
    MAYANew.main()
else:
    print("تم استيراد MAYANew بنجاح، ولكن لا توجد دالة main للتشغيل.")

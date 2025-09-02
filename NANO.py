
# ملف تشغيل للوحدة المشفرة NANO.cpython-312.so
import NANO

# تأكد أن الدالة الرئيسية موجودة داخل الملف الأصلي
if hasattr(NANO, 'main'):
    NANO.main()
else:
    print("تم استيراد NANO بنجاح، ولكن لا توجد دالة main للتشغيل.")

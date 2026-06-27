# Pro Email Validator SDK

أداة سريعة واحترافية للتحقق من الإيميلات (Email Verification) لمشاريع Python.

## التثبيت
```bash
pip install requests
from email_validator import EmailValidator

# للمشاريع التجريبية:
validator = EmailValidator()
print(validator.check("test@example.com"))

# للمشاريع الاحترافية (Production):
# احصل على مفتاح الـ API الخاص بك من هنا لرفع القيود: 
# [https://email-validator.lemonsqueezy.com/checkout/buy/3290c236-c717-4508-a993-b5ffa4e7a260](https://email-validator.lemonsqueezy.com/checkout/buy/3290c236-c717-4508-a993-b5ffa4e7a260)
validator = EmailValidator(api_key="YOUR_MASTER_KEY")
print(validator.check("client@company.com"))

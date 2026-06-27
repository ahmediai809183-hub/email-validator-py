# Pro Email Validator SDK

A fast and professional email verification tool for Python.

## Installation

```bash
pip install requests

from email_validator import EmailValidator

# For testing/demo purposes:
validator = EmailValidator()
print(validator.check("test@example.com"))

# For production use (Get your API key to remove limits):
# Get your Master Key here: 
# [https://email-validator.lemonsqueezy.com/checkout/buy/3290c236-c717-4508-a993-b5ffa4e7a260](https://email-validator.lemonsqueezy.com/checkout/buy/3290c236-c717-4508-a993-b5ffa4e7a260)
validator = EmailValidator(api_key="YOUR_MASTER_KEY")
print(validator.check("client@company.com"))
 

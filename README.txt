# company_auth_project
Bu klasör, Django ile geliştirilen basit bir kayıt & giriş uygulamasını içerir.

## Kurulum (Windows / macOS / Linux)
1. Python 3.10+ kurulu olmalı. `python --version` ile kontrol edin.
2. Sanal ortam oluşturun ve aktif edin:
   - Windows (PowerShell): `python -m venv .venv; .venv\Scripts\Activate.ps1`
   - macOS/Linux (bash): `python -m venv .venv && source .venv/bin/activate`
3. Gerekli paketleri kurun: `pip install -r requirements.txt`
4. Veritabanını hazırlayın: `python manage.py migrate`
5. Sunucuyu başlatın: `python manage.py runserver`
6. Tarayıcıdan `http://127.0.0.1:8000` adresine gidin.

> Kayıt olabilmek için modal penceredeki "Anahtar" alanına **ahmet** yazın.

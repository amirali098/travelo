# انتخاب image پایه برای python
FROM python:3.9-slim

# نصب nginx
RUN apt-get update

# تعیین دایرکتوری کاری داخل کانتینر
WORKDIR /app

# نصب پکیج‌های مورد نیاز
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# کپی تمام فایل‌های پروژه
COPY . /app/

# کپی فایل پیکربندی nginx به مسیر مناسب
COPY nginx.conf /etc/nginx/nginx.conf

# اجرای دستورات مربوط به migrate و collectstatic
RUN python manage.py migrate --noinput
RUN python manage.py collectstatic --noinput
#RUN python manage.py compress --force  # Keep this commented if not needed

# باز کردن پورت برای ارتباط
EXPOSE 80



# اجرای gunicorn برای محیط production
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "travelo.wsgi:application"]

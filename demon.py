Создайте файл службы: Пожалуйста, создайте файл службы в каталоге /etc/systemd/system/. Например, назовите его my_daemon.service.
   Для этого откройте терминал и выполните:

   

bash

 Копировать код
sudo nano /etc/systemd/system/my_daemon.service

Добавьте следующие строки в файл службы:
   

ini

 Копировать код
[Unit]
   Description=My Python Daemon
   After=network.target

   [Service]
   ExecStart=/usr/bin/python3 /path/to/your/script/my_daemon.py
   WorkingDirectory=/path/to/your/script/
   StandardOutput=journal
   StandardError=journal
   Restart=always

   [Install]
   WantedBy=multi-user.target
   Убедитесь, что вы указали правильный путь к интерпретатору Python и вашему скрипту.

Сохраните и выйдите из редактора: В nano это делается с помощью Ctrl+X, затем Y для подтверждения и Enter для сохранения.

Перезагрузите systemd, чтобы он обнаружил новую службу:
   

bash

 Копировать код
sudo systemctl daemon-reload

Включите службу на автоматический запуск при загрузке системы:
   

bash

 Копировать код
sudo systemctl enable my_daemon.service

Запустите службу:
   

bash

 Копировать код
sudo systemctl start my_daemon.service

Проверьте статус службы:
   

bash

 Копировать код
sudo systemctl status my_daemon.service
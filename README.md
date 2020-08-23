# Dominator
![Логитип бота Dominator](./images/1.png)

## О проекте
Бот для модерации и веселья в Discord.

## Функционал
- Возможности
    - Сменный префикс
    - Возможность удаления команд после исполнения
    - Выбор роли для mute
- Модерация
    - Кик (+причина)
    - Бан (+причина)
    - Разбан (по ID)
    - Мут
    - Размут
    

## Планы на будущее
- [x] Добавить сменный префикс.
- [x] Сделать функции модерации.
- [ ] Добавить функции для развлечения.
- [ ] Сделать админку.

## Запуск
### Linux
```bash
git clone https://github.com/hilight3r/Dominator.git
cd Dominator
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
nano config.py
python3 main.py
```
### Windows
```powershell
# Клонируете репозиторий
cd Dominator
python -m pip install --upgrade pip
pip install -r requirements.txt
# Тут редактируете файл конфикурации config.py
python main.py
```

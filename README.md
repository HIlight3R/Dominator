# ПРОЕКТ ЗАКРЫТ, ДАЛЬНЕЙШАЯ РАЗРАБОТКА НЕ ПЛАНИРУЕТСЯ!
# Dominator

<p align="center">
    <img src="./images/1.png" alt="Логотип">
    <br>
	<img src="https://img.shields.io/github/license/hilight3r/Dominator?label=%D0%9B%D0%B8%D1%86%D0%B5%D0%BD%D0%B7%D0%B8%D1%8F" alt="Лицензия">
	<br>
	<img src="https://img.shields.io/github/stars/hilight3r/Dominator?label=%D0%97%D0%B2%D0%B5%D0%B7%D0%B4%D1%8B" alt="Звезды">
	<img src="https://img.shields.io/github/watchers/hilight3r/Dominator?label=%D0%9F%D1%80%D0%BE%D1%81%D0%BC%D0%BE%D1%82%D1%80%D1%8B" alt="Просмотры">
	<img src="https://img.shields.io/github/forks/hilight3r/Dominator?label=%D0%9E%D1%82%D0%B2%D0%B5%D1%82%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F" alt="Ответвления">
	<hr>
</p>

## О проекте
Бот для модерации и веселья в Discord.

## Функционал
- Возможности
    - Сменный префикс
    - Возможность удаления команд после исполнения
    - Выбор роли для мьюта
    - Автороль
    - Уведомления о новых участниках
    - Фильтрация чата
    - Отправка личных сообщений при наказаниях и их отмене
- Модерация
    - Кик (+причина)
    - Бан (+причина)
    - Разбан (по ID)
    - Мут
    - Размут
- Развлечения
    - Музыка (YouTube)
    

## Планы на будущее
- [x] ~~Добавить сменный префикс.~~
- [x] ~~Сделать функции модерации.~~
- [x] ~~Добавить функции для развлечения.~~
- [ ] ~~Сделать админку.~~

## Запуск
### Linux
```bash
# Клонируете репозиторий
git clone https://github.com/hilight3r/Dominator.git
cd Dominator
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
# Тут редактируете файл конфигурации config.py
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

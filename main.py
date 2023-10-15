import json
import datetime


# сохранение заметки
def save_notes(notes):
    with open(file_path, "w", encoding="UTF-8") as file:
        json.dump(notes, file, indent=4)


# чтение заметки
def load_notes(file_path):
    try:
        with open(file_path, "r", encoding="UTF-8") as file:
            notes = json.load(file)
            return notes
    except FileNotFoundError:
        return []


# добавление заметки
def add_note():
    # Получаем максим идентификатор из существующих заметок
    title = input("Введите заголовок заметки: ")
    body = input("Введите тект заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    max_id = max(note["id"] for note in notes) if notes else 0
    new_note = {
        "id": max_id + 1,
        "title": title,
        "body": body,
        "datetime": timestamp,
    }
    notes.append(new_note)
    save_notes(notes)


# редактирование заметки
def edit_note():
    note_id = int(input("Введите ID заметки для редактирования :"))
    new_title = input("Введите новый заголовок заметки или оставьте пустым: ")
    new_body = input("Введите новый текст заметки или оставьте пустым: ")
    for note in notes:
        if note["id"] == note_id:
            if new_title:
                note["title"] = new_title
            if new_body:
                note["body"] = new_body
            note["datetime"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            break
    save_notes(notes)
    return


# удаление заметки
def delete_note():
    note_id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes(notes)
    return


def print_notes():
    for note in notes:
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Текст: {note['body']}")
        print(f"Дата/Время: {note['datetime']}")
        print()


file_path = "notes.json"
notes = load_notes(file_path)

while True:
    print("1. Вывести все заметки")
    print("2. Добавить заметку")
    print("3. Редактировать заметку")
    print("4. Удалить заметку")
    print("5. Выйти")

    choice = input("Выберите один из пунктов меню: ")

    if choice == "1":
        print_notes()
    elif choice == "2":
        add_note()
    elif choice == "3":
        edit_note()
    elif choice == "4":
        delete_note()
    elif choice == "5":
        break
    else:
        print("Неверный выбор. Попробуйте еще раз")

from view import *
from note import Note
from view import ManagerJSON
import random
import datetime

def main():
  js = ManagerJSON("my_notes.json")
  while True:
    command = input("Введите команду (add, read, edit, delete, show, end): ").lower().strip()
    if command == 'end':
      break
    if command == 'add':
      js.create_note(get_data())
    if command == 'delete':
      delete_id = input("Введите идентификатор заметки, которую необходимо удалить: ")
      js.delete_note(delete_id)
    if command == 'read':
       js.read_notes()
    if command == 'show':
       id = input("Введите идентификатор необходимой заметки: ")
       js.show_note(id)
    if command == 'edit':
      change_id = input("Введите идентификатор заметки, которую необходимо исправить: ")
      js.update_note(change_id)

   # Получить данные у пользователя.
def get_data():
      note_id = random.randint(0, 10000)
      heading = input("Введите заголовок заметки: ")
      note = input("Введите заметку: ")
      now = get_time()
      return Note(note_id, heading, note, now)

    # Получение текущего времени
def get_time():
      return datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S")

main()
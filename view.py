from note import Note
import json


class ManagerJSON(object):

    def __init__(self, filename):
        self.filename = filename
        self.notes = list()

    def create_note(self, note):
        self.notes = self.read_notes()
        self.notes.append(note)
        self.write_json(self.notes)

    # Список данных.
    def read_notes(self):
        return self.read_json()

    # Десериализуем данные файла json.
    def read_json(self):
        notes_list = list()
        try:
            with open(self.filename, "r", encoding="utf-8") as json_file:
                notes_json = json_file.read()
            data = json.loads(notes_json)
            data.sort(key=lambda x: x["date"])
            for item in data:
                notes_list.append(
                    Note(item["id"], item["heading"], item["note"], item["date"])
                )

            return notes_list
        except ValueError:
            return self.notes

    # Записываем данные в список и переносим в файл в json формате.
    def write_json(self, notes):
        lst = list()
        for note in notes:
            lst.append(
                {
                    "id": note.id,
                    "heading": note.heading,
                    "note": note.note,
                    "date": note.date,
                }
            )

        notes_json = json.dumps(
            lst, indent=4, ensure_ascii=False, sort_keys=False, default=str
        )
        with open(self.filename, "w", encoding="utf-8") as json_file:
            json_file.write(notes_json)

    # Поиск записи по Id
    def show_note(self, search_id):
        self.notes = self.read_notes()
        for note in self.notes:
            if note.id == search_id:
                return note
        else:
            print("Идентификатор не найден.")

    # Изменение данных.
    def update_note(self, search_id, note):
        self.notes = self.read_notes()
        for item in self.notes:
            if item.id == search_id:
                item.heading = note.heading
                item.note = note.note
                item.date = note.date
            else:
                print("Заметки под таким идентификатором не существует.")
        self.write_json(self.notes)

    # Удаление заметки.
    def delete_note(self, search_id):
        self.notes = self.read_notes()
        for index, note in enumerate(self.notes):
            if note.id == search_id:
                del self.notes[index]
            else:
                print("Заметки под таким идентификатором не существует.")

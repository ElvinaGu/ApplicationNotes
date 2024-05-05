class Note(object):

  def __init__(self, id, heading, note, date):
    self.id = id
    self.heading = heading
    self.note = note
    self.date = date

    @property
    def heading(self):
      return self._heading
    
    @heading.setter
    def heading(self, heading):
      self._heading = heading

    @property
    def note(self):
      return self._note
    
    @note.setter
    def note(self, note):
      self._note = note

    @property
    def id(self):
      return self._id
    
    @id.setter
    def id(self, id):
      self._id = id

    @property
    def date(self):
      return self._date
    
    @date.setter
    def date(self, date):
      self._date = date

    def __str__(self):
      return f'\nИдентификатор: {self._id}\nЗаголовок: {self._heading}\nЗаметка: {self._note}\nДата создания (изменения): {self._date}\n'

 
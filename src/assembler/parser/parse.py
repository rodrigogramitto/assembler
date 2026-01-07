from pathlib import Path
from collections import deque
import re

class Parser:
  def __init__(self, filepath):
    filepath = Path(filepath).resolve()
    self.cur_instruction = None
    with open(filepath) as file:
      self.lines = deque(file.readlines())

  def hasMoreLines(self):
    return len(self.lines) > 0

  def advance(self):
    while self.hasMoreLines():
      curline = self.lines.popleft()
      curline = re.sub(r"//.*", "", curline.strip())
      if not curline:
        continue
      self.cur_instruction = curline
      return

  def instructionType(self):

    if self.cur_instruction.startswith('@'):
      return 'A_COMMAND'
    elif self.cur_instruction.startswith('('):
      return 'L_COMMAND'
    else:
      return 'C_COMMAND'

  def symbol(self):
    if self.instructionType() == 'A_COMMAND':
      return self.cur_instruction[1::]
    else:
      return self.cur_instruction[1:-1]

  def dest(self):
    if '=' in self.cur_instruction:
      return self.cur_instruction[:self.cur_instruction.index('=')]
    else:
      return None

  def comp(self):
    start, end = 0, len(self.cur_instruction)
    if '=' in self.cur_instruction:
      start = self.cur_instruction.index('=') + 1
    if ';' in self.cur_instruction:
      end = self.cur_instruction.index(';')
    return self.cur_instruction[start:end]

  def jump(self):
    if ';' in self.cur_instruction:
      return self.cur_instruction[self.cur_instruction.index(';') + 1:]
    else:
      return None
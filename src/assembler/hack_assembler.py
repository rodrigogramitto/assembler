from src.assembler.parser.parse import Parser
from src.assembler.code.code import Code
from src.assembler.symbol_table.table import SymbolTable
import os



class HackAssembler:
  def __init__(self):
    self.code = Code()
    self.symbol_table = SymbolTable()

  def get_file_name(self, filepath):
    base, ext = os.path.splitext(filepath)
    output_path = base + ".hack"
    return output_path


  def get_a_command(self, sym):
    if sym.isdecimal():
      return int(sym)
    elif not self.symbol_table.contains(sym):
      self.symbol_table.addEntry(sym, self.symbol_table.get_next_address())
    return self.symbol_table.get_address(sym)

  def parse_symbols(self, filepath):
    self.parser = Parser(filepath)
    line_number = 0
    while self.parser.hasMoreLines():
      self.parser.advance()
      if self.parser.instructionType() == 'L_COMMAND':
        sym = self.parser.symbol()
        if not self.symbol_table.contains(sym):
          self.symbol_table.addEntry(sym, line_number)
      else:
        line_number += 1

  def build_executable(self, filepath):
    self.parser = Parser(filepath)
    name = self.get_file_name(filepath)
    with open(name, "w") as out:
      while self.parser.hasMoreLines():
        self.parser.advance()
        instruction = ''
        if self.parser.instructionType() == 'A_COMMAND':
          sym = self.get_a_command(self.parser.symbol())
          instruction = '0' + format(sym, '015b')
        elif self.parser.instructionType() == 'L_COMMAND':
          continue
        elif self.parser.instructionType() == 'C_COMMAND':
          comp = self.code.comp(self.parser.comp())
          dest = self.code.dest(self.parser.dest())
          jmp = self.code.jump(self.parser.jump())
          instruction = '111' + comp + dest + jmp
        out.write(instruction)
        if self.parser.hasMoreLines():
          out.write('\n')

  def assemble(self, filepath):
    self.parse_symbols(filepath)
    print(self.symbol_table.symbols)
    self.build_executable(filepath)


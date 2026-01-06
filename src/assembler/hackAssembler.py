from src.assembler.parser.parse import Parser
from src.assembler.code.code import Code
from src.assembler.symbol_table.table import SymbolTable

class HackAssembler:
  def __init__(self):
    self.parser = Parser("Add.asm")
    self.code = Code()
    self.symbol_table = SymbolTable()

  def assemble(self, filepath):
    while self.parser.hasMoreLines():
      self.parser.advance()
      if self.parser.instructionType() != 'C_COMMAND':
        sym = self.parser.symbol()
      else:
        dest = self.parser.dest()
        comp = self.parser.comp()
        jump = self.parser.jump()

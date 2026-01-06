from src.assembler.parser.parse import Parser
from src.assembler.code.code import Code
from src.assembler.symbol_table.table import SymbolTable
from pathlib import Path

class HackAssembler:
  def __init__(self):
    self.parser = Parser()
    self.code = Code()
    self.symbol_table = SymbolTable()

  def assemble(self, filepath):
    filepath = Path(filepath).resolve()
    with open(filepath) as f:
      lines = f.readlines()
      print(lines)
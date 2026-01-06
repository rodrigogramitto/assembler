from src.assembler.parser.parse import Parser
from src.assembler.code.code import Code
from src.assembler.symbol_table.table import SymbolTable

class HackAssembler:
  def __init__(self):
    self.parser = Parser()
    self.code = Code()
    self.symbol_table = SymbolTable()
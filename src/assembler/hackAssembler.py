from src.assembler.parser.parse import Parser
from src.assembler.code.code import Code
from src.assembler.symbol_table.table import SymbolTable

class HackAssembler:
  def __init__(self):
    self.parser = Parser("PongL.asm")
    self.code = Code()
    self.symbol_table = SymbolTable()

    # still to do is resolve the target file, strip the name and make a new file with the name

  def get_a_command(self, sym):
    if sym.isdecimal():
      return int(sym)
    else:
      return self.symbol_table.get_address(sym)

  def assemble(self, filepath):
    with open("PongL.hack", "w") as out:
      while self.parser.hasMoreLines():
        self.parser.advance()
        instruction = ''
        if self.parser.instructionType() == 'A_COMMAND':
          sym = self.get_a_command(self.parser.symbol())
          instruction = '0' + format(sym, '015b')
        else:
          comp = self.code.comp(self.parser.comp())
          dest = self.code.dest(self.parser.dest())
          jmp = self.code.jump(self.parser.jump())
          instruction = '111' + comp + dest + jmp
        out.write(instruction)
        if self.parser.hasMoreLines():
          out.write('\n')

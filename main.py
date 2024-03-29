#!/bin/python3.10
from os import curdir
from karnaugh import simplify

NUM_BITS = 4
MAX_4_BIT_NUMBER = 0xF

def get_bit(value, n):
  return (value >> n & 1) != 0
def set_bit(value, n):
  return value | (1 << n)
def clear_bit(value, n):
  return value & ~(1 << n)
def toggle_bit(value, n):
  return clear_bit(value, n) if get_bit(value, n) else set_bit(value, n)

def bitarray_to_int(bitarray):
  return int(''.join(map(str, bitarray)), 2)

def permutate(n):
  return [toggle_bit(n, i) for i in range(NUM_BITS)]
def get_valid_permutations(n, numbers):
  permutations = permutate(n)
  return [p for p in permutations if p not in numbers]

class JK:
  def __init__(self, j, k) -> None:
    self.j = j
    self.k = k
  
  #only valid values of jk are 'j' and 'k'
  def get(self, jk):
    return self.j if jk == 'j' else self.k

  def __repr__(self) -> str:
    return f'JK(j={self.j}, k={self.k})'
def get_jk_value(prev_bit, next_bit) -> JK:
  match (prev_bit, next_bit):
    case (0, 0):
      return JK(j=0, k=None)
    case (0, 1):
      return JK(j=1, k=None)
    case (1, 0):
      return JK(j=None, k=1)
    case (1, 1):
      return JK(j=None, k=0)
    case (None, None):
      return JK(j=None, k=None)
def get_next_value(prev_bit, jk_value) -> JK:
  match (prev_bit, jk_value.j, jk_value.k):
    case (0, 0, _):
      return 0
    case (0, 1, _):
      return 1
    case (1, _, 1):
      return 0
    case (1, _, 0):
      return 1

# pretty print j or k
def ppjk(jk) -> str:
  return str(jk) if jk is not None else 'x'
# pretty print number in binary
def ppb(n):
  if n is None:
    return "x" * NUM_BITS
  return "{0:b}".format(n).rjust(NUM_BITS, '0')
# pretty print binary list
def ppbl(lst):
  return [ppb(x) for x in lst]
   

class TransitionTable:
  def __init__(self, numbers) -> None:
    self.numbers = numbers
    self.transitions = []
    # Sort transitions by the previous number.
    self.transitions = sorted(self.transitions, key=lambda x: x[0])
    
    self.calculate()
    self.insert_remaining_transitions()
    # Sort transitions by the previous number.
    self.transitions = sorted(self.transitions, key=lambda x: x[0])

  def calculate(self) -> None:
    # Calculate transitions
    for i, prev in enumerate(self.numbers):
      # transitions = [(prev, next, JKS=(JK1, JK2, ...))]

      # if we reach the end, the next item is the first item. we want a loop.
      nxt_i = (i + 1) if (i + 1) < len(self.numbers) else 0
      nxt = self.numbers[nxt_i]

      JKs = []
      for x in range(NUM_BITS):
        JKs.append(
          get_jk_value(
            prev_bit=get_bit(prev, x), 
            next_bit=get_bit(nxt, x)
            )
        )

      self.transitions.append([prev, nxt, JKs])

  def insert_remaining_transitions(self) -> None:
    # Insert remaining transitions
    for i in range(MAX_4_BIT_NUMBER+1):
      if i not in self.numbers:
        self.transitions.append([i, None, [JK(None, None)]*4])

  # jk = 'j' if we want to get the J value, 'k' if we want to get the K value.
  # returns the number for the asked j or k value, as a string of 0s and 1s.
  def get_transitions_by_jkn(self, jk, n):
    transitions_by_jkn = { 0: [], 1: [], 'x': [] }
    for prev, _, JKs in self.transitions:
      match JKs[n].get(jk):
        case 0:
          transitions_by_jkn[0].append(ppb(prev))
        case 1:
          transitions_by_jkn[1].append(ppb(prev))
        case None:
          transitions_by_jkn['x'].append(ppb(prev))
    return transitions_by_jkn

  def __repr__(self) -> str:
    string = "prev -> next | J K3| J K2| J K1| J K0\n"
    for prev, nxt, JKs in self.transitions:
      jks_display = " | ".join([f"{ppjk(jk.j)} {ppjk(jk.k)}" for jk in JKs[::-1]])
      string += f"{str(ppb(prev))} -> {str(ppb(nxt))} | {jks_display}\n"
    
    return string

class JKEquation:
  def __init__(self, unp_groups:list) -> None:
    # ones, zeroes are a list of 
    # unp_groups is a list that contain q_states
    # q_state is a tuple of q's. (q3, q2, q1, q0...)
    # if qn is 0, then qn is negated, if it is 1, it is not.
    
    # i parse those into a list of numbers so multiplication and reading is easier.

    self.parse_groups(unp_groups)

  def parse_groups(self, unp_groups: list) -> None:
    self.groups = []
    for group in unp_groups:
      p_group = []
      for q in group[::-1]:
        match q:
          case '0':
            p_group.append(0)
          case '1':
            p_group.append(1)
          case _:
            p_group.append(None)
      self.groups.append(p_group)
  
  def calculate(self, prev) -> None:
    # If we only have one group, and it's all nones, the result is a 1, by default.
    if len(self.groups) == 1 and self.groups[0] == [None]*len(self.groups[0]):
      return 1
    
    # Calculate the result of the equation for a given previous number.
    result = 0
    for group in self.groups:
      # Calculate the result of the group.
      group_result = 1
      for i, q in enumerate(group):
        # print(f"prev: {ppb(prev)}, bit: {bit}, q={q}, group_result={group_result}, result={result}, eq={self.__repr__()}")
        if q == None:
          continue

        bit = get_bit(prev, i)
        group_result *= bit if q == 1 else not bit

      result += group_result
      # print(f"grup: {group}: {result}")
    
    if result > 1:
      result = 1
    return result
      

  def __repr__(self) -> str:
    monomials = []
    for group in self.groups:
      string = ""
      # we iterate from right to left (q3, q2, q1, q0) instead of (q0, q1, q2, q3)
      for i, q in enumerate(group):
        match q:
          case 0:
            string += f"nQ{i}"
          case 1:
            string += f"Q{i}"
      monomials.append(string)
    
    ret = " + ".join(monomials)
    return ret if ret != "" else "1"

## EXECUTE
def switch_numbers(numbers: list) -> list:
  ## Cambiar el repetido por otro con 1 bit de diferencia
  # Busco el primer número repetido y añado a switched_numbers una lista que tenga ese número pero cambiado.
  switched_numbers = []
  for i, number_to_switch in enumerate(numbers):
    if numbers.count(number_to_switch) > 1:
      valid_permutations = get_valid_permutations(number_to_switch, numbers)
      print(f"Found permutations for {ppb(number_to_switch)}: {ppbl(valid_permutations)}")
      switched_numbers += [[v if j != i else p for j, v in enumerate(numbers)] for p in valid_permutations]
      break
  # Cambiar el segundo número repetido por otro con 1 bit de diferencia.
  for inverse_i, number_to_switch in enumerate(numbers[::-1]):
    i = len(numbers) - 1 - inverse_i
    if numbers.count(number_to_switch) > 1:
      valid_permutations = get_valid_permutations(number_to_switch, numbers)
      print(f"Found permutations for {ppb(number_to_switch)}: {ppbl(valid_permutations)}")
      switched_numbers += [[v if j != i else p for j, v in enumerate(numbers)] for p in valid_permutations]
      break

  # # Si no hay ningún número repetido, la lista sobre la que trabajamos es la misma que la de entrada.
  # return (switched_numbers if len(switched_numbers) > 0 else [numbers])

  # Devolvemos switched numbers vacio si así sale para una comprobación más adelante
  return switched_numbers

def table_2_karnaugh(tt:TransitionTable) -> dict:
  equations_by_jkn = { 'j': {}, 'k': {} }
  
  for jk in ('j', 'k'):
    for n in range(NUM_BITS):
      transition_by_jkn = tt.get_transitions_by_jkn(jk, n)
      # print(f"Transition {jk}_{n}: {transition_by_jkn")

      simplified_by_jkn = simplify(transition_by_jkn[1], transition_by_jkn['x'])
      # print(f"Simplified {jk}_{n}: {simplified_by_jkn}")

      equations_by_jkn[jk][n] = JKEquation(simplified_by_jkn)

      print(f"Equation {jk}_{n}: {equations_by_jkn[jk][n]}")
      # equation_result_by_jkn[jk][n] = equation.calculate(0b0100)
  
  return equations_by_jkn

def karnaugh_2_table(tt:TransitionTable, equations:dict) -> None:
  ## Fill transition table back.
  for i, (prev, nxt, JKs) in enumerate(tt.transitions):
    if nxt != None:
      continue
    
    equation_result_by_jkn = { 'j': {}, 'k': {} }
    for jk in ('j', 'k'):
      for n in range(NUM_BITS):
        equation_result_by_jkn[jk][n] = equations[jk][n].calculate(prev)
        # print(f"Calculated {jk}_{n} for {ppb(prev)}={equation_result_by_jkn[jk][n]}")

    
    nxt_lst = []
    for n in range(NUM_BITS):
      jk_value = JK(equation_result_by_jkn['j'][n], equation_result_by_jkn['k'][n])
      bit = get_bit(prev, n)
      nxt_lst.append(get_next_value(bit, jk_value))
      match bit:
        case 0:
          jk_value.k = None
        case 1:
          jk_value.j = None

      tt.transitions[i][2][n] = jk_value
    tt.transitions[i][1] = bitarray_to_int(nxt_lst[::-1])

def get_invalid_solutions(tt:TransitionTable) -> list:
  invalid = []
  invalid_sequence = []
  
  for i in range(2**NUM_BITS):
    invalid_sequence = []
    curr, nxt = tt.transitions[i][:2]
    
    for j in range(2**NUM_BITS - len(numbers) + 1):
      if curr in numbers:
        break
      else:
        invalid_sequence.append(curr)
      
      if nxt in invalid_sequence:
        invalid += [invalid_sequence]
        break
      
      curr = nxt
      nxt = tt.transitions[nxt][1]

  return invalid

    # if not found:
    #   invalid += [tt.transitions[i][1]]
    #   print(f"------------ {tt.transitions[i][1]} doesn't leed to the main loop!! ------------")
    #   print(f"--------------- don't trust this solution, get to the next one :) --------------")

def get_switching_equation(numbers:list, switched_numbers:list, tt:TransitionTable) -> str:
  # Get the switched number
  for n, sn in zip(numbers, switched_numbers):
    if n != sn:
      switched_number = (ppb(n), ppb(sn))
      break

  # Find the bit that changes
  for x in range(NUM_BITS):
    if switched_number[0][x] != switched_number[1][x]:
      dif_bit = x;
  
  # Karnaugh
  ones = []
  xs = []
  for transition in tt.transitions:
    curr = ppb(transition[0])
    nxt = transition[1]

    if nxt == None:
      xs.append(curr)
    elif curr[dif_bit] == '1':
      ones.append(curr)
  
  if switched_number[0][dif_bit] == '1':
    ones.append(switched_number[1])
  else:
    ones.remove(switched_number[1])
  
  eq = JKEquation(simplify(ones, xs))
  return eq

def count_gates(equations:dict, switch:JKEquation) -> dict:
  gate_count = {
    "total": 0,
    "or": [0, 0, 0],
    "and": [0, 0, 0]
  }
  
  equations['s'] = [switch]

  for jk in ('j', 'k', 's'):
    for x in range(len(equations[jk])):
      eq = equations[jk][x].groups
      
      val = 0;
      # Empty group
      if (len(eq) == 1 and eq[0] == [None] * NUM_BITS):
        val = 0;

      # Not empty group
      # Count and gates
      for group in eq:
        not_none_count = NUM_BITS - group.count(None)
        if not_none_count > 1:
          gate_count["and"][not_none_count - 2] += 1

      # Count or gates
      if len(eq) > 1:
        gate_count["or"][len(eq) - 2] += 1

  gate_count["total"] = sum([(1 + 0.5*x) * (gate_count["or"][x] + gate_count["and"][x]) for x in range(3)]) + 24

  return gate_count


def execute(numbers: list) -> None:

  switched_numbers = switch_numbers(numbers)
  if len(switched_numbers) == 0:
    switched_numbers = [list(numbers)]
    switched = False
  else:
    switched = True

  print(f"Switched numbers (len {len(switched_numbers)}): {switched_numbers}")
  

  for switched_number_list_i, switched_number_list in enumerate(switched_numbers):
    print(f"===================")
    print(f"Working with list {switched_number_list_i}: {ppbl(switched_number_list)}")
    print(f"Switched number list {switched_number_list_i}: {switched_number_list}")

    # Calculate JK
    tt = TransitionTable(switched_number_list)
    print("Table: ")
    print(tt)

    ## Number switch gate
    # print(switched)
    if switched:
      switch_equation = get_switching_equation(numbers, switched_number_list, tt)
      print(f"The equation for switching the repeated number is: {switch_equation}\n")
    else:
      switch_equation = JKEquation(["****"])  # Me estoy tirando un triple aquí :)

    # Karnaugh
    equations_by_jkn = table_2_karnaugh(tt)

    ## Fill transition table back.
    karnaugh_2_table(tt, equations_by_jkn)
    print()
    print("Table filled: ")
    print(tt)

    ## Check if it is a valid solution
    invalids = get_invalid_solutions(tt)
    if len(invalids) > 0:
      for invalid in invalids:
        print(f"The series {invalid} is a loop and isn't part of the main one!!!")
      print("If you need this solution, fix it yourself :)")
    
    ## Gate count
    gate_count = count_gates(equations_by_jkn, switch_equation)

    # print(gate_count)
    print(f"Circuit has {gate_count['total']} gates. (Gates can have more than 2 inputs, each input costs .5)")
    print(f"24 JK registers")
    print(f"{sum([(1 + 0.5 * i) * g for i, g in enumerate(gate_count['and'])])} AND gates")
    print(f"{sum([(1 + 0.5 * i) * g for i, g in enumerate(gate_count['or'])])} OR gates")
    print("**This COUNTS the module to replace numbers**")
    print("**Remember that wires can be shared, so the real number might be lower**\n")


if __name__ == '__main__':
  ## Leer la serie de números
  # numbers = [int(n) for n in "0-1-4-2-3-5-8-13".split("-")]
  # numbers = [int(n) for n in "0-9-15-13-12-8-12-2".split("-")]
  # numbers = [int(n) for n in "13-10-8-15-5-2-0-15".split("-")]
  # numbers = [int(n) for n in "7-1-4-15-12-2-4-14".split("-")]
  numbers = [int(n) for n in input("Números: ").split(" ")]
  print(f"Numbers: {ppbl(numbers)}")
  execute(numbers)
  

# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'EQ EQUALS FOR GE GT ID INT LBRACE LE LPAREN LT NE NUMBER PLUSPLUS PRINTLN RBRACE RPAREN SEMICOLONprogram : statement_liststatement_list : statement\n                      | statement_list statementstatement : declaration\n                 | for_loop\n                 | block\n                 | printlndeclaration : INT ID SEMICOLONfor_loop : FOR LPAREN assignment SEMICOLON condition SEMICOLON increment RPAREN blockassignment : ID EQUALS NUMBERcondition : ID LT NUMBER\n                 | ID GT NUMBER\n                 | ID LE NUMBER\n                 | ID GE NUMBER\n                 | ID EQ NUMBER\n                 | ID NE NUMBERincrement : ID PLUSPLUSblock : LBRACE statement_list RBRACEprintln : PRINTLN LPAREN ID RPAREN SEMICOLON'
    
_lr_action_items = {'INT':([0,2,3,4,5,6,7,10,12,15,17,20,28,46,],[8,8,-2,-4,-5,-6,-7,8,-3,8,-8,-18,-19,-9,]),'FOR':([0,2,3,4,5,6,7,10,12,15,17,20,28,46,],[9,9,-2,-4,-5,-6,-7,9,-3,9,-8,-18,-19,-9,]),'LBRACE':([0,2,3,4,5,6,7,10,12,15,17,20,28,44,46,],[10,10,-2,-4,-5,-6,-7,10,-3,10,-8,-18,-19,10,-9,]),'PRINTLN':([0,2,3,4,5,6,7,10,12,15,17,20,28,46,],[11,11,-2,-4,-5,-6,-7,11,-3,11,-8,-18,-19,-9,]),'$end':([1,2,3,4,5,6,7,12,17,20,28,46,],[0,-1,-2,-4,-5,-6,-7,-3,-8,-18,-19,-9,]),'RBRACE':([3,4,5,6,7,12,15,17,20,28,46,],[-2,-4,-5,-6,-7,-3,20,-8,-18,-19,-9,]),'ID':([8,14,16,22,29,],[13,19,21,26,37,]),'LPAREN':([9,11,],[14,16,]),'SEMICOLON':([13,18,24,25,27,38,39,40,41,42,43,],[17,22,28,29,-10,-11,-12,-13,-14,-15,-16,]),'EQUALS':([19,],[23,]),'RPAREN':([21,36,45,],[24,44,-17,]),'NUMBER':([23,30,31,32,33,34,35,],[27,38,39,40,41,42,43,]),'LT':([26,],[30,]),'GT':([26,],[31,]),'LE':([26,],[32,]),'GE':([26,],[33,]),'EQ':([26,],[34,]),'NE':([26,],[35,]),'PLUSPLUS':([37,],[45,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement_list':([0,10,],[2,15,]),'statement':([0,2,10,15,],[3,12,3,12,]),'declaration':([0,2,10,15,],[4,4,4,4,]),'for_loop':([0,2,10,15,],[5,5,5,5,]),'block':([0,2,10,15,44,],[6,6,6,6,46,]),'println':([0,2,10,15,],[7,7,7,7,]),'assignment':([14,],[18,]),'condition':([22,],[25,]),'increment':([29,],[36,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement_list','program',1,'p_program','app2.py',63),
  ('statement_list -> statement','statement_list',1,'p_statement_list','app2.py',67),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','app2.py',68),
  ('statement -> declaration','statement',1,'p_statement','app2.py',72),
  ('statement -> for_loop','statement',1,'p_statement','app2.py',73),
  ('statement -> block','statement',1,'p_statement','app2.py',74),
  ('statement -> println','statement',1,'p_statement','app2.py',75),
  ('declaration -> INT ID SEMICOLON','declaration',3,'p_declaration','app2.py',79),
  ('for_loop -> FOR LPAREN assignment SEMICOLON condition SEMICOLON increment RPAREN block','for_loop',9,'p_for_loop','app2.py',87),
  ('assignment -> ID EQUALS NUMBER','assignment',3,'p_assignment','app2.py',91),
  ('condition -> ID LT NUMBER','condition',3,'p_condition','app2.py',99),
  ('condition -> ID GT NUMBER','condition',3,'p_condition','app2.py',100),
  ('condition -> ID LE NUMBER','condition',3,'p_condition','app2.py',101),
  ('condition -> ID GE NUMBER','condition',3,'p_condition','app2.py',102),
  ('condition -> ID EQ NUMBER','condition',3,'p_condition','app2.py',103),
  ('condition -> ID NE NUMBER','condition',3,'p_condition','app2.py',104),
  ('increment -> ID PLUSPLUS','increment',2,'p_increment','app2.py',112),
  ('block -> LBRACE statement_list RBRACE','block',3,'p_block','app2.py',120),
  ('println -> PRINTLN LPAREN ID RPAREN SEMICOLON','println',5,'p_println','app2.py',124),
]

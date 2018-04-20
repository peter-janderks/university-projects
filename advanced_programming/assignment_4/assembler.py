#!/usr/bin/env python
# -*- mode: python; coding: utf-8; -*-

import re
import sys
from dictionaries import *

############################################################
# Parser Class
# Encapsulates access to the input code. Reads an assembly language command, 
# parses it, and provides convenient access to the command’s components
# (fields and symbols). In addition, removes all white space and comments.
############################################################
class parser():
   
    def constructor():
        """opens the file and returns a list containing each command as a seperate element 
        in  string format."""
        assembly_file = sys.stdin.readlines()
        assembly_file = parser.clean_up_file(assembly_file)
        return(assembly_file)

    def clean_up_file(file):
        """calls the function that removes all characters which are not part of a command 
        and afterwards removes empty list elements"""
        commands = []
        for lines in file:
            commands.append(parser.remove_comments(lines))
        commands = list(filter(None, commands))
        return(commands)

    def remove_comments(string):
        """removes sections of the string  with // and removes \n and whitespaces from the string"""
        string = re.sub(re.compile("//.*?\n" ) ,"" ,string)
        string = re.sub(re.compile("\n" ) ,"" ,string)
        string = string.strip()
        return(string)

    def command_type(command):
        """Returns the type of the current command"""
        if command[0] == '@':
            return("a_command")
        elif "=" in command or ";" in command:
            return("c_command")
        else:
            return("l_command")
    
    def a_instruction(a_command, dict, RAM):
        """ Returns the binary code corresponding to an a_command"""
        address = dict.get(a_command,'not found')
        if address == 'not found':
            if parser.has_numbers(a_command[0]) == True:
                return(parser.symbol(int(a_command[0:])),RAM)
            else:
                bin = parser.symbol(RAM)
                RAM +=1
                return (bin,RAM)
        else:
            address = parser.symbol(address)
            return (address,RAM)
      
    def has_numbers(input_string):
        return bool(re.search(r'\d', input_string))
        
    def c_instruction(c_command):
        """ Returns the binary code corresponding to an a_command"""
        list = ['111']
        if '=' in c_command:
            c_command = c_command.split('=')
            list.append(code.translation_into_binary(c_command[1],comp_dict))
            list.append(code.translation_into_binary(c_command[0],dest_dict))
            list.append('000')
        else:
            c_command = c_command.split(';')
            list.append(code.translation_into_binary(c_command[0],comp_dict))
            list.append('000')
            list.append(code.translation_into_binary(c_command[1],jump_dict))
        list = ''.join(list)
        return(list)
    
    def symbol(decimal_number):
        return("0{:015b}".format(decimal_number))            
    
############################################################
# Code Class
# Translates Hack assembly language mnemonics into binary codes.
############################################################  

class code():

    def translation_into_binary(mnemonic, dict):
        """Returns the binary code of the mnemonic. Dictionaries used are imported from the 
        file dictionaries.py"""
        return(dict.get(mnemonic, '000'))
   
############################################################
# Assembler 
############################################################


def ROM_values(first_pass_list,dict):
    """each time a pseudocommand (xxx) is encountered, a new entry is added to the symbol table (which is a 
    dictionary) associating xxx with  the ROM address."""
    ROM = 0
    for element in first_pass_list:
        type_of_command = parser.command_type(element)
        if type_of_command == "c_command" or type_of_command ==  "a_command":
            ROM = ROM + 1
        else:
            element = element.strip("()")
            dict[element] = ROM
    return(dict)

def first_pass():
    first_pass_list = parser.constructor()
    return(ROM_values(first_pass_list, predef_dict),first_pass_list)

def second_pass(list_of_commands,dict):
    binary_list = []
    RAM = 16
    for element in list_of_commands:
        type_of_command = parser.command_type(element)
        if type_of_command == "a_command":
            (bin,RAM) = (parser.a_instruction(element[1:],dict,RAM))
            binary_list.append(bin)
                 
        elif type_of_command == "c_command":
            binary_list.append(parser.c_instruction(element))
    return binary_list

def write_file(lines):
    for line in lines:
        print(line)
  

############################################################
# Commands to run the file
############################################################

ROM_list, command_list = first_pass()
write_file(second_pass(command_list, ROM_list))



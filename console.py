#!/usr/bin/python3
"""
Command interpreter for the AirBnB clone project.
Interpreter can be used to manage objects
"""
import cmd
from shlex import split
import re
from models import storage


def parse_arguments(args):
    braces = re.search(r'\{(.*?)\}', args)
    brackets = re.search(r'\[(.*?)\]', args)
    if braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(args)]
        else:
            lexer = split(args[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(args[:braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """
    Entry point of the command interpreter
    Attributes:
        prompt (str): command prompt
    """

    prompt = "(hbnb) "
    missing_class = "** class name missing **"
    missing_id = "** instance id missing **"
    missing_attr = "** attribute name missing **"
    missing_val = "** value missing **"
    unknown_class = "** class doesn't exist **"
    unknown_id = "** no instance found **"
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def default(self, args):
        """Default method for command interpreter"""
        arg_dict = {
            "all": self.do_all,
            "count": self.do_count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update
        }
        re_match = re.search(r'\.', args)
        if re_match is not None:
            argl = [args[:re_match.span()[0]], args[re_match.span()[1]:]]
            re_match = re.search(r'\((.*?)\)', argl[1])
            if re_match is not None:
                my_cmd = [argl[1][:re_match.span()[0]],
                          re_match.group()[1:-1]]
                if my_cmd[0] in arg_dict.keys():
                    call = "{} {}".format(argl[0], my_cmd[1])
                    return arg_dict[my_cmd[0]](call)
        print("*** Unknown syntax: {}".format(args))
        return False

    def emptyline(self, args):
        """
        Overwrites emptyline method to
        not execute previous command
        """
        pass

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """EOF command  exit the program"""
        print("")
        return True

    def do_create(self, args):
        """
        Usage: create <class name> <key 1>=<value 1> <key 2>=<value 2>...
        Creates a new instance of model,
        saves it (to the JSON file) and prints the id
        """

        try:
            if not args:
                raise SyntaxError()
            cmd_list = args.split(" ")
            kwargs = {}

            for i in range(1, len(cmd_list)):
                key, value = cmd_list[i].split("=")
                if value[0] == '"' and value[-1] == '"':
                    value = value.strip('"').replace('_', ' ')
                else:
                    try:
                        value = eval(value)
                    except (SyntaxError, NameError):
                        continue
                kwargs[key] = value

            if kwargs == {}:
                obj = eval(cmd_list[0])()
            else:
                obj = eval(cmd_list[0])(**kwargs)
                storage.new(obj)
            print(obj.id)
            obj.save()

        except SyntaxError:
            print(self.missing_class)
        except NameError:
            print(self.unknown_class)

    def do_show(self, args):
        """
        Usage: show <class name> <id>
        Prints the string representation of an instance
        based on the class name and id
        """

        argl = parse_arguments(args)
        obj_dict = storage.all()
        if len(argl) == 0:
            print(self.missing_class)
        elif argl[0] not in HBNBCommand.__classes:
            print(self.unknown_class)
        elif len(argl) == 1:
            print(self.missing_id)
        elif "{}.{}".format(argl[0], argl[1]) not in obj_dict:
            print(self.unknown_id)
        else:
            print(obj_dict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, args):
        """
        Usage: destroy <class name> <id> or <class >.destry(<id>)
        Delete an instance based on the class name and id
        """
        argl = parse_arguments(args)
        obj_dict = storage.all()
        if len(argl) == 0:
            print(self.missing_class)
        elif argl[0] not in HBNBCommand.__classes:
            print(self.unknown_class)
        elif len(argl) == 1:
            print(self.missing_id)
        elif "{}.{}".format(argl[0], argl[1]) not in obj_dict:
            print(self.unknown_id)
        else:
            del obj_dict["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def do_all(self, args):
        """
        Usage: all or all <class name>
        Prints all string representation of all instances
        based or not on the class name
        """
        argl = parse_arguments(args)
        if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
            print(self.unknown_class)
        else:
            objl = []
            obj_dict = storage.all()
            for obj in obj_dict.values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_update(self, args):
        """
        Usage: update <class name> <id> <attribute name> "<attribute value>" or
        <class name>.update(<id>, <attribute name>, <attribute value>) or
        <class name>.update(<id>, <dictionary >)
        """

        argl = parse_arguments(args)
        obj_dict = storage.all()

        if len(argl) == 0:
            print(self.missing_class)
            return False
        if argl[0] not in HBNBCommand.__classes:
            print(self.unknown_class)
            return False
        if len(argl) == 1:
            print(self.missing_id)
            return False
        if "{}.{}".format(argl[0], argl[1]) not in obj_dict:
            print(self.unknown_id)
            return False
        if len(argl) == 2:
            print(self.missing_attr)
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print(self.missing_val)
                return False
        if len(argl) == 4:
            obj = obj_dict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = obj_dict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys()
                    and type(obj.__class__.__dict__[k])
                        in {str, int, float}):
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v

        storage.save()

    def do_count(self, args):
        """
        Usage: count <class name> or <class name>.count()
        The count command returns the number of instances
        """

        argl = parse_arguments(args)
        count = 0
        for obj in storage.all().values():
            if obj.__class__.__name__ == argl[0]:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3
"""
The base class
"""
import json
import csv
import turtle


class Base:
    """
    base classe
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializing base class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation
        of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation
        of list_objs to a file"""
        file = cls.__name__ + '.json'
        li = []
        if list_objs is None:
            csvfile.write("[]")
        if list_objs is not None:
            li = [obj.to_dictionary() for obj in list_objs]
        if file:
            with open(file, mode='w', encoding='utf-8') as f:
                f.write(cls.to_json_string(li))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string
        representation json_string"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        file = cls.__name__ + '.json'
        try:
            with open(file, mode='r') as f:
                data = f.read()
        except FileNotFoundError:
            return []
        i = cls.from_json_string(data)
        instances = [cls.create(**obj) for obj in i]
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ writes list_objs to a csv file"""
        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.width, obj.height,
                                    obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """serializes and deserializes CSV"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                if cls.__name__ == "Rectangle":
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == "Square":
                    fields = ['id', 'size', 'x', 'y']
                obj_list = []
                for row in reader:
                    data = [int(x) for x in row]
                    obj = cls(*data)
                    obj_list.append(obj)
                return obj_list
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares"""
        t = turtle.Turtle()
        screen = turtle.Screen()
        screen.setup(800, 600)

        for rect in list_rectangles:
            for _ in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)
        for square in list_squares:
            for _ in range(4):
                t.forward(square.size)
                t.left(90)
        screen.exitonclick()

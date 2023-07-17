#!/usr/bin/python3
"""
The base class
"""
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
        if list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation
        of list_objs to a file"""
        file = cls.__name__ + '.json'
        li = []
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
        file_1 = cls.__name__ + '.csv'
        fieldnames = []
        if cls.__name__ == 'Rectangle':
            fieldnames = ['id', 'width', 'height', 'x', 'y']
        if cls.__name__ == 'Square':
            fieldnames = ['id', 'size', 'x', 'y']
        with open(file_1, mode='w') as f:
            csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
            csv_writer.writeheader()
            for i in list_objs:
                csv_writer.writerow(i.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """serializes and deserializes CSV"""
        class_name = cls.__name__
        file_name = class_name + ".csv"

        with open(file_name, mode='r', newline='') as file:
            reader = csv.reader(file)
            objects = []

            next(reader)

            if class_name == "Rectangle":
                for row in reader:
                    if len(row) >= 5:
                        obj = cls(0, 0)
                        obj.id = int(row[0])
                        obj.width = int(row[1])
                        obj.height = int(row[2])
                        obj.x = int(row[3])
                        obj.y = int(row[4])
                        objects.append(obj)

            elif class_name == "Square":
                for row in reader:
                    if len(row) >= 4:
                        obj = cls(0)
                        obj.id = int(row[0])
                        obj.size = int(row[1])
                        obj.x = int(row[2])
                        obj.y = int(row[3])
                        objects.append(obj)

            return objects

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

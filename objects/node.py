from objects.game_object import GameObject, delete_game_object, get_object_pool, get_object_types, validate_type_name

class Node(GameObject):
    type = '__node'

    class Schema(GameObject.Schema):
        # serialize ids because non-root nodes need them
        do_not_serialize = ['deleted', 'children', 'linked', 'parent']
        is_node = True

    def __init__(self) -> None:
        super().__init__()

        self.children : list[Node] = []
        self.parent : Node = None
    
    def has_child(self, type_name):
        type_name = validate_type_name(type_name)

        for child in self.children:
            if child.type == type_name:
                return True

    def get_child(self, type_name):
        type_name = validate_type_name(type_name)

        for child in self.children:
            if child.type == type_name:
                return child

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def remove_child(self, child):
        child.parent = None
        self.children.remove(child)
    
    def delete_child(self, child):
        self.children.remove(child)
        self.children.remove(child)
        delete_game_object(child)
    
    def get_children(self, type_name):
        list = []
        type_name = validate_type_name(type_name)

        for child in self.children:
            if child.type == type_name:
                list.append(child)

        return child
    
    def __serialize__(self) -> dict:
        dict = super().__serialize__()

        if len(self.children) > 0:
            dict['children'] = [node.__serialize__() for node in self.children]

        # root nodes don't need ids
        if self.parent is None:
            dict.pop('id')
        
        return dict
    
    def post_construction(self) -> None:
        if not hasattr(self, 'children'):
            self.__setattr__('children', [])

        return super().post_construction()

def establish_parents(node : Node):
    for child in node.children:
        child.parent = node
        establish_parents(child)

def establish_all_parents():
    for type, data in get_object_pool().items():
        schema : GameObject.Schema = get_object_types()[type].Schema

        if not schema.is_node:
            continue
        
        if schema.is_singleton:
            data.parent = None
            establish_parents(data)
        else:
            for id, obj in data.items():
                obj.parent = None
                establish_parents(obj)

def remove_non_root_nodes():
    pool = get_object_pool()
    types_to_rmv = []
    objs_to_rmv = []

    for type, data in pool.items():
        schema : GameObject.Schema = get_object_types()[type].Schema

        if not schema.is_node:
            continue
        
        if schema.is_singleton:
            if data.parent is not None:
                types_to_rmv.append(type)
        else:
            for id, obj in data.items():
                if obj.parent is not None:
                    objs_to_rmv.append((type, id))
    
    for type in types_to_rmv:
        pool.pop(type)
    
    for type, id in objs_to_rmv:
        pool[type].pop(id)
from objects.game_object import GameObject

def compare_without_ids(obj1 : GameObject, obj2 : GameObject) -> bool:
    data1 = obj1.__serialize__()
    data2 = obj2.__serialize__()

    def trim_ids(obj):
        if isinstance(obj, dict):
            data = {}

            for key, val in obj.items():
                if key == 'id':
                    continue
                else:
                    data[key] = trim_ids(val)

            return data
        elif isinstance(obj, list):
            return [trim_ids(val) for val in obj]
        else:
            return obj
        
    data1 = trim_ids(data1)
    data2 = trim_ids(data2)

    return data1 == data2
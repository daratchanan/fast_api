def tag_serializer(tag) -> dict:
    return {
        'id':str(tag["_id"]),
        'name':tag["name"],
        # 'slug':"",
        'description':tag["description"],
        # 'policy_count':int(tag["policy_count"]),
       
    }

def tages_serializer(tages) -> list:
    return [tag_serializer(tag) for tag in tages ] 
def build_profile(first, last, **user_info):
    user_info["First name"] = first
    user_info["Last name"] = last
    return user_info

user_profile = build_profile("Vincenzo", "Navarra",
                             location="Warrington",
                             field="Law")
print(user_profile)
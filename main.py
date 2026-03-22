import init_django_orm  # noqa: F401


from db.models import Race, Skill, Player, Guild


import json


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for nickname, playerinfo in players.items():
        race_data = playerinfo["race"]
        race_name = race_data["name"]
        race_description = race_data["description"]
        guild_data = playerinfo["guild"]
        race, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_description})
        if guild_data:
            guild_name = guild_data["name"]
            guild_description = guild_data["description"]
            guild, _ = Guild.objects.get_or_create(
                name=guild_name,
                defaults={"description": guild_description})
        else:
            guild = None
        skills = race_data["skills"]
        for skill_ in skills:
            Skill.objects.get_or_create(
                name=skill_["name"],
                defaults={"bonus": skill_["bonus"], "race": race})

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": playerinfo["email"],
                "bio": playerinfo["bio"],
                "race": race,
                "guild": guild})


if __name__ == "__main__":
    main()

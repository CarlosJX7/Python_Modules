import alchemy.grimoire


print("=== Kaboom 0 ===")
print("Using grimoire module directly")
s_name = "Fantasy"
s_type = "Earth, wind and fire"
print(f"Testing record light spell: "
      f"{alchemy.grimoire.light_spell_record(s_name, s_type)}")

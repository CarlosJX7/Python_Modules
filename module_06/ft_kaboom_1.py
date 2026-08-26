from alchemy.grimoire.dark_spellbook import dark_spell_record
print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")

s_name = "Fantasy"
s_type = "Earth, wind and fire"
print(f"Testing record light spell: {dark_spell_record(s_name, s_type)}")

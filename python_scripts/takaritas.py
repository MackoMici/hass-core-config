ROOM_ENTITIES= ["input_boolean.nappali", "input_boolean.ebedlo", "input_boolean.konyha", "input_boolean.haloszoba", "input_boolean.folyoso", "input_boolean.eloszoba","input_boolean.gyerekszoba"]

CLEAN_ENTITIES= ["input_datetime.nappali_utolso_takaritas", "input_datetime.ebedlo_utolso_takaritas", "input_datetime.konyha_utolso_takaritas", "input_datetime.haloszoba_utolso_takaritas", "input_datetime.folyoso_utolso_takaritas", "input_datetime.eloszoba_utolso_takaritas","input_datetime.gyerekszoba_utolso_takaritas"]


num_open_room = 0
get_time = data.get('ido')
logger.debug("Mikor volt takarítva, idő beállíáts")
for count in range(len(ROOM_ENTITIES)):
  logger.debug("Helység száma: %s",count)
  logger.debug("Helység neve: %s", ROOM_ENTITIES[count])
  if (hass.states.get(ROOM_ENTITIES[count]).state) == "on":
    logger.debug("%s helységet takarítjunk",ROOM_ENTITIES[count])
    hass.services.call("input_boolean", "turn_off", {"entity_id" : ROOM_ENTITIES[count]}, False)
    hass.states.set(CLEAN_ENTITIES[count], get_time, {})
    num_open_room = num_open_room + 1
logger.debug("Osszesen %s helységet takarítunk",num_open_room)

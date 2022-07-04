from console.command.query_command import QueryCommand
from settlers_of_valgard.settler.settler import Settler

QueryCommand(
    "settlers", 
    "lists the settlers of your settlement",
    Settler,
    aliases=["s", "settler"]
)
class User:
    def __init__(self, username: str, name: str, age: int, steamid64: str):
        self.steamid64 = None
        self.username = username
        self.name = name
        self.age = age

    def ConnectSteam(self, steamid64):
        # Just getting the idea of connecting steam accounts to users via steam API
        self.steamid64 = steamid64


class Lobby:
    def __init__(self, lobbyid: int, users: [], status: str, slots: int, lock: bool, roles: [], description: str):
        self.status = 'Inactive'
        self.slots = 0
        self.users = []
        # Claiming if the lobby is locked or free to join for every1
        self.lock = False
        # Roles that are free to join
        self.roles = []
        # Just some space for writing more info about the lobby
        self.description = ''

    def EnableSearch(self, slots, roles):
        # Publishing search to lobby list
        self.status = 'Active'
        self.slots = slots
        self.roles.append(roles)

    def DisableSearch(self):
        # Disabling lobby from lobby list
        self.status = 'Inactive'

    def JoiningLobby(self, user):
        self.users.append(user)

    def LeavingLobby(self, user):
        self.users.pop(user)


def main():
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

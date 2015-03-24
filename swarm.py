class Swarm:

    PIECES_TARGET_INSTANCES = 1

    def __init__(self):

        self.pieces_table = dict()
        self.users = dict()

    def add(self, user):

        for f in user.arbo:
            # f[1] is the file's hash
            self.upload_file(f[1], user)
        self.add_user(user)

    def add_user(self, user):
        self.users[user] = user

    def user_get(self, i):
        if not self.users:
            print('WARNING: there is no user')
            return None
        return self.users.values()[i % len(self.users)]

    def upload_file(self, f, user_src, user_storing = 0):

        # take some available users and ask them to store the file
        for i in range(self.PIECES_TARGET_INSTANCES):
            self.order_user_hosting(self.user_get(user_storing), user_src, f)
            user_storing += 1

    def order_user_hosting(self, user_target, user_src, what):
        print('---------> ' + user_src.ip_addr)
        if user_target is None:
            return
        user_target.send('SEND ' + user_src.ip_addr + ' ' + what)
        #TODO: confirm with callback from user_target

        if not what in self.pieces_table:
            self.pieces_table[what] = list()
        self.pieces_table[what].append(user_target)
        print(what + ' is owned by ' + user_target.name)

    def hash_piece_get(self, hsh, i):
        return self.pieces_table[hsh][i % len(self.pieces_table[hsh])]

    def recover_file(self, user_target, hsh, user_storing = 0):

        if not hsh in self.pieces_table:
            user_target.send('ERRO piece ' + hsh + ' is not alive')
        user_target.send('RECV ' + hsh + ' ' + self.hash_piece_get(hsh, user_storing).ip_addr)
        user_storing += 1

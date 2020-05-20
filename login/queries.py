from django.db import connection, DatabaseError
from farmakami.utility import dict_fetch_all, dict_fetch_one, DatabaseAttributeError

"""
Kode yang melakukan semua query dan memasukkannya ke Object yang sesuai.
"""

class PK(object):
    """
    Black magic agar bisa menggunakan method login.
    """

    def __init__(self, pk_field):
        self.pk = pk_field

    def value_to_string(self, object):
        return self.pk

class Meta(object):
    """
    Black magic agar bisa menggunakan method login.
    """

    def __init__(self, pk_field):
        self.pk = PK(pk_field)

class Pengguna(object):
    def __init__(self, email, telepon, password, nama_lengkap):
        self.email = email if email else None
        self.telepon = telepon if telepon else None
        self.password = password if password else None
        self.nama_lengkap = nama_lengkap if nama_lengkap else None
        self.is_authenticated = True
        self.is_admin = Admin.check_one_where_email_exist(self.email)
        self.is_konsumen = Konsumen.check_one_where_email_exist(self.email)
        self.is_kurir = Kurir.check_one_where_email_exist(self.email)
        self.is_cs = Cs.check_one_where_email_exist(self.email)
        self.backend = 'login.backends.FarmakamiAuthBackend'
        self.errors = []
        self._meta = Meta(email)

        def save(self, update_fields):
            return None
        
        def is_valid(self):
            if self.email is None:
                error = DatabaseAttributeError('email', 'Email tidak boleh kosong!')
                self.errors.append(error)
            elif self.email.check_one_where_email_exist(self.email):
                error = DatabaseAttributeError('email', 'Email sudah terdaftar')
                self.errors.append(error)
            
            if self.password is None:
                error = DatabaseAttributeError('password', 'Password tidak boleh kosong')
                self.errors.append(error)
            
            if self.nama_lengkap is None:
                error = DatabaseAttributeError('nama_lengkap', 'Nama Lengkap tidak boleh kosong')

            return not self.errors
        
        @staticmethod
        def select_all_where_email(email):
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM pengguna WHERE email = %s", [str(email)])
                list_pengguna_dict = dict_fetch_all(cursor)
                list_pengguna_obj = []
                for pengguna in list_pengguna_dict:
                    pengguna_obj = Pengguna(pengguna['email'], pengguna['telepon'], pengguna['password'], pengguna['nama_lengkap'])
                    list_pengguna_obj.append(pengguna_obj)
                return list_pengguna_obj
            
        @staticmethod
        def select_one_where_email(email):
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM pengguna WHERE email = %s", [str(email)])
                list_pengguna_dict = dict_fetch_one(cursor)
                for pengguna in list_pengguna_dict:
                    pengguna_obj = Pengguna(pengguna['email'], pengguna['telepon'], pengguna['password'], pengguna['nama_lengkap'])
                
                return pengguna_obj
            
        @staticmethod
        def check_one_where_email_exist(email):
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1 FROM pengguna WHERE email = %s", [str(email)])
                pengguna = dict_fetch_one(email)
                return pengguna is not None
        
        def insert(self):
            with connection.cursor() as cursor:
                try:
                    insert_query = "INSERT INTO pengguna VALUES (%s, %s, %s, %s)"
                    attr_to_insert = (self.email, self.telepon, self.password, self.nama_lengkap)
                    cursor.execute(insert_query, attr_to_insert)
                except(DatabaseError, TypeError) as e:
                    print(str(e))
                    raise e
                return True

class Apoteker(object):
    def __init__(self, email):
        self.email = email if email else None
        self.errors = []

    def is_valid(self):
        if self.email is None:
            error = DatabaseAttributeError('email', 'Email tidak boleh kosong')
            self.errors.append(error)
        elif Apoteker.check_one_where_email_exist(email):
            error = DatabaseAttributeError('email', 'Email sudah di daftarkan')
            self.errors.append(error)
        return not self.errors
    
    @staticmethod
    def select_all_where_email(email):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM apoteker WHERE email = %s", [str(email)])
            list_apoteker_dict = dict_fetch_all(cursor)
            list_apoteker_obj = []
            for apoteker in list_apoteker_dict:
                apoteker_obj = Apoteker(apoteker['email'])
                list_apoteker_obj.append(apoteker_obj)
            return list_apoteker_obj
    
    @staticmethod
    def select_one_where_email(email):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM apoteker WHERE email = %s", [str(email)])
            apoteker = dict_fetch_one(cursor)
            if apoteker is not None:
                apoteker = Apoteker(apoteker['email'])
            return apoteker
    
    @staticmethod
    def check_one_where_email_exist(email):
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1 FROM apoteker WHERE email = %s", [str(email)])
            apoteker = dict_fetch_one(cursor)
            return apoteker is not None
    
    def insert(self):
        with connection.cursor() as cursor:
            try:
                cursor.execute("INSERT INTO apoteker VALUES(%s)", [self.email])
            except (DatabaseError, TypeError) as e:
                print(str(e))
                raise e
            return True

class Admin(object):
    def __init__(self, email, id_apotek):
        self.email = email if email else None
        self.id_apotek = id_apotek if id_apotek else None
        self.errors = []
    
    def is_valid(self):
        if self.email is None:
            error = DatabaseAttributeError('email', 'Email tidak boleh kosong')
            self.errors.append(error)
        elif Admin.check_one_where_email_exist(self.email):
            error = DatabaseAttributeError('email', 'Email sudah terdaftar')
            self.errors.append(error)
    
        if self.id_apotek is None:
            error = DatabaseAttributeError('id_apotek', 'Id_apotek tidak boleh kosong')
            self.errors.append(error)
        return not self.errors

    @staticmethod
    def select_one_where_email(email):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM admin_apotek WHERE email = %s", [str(email)])
            admin = dict_fetch_one(cursor)
            if admin is not None:
                admin = Admin(admin['email'], admin['id_apotek'])
            return admin

    @staticmethod
    def check_one_where_email_exist(email):
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1 WHERE email = %s", [str(email)])
            admin = dict_fetch_one(cursor)
            return admin is not None
    
    def insert(self):
        with connection.cursor() as cursor:
            try:
                cursor.execute("INSERT INTO admin_apotek VALUES(%s, %s)", [self.email, self.id_apotek])
            except (DatabaseError, TypeError) as e:
                print(str(e))
                raise e
            return True

class Konsumen(object):
    pass

class Kurir(object):
    pass

class Cs(object):
    pass
            
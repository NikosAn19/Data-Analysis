import pyodbc
import generator
import Data
# DRIVER_NAME = 'SQL_SERVER'
# SERVER_NAME = 'DESKTOP-O2F93VK\SQLEXPRESS'
# DATABASE_NAME = 'Equipment'
#
# connection_string = f"""
#     DRIVER = {{{DRIVER_NAME}}};
#     SERVER = {SERVER_NAME};
#     DATABASE = {DATABASE_NAME};
#     Trust_Connection = yes;
# """

conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                      "Server=DESKTOP-O2F93VK\SQLEXPRESS;"
                      "Database=Equipment;"
                      "Trusted_Connection=yes;")
print(conn)
cursor = conn.cursor()
insert_pcs_str = "INSERT INTO PC(mac_address, pc_name, ram, windows_licence, office_licence, cpu, section_id, arrival_date) values (?, ?, ?, ?, ?, ?, ?, ?)"
insert_printers_str = "INSERT INTO PRINTER(mac_address, brand, model, ink_storage, section_id, arrival_date) values (?, ?, ?, ?, ?, ?)"
insert_photocopiers_str = "INSERT INTO PHOTOCOPIER(mac_address, brand, model, arrival_date, section_id) values (?, ?, ?, ?, ?)"
insert_scanners_str = "INSERT INTO SCANNER(mac_address, brand, model, arrival_date, section_id) values (?, ?, ?, ?, ?)"
insert_routers_str = "INSERT INTO ROUTER(mac_address, section_id, brand, model, arrival_date) values (?, ?, ?, ?, ?)"
insert_sections_str = "INSERT INTO SECTION(section_id, total_pcs, total_printers, total_scanners, total_photocopiers, total_routers) values (?, ?, ?, ?, ?, ?)"

insert_pc_repairs_str = "INSERT INTO PC_REPAIR(mac_address, repair, date, repair_description) values (?, ?, ? ,?)"
insert_pc_update_str = "INSERT INTO PC_UPDATE(mac_address, pc_update, date, update_description) values (?, ?, ? ,?)"
insert_printer_repair_str = "INSERT INTO PRINTER_REPAIR(mac_address, printer_repair, date, repair_description) values (?, ?, ? ,?)"
insert_photocopier_repair_str = "INSERT INTO PHOTOCOPIER_REPAIR(mac_address, photocopier_repair, date, repair_description) values (?, ?, ? ,?)"
insert_scanner_repair_str = "INSERT INTO SCANNER_REPAIR(mac_address, scanner_repair, date, repair_description) values (?, ?, ? ,?)"
insert_router_repair_str = "INSERT INTO ROUTER_REPAIR(mac_address, router_repair, date, repair_description) values (?, ?, ? ,?)"


def insert_sections():
    section = ('1', '0', '0', '0', '0', '0')
    section2 = ('2', '0', '0', '0', '0', '0')
    section3 = ('3', '0', '0', '0', '0', '0')
    section4 = ('4', '0', '0', '0', '0', '0')
    result = cursor.execute(insert_sections_str, section)
    result2 = cursor.execute(insert_sections_str, section2)
    result3 = cursor.execute(insert_sections_str, section3)
    result4 = cursor.execute(insert_sections_str, section4)
    conn.commit()


def insert_pcs():
    pcs = Data.generate_pc_data(100)
    for pc in pcs:
        print(pc)
        result = cursor.execute(insert_pcs_str, pc)

    conn.commit()


def insert_printers():
    printers = Data.generate_printer_data(100)
    for printer in printers:
        print(printer)
        result = cursor.execute(insert_printers_str, printer)

    conn.commit()


def insert_photocopiers():
    photocopiers = Data.generate_photocopier_data(100)
    for photocopier in photocopiers:
        print(photocopier)
        result = cursor.execute(insert_photocopiers_str, photocopier)

    conn.commit()


def insert_scanners():
    scanners = Data.generate_scanner_data(100)
    for scanner in scanners:
        print(scanner)
        result = cursor.execute(insert_scanners_str, scanner)

    conn.commit()


def insert_routers():
    routers = Data.generate_router_data(100)
    for router in routers:
        print(router)
        result = cursor.execute(insert_routers_str, router)

    conn.commit()


def insert_pc_repairs():
    pc_repairs = Data.generate_pc_repair_data(100)
    for pc_repair in pc_repairs:
        print(pc_repair)
        result = cursor.execute(insert_pc_repairs_str, pc_repair)

        conn.commit()


def insert_pc_updates():
    pc_updates = Data.generate_pc_update_data(100)
    for pc_update in pc_updates:
        print(pc_update)
        result = cursor.execute(insert_pc_update_str, pc_update)

    conn.commit()


def insert_printer_repairs():
    printer_repairs = Data.generate_printer_repair_data(70)
    for printer_repair in printer_repairs:
        print(printer_repair)
        result = cursor.execute(insert_printer_repair_str, printer_repair)

    conn.commit()


def insert_photocopier_repairs():
    photocopiers_repairs = Data.generate_photocopier_repair_data(70)
    for photocopiers_repair in photocopiers_repairs:
        print(photocopiers_repair)
        result = cursor.execute(insert_photocopier_repair_str, photocopiers_repair)

    conn.commit()


def insert_scanner_repairs():
    scanner_repairs = Data.generate_scanner_repair_data(70)
    for scanner_repair in scanner_repairs:
        print(scanner_repair)
        result = cursor.execute(insert_scanner_repair_str, scanner_repair)

    conn.commit()


def insert_router_repairs():
    router_repairs = Data.generate_router_repair_data(70)
    for router_repair in router_repairs:
        print(router_repair)
        result = cursor.execute(insert_router_repair_str, router_repair)

    conn.commit()


def insert_pc(pc):
    global conn
    global cursor
    global insert_pcs_str
    query_result = cursor.execute(insert_pcs_str, pc)
    print(query_result)
    conn.commit()


def insert_pc_repair(pc_repair):
    global conn
    global cursor
    global insert_pc_repairs_str
    query_result = cursor.execute(insert_pc_repairs_str, pc_repair)
    print(query_result)
    conn.commit()


def insert_pc_update(pc_update):
    global conn
    global cursor
    global insert_pc_update_str
    query_result = cursor.execute(insert_pc_update_str, pc_update)
    print(query_result)
    conn.commit()


def insert_section(section):
    global conn
    global cursor
    global insert_pcs_str
    query_result = cursor.execute(insert_sections_str, section)
    print(query_result)
    conn.commit()


def insert_printer(printer):
    global conn
    global cursor
    global insert_printers_str
    query_result = cursor.execute(insert_pcs_str, printer)
    conn.commit()


def insert_printer_repair(printer_repair):
    global conn
    global cursor
    global insert_printer_repair_str
    query_result = cursor.execute(insert_printers_str, printer_repair)
    print(query_result)
    conn.commit()


def insert_photocopier(photocopier):
    global conn
    global cursor
    global insert_photocopiers_str
    query_result = cursor.execute(insert_pcs_str, photocopier)
    conn.commit()


def insert_photocopier_repair(photocopier_repair):
    global conn
    global cursor
    global insert_photocopier_repair_str
    query_result = cursor.execute(insert_photocopier_repair_str, photocopier_repair)
    print(query_result)
    conn.commit()


def insert_scanner(scanner):
    global conn
    global cursor
    global insert_scanners_str
    query_result = cursor.execute(insert_pcs_str, scanner)
    conn.commit()


def insert_scanner_repair(scanner_repair):
    global conn
    global cursor
    global insert_scanner_repair_str
    query_result = cursor.execute(insert_scanner_repair_str, scanner_repair)
    print(query_result)
    conn.commit()


def insert_router(router):
    global conn
    global cursor
    global insert_routers_str
    query_result = cursor.execute(insert_pcs_str, router)
    conn.commit()


def insert_router_repair(router_repair):
    global conn
    global cursor
    global insert_router_repair_str
    query_result = cursor.execute(insert_router_repair_str, router_repair)
    print(query_result)
    conn.commit()


def insert_generated_data():
    insert_sections()
    insert_pcs()
    insert_printers()
    insert_photocopiers()
    insert_scanners()
    insert_routers()
    insert_pc_repairs()
    insert_pc_updates()
    insert_printer_repairs()
    insert_photocopier_repairs()
    insert_scanner_repairs()
    insert_router_repairs()


def get_mac_address_pc():
    global cursor
    global conn
    statement = 'SELECT mac_address from PC'
    result = cursor.execute(statement)
    return result


def get_mac_address_photocopier():
    global cursor
    global conn
    statement = 'SELECT mac_address from PRINTER'
    result = cursor.execute(statement)
    return result


def get_mac_address_printer():
    global cursor
    global conn
    statement = 'SELECT mac_address from PRINTER'
    result = cursor.execute(statement)
    return result


def get_mac_address_scanner():
    global cursor
    global conn
    statement = 'SELECT mac_address from SCANNER'
    result = cursor.execute(statement)
    return result


def get_mac_address_router():
    global cursor
    global conn
    statement = 'SELECT mac_address from ROUTER'
    result = cursor.execute(statement)
    return result

import random

# from openpyxl.reader.excel import load_workbook
# from openpyxl.styles import Font
# from openpyxl.utils import get_column_letter
# from openpyxl.workbook import Workbook

mac_addresses = []
ma_1 = 'A'
ma_2 = 'B'
ma_3 = 'C'
ma_4 = 'D'
ma_5 = 'E'
ma_6 = 'F'
ma_7 = 'G'
ma_8 = 'H'


def generate_mac_addresses():
    for i in range(0, 10):
        mac_address = str(i) + ma_1 + ':' + str(0) + ma_2 + ':' + str(0) + ma_3 + ':' + str(0) + ma_4 + ':' + str(
            0) + ma_5 + ':' + str(0) + ma_6
        mac_addresses.append(mac_address)

    for i in range(1, 10):
        mac_address = str(0) + ma_1 + ':' + str(i) + ma_2 + ':' + str(0) + ma_3 + ':' + str(0) + ma_4 + ':' + str(
            0) + ma_5 + ':' + str(0) + ma_6
        mac_addresses.append(mac_address)

    for i in range(1, 10):
        mac_address = str(0) + ma_1 + ':' + str(0) + ma_2 + ':' + str(i) + ma_3 + ':' + str(0) + ma_4 + ':' + str(
            0) + ma_5 + ':' + str(0) + ma_6
        mac_addresses.append(mac_address)

    for i in range(1, 10):
        mac_address = str(0) + ma_1 + ':' + str(0) + ma_2 + ':' + str(0) + ma_3 + ':' + str(i) + ma_4 + ':' + str(
            0) + ma_5 + ':' + str(0) + ma_6
        mac_addresses.append(mac_address)

    for i in range(1, 10):
        mac_address = str(0) + ma_1 + ':' + str(0) + ma_2 + ':' + str(0) + ma_3 + ':' + str(0) + ma_4 + ':' + str(
            i) + ma_5 + ':' + str(0) + ma_6
        mac_addresses.append(mac_address)

    for i in range(1, 10):
        mac_address = str(0) + ma_1 + ':' + str(0) + ma_2 + ':' + str(0) + ma_3 + ':' + str(0) + ma_4 + ':' + str(
            0) + ma_5 + ':' + str(i) + ma_6
        mac_addresses.append(mac_address)

    for i in range(0, 10):
        mac_address = str(i) + ma_1 + ':' + str(1) + ma_2 + ':' + str(1) + ma_3 + ':' + str(1) + ma_4 + ':' + str(
            1) + ma_5 + ':' + str(1) + ma_6
        mac_addresses.append(mac_address)

    for i in range(0, 10):
        if i == 1:
            continue
        else:
            mac_address = str(1) + ma_1 + ':' + str(i) + ma_2 + ':' + str(1) + ma_3 + ':' + str(1) + ma_4 + ':' + str(
                1) + ma_5 + ':' + str(1) + ma_6
            mac_addresses.append(mac_address)

    for i in range(0, 10):
        if i == 1:
            continue
        else:
            mac_address = str(1) + ma_1 + ':' + str(1) + ma_2 + ':' + str(i) + ma_3 + ':' + str(1) + ma_4 + ':' + str(
                1) + ma_5 + ':' + str(1) + ma_6
            mac_addresses.append(mac_address)

    for i in range(0, 10):
        if i == 1:
            continue
        else:
            mac_address = str(1) + ma_1 + ':' + str(1) + ma_2 + ':' + str(1) + ma_3 + ':' + str(i) + ma_4 + ':' + str(
                1) + ma_5 + ':' + str(1) + ma_6
            mac_addresses.append(mac_address)

    for i in range(0, 10):
        if i == 1:
            continue
        else:
            mac_address = str(1) + ma_1 + ':' + str(1) + ma_2 + ':' + str(1) + ma_3 + ':' + str(1) + ma_4 + ':' + str(
                i) + ma_5 + ':' + str(1) + ma_6
            mac_addresses.append(mac_address)

    for i in range(0, 10):
        if i == 1:
            continue
        else:
            mac_address = str(1) + ma_1 + ':' + str(1) + ma_2 + ':' + str(1) + ma_3 + ':' + str(1) + ma_4 + ':' + str(
                1) + ma_5 + ':' + str(i) + ma_6
            mac_addresses.append(mac_address)

    for i in range(0, 10):
        if i == 2:
            continue
        else:
            mac_address = str(i) + ma_1 + ':' + str(2) + ma_2 + ':' + str(2) + ma_3 + ':' + str(2) + ma_4 + ':' + str(
                2) + ma_5 + ':' + str(2) + ma_6
            mac_addresses.append(mac_address)

    for i in range(0, 10):
        if i == 2:
            continue
        else:
            mac_address = str(2) + ma_1 + ':' + str(i) + ma_2 + ':' + str(2) + ma_3 + ':' + str(2) + ma_4 + ':' + str(
                2) + ma_5 + ':' + str(2) + ma_6
            mac_addresses.append(mac_address)

    for i in range(0, 10):
        if i == 2:
            continue
        else:
            mac_address = str(2) + ma_1 + ':' + str(2) + ma_2 + ':' + str(i) + ma_3 + ':' + str(2) + ma_4 + ':' + str(
                2) + ma_5 + ':' + str(2) + ma_6
            mac_addresses.append(mac_address)

    for i in range(0, 10):
        if i == 2:
            continue
        else:
            mac_address = str(2) + ma_1 + ':' + str(2) + ma_2 + ':' + str(2) + ma_3 + ':' + str(i) + ma_4 + ':' + str(
                2) + ma_5 + ':' + str(2) + ma_6
            mac_addresses.append(mac_address)

    for i in range(0, 10):
        if i == 2:
            continue
        else:
            mac_address = str(2) + ma_1 + ':' + str(2) + ma_2 + ':' + str(2) + ma_3 + ':' + str(2) + ma_4 + ':' + str(
                i) + ma_5 + ':' + str(2) + ma_6
            mac_addresses.append(mac_address)

    for i in range(0, 10):
        if i == 2:
            continue
        else:
            mac_address = str(2) + ma_1 + ':' + str(2) + ma_2 + ':' + str(2) + ma_3 + ':' + str(2) + ma_4 + ':' + str(
                2) + ma_5 + ':' + str(i) + ma_6
            mac_addresses.append(mac_address)
    for i in range(0, 10):
        mac_address = str(i) + ma_1 + ':' + str(3) + ma_2 + ':' + str(3) + ma_3 + ':' + str(3) + ma_4 + ':' + str(
            3) + ma_5 + ':' + str(3) + ma_6
        mac_addresses.append(mac_address)
    for i in range(0, 10):
        if i == 3:
            continue
        else:
            mac_address = str(3) + ma_1 + ':' + str(i) + ma_2 + ':' + str(3) + ma_3 + ':' + str(3) + ma_4 + ':' + str(
                3) + ma_5 + ':' + str(3) + ma_6
            mac_addresses.append(mac_address)
    for i in range(0, 10):
        if i == 3:
            continue
        else:
            mac_address = str(3) + ma_1 + ':' + str(3) + ma_2 + ':' + str(i) + ma_3 + ':' + str(3) + ma_4 + ':' + str(
                3) + ma_5 + ':' + str(3) + ma_6
            mac_addresses.append(mac_address)
    for i in range(0, 10):
        if i == 3:
            continue
        else:
            mac_address = str(3) + ma_1 + ':' + str(3) + ma_2 + ':' + str(3) + ma_3 + ':' + str(i) + ma_4 + ':' + str(
                3) + ma_5 + ':' + str(3) + ma_6
            mac_addresses.append(mac_address)
    for i in range(0, 10):
        if i == 1:
            continue
        else:
            mac_address = str(3) + ma_1 + ':' + str(3) + ma_2 + ':' + str(3) + ma_3 + ':' + str(3) + ma_4 + ':' + str(
                i) + ma_5 + ':' + str(3) + ma_6
            mac_addresses.append(mac_address)
    for i in range(0, 10):
        if i == 3:
            continue
        else:
            mac_address = str(3) + ma_1 + ':' + str(3) + ma_2 + ':' + str(3) + ma_3 + ':' + str(3) + ma_4 + ':' + str(
                3) + ma_5 + ':' + str(i) + ma_6
            mac_addresses.append(mac_address)
    for i in range(0, 10):
        mac_address = str(i) + ma_1 + ':' + str(4) + ma_2 + ':' + str(4) + ma_3 + ':' + str(4) + ma_4 + ':' + str(
            4) + ma_5 + ':' + str(4) + ma_6
        mac_addresses.append(mac_address)
    for i in range(0, 10):
        if i == 4:
            continue
        else:
            mac_address = str(4) + ma_1 + ':' + str(i) + ma_2 + ':' + str(4) + ma_3 + ':' + str(4) + ma_4 + ':' + str(
                4) + ma_5 + ':' + str(4) + ma_6
            mac_addresses.append(mac_address)
    for i in range(0, 10):
        if i == 4:
            continue
        else:
            mac_address = str(4) + ma_1 + ':' + str(4) + ma_2 + ':' + str(i) + ma_3 + ':' + str(4) + ma_4 + ':' + str(
                4) + ma_5 + ':' + str(4) + ma_6
            mac_addresses.append(mac_address)
    for i in range(0, 10):
        if i == 4:
            continue
        else:
            mac_address = str(4) + ma_1 + ':' + str(4) + ma_2 + ':' + str(4) + ma_3 + ':' + str(i) + ma_4 + ':' + str(
                4) + ma_5 + ':' + str(4) + ma_6
            mac_addresses.append(mac_address)
    for i in range(0, 10):
        if i == 4:
            continue
        else:
            mac_address = str(4) + ma_1 + ':' + str(4) + ma_2 + ':' + str(4) + ma_3 + ':' + str(4) + ma_4 + ':' + str(
                i) + ma_5 + ':' + str(4) + ma_6
            mac_addresses.append(mac_address)
    for i in range(0, 10):
        if i == 4:
            continue
        else:
            mac_address = str(4) + ma_1 + ':' + str(4) + ma_2 + ':' + str(4) + ma_3 + ':' + str(4) + ma_4 + ':' + str(
                4) + ma_5 + ':' + str(i) + ma_6
            mac_addresses.append(mac_address)
    for mac in mac_addresses:
        print(mac)
    print(len(mac_addresses))


pc_macs = []
printer_macs = []
photocopier_macs = []
scanner_macs = []
router_macs = []


def split_mac_addresses():
    for i in range(0, len(mac_addresses)):
        if i <= 99:
            pc_macs.append(mac_addresses[i])
        if 100 <= i <= 149:
            printer_macs.append(mac_addresses[i])
        if 150 <= i <= 199:
            photocopier_macs.append(mac_addresses[i])
        if 200 <= i <= 236:
            scanner_macs.append(mac_addresses[i])
        if 237 <= i <= 274:
            router_macs.append(mac_addresses[i])

    print('PC MACS :', len(pc_macs))
    print('PRINTER MACS :', len(printer_macs))
    print('PHOTOCOPIER MACS :', len(photocopier_macs))
    print('SCANNER MACS:', len(scanner_macs))
    print('ROUTER MACS :', len(router_macs))


# split_mac_addresses()
pc_names = []


def generate_pc_names():
    for i in range(0, 100):
        pc_name = 'pc' + str(i)
        pc_names.append(pc_name)
    for name in pc_names:
        print(name)


# generate_pc_names()

rams_pool = [4, 8, 16]
# pc_ram = random.choice(rams_pool)
section_ids_pool = ['1', '2', '3', '4']
# pc_section_id = random.choice(section_ids_pool)
windows_licence_pool = ['11', '10', '7']
# pc_windows_licence = random.choice(windows_licence_pool)
office_licence_pool = ['2016', '2019', '2021']
# pc_office_licence = random.choice(office_licence_pool)
cpu_pool = ['AMD', 'INTEL', 'NVIDIA']
# pc_cpu = random.choice(cpu_pool)
arrival_dates_pool = ['2012-01-05', '2011-02-15', '2015-06-05', '2013-07-07', '2009-09-13', '2008-05-04', '2017-01-01']


# pc_arrival_date = random.choice(arrival_dates_pool)
# pc = (mac_addresses[1], pc_names[1], pc_ram, pc_cpu, pc_windows_licence, pc_office_licence, pc_section_id,  pc_arrival_date)

def generate_pcs():
    pcs = []
    global rams_pool
    global section_ids_pool
    global windows_licence_pool
    global office_licence_pool
    global arrival_dates_pool
    global pc_names
    global cpu_pool
    global mac_addresses
    global pc_macs
    generate_mac_addresses()
    split_mac_addresses()
    generate_pc_names()

    for i in range(0, len(pc_macs)):
        pc_ram = random.choice(rams_pool)
        pc_section_id = random.choice(section_ids_pool)
        pc_windows_licence = random.choice(windows_licence_pool)
        pc_office_licence = random.choice(office_licence_pool)
        pc_cpu = random.choice(cpu_pool)
        pc_arrival_date = random.choice(arrival_dates_pool)
        pc = (pc_macs[i], pc_names[i], pc_ram, pc_cpu, pc_windows_licence, pc_office_licence, pc_section_id,
              pc_arrival_date)
        # write_to_excel(pc)
        pcs.append(pc)
    return pcs


def generate_printers():
    printers = []
    global printer_brands_pool
    global section_ids_pool
    global canon_dict
    global hp_dict
    global kyocera_dict
    global printers_arrival_dates_pool
    global mac_addresses
    global printers_ink_storage_pool
    global printer_macs

    # generate_mac_addresses()
    # split_mac_addresses()
    # generate_pc_names()

    for i in range(0, len(printer_macs)):
        printer_brand = random.choice(printer_brands_pool)
        printer_section_id = random.choice(section_ids_pool)
        if printer_brand == 'HP':
            printer_model = hp_dict[random.randint(1, 3)]
        elif printer_brand == 'CANON':
            printer_model = canon_dict[random.randint(1, 3)]
        else:
            printer_model = kyocera_dict[random.randint(1, 3)]
        printer_ink_storage = random.choice(printers_ink_storage_pool)
        printer_arrival_date = random.choice(printers_arrival_dates_pool)
        printer = (printer_macs[i], printer_brand, printer_model, printer_ink_storage, printer_section_id,
                   printer_arrival_date)
        # write_to_excel(pc)
        printers.append(printer)
    return printers


def generate_photocopiers():
    photocopiers = []
    global photocopiers_brands_pool
    global section_ids_pool
    global ricoh_dict
    global sharp_dict
    global toshiba_dict
    global photocopiers_arrival_date_pool
    global photocopier_macs

    # generate_mac_addresses()
    # split_mac_addresses()
    # generate_pc_names()

    for i in range(0, len(photocopier_macs)):
        photocopier_brand = random.choice(photocopiers_brands_pool)
        photocopier_section_id = random.choice(section_ids_pool)
        if photocopier_brand == 'RICOH':
            photocopier_model = ricoh_dict[random.randint(1, 3)]
        elif photocopier_brand == 'SHARP':
            photocopier_model = sharp_dict[random.randint(1, 3)]
        else:
            photocopier_model = toshiba_dict[random.randint(1, 3)]
        photocopier_arrival_date = random.choice(printers_arrival_dates_pool)
        photocopier = (photocopier_macs[i], photocopier_brand, photocopier_model,
                       photocopier_arrival_date, photocopier_section_id)
        # write_to_excel(pc)
        photocopiers.append(photocopier)
    return photocopiers


def generate_scanners():
    scanners = []
    global scanner_brands_pool
    global section_ids_pool
    global kodak_dict
    global panasonic_dict
    global epson_dict
    global scanners_arrival_date_pool
    global scanner_macs

    # generate_mac_addresses()
    # split_mac_addresses()
    # generate_pc_names()

    for i in range(0, len(scanner_macs)):
        scanner_brand = random.choice(scanner_brands_pool)
        scanner_section_id = random.choice(section_ids_pool)
        if scanner_brand == 'KODAK':
            scanner_model = kodak_dict[random.randint(1, 3)]
        elif scanner_brand == 'EPSON':
            scanner_model = epson_dict[random.randint(1, 3)]
        else:
            scanner_model = panasonic_dict[random.randint(1, 3)]
        scanner_arrival_date = random.choice(scanners_arrival_date_pool)
        scanner = (scanner_macs[i], scanner_brand, scanner_model,
                   scanner_arrival_date, scanner_section_id)
        # write_to_excel(pc)
        scanners.append(scanner)
    return scanners


def generate_routers():
    routers = []
    global router_brands_pool
    global section_ids_pool
    global abocom_dict
    global addon_dict
    global acer_dict
    global routers_arrival_dates_pool
    global router_macs

    # generate_mac_addresses()
    # split_mac_addresses()
    # generate_pc_names()

    for i in range(0, len(router_macs)):
        router_brand = random.choice(router_brands_pool)
        router_section_id = random.choice(section_ids_pool)
        if router_brand == 'ABOCOM':
            router_model = abocom_dict[random.randint(1, 3)]
        elif router_brand == 'ADDON':
            router_model = addon_dict[random.randint(1, 3)]
        else:
            router_model = acer_dict[random.randint(1, 3)]
        router_arrival_date = random.choice(routers_arrival_dates_pool)
        router = (router_macs[i], router_section_id, router_brand, router_model,
                  router_arrival_date)
        # write_to_excel(pc)
        routers.append(router)
    return routers


# PC REPAIRS
pc_repairs_pool = ['CPU REPAIR', 'GPU REPAIR', 'SCREEN REPAIR']
cpu_repairs_description_pool = ['CHANGED INNER CIRCUIT', 'REFRESHED COOL SYSTEM', 'CHANGED CPU']
gpu_repairs_description_pool = ['CHANGED INNER CIRCUIT', 'CHANGED CONDUIT ', 'CHANGED GPU']
screen_repair_description_pool = ['CHANGED FRONT END OF SCREEN', 'CHANGED INNER CIRCUIT', 'CHANGED SCREEN']
repair_dates_pool = ['18-7/2022', '20/7/2021', '12/11/2020', '7/7/2019', '21/8/2022', '1/1/2021', '5/7/2018']

# PC UPDATES
pc_updates_pool = ['UPDATED WINDOWS', 'UPDATED OFFICE', 'UPDATED INFORMATIVE SYSTEM']
windows_updates_pool = ['TO WINDOWS 10', 'TO WINDOWS 11']
office_updates_pool = ['TO 2019', 'TO 2021']
windows_updates_description_pool = ['TO 2019 FOR COMPATIBILITY', 'TO 2021 FOR COMPATIBILITY']
update_dates_pool = ['26/3/2022', '7/8/2024', '15/8/2020', '2/6/2018', '6/6/2022', '25/11/2023']

# PRINTERS
printer_brands_pool = ['HP', 'CANON', 'KYOCERA']
canon_dict = {
    1: 'G540',
    2: 'TM-300',
    3: 'G640'
}
hp_dict = {
    1: 'LASERJET',
    2: 'TANK-670',
    3: 'T230'
}
kyocera_dict = {
    1: 'M8130',
    2: 'P3045',
    3: 'M2540'
}
# canon_models = ['G540', 'TM-300', 'G640']
# hp_models = ['LASERJET', 'TANK-670', 'T230']
# kyocera_models = ['M8130', 'P3045', 'M2540']
printers_arrival_dates_pool = ['2011-04-03', '2013-07-15', '2012-09-06', '2017-07-06', '2014-03-03', '2017-09-05',
                               '2010-06-06']
printers_ink_storage_pool = [3, 4, 5]

# PRINTERS REPAIRS
printer_repairs_pool = ['CHANGED INK MECHANISM', 'CHANGED ACCESSORIES', 'CHANGED PRINTER']
printer_repairs_description_pool = ['INK MECHANISM BURNED', 'FIXED PLASTICS AFTER CRASH']
printer_repairs_dates_pool = ['14/2/2020', '8/10/2022', '19/11/2021']

# PHOTOCOPIERS
photocopiers_brands_pool = ['RICOH', 'SHARP', 'TOSHIBA']
ricoh_dict = {
    1: 'IM 2702',
    2: 'MP 650',
    3: 'MP 505'
}
sharp_dict = {
    1: 'BS 500',
    2: 'BWS 50',
    3: 'RAPID SPEED'
}
toshiba_dict = {
    1: '1500C',
    2: 'C2244E',
    3: 'EAZ42'
}
# ricoh_models = ['IM 2702', 'MP 650', 'MP 505']
# sharp_models = ['BS 500', 'BWS 50', 'RAPID SPEED']
# toshiba_models = ['1500C', 'C2244E', 'EAZ42']
photocopiers_arrival_date_pool = ['2011-06-05', '2012-07-06', '2014-10-09', '2012-01-01', '2013-08-07', '2017-04-03',
                                  '2015-09-17']

# PHOTOCOPIERS REPAIRS
photocopiers_repairs_pool = ['CHANGED SCREEN', 'CHANGED LASER CIRCUIT', 'CHANGED PHOTOCOPIER']
photocopiers_repairs_description_pool = ['CHANGED TOUCH SCREEN', 'CHANGED INNER LASER CIRCUIT']
photocopiers_repairs_dates_pool = ['11/3/2020', '7/12/2022', '25/3/2021', '5/8/2022', '7/7/2023', '1/3/2019']

# SCANNERS
scanner_brands_pool = ['KODAK', 'EPSON', 'PANASONIC']
kodak_dict = {
    1: 'SZ32',
    2: 'POWER FORM4',
    3: 'T789'
}
epson_dict = {
    1: 'K1',
    2: 'ULTRA SCAN',
    3: 'MN7000'
}
panasonic_dict = {
    1: 'SS345',
    2: 'GF890',
    3: 'SMN 4'
}
# kodak_models = ['SZ32', 'POWER FORM4', 'T789']
# epson_models = ['K1', 'ULTRA SCAN', 'MN7000']
# panasonic_models = ['SS345', 'GF890', 'SMN 4']
scanners_arrival_date_pool = ['2011-02-01', '2016-07-06', '2017-08-05', '2013-02-01', '2016-12-16', '2014-06-15']

# SCANNERS REPAIRS
scanners_repairs_pool = ['CHANGED SCREEN', 'CHANGED LASER CIRCUIT', 'CHANGED PHOTOCOPIER']
scanners_repairs_description_pool = ['CHANGED TOUCH SCREEN', 'CHANGED INNER LASER CIRCUIT']
scanners_repairs_dates_pool = ['8/9/2020', '12/2/2022', '9/3/2021', '5/8/2023', '19/11/2023']

# ROUTERS
router_brands_pool = ['ABOCOM', 'ADDON', 'ACER']
abocom_dict = {
    1: 'EZ GG',
    2: 'WS32',
    3: 'FFX1'
}
addon_dict = {
    1: 'KLX 550',
    2: 'YZF 30',
    3: 'TMS35'
}
acer_dict = {
    1: 'ADX 56',
    2: 'EX1',
    3: 'ZZ ROT'
}
# abocom_models = ['EZ GG', 'WS32', 'FFX1']
# addon_models = ['KLX 550', 'YZF 30', 'TMS35']
# acer_models = ['ADX 56', 'EX1', 'ZZ ROT']
routers_arrival_dates_pool = ['2015-07-08', '2012-03-02', '2016-05-22', '2014-02-01', '2013-07-06']

# ROUTERS REPAIRS
routers_repairs_pool = ['CHANGED CIRCUIT', 'CHANGED ROUTER']
routers_repairs_description_pool = ['CURCUIT CHANGED AFTER BURNED']
routers_repairs_date_pool = ['5/8/2018', '17/9/2021', '17/9/2022', '20/3/2017', '7/8/2022', '7/9/2016']






# def get_pcs():
#    pcs = generate_pcs()

# main_workbook = Workbook()
# pc_ws = main_workbook.active
#
# pc_ws.append(
#     ["Mac Address", "PC Name", "RAM", "CPU", "Windows Licence", "Office Licence", "Section ID", "Arrival Date"])
#
# for col in range(1, 9):
#     pc_ws[get_column_letter(col) + '1'].font = Font(bold=True)
# main_workbook.save("C:\\Users\\nikas\\Desktop\\PC`s.xlsx")
#

# def write_mac_address(mac_address, iterator):
#     should_exit = False
#     for row in pc_ws.iter_rows(min_row=iterator, max_row=iterator, min_col=1, max_col=1):
#         for cell in row:
#             if cell.value in [None, '']:
#                 cell.value = mac_address
#                 should_exit = True
#                 break
#         if should_exit:
#             break
#
#
# def write_pc_name(pc_name, iterator):
#     should_exit = False
#     for row in pc_ws.iter_rows(min_row=iterator, max_row=iterator, min_col=2, max_col=2):
#         for cell in row:
#             if cell.value in [None, '']:
#                 cell.value = pc_name
#                 should_exit = True
#                 break
#         if should_exit:
#             break
#
#
# def write_ram(ram, iterator):
#     should_exit = False
#     for row in pc_ws.iter_rows(min_row=iterator, max_row=iterator, min_col=3, max_col=3):
#         for cell in row:
#             if cell.value in [None, '']:
#                 cell.value = ram
#                 should_exit = True
#                 break
#         if should_exit:
#             break
#
#
# def write_cpu(pc_cpu, iterator):
#     should_exit = False
#     for row in pc_ws.iter_rows(min_row=iterator, max_row=iterator, min_col=4, max_col=4):
#         for cell in row:
#             if cell.value in [None, '']:
#                 cell.value = pc_cpu
#                 should_exit = True
#                 break
#         if should_exit:
#             break
#
#
# def write_windows_licence(pc_windows_licence, iterator):
#     should_exit = False
#     for row in pc_ws.iter_rows(min_row=iterator, max_row=iterator, min_col=5, max_col=5):
#         for cell in row:
#             if cell.value in [None, '']:
#                 cell.value = pc_windows_licence
#                 should_exit = True
#                 break
#         if should_exit:
#             break
#
#
# def write_office_licence(pc_office_licence, iterator):
#     should_exit = False
#     for row in pc_ws.iter_rows(min_row=iterator, max_row=iterator, min_col=6, max_col=6):
#         for cell in row:
#             if cell.value in [None, '']:
#                 cell.value = pc_office_licence
#                 should_exit = True
#                 break
#         if should_exit:
#             break
#
#
# def write_section_id(pc_section_id, iterator):
#     should_exit = False
#     for row in pc_ws.iter_rows(min_row=iterator, max_row=iterator, min_col=7, max_col=7):
#         for cell in row:
#             if cell.value in [None, '']:
#                 cell.value = pc_section_id
#                 should_exit = True
#                 break
#         if should_exit:
#             break
#
#
# def write_arrival_date(pc_arrival_date, iterator):
#     should_exit = False
#     for row in pc_ws.iter_rows(min_row=iterator, max_row=iterator, min_col=8, max_col=8):
#         for cell in row:
#             if cell.value in [None, '']:
#                 cell.value = pc_arrival_date
#                 should_exit = True
#                 break
#         if should_exit:
#             break
#
#
# iterator = 1
#
#
# def write_to_excel(element):
#     global iterator
#     write_mac_address(element[0], iterator)
#     write_pc_name(element[1], iterator)
#     write_ram(element[2], iterator)
#     write_cpu(element[3], iterator)
#     write_windows_licence(element[4], iterator)
#     write_office_licence(element[5], iterator)
#     write_section_id(element[6], iterator)
#     write_arrival_date(element[7], iterator)
#     main_workbook.save("C:\\Users\\nikas\\Desktop\\PC`s.xlsx")
#     iterator = iterator + 1
#

# generate_pcs()

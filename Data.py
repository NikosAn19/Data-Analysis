import random
import string
from datetime import datetime, timedelta


def random_pc_string(length=8):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))


pc_macs = []
printer_macs = []
photocopier_macs = []
scanner_macs = []
router_macs = []

pc_data_computing = []
printer_data_computing = []
photocopier_data_computing = []
scanner_data_computing = []
router_data_computing = []


def random_pc_mac():
    return "02:00:00:%02x:%02x:%02x" % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )


def random_pc_date(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())),
    )


def generate_pc_data(num_records):
    global pc_macs
    pc_data = []
    global pc_data_computing
    start_date = datetime(2010, 1, 1)
    end_date = datetime(2023, 12, 31)

    for i in range(num_records):
        mac_address = random_pc_mac()
        pc_macs.append(mac_address)
        pc_name = random_pc_string(10)
        ram = random.choice([4, 8, 16, 32, 64])
        windows_licence = random.choice([True, False])
        office_licence = random.choice([True, False])
        cpu = random.choice(['i3', 'i5', 'i7', 'i9', 'Ryzen 3', 'Ryzen 5', 'Ryzen 7', 'Ryzen 9'])
        section_id = random.randint(1, 4)
        arrival_date = random_pc_date(start_date, end_date)

        pc = (mac_address, pc_name, ram, windows_licence, office_licence, cpu, section_id, arrival_date)
        pc_data.append(pc)
        pc_data_computing.append({
            'mac_address': mac_address,
            'pc_name': pc_name,
            'ram': ram,
            'windows_licence': windows_licence,
            'office_licence': office_licence,
            'cpu': cpu,
            'section_id': section_id,
            'arrival_date': arrival_date.strftime('%Y-%m-%d')
        })

    return pc_data



# Generate 100 records for example
# pc_records = generate_pc_data(100)


# for record in pc_records:
#     print(record)

def random_printer_string(length=8):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))


def random_printer_mac():
    return "03:00:00:%03x:%03x:%03x" % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )


def random_printer_date(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())),
    )


def generate_printer_data(num_records):
    global printer_data_computing
    printer_data = []
    start_date = datetime(2010, 1, 1)
    end_date = datetime(2023, 12, 31)

    brands = ['HP', 'Canon', 'Epson', 'Brother', 'Samsung']
    models = ['LaserJet', 'DeskJet', 'Pixma', 'EcoTank', 'HL-L']

    for i in range(num_records):
        mac_address = random_printer_mac()
        printer_macs.append(mac_address)
        brand = random.choice(brands)
        model = random.choice(models) + " " + str(random.randint(100, 999))
        ink_storage = random.choice([True, False])
        section_id = random.randint(1, 4)
        arrival_date = random_printer_date(start_date, end_date)

        printer = (mac_address, brand, model, ink_storage, section_id, arrival_date.strftime('%Y-%m-%d'))
        printer_data.append(printer)
        printer_data_computing.append({
            'mac_address': mac_address,
            'brand': brand,
            'model': model,
            'ink_storage': ink_storage,
            'section_id': section_id,
            'arrival_date': arrival_date.strftime('%Y-%m-%d')
        })

    return printer_data


# Generate 100 records for example
# printer_records = generate_printer_data(100)

# for record in printer_records:
#     print(record)


def random_photocopier_string(length=8):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))


def random_photocopier_mac():
    return "04:00:00:%04x:%04x:%04x" % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )


def random_photocopier_date(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())),
    )


def generate_photocopier_data(num_records):
    global photocopier_data_computing
    photocopier_data = []
    start_date = datetime(2010, 1, 1)
    end_date = datetime(2023, 12, 31)

    brands = ['Xerox', 'Ricoh', 'Konica Minolta', 'Brother', 'Canon']
    models = ['WorkCentre', 'Aficio', 'Bizhub', 'DCP', 'ImageRunner']

    for i in range(num_records):
        mac_address = random_photocopier_mac()
        photocopier_macs.append(mac_address)
        brand = random.choice(brands)
        model = random.choice(models) + " " + str(random.randint(1000, 9999))
        section_id = random.randint(1, 4)
        arrival_date = random_photocopier_date(start_date, end_date)
        photocopier = (mac_address, brand, model,  arrival_date.strftime('%Y-%m-%d'), section_id)
        photocopier_data.append(photocopier)
        photocopier_data_computing.append({
            'mac_address': mac_address,
            'brand': brand,
            'model': model,
            'section_id': section_id,
            'arrival_date': arrival_date.strftime('%Y-%m-%d')
        })

    return photocopier_data


# Generate 100 records for example
# photocopier_records = generate_photocopier_data(100)

# for record in photocopier_records:
#     print(record)


def random_string(length=8):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))


def random_scanner_mac():
    return "05:00:00:%05x:%05x:%05x" % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )


def random_scanner_date(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())),
    )


def generate_scanner_data(num_records):
    global scanner_data_computing
    scanner_data = []
    start_date = datetime(2010, 1, 1)
    end_date = datetime(2023, 12, 31)

    brands = ['Canon', 'Epson', 'Fujitsu', 'HP', 'Brother']
    models = ['ScanJet', 'Perfection', 'ScanSnap', 'ImageCenter', 'DCP']

    for i in range(num_records):
        mac_address = random_scanner_mac()
        scanner_macs.append(mac_address)
        brand = random.choice(brands)
        model = random.choice(models) + " " + str(random.randint(1000, 9999))
        section_id = random.randint(1, 4)
        arrival_date = random_scanner_date(start_date, end_date)
        scanner = (mac_address, brand, model, arrival_date.strftime('%Y-%m-%d'), section_id)
        scanner_data.append(scanner)

        scanner_data_computing.append({
            'mac_address': mac_address,
            'brand': brand,
            'model': model,
            'section_id': section_id,
            'arrival_date': arrival_date.strftime('%Y-%m-%d')
        })

    return scanner_data


# Generate 100 records for example
# scanner_records = generate_scanner_data(100)

# for record in scanner_records:
#     print(record)


def random_router_string(length=8):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))


def random_router_mac():
    return "06:00:00:%06x:%06x:%06x" % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )


def random_router_date(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())),
    )


def generate_router_data(num_records):
    global router_data_computing
    router_data = []
    start_date = datetime(2010, 1, 1)
    end_date = datetime(2023, 12, 31)

    brands = ['Netgear', 'TP-Link', 'Linksys', 'Asus', 'D-Link']
    models = ['Nighthawk', 'Archer', 'Max-Stream', 'RT-AC', 'DIR']

    for i in range(num_records):
        mac_address = random_router_mac()
        router_macs.append(mac_address)
        brand = random.choice(brands)
        model = random.choice(models) + " " + str(random.randint(100, 999))
        section_id = random.randint(1, 4)
        arrival_date = random_router_date(start_date, end_date)
        router = (mac_address, section_id, brand, model, arrival_date.strftime('%Y-%m-%d'))
        router_data.append(router)

        router_data_computing.append({
            'mac_address': mac_address,
            'brand': brand,
            'model': model,
            'section_id': section_id,
            'arrival_date': arrival_date.strftime('%Y-%m-%d')
        })

    return router_data


# Generate 100 records for example
# router_records = generate_router_data(100)

# for record in router_records:
#     print(record)


def random_date(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())),
    )


def generate_pc_repair_data(num_records):
    global pc_data_computing
    repair_data = []
    repair_types = ['Hardware Fix', 'Software Update', 'Virus Removal', 'OS Reinstallation', 'Component Replacement']
    descriptions = [
        'Fixed hardware issues',
        'Updated software',
        'Removed viruses and malware',
        'Reinstalled operating system',
        'Replaced faulty components'
    ]

    used_macs = set()

    i = 0
    while len(repair_data) < num_records:

        pc = pc_data_computing[i]
        mac_address = pc['mac_address']
        print('Mac = ', mac_address)
        if mac_address in used_macs:
            i = i + 1
            continue

        repair = random.choice(repair_types)
        arrival_date = datetime.strptime(pc['arrival_date'], '%Y-%m-%d')
        date = random_date(arrival_date, datetime(2023, 12, 31))
        repair_description = random.choice(descriptions)
        pc_repair = (mac_address, repair, date, repair_description)

        repair_data.append(pc_repair)
        used_macs.add(mac_address)
        i = i + 1

    for item in pc_data_computing:
        print(item)
    for item2 in repair_data:
        print(item2)
    return repair_data


# Generate 100 records for PC_REPAIR
# pc_repair_records = generate_pc_repair_data(70)

# for record in pc_repair_records:
#     print(record)


def generate_pc_update_data(num_records):
    global pc_data_computing
    update_data = []
    update_types = ['Security Patch', 'Software Upgrade', 'Driver Update', 'OS Update', 'Firmware Update']
    descriptions = [
        'Applied security patch',
        'Upgraded software to latest version',
        'Updated drivers for better performance',
        'Updated operating system to latest version',
        'Updated firmware for better stability'
    ]

    used_macs = set()

    while len(update_data) < num_records:
        pc = random.choice(pc_data_computing)
        mac_address = pc['mac_address']
        if mac_address in used_macs:
            continue

        update = random.choice(update_types)
        arrival_date = datetime.strptime(pc['arrival_date'], '%Y-%m-%d')
        date = random_date(arrival_date, datetime(2023, 12, 31))
        update_description = random.choice(descriptions)
        pc_update = (mac_address, update, date, update_description)
        update_data.append(pc_update)
        used_macs.add(mac_address)

    return update_data


# Generate 100 records for PC_UPDATE
# pc_update_records = generate_pc_update_data(100)

# for record in pc_update_records:
#     print(record)


def generate_printer_repair_data(num_records):
    global printer_data_computing
    repair_data = []
    repair_types = ['Paper Jam Fix', 'Ink Cartridge Replacement', 'Hardware Repair', 'Software Update',
                    'Network Issue Fix']
    descriptions = [
        'Fixed paper jam issues',
        'Replaced ink cartridges',
        'Repaired hardware components',
        'Updated printer software',
        'Fixed network connectivity issues'
    ]

    used_macs = set()

    while len(repair_data) < num_records:
        printer = random.choice(printer_data_computing)
        mac_address = printer['mac_address']
        if mac_address in used_macs:
            continue

        repair = random.choice(repair_types)
        arrival_date = datetime.strptime(printer['arrival_date'], '%Y-%m-%d')
        date = random_date(arrival_date, datetime(2023, 12, 31))
        repair_description = random.choice(descriptions)
        printer = (mac_address, repair, date, repair_description)
        repair_data.append(printer)
        used_macs.add(mac_address)

    return repair_data


# Generate 100 records for PRINTER_REPAIR
# printer_repair_records = generate_printer_repair_data(70)

# for record in printer_repair_records:
#     print(record)


def generate_photocopier_repair_data(num_records):
    global photocopier_data_computing
    repair_data = []
    repair_types = ['Paper Jam Fix', 'Toner Replacement', 'Hardware Repair', 'Software Update', 'Network Issue Fix']
    descriptions = [
        'Fixed paper jam issues',
        'Replaced toner',
        'Repaired hardware components',
        'Updated photocopier software',
        'Fixed network connectivity issues'
    ]

    used_macs = set()

    while len(repair_data) < num_records:
        photocopier = random.choice(photocopier_data_computing)
        mac_address = photocopier['mac_address']
        if mac_address in used_macs:
            continue

        repair = random.choice(repair_types)
        arrival_date = datetime.strptime(photocopier['arrival_date'], '%Y-%m-%d')
        date = random_date(arrival_date, datetime(2023, 12, 31))
        repair_description = random.choice(descriptions)
        photocopier_repair = (mac_address, repair, date, repair_description)
        repair_data.append(photocopier_repair)
        used_macs.add(mac_address)

    return repair_data


# Generate 100 records for PHOTOCOPIER_REPAIR
# photocopier_repair_records = generate_photocopier_repair_data(100)

# for record in photocopier_repair_records:
#     print(record)


def generate_scanner_repair_data(num_records):
    global scanner_data_computing
    repair_data = []
    repair_types = ['Glass Cleaning', 'Software Update', 'Hardware Repair', 'Driver Update', 'Network Issue Fix']
    descriptions = [
        'Cleaned scanner glass',
        'Updated scanner software',
        'Repaired hardware components',
        'Updated scanner drivers',
        'Fixed network connectivity issues'
    ]

    used_macs = set()

    while len(repair_data) < num_records:
        scanner = random.choice(scanner_data_computing)
        mac_address = scanner['mac_address']
        if mac_address in used_macs:
            continue

        repair = random.choice(repair_types)
        arrival_date = datetime.strptime(scanner['arrival_date'], '%Y-%m-%d')
        date = random_date(arrival_date, datetime(2023, 12, 31))
        repair_description = random.choice(descriptions)
        scanner_repair = (mac_address, repair, date, repair_description)
        repair_data.append(scanner_repair)
        used_macs.add(mac_address)

    return repair_data


# Generate 100 records for SCANNER_REPAIR
# scanner_repair_records = generate_scanner_repair_data(100)

# for record in scanner_repair_records:
#     print(record)


def generate_router_repair_data(num_records):
    global router_data_computing
    repair_data = []
    repair_types = ['Firmware Update', 'Network Issue Fix', 'Hardware Repair', 'Software Update', 'Configuration Reset']
    descriptions = [
        'Updated router firmware',
        'Fixed network connectivity issues',
        'Repaired hardware components',
        'Updated router software',
        'Reset router configuration'
    ]

    used_macs = set()

    while len(repair_data) < num_records:
        router = random.choice(router_data_computing)
        mac_address = router['mac_address']
        if mac_address in used_macs:
            continue

        repair = random.choice(repair_types)
        arrival_date = datetime.strptime(router['arrival_date'], '%Y-%m-%d')
        date = random_date(arrival_date, datetime(2023, 12, 31))
        repair_description = random.choice(descriptions)
        router_repair = (mac_address, repair, date, repair_description)
        repair_data.append(router_repair)
        used_macs.add(mac_address)

    return repair_data


# Generate 100 records for ROUTER_REPAIR
# router_repair_records = generate_router_repair_data(100)
#
# for record in router_repair_records:
#     print(record)


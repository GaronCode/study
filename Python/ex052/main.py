from directory import G_directory

dir = G_directory('Book_1')
dir2 = G_directory('test')
dir.add_record('Иван Васильич', '+7 999 999 99 99')
dir.add_record('aВасильич', '+7 799 999 99 99')

dir2.import_xml_str(dir.export_xml_str())
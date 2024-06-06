# write() #writelines()
arquivo = open('new_file.txt', 'w', encoding='utf-8')

arquivo.write("Escrevendo no arquivo com write utf-8 çáôõ")

arquivo.writelines("\ntestando writelines\n")

arquivo.writelines(["nova\n","escrita\n","no\n",
                    "arquivo\n","com\n","writelines\n"])

print(f"Escrita concluída no arquivo: {arquivo.name}")
arquivo.close()
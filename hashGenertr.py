import hashlib
from hashlib import blake2b
from hashlib import blake2s
import pyfiglet
import time


class HashGenerator:

    resultAsc = pyfiglet.figlet_format("HASH GENERATOR +/*")
    print(resultAsc)

    def __int__(self):
        print("Hash Generator Initialize....")


    def chooseOptions(self):


        time.sleep(1)


        while 1==1:

            print("""

                    [1].Password Hashing 
                    [2].File Hashing
                    [3].Help 
                    [4].Show Options
                    [5].Exit

                    """)


            options = input("Select Options >>> ")



            if options.lower() == "use 1" or options == "1":

                time.sleep(1)



                while 1==1:

                    print("ENCRYPTION ALGORITHMS")
                    print("""
                                    [1].md5
                                    [2].sha-256
                                    [3].sha-384
                                    [4].sha-512
                                    [5].BLAKE2
                                    [6].Help
                                    [7].Show options
                                    [8].Exit
                                    """)


                    chose = input("Select Options >>> ")


                    time.sleep(1)

                    if chose.lower() == "use 1" or chose == "1":

                        word = input("Enter a word >>> ")
                        word = bytearray(word,'utf8')
                        lockword = hashlib.md5()
                        lockword.update(word)


                        print("Your character encrypted with MD5 => {} ".format(lockword.hexdigest()))
                        time.sleep(7)





                    if chose.lower() == "use 2" or chose == "2":

                        word = input("Enter a word >>> ")
                        word = bytearray(word, 'utf8')
                        lockword = hashlib.sha256()
                        lockword.update(word)

                        print("Your character encrypted with SHA-256 => {} ".format(lockword.hexdigest()))
                        time.sleep(7)




                    if chose.lower() == "use 3" or chose == "3":

                        word = input("Enter a word >>> ")
                        word = bytearray(word, 'utf8')
                        lockword = hashlib.sha384()
                        lockword.update(word)

                        print("Your character encrypted with SHA3384 => {} ".format(lockword.hexdigest()))
                        time.sleep(7)



                    if chose.lower() == "use 4" or chose == "4":


                        word = input("Enter a word >>> ")
                        word = bytearray(word, 'utf8')
                        lockword = hashlib.sha512()
                        lockword.update(word)

                        print("Your character encrypted with SHA-512 => {} ".format(lockword.hexdigest()))
                        time.sleep(7)



                    if chose.lower() == "use 5" or chose == "5":

                        print("""
                        [1].Blake2b
                        [2].Blake2s
                        [3].Exit
                        """)

                        time.sleep(1)

                        while 1==1:

                            opts = input("Select Options(Encryption Algorithms) >>> ")

                            time.sleep(1)

                            if opts.lower() == "use 1" or opts == "1":

                                word = input("Enter a word >>> ")
                                word = bytearray(word, 'utf8')
                                lockword = blake2b()
                                lockword.update(word)

                                print("Your character encrypted with BLAKE2B => {} ".format(lockword.hexdigest()))
                                time.sleep(7)



                            if opts.lower() == "use 2" or opts == "2":

                                word = input("Enter a word >>> ")
                                word = bytearray(word, 'utf8')
                                lockword = blake2s()
                                lockword.update(word)

                                print("Your character encrypted with BLAKE2S => {} ".format(lockword.hexdigest()))
                                time.sleep(7)

                            if opts.lower() == "exit":
                                break





                    if chose.lower() == "use 6" or chose == "6":

                        print("""
                            >>> You can use it by placing the use keyword in front of the number you want to select. <<<

                            Exam => use 1 
                            Exam => use 2 
                            
                        """)


                    if chose.lower() == "use 7" or chose == "7":

                        print("ENCRYPTION ALGORITHMS")
                        print("""
                        [1].md5
                        [2].sha-256
                        [3].sha-384
                        [4].sha-512
                        [5].BLAKE2
                        [6].Help
                        [7].Show options
                        [8].Exit
                        """)

                    if chose.lower() == "exit":
                        break
                        



            if options.lower() == "use 2" or options == "2":

                #print("Exam => /home/kali/downloads ")
                filename = input("Enter the filename: ")

                try:
                    with open(filename, 'rb') as file:
                        chunk = file.read()
                        lockword = None


                except FileNotFoundError:
                    print("File not found!")
                    exit()


                while True:
                    print("ENCRYPTION ALGORITHMS")
                    print("""
                    [1].md5
                    [2].sha-256
                    [3].sha-512
                    [4].Exit
                    """)

                    option = input("Enter an option (Encryption Algorithms): ")

                    if option.lower() == "use 1" or option == "1":
                        lockword = hashlib.md5(chunk)


                    if option.lower() == "use 2" or option == "2":
                        lockword = hashlib.sha256(chunk)


                    if option.lower() == "use 3" or option == "3":
                        lockword = hashlib.sha512(chunk)


                    if option.lower() == "exit" or option == "4":
                        break

                    else:
                        print("Invalid option.")
                        continue

                    if lockword:
                        print("Your file encrypted with {} => {}".format(lockword.name, lockword.hexdigest()))



            if options.lower() == "use 3" or options == "3":
                print("""
                
                >>> You can use it by placing the use keyword in front of the number you want to select. <<<
                
                Exam => use 1 
                Exam => use 2 
                
                Exam => exit
                
                """)

                time.sleep(10)


            if options.lower() == "use 4" or options == "4":
                print("""

                       [1].Password Hashing 
                       [2].File Hashing
                       [3].Help 
                       [4].Show Options

                """)


            if options.lower() == "exit" or options == "5":
                break





hashgen = HashGenerator()
hashgen.resultAsc
hashgen.chooseOptions()
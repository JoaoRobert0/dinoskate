with open('DINOsc5.asm', 'a') as arquivo:
    l = [508, 1020, 1532, 2044, 2556, 3068, 3580, 4092, 4604, 5116, 5628, 6140, 6652, 7164, 7676, 8188, 8700, 9212, 9724, 10236, 10748, 11260, 11772, 12284, 12796, 13308, 13820, 14332, 14844, 15356, 15868, 16380, 16892, 17404, 17916, 18428, 18940, 19452, 19964, 20476, 20988, 21500, 22012, 22524, 23036, 23548, 24060, 24572, 25084]

    arquivo.write(
        f".text
        \nlui $t9, 0x1001
        \n#COLOR PALETTE
        \naddi $t0, $zero, 0X0049B6CD #Dark Cyan
        \naddi $t1, $zero, 0X007BDCED #Cyan
        \naddi $t2, $zero, 0X00B4FAFC #Light Cyan
        \naddi $t3, $zero, 0X00930004 #Dark Red
        \naddi $t4, $zero, 0X00C7041F #Ligth Red
        \naddi $t5, $zero, 0X00000000 #Black
        \naddi $t6, $zero, 0X00FFFD00 #Yellow
        \n\n"
        )

    for i in range(128, -1, -1):
        arquivo.write(f"        sw $t0, {str(l[0])}($t9) #Column{str(i)}\n")
        arquivo.write(f"        sw $t0, {str(l[1])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[2])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[3])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[4])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[5])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[6])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[7])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[8])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[9])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[10])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[11])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[12])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[13])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[14])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[15])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[16])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[17])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[18])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[19])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[20])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[21])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[22])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[23])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[24])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[25])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[26])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[27])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[28])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[29])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[30])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[31])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[32])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[33])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[34])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[35])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[36])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[37])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[38])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[39])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[40])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[41])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[42])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[43])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[44])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[45])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[46])}($t9)\n")
        arquivo.write(f"        sw $t0, {str(l[47])}($t9)\n\n")

        for j in range(0, len(l)):
            l[j] = l[j] - 4
import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def main():
    print("Program: Remove Duplicates")
    print("Release: 0.1.0")
    print("Date: 2019-10-15")
    print("Author: Brian Neely")
    print()
    print()
    print("This program reads a csv file remove duplicates.")
    print()
    print()

    # Hide Tkinter GUI
    Tk().withdraw()

    # Find input file
    file_in = select_file_in()

    # Ask for delimination
    delimination = input("Enter Deliminator: ")

    # Open input csv using the unknown encoder function
    print()
    print("Opening File: {" + file_in + "}...")
    data = open_unknown_csv(file_in, delimination)
    print(file_in + " Opened!")

    # Confirm remove duplicates
    print()
    if y_n_question("Proceed with removing of duplicates (y/n): "):
        # Set output file
        print()
        print("Setting output file...")
        file_out = select_file_out(file_in)

        # Number of rows
        n_rows_orig = data.shape[0]
        print()
        print("Number of rows: " + str(n_rows_orig))

        # Drop Duplicates
        print()
        print("Dropping Duplicates")
        data.drop_duplicates(inplace=True)

        # Number of duplicates dropped
        n_rows_new = data.shape[0]
        print()
        print("Number of duplicate rows dropped: " + str(n_rows_orig - n_rows_new))
        print("Remaining rows: " + str(n_rows_new))

        # Writing output file
        print()
        print("Writing output file...")
        data.to_csv(file_out, index=False)
        print("Output file wrote!")

        input("Program Ended Successfully. Press Enter to continue...")

    else:
        input("Program Terminated. Press Enter to continue...")
        exit()


def select_file_in():
    file_in = askopenfilename(initialdir="../", title="Select file",
                              filetypes=(("Comma Separated Values", "*.csv"), ("all files", "*.*")))
    if not file_in:
        input("Program Terminated. Press Enter to continue...")
        exit()

    return file_in


def select_file_out(file_in):
    file_out = asksaveasfilename(initialdir=file_in, title="Select file",
                                 filetypes=(("Comma Separated Values", "*.csv"), ("all files", "*.*")))
    if not file_out:
        input("Program Terminated. Press Enter to continue...")
        exit()

    # Create an empty output file
    open(file_out, 'a').close()

    return file_out


def y_n_question(question):
    while True:
        # Ask question
        answer = input(question)
        answer_cleaned = answer[0].lower()
        if answer_cleaned == 'y' or answer_cleaned == 'n':
            return answer_cleaned
        else:
            print("Invalid input, please try again.")


def open_unknown_csv(file_in, delimination):
    encode_index = 0
    encoders = ['utf_8', 'latin1', 'utf_16',
                'ascii', 'big5', 'big5hkscs', 'cp037', 'cp424',
                'cp437', 'cp500', 'cp720', 'cp737', 'cp775',
                'cp850', 'cp852', 'cp855', 'cp856', 'cp857',
                'cp858', 'cp860', 'cp861', 'cp862', 'cp863',
                'cp864', 'cp865', 'cp866', 'cp869', 'cp874',
                'cp875', 'cp932', 'cp949', 'cp950', 'cp1006',
                'cp1026', 'cp1140', 'cp1250', 'cp1251', 'cp1252',
                'cp1253', 'cp1254', 'cp1255', 'cp1256', 'cp1257',
                'cp1258', 'euc_jp', 'euc_jis_2004', 'euc_jisx0213', 'euc_kr',
                'gb2312', 'gbk', 'gb18030', 'hz', 'iso2022_jp',
                'iso2022_jp_1', 'iso2022_jp_2', 'iso2022_jp_2004', 'iso2022_jp_3', 'iso2022_jp_ext',
                'iso2022_kr', 'latin_1', 'iso8859_2', 'iso8859_3', 'iso8859_4',
                'iso8859_5', 'iso8859_6', 'iso8859_7', 'iso8859_8', 'iso8859_9',
                'iso8859_10', 'iso8859_11', 'iso8859_13', 'iso8859_14', 'iso8859_15',
                'iso8859_16', 'johab', 'koi8_r', 'koi8_u', 'mac_cyrillic',
                'mac_greek', 'mac_iceland', 'mac_latin2', 'mac_roman', 'mac_turkish',
                'ptcp154', 'shift_jis', 'shift_jis_2004', 'shift_jisx0213', 'utf_32',
                'utf_32_be', 'utf_32_le', 'utf_16', 'utf_16_be', 'utf_16_le',
                'utf_7', 'utf_8', 'utf_8_sig']

    data = open_file(file_in, encoders[encode_index], delimination)
    while data is str:
        if encode_index < len(encoders) - 1:
            encode_index = encode_index + 1
            data = open_file(file_in, encoders[encode_index], delimination)
        else:
            print("Can't find appropriate encoder")
            exit()

    return data


def open_file(file_in, encoder, delimination):
    try:
        data = pd.read_csv(file_in, low_memory=False, encoding=encoder, delimiter=delimination)
        print("Opened file using encoder: " + encoder)

    except UnicodeDecodeError:
        print("Encoder Error for: " + encoder)
        return "Encode Error"
    return data


if __name__ == '__main__':
    main()

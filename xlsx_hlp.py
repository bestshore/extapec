#!/usr/bin/env python3
# coding=UTF-8

import xlrd
import xlsxwriter
import os
from scr_hlp import scr_hlp


class xlsx_hlp:
    wb = None
    folder_name = ""
    filename = ""
    current = ""
    ws_main = None
    headers_main = ['datasource', 'profile_url', 'id', 'date_maj', 'nb_consult', 'date_der_consult', 'photo_url',
                    'name', 'poste', 'experience', 'title', 'dispo', 'file_url', 'file_dd_url', 'linkedin_url',
                    'contact_tel', 'contact_email', 'objectifs', 'souhait_fonctions', 'souhait_salaire',
                    'souhait_lieux']
    row_num_main = 1

    ws_comp = None
    headers_comp = ['id', 'comp', 'compstars', 'complevel', 'compdesc']
    row_num_comp = 1

    ws_lang = None
    headers_lang = ['id', 'lang', 'langstars', 'langlevel']
    row_num_lang = 1

    ws_atouts = None
    headers_atouts = ['id', 'Atouts']
    row_num_atouts = 1

    ws_nb_moments = None
    headers_nb_moments = ['id', 'dd_mom', 'df_mom', 'type_mom', 'title_mom', 'tagline_mom', 'comp_mom', 'location_mom',
                          'desc_mom']
    row_num_nb_moments = 1

    # @staticmethod
    # def create_wb(filtername=""):

    #     if not os.path.isdir(xlsx_hlp.folder_name):
    #         os.mkdir(xlsx_hlp.folder_name)
    #     if not os.path.isfile(os.path.join(xlsx_hlp.folder_name,xlsx_hlp.filename+filtername+".xlsx")):
    #         xlsx_hlp.current = os.path.join(xlsx_hlp.folder_name,xlsx_hlp.filename+filtername+".xlsx")
    #     else:
    #         i = 1
    #         while os.path.isfile(os.path.join(xlsx_hlp.folder_name,xlsx_hlp.filename+filtername+"(%i).xlsx"%i)):
    #             i += 1
    #         xlsx_hlp.current = os.path.join(xlsx_hlp.folder_name,xlsx_hlp.filename+filtername+"(%i).xlsx"%i)
    #     xlsx_hlp.wb = xlsxwriter.Workbook(xlsx_hlp.current)
    #     xlsx_hlp.ws_main = xlsx_hlp.wb.add_worksheet('main')
    #     xlsx_hlp.row_num_main = 1
    #     xlsx_hlp.ws_comp = xlsx_hlp.wb.add_worksheet('compétences')
    #     xlsx_hlp.row_num_comp = 1
    #     xlsx_hlp.ws_lang = xlsx_hlp.wb.add_worksheet('lang')
    #     xlsx_hlp.row_num_lang = 1
    #     xlsx_hlp.ws_atouts = xlsx_hlp.wb.add_worksheet('atouts')
    #     xlsx_hlp.row_num_atouts = 1
    #     xlsx_hlp.ws_nb_moments = xlsx_hlp.wb.add_worksheet('nb_moments_cles')
    #     xlsx_hlp.row_num_nb_moments = 1

    @staticmethod
    def create_wb(filtername=""):

        # create folder if not present
        if not os.path.isdir(xlsx_hlp.folder_name):
            os.mkdir(xlsx_hlp.folder_name)

        xlsx_hlp.current = os.path.join(xlsx_hlp.folder_name, xlsx_hlp.filename + filtername + ".xlsx")

        # if this file is already present
        if os.path.isfile(xlsx_hlp.current):
            xlsx_hlp.open_wb()
        else:
            # create excel object with current file name
            xlsx_hlp.wb = xlsxwriter.Workbook(xlsx_hlp.current)

            xlsx_hlp.wb = xlsxwriter.Workbook(xlsx_hlp.current)
            xlsx_hlp.ws_main = xlsx_hlp.wb.add_worksheet('main')
            xlsx_hlp.row_num_main = 1
            xlsx_hlp.ws_comp = xlsx_hlp.wb.add_worksheet('compétences')
            xlsx_hlp.row_num_comp = 1
            xlsx_hlp.ws_lang = xlsx_hlp.wb.add_worksheet('lang')
            xlsx_hlp.row_num_lang = 1
            xlsx_hlp.ws_atouts = xlsx_hlp.wb.add_worksheet('atouts')
            xlsx_hlp.row_num_atouts = 1
            xlsx_hlp.ws_nb_moments = xlsx_hlp.wb.add_worksheet('nb_moments_cles')
            xlsx_hlp.row_num_nb_moments = 1
            xlsx_hlp.set_all_headers()
            xlsx_hlp.wb.close()
            scr_hlp.pause_if_EXTRADEBUG("New File created")
            xlsx_hlp.open_wb()

    @staticmethod
    def open_wb():
        scr_hlp.print_if_DEBUG("Opening an existing sheet named = %s" % xlsx_hlp.current)
        wbRD = xlrd.open_workbook(xlsx_hlp.current)
        sheets = wbRD.sheets()
        xlsx_hlp.wb = xlsxwriter.Workbook(xlsx_hlp.current)
        for sheet in sheets:  # write data from old file
            if sheet.name == 'main':
                ws = xlsx_hlp.ws_main = xlsx_hlp.wb.add_worksheet(sheet.name)
                xlsx_hlp.row_num_main = sheet.nrows
                scr_hlp.print_if_DEBUG("%s was having %i rows previously." % (sheet.name, sheet.nrows - 1))

            elif sheet.name == 'compétences':
                ws = xlsx_hlp.ws_comp = xlsx_hlp.wb.add_worksheet(sheet.name)
                xlsx_hlp.row_num_comp = sheet.nrows
                scr_hlp.print_if_DEBUG("%s was having %i rows previously." % (sheet.name, sheet.nrows - 1))

            elif sheet.name == 'lang':
                ws = xlsx_hlp.ws_lang = xlsx_hlp.wb.add_worksheet(sheet.name)
                xlsx_hlp.row_num_lang = sheet.nrows
                scr_hlp.print_if_DEBUG("%s was having %i rows previously." % (sheet.name, sheet.nrows - 1))

            elif sheet.name == 'atouts':
                ws = xlsx_hlp.ws_atouts = xlsx_hlp.wb.add_worksheet(sheet.name)
                xlsx_hlp.row_num_atouts = sheet.nrows
                scr_hlp.print_if_DEBUG("%s was having %i rows previously." % (sheet.name, sheet.nrows - 1))

            elif sheet.name == 'nb_moments_cles':
                ws = xlsx_hlp.ws_nb_moments = xlsx_hlp.wb.add_worksheet(sheet.name)
                xlsx_hlp.row_num_nb_moments = sheet.nrows
                scr_hlp.print_if_DEBUG("%s was having %i rows previously." % (sheet.name, sheet.nrows - 1))

            else:
                raise NameError("Some Problem in Excel file")

            for row in range(sheet.nrows):
                for col in range(sheet.ncols):
                    ws.write(row, col, sheet.cell(row, col).value)
        # scr_hlp.pause_if_EXTRADEBUG("Existing sheet opened")

    @staticmethod
    def save_wb():
        xlsx_hlp.wb.close()
        scr_hlp.pause_if_EXTRADEBUG("Excel file saved")
        xlsx_hlp.open_wb()

    @staticmethod
    def set_all_headers():
        all_ws = [xlsx_hlp.ws_main, xlsx_hlp.ws_comp, xlsx_hlp.ws_lang, xlsx_hlp.ws_atouts, xlsx_hlp.ws_nb_moments]
        all_headers = [xlsx_hlp.headers_main, xlsx_hlp.headers_comp, xlsx_hlp.headers_lang, xlsx_hlp.headers_atouts,
                       xlsx_hlp.headers_nb_moments]
        for ws, h in zip(all_ws, all_headers):
            xlsx_hlp.set_h_ws(ws, h)

    @staticmethod
    def set_h_ws(ws, headers):
        for col in range(0, len(headers)):
            ws.write(0, col, headers[col])

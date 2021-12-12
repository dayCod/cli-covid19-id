from api import *
from collections import OrderedDict

user_option = ""
while user_option != "exit":
    # ========== GLOBAL VARIABLES ==========
    # LOCAL API JSON
    ina_json = indonesia_api.json()
    ina_api = ina_json[0]
    # Data PrintOut
    print("\nINDONESIA COVID-19 DATA\n")
    print(f"- Nama Negara : {ina_api['name']}\n- Positif : {ina_api['positif']}\n- Sembuh : {ina_api['sembuh']}\n- Meninggal : {ina_api['meninggal']}\n- Dirawat : {ina_api['dirawat']}")
    # SELECT OPTION
    spaces = "       "
    option = ["province","hospital","vaccines_test"]
    print(f"NOTE : province = PROVINCE DATA | hospital : HOSPITAL DATA | vaccines_test = VACCINES AND TEST COVID 19 DATA\n{spaces}Choose one data above by typing = province, hospital, or vaccines_test. With lower case alphabet\n{spaces}Type 'exit' for close the app")
    print(option)
    user_option = input("\nCHOOSE ONE OF THE OPTION ABOVE : ").lower()

    if user_option == option[0]:
        # PROVINCE DATA
        print("\nPROVINCE DATA \n")
        province_json = province.json()
        list_data = province_json["list_data"]
        stp = ""
        for province_data in list_data:
            province_list = province_data["key"]
            print(f"- {province_list}")
    
        user_input_province = input("\nCHOOSE ONE OF THE PROVINCES : ").upper()
    
        for provinceee in list_data:
            province_key = provinceee["key"]
            if user_input_province == province_key  and user_input_province in province_key:
                for province_stat in list_data:
                    try:
                        province_detail = province_stat["key"]
                        # RATIO
                        ratio = province_stat["doc_count"]
                        formated_ratio = '{:.2f}'.format(ratio)
                        #  GENDER MALE AND FEMALE
                        gender_province = province_stat["jenis_kelamin"]
                        detail_gender_lk = gender_province[0]
                        detail_gender_pr = gender_province[1]
                        #  AGE GROUP
                        a_group = province_stat["kelompok_umur"]
                        zf = a_group[0] # 0 - 5 range of age
                        se = a_group[1] # 6 - 18 range of age
                        nt_t = a_group[2] # 19 - 30 range of age
                        to_ff = a_group[3] # 31 - 45 range of age
                        fs_fn = a_group[4] # 46 - 59 range of age
                        sixty_up = a_group[5] # bigger than equal to sixty

                        if user_input_province == province_detail and user_input_province in province_detail:
                            print(f"\n{province_detail.upper()}\n\n- RATE : {formated_ratio}%\n- JUMLAH KASUS : {province_stat['jumlah_kasus']}\n- JUMLAH SEMBUH : {province_stat['jumlah_sembuh']}\n- JUMLAH MENINGGAL : {province_stat['jumlah_meninggal']}\n- JUMLAH DIRAWAT : {province_stat['jumlah_dirawat']}\n- {detail_gender_lk['key']} : {detail_gender_lk['doc_count']}\n- {detail_gender_pr['key']} : {detail_gender_pr['doc_count']}\n\nKELOMPOK UMUR\n- {zf['key']} : {zf['doc_count']}\n- {se['key']} : {se['doc_count']}\n- {nt_t['key']} : {nt_t['doc_count']}\n- {to_ff['key']} : {to_ff['doc_count']}\n- {fs_fn['key']} : {fs_fn['doc_count']}\n- >=60 : {sixty_up['doc_count']}")
                    except IndexError:
                        stp
                        # print(gender_province)
                # CITY
                validating_city = input("\nContinue to Find City Risk Score (Y/n) : ").upper()
                city = city_risk_score.json()
                city_date = city["tanggal"]
                city_stat = city["data"]

                if validating_city == "Y":
                    print(f"\nCITY LIST IN {user_input_province}\n")
                    for city_data in city_stat:
                        city_detail = city_data["kota"]
                        if user_input_province == city_data["prov"]:
                            print(f"- {city_detail}")
                    
                    user_input_city = input("\nFind ur City Zone : ").upper()
                    for city_risk_data in city_stat:
                        city_title = city_risk_data["kota"]
                        if user_input_city == city_title:
                            print(f"\n{city_title} Risk Score\n- Provinsi : {city_risk_data['prov']}\n- Kode Provinsi : {city_risk_data['kode_prov']}\n- Kota : {city_title}\n- Kode Kota : {city_risk_data['kode_kota']}\n- City Risk Score : {city_risk_data['hasil']}")

                    # DISTRICT
                    validating_district = input("\nContinue to Find District Risk Score (Y/n) : ").upper()
                    district = kecamatan.json()
                    district_stat = district

                    if validating_district == "Y":
                        print(f"\nDISTRICT LIST IN {user_input_province}\n")
                        for district_data in district_stat:
                            district_detail = district_data["title"]
                            if user_input_province in district_detail:
                                print(f"- {district_detail}")  

                        user_input_district = input("\nFind ur District Zone : ").upper()
                        for district_risk_score in district_stat:
                            district_title = district_risk_score["title"]
                            district_coordinate_point = district_risk_score["lokasi"]
                            if user_input_district in district_title and user_input_province in district_title:
                                print(f"\n{district_title}\n\n- Latitude : {district_coordinate_point['lat']}\n- Longitude : {district_coordinate_point['lon']}\n- Risk Score : {district_risk_score['kategori']}")
                    else:
                        print("\nTHANKS FOR USED OUR APP")
                else:
                    print("\nTHANKS FOR USED OUR APP")

    elif user_option == option[1]:
        province_json = province.json()
        hospital_json = hospital.json()
        # PROVINCE DATA
        print("\nPROVINCE DATA \n")
        data_list = province_json["list_data"]
        stp = ""
        for province_data in data_list:
            province_key = province_data["key"]
            print(f"- {province_key}")
    
        user_input_province = input("\nCHOOSE ONE OF THE PROVINCES : ").upper()


        print(f"\n{user_input_province}\n")
        for province_detail in data_list:
            province_key = province_detail["key"]
            if user_input_province == province_key and user_input_province in province_key:
                # LOAD CITY DATA FROM CITY API
                city = city_risk_score.json()
                city_date = city["tanggal"]
                city_stat = city["data"]
                # LOAD ALL OF CITY DATA
                for city_data in city_stat:
                        city_detail = city_data["kota"]
                        if user_input_province == city_data["prov"]:
                            print(f"- {city_detail}")
                user_input_city = input("\nCHOOSE ON OF THE CITIES : ").upper()

                print(f"\nDATA RUMAH SAKIT DI {user_input_city}\n")
                for city_data in city_stat:
                    city_detail = city_data["kota"]
                    if user_input_city == city_detail and user_input_city in city_detail:
                        # remove duplicated values in hospital name
                        already_printed = set()
                        for hospital_data in hospital_json:
                            hospital_zone = hospital_data["wilayah"]
                            hospital_name = hospital_data["nama"]
                            if city_detail in hospital_zone and hospital_name not in already_printed:
                                print(hospital_name)
                                already_printed.add(hospital_name)
                                
                user_input_hospital = input("\nCHOOSE ONE OF THE HOSPITALS : ").upper()
                print(f"\n{user_input_hospital}\n")
                already_printed2 = set()
                for list_of_hospital in hospital_json:
                    name_of_hospital = list_of_hospital["nama"]
                    if user_input_hospital == name_of_hospital and name_of_hospital not in already_printed2:
                        print(f"- Nama RS : {name_of_hospital}\n- Kode RS : {list_of_hospital['kode_rs']}\n- Tempat Tidur : {list_of_hospital['tempat_tidur']}\n- Telepon : {list_of_hospital['telepon']}\n- Alamat : {list_of_hospital['alamat']}\n- Tipe : {list_of_hospital['tipe']}\n- Wilayah : {list_of_hospital['wilayah']}")
                        
                        already_printed2.add(name_of_hospital)
    
    elif user_option == option[2]:
        test_vacc_json = testing_and_vaccination.json()
        print("\nTESTING AND VACCINATION OVERALL DATA\n")
        print("PENAMBAHAN TESTING DAN VAKSINASI\n")
        pemeriksaan = test_vacc_json["pemeriksaan"]
        vaksinasi = test_vacc_json["vaksinasi"]
        penambahan = pemeriksaan["penambahan"]
        penambahan_vaksinasi = vaksinasi["penambahan"]
        harian = pemeriksaan["harian"]
        total = pemeriksaan["total"]
        total_vaccination = vaksinasi["total"]
        # print TEST AND VACCINATION ADDITION DATA 
        print(f"- Jumlah Spesimen PCR + TCM : {penambahan['jumlah_spesimen_pcr_tcm']}\n- Jumlah Spesimen Antigen : {penambahan['jumlah_spesimen_antigen']}\n- Jumlah Orang PCR + TCM : {penambahan['jumlah_orang_pcr_tcm']}\n- Jumlah Orang Antigen : {penambahan['jumlah_orang_antigen']}\n- Tanggal : {penambahan['tanggal']}\n- Dibuat Pada : {penambahan['created']}\n\nTOTAL SESI 1 DAN SESI 2 DATA VAKSINASI\n")
        # print DAILY TOTAL SESSION 1 AND SESSION 2 VACCINATION DATA
        print(f"- Jumlah Vaksinasi 1 : {penambahan_vaksinasi['jumlah_vaksinasi_1']}\n- Jumlah Vaksinasi 2 : {penambahan_vaksinasi['jumlah_vaksinasi_2']}\n- Tanggal : {penambahan_vaksinasi['tanggal']}\n- Dibuat Pada : {penambahan_vaksinasi['created']}\n\nTOTAL DATA VAKSINASI SESI 1 DAN SESI 2\n")
        # print TOTAL SESSION 1 AND SESSION 2 VACCINATION DATA
        print(f"- Jumlah Vaksinasi 1 : {total_vaccination['jumlah_vaksinasi_1']}\n- Jumlah Vaksinasi 2 : {total_vaccination['jumlah_vaksinasi_2']}")

                

                                 
                    
            
    



        




        
    
        


















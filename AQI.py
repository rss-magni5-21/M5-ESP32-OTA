import UMux_Sensors
import Display

"""
As we are checking AQI for VOC, PM2.5, PM10

All should be in ug/m3

VOC is in ppb, so converting formula:
1 ppb ≈ 1.8 µg/m³ (for common VOCs)

PM2.5, PM10 all will be in ug/m3

          IH-IL
AQI =   ---------  * (C-CL) + IL
          CH-CL
"""
IH = 0
IL = 0

AQI_D = 0
AQI_PM25 = 0
AQI_PM10 = 0
AQI_VOC = 0

VOC_MW = 30.03  # Molecular Weight of formaldehyde in g/mol
VOC_CONVERSION_FACTOR = 24.45 / VOC_MW  # ≈ 0.8144

VOC_UGM3 = 0

Pollutant_AQI = 0

# AQI Ranges
AQI_Good_low = 0
AQI_Good_High = 50

AQI_Sati_low = 51
AQI_Sati_High = 100

AQI_Mode_low = 101
AQI_Mode_High = 150

AQI_Poor_low = 151
AQI_Poor_High = 200

AQI_Vpoor_low = 201
AQI_Vpoor_High = 250

AQI_Sever = 251

# PM2.5 Ranges
PM25_Good_low = 0
PM25_Good_High = 30

PM25_Sati_low = 31
PM25_Sati_High = 60

PM25_Mode_low = 61
PM25_Mode_High = 90

PM25_Poor_low = 91
PM25_Poor_High = 120

PM25_Vpoor_low = 121
PM25_Vpoor_High = 250

PM25_Sever = 251

# PM10 Ranges
PM10_Good_low = 0
PM10_Good_High = 50

PM10_Sati_low = 51
PM10_Sati_High = 100

PM10_Mode_low = 101
PM10_Mode_High = 250

PM10_Poor_low = 251
PM10_Poor_High = 350

PM10_Vpoor_low = 351
PM10_Vpoor_High = 430

# VOC Ranges
# VOC_Good_low = 0
# VOC_Good_High = 220
#
# VOC_Sati_low = 221
# VOC_Sati_High = 660
#
# VOC_Mode_low = 661
# VOC_Mode_High = 1100
#
# VOC_Poor_low = 1101
# VOC_Poor_High = 2200
#
# VOC_Vpoor_low = 2201
# VOC_Vpoor_High =

VOC_Good_low = 0
VOC_Good_High = 50

VOC_Sati_low = 51
VOC_Sati_High = 100

VOC_Mode_low = 101
VOC_Mode_High = 168

VOC_Poor_low = 169
VOC_Poor_High = 208

VOC_Vpoor_low = 209
VOC_Vpoor_High = 748


def Get_AQI_PM25():
    global AQI_PM25
    print("Current PM2.5 :", UMux_Sensors.pm2)
    Check_AQI_Range(UMux_Sensors.pm2)
    if PM25_Good_low <= UMux_Sensors.pm2 <= PM25_Good_High:
        CH = PM25_Good_High
        CL = PM25_Good_low
        print("PM2.5 in Good")
        print("CH:", CH)
        print("CH:", CL)

    if PM25_Sati_low <= UMux_Sensors.pm2 <= PM25_Sati_High:
        CH = PM25_Sati_High
        CL = PM25_Sati_low
        print("PM2.5 in Satisfactory")
        print("CH:", CH)
        print("CH:", CL)
    if PM25_Mode_low <= UMux_Sensors.pm2 <= PM25_Mode_High:
        CH = PM25_Mode_High
        CL = PM25_Mode_low
        print("PM2.5 in Moderate")
        print("CH:", CH)
        print("CH:", CL)
    if PM25_Poor_low <= UMux_Sensors.pm2 <= PM25_Poor_High:
        CH = PM25_Poor_High
        CL = PM25_Poor_low
        print("PM2.5 in Poor")
        print("CH:", CH)
        print("CH:", CL)
    if PM25_Vpoor_low <= UMux_Sensors.pm2 <= PM25_Vpoor_High:
        CH = PM25_Vpoor_High
        CL = PM25_Vpoor_low
        print("PM2.5 in Very Poor")
        print("CH:", CH)
        print("CH:", CL)

    AQI_PM25 = (((IH - IL) / (CH - CL)) * (UMux_Sensors.pm2 - CL)) + IL
    print("AQI of PM2.5 : ", AQI_PM25)


def Get_AQI_PM10():
    global AQI_PM10
    print("Current PM2.5 :", UMux_Sensors.pm10)
    Check_AQI_Range(UMux_Sensors.pm10)
    if PM10_Good_low <= UMux_Sensors.pm10 <= PM10_Good_High:
        CH = PM10_Good_High
        CL = PM10_Good_low
        print("PM10 in Good")
        print("CH:", CH)
        print("CH:", CL)
    if PM10_Sati_low <= UMux_Sensors.pm10 <= PM10_Sati_High:
        CH = PM10_Sati_High
        CL = PM10_Sati_low
        print("PM10 in Satisfactory")
        print("CH:", CH)
        print("CH:", CL)
    if PM10_Mode_low <= UMux_Sensors.pm10 <= PM10_Mode_High:
        CH = PM10_Mode_High
        CL = PM10_Mode_low
        print("PM10 in Moderate")
        print("CH:", CH)
        print("CH:", CL)
    if PM10_Poor_low <= UMux_Sensors.pm10 <= PM10_Poor_High:
        CH = PM10_Poor_High
        CL = PM10_Poor_low
        print("PM10 in Poor")
        print("CH:", CH)
        print("CH:", CL)
    if PM10_Vpoor_low <= UMux_Sensors.pm10 <= PM10_Vpoor_High:
        CH = PM10_Vpoor_High
        CL = PM10_Vpoor_low
        print("PM10 in Very Poor")
        print("CH:", CH)
        print("CH:", CL)
    # if PM10_Sever > 250:
    #     print("PM2.5 is very sever")

    AQI_PM10 = (((IH - IL) / (CH - CL)) * (UMux_Sensors.pm10 - CL)) + IL
    print("AQI of PM10 : ", AQI_PM10)


def Get_AQI_VOC():
    global AQI_VOC
    print("Current VOC (PPB) :", UMux_Sensors.VoC)
    Convert_VOC_PPB_UgM3()
    Check_AQI_Range(UMux_Sensors.VoC)

    if VOC_Good_low <= UMux_Sensors.VoC <= VOC_Good_High:
        CH = VOC_Good_High
        CL = VOC_Good_low
        print("VOC in Good")
    elif VOC_Sati_low <= UMux_Sensors.VoC <= VOC_Sati_High:
        CH = VOC_Sati_High
        CL = VOC_Sati_low
        print("VOC in Satisfactory")
    elif VOC_Mode_low <= UMux_Sensors.VoC <= VOC_Mode_High:
        CH = VOC_Mode_High
        CL = VOC_Mode_low
        print("VOC in Moderate")
    elif VOC_Poor_low <= UMux_Sensors.VoC <= VOC_Poor_High:
        CH = VOC_Poor_High
        CL = VOC_Poor_low
        print("VOC in Poor")
    elif VOC_Vpoor_low <= UMux_Sensors.VoC <= VOC_Vpoor_High:
        CH = VOC_Vpoor_High
        CL = VOC_Vpoor_low
        print("VOC in Very Poor")
    else:
        return

    AQI_VOC = (((IH - IL) / (CH - CL)) * (UMux_Sensors.VoC - CL)) + IL
    print("AQI of VOC : ", AQI_VOC)


def Check_AQI_Range(Pollutant_AQI):
    global IH, IL
    if AQI_Good_low <= Pollutant_AQI <= AQI_Good_High:
        IH = AQI_Good_High
        IL = AQI_Good_low
    elif AQI_Sati_low <= Pollutant_AQI <= AQI_Sati_High:
        IH = AQI_Sati_High
        IL = AQI_Sati_low
    elif AQI_Mode_low <= Pollutant_AQI <= AQI_Mode_High:
        IH = AQI_Mode_High
        IL = AQI_Mode_low
    elif AQI_Poor_low <= Pollutant_AQI <= AQI_Poor_High:
        IH = AQI_Poor_High
        IL = AQI_Poor_low
    elif AQI_Vpoor_low <= Pollutant_AQI <= AQI_Vpoor_High:
        IH = AQI_Vpoor_High
        IL = AQI_Vpoor_low


def Convert_VOC_PPB_UgM3():
    global VOC_UGM3
    VOC_UGM3 = UMux_Sensors.VoC * VOC_CONVERSION_FACTOR
    UMux_Sensors.VoC = VOC_UGM3 # * 10
    print("VOC in ug/m3:", VOC_UGM3)
    print("VOC in ug/m3:", UMux_Sensors.VoC)


def find_max(num1, num2, num3):
    return max(num1, num2, num3)


def Get_AQI():
    global AQI_D
    try:
        Get_AQI_PM25()
        Get_AQI_PM10()
        Get_AQI_VOC()
        maximum = find_max(AQI_PM25, AQI_PM10, AQI_VOC)
        print(f"The AQI of This Area is: {maximum}")
        Check_AQI_Range(maximum)
        AQI_D = int(maximum)
        Display.AQI_Parameters_Data(Display.AQI_VP, AQI_D)
    except OSError as e:
        print("Sensor read error:", e)
    except Exception as e:
        print("Unexpected error:", e)

# import UMux_Sensors
# import Display
#
# """
#
# As we are checking AQI for o3,PM2.5,PM10
#
# All should be in ug/m3
#
# so o3 in ppb so converting formula  (The molecular weight of ozone (O₃) is 48.00 g/mol.)
#                                      Standard molar volume of air (24.45 L at standard temperature and pressure)
#
#                   MW (molecular weight)
# o3 ug/m3 = ppb * ------------------------
#                            24.45
#
# PM2.5 , PM10 all will be in ug/m3
#
#
#           IH-IL
# AQI =   ---------  * (C-CL) + IL
#           CH-CL
#
# """
# IH = 0
# IL = 0
#
# AQI_D = 0
# AQI_PM25 = 0
# AQI_PM10 = 0
# AQI_O3 = 0
#
# O3_molecular_Wt = 48
# molar_vlm_air = 24.45
# O3_UGM3 = 0
#
# Pollutant_AQI = 0
#
# AQI_Good_low = 0
# AQI_Good_High = 50
#
# AQI_Sati_low = 51
# AQI_Sati_High = 100
#
# AQI_Mode_low = 101
# AQI_Mode_High = 150
#
# AQI_Poor_low = 151
# AQI_Poor_High = 200
#
# AQI_Vpoor_low = 201
# AQI_Vpoor_High = 250
#
# AQI_Sever = 251
# # ------------------------------------------------------------------
# # ------------------------------------------------------------------
#
# PM25_Good_low = 0
# PM25_Good_High = 30
#
# PM25_Sati_low = 31
# PM25_Sati_High = 60
#
# PM25_Mode_low = 61
# PM25_Mode_High = 90
#
# PM25_Poor_low = 91
# PM25_Poor_High = 120
#
# PM25_Vpoor_low = 121
# PM25_Vpoor_High = 250
#
# PM25_Sever = 251
#
# # ------------------------------------------------------------------
# # ------------------------------------------------------------------
#
# PM10_Good_low = 0
# PM10_Good_High = 50
#
# PM10_Sati_low = 51
# PM10_Sati_High = 100
#
# PM10_Mode_low = 101
# PM10_Mode_High = 250
#
# PM10_Poor_low = 251
# PM10_Poor_High = 350
#
# PM10_Vpoor_low = 351
# PM10_Vpoor_High = 430
#
# #PM10_Sever = 431
#
# # ------------------------------------------------------------------
# # ------------------------------------------------------------------
#
# O3_Good_low = 0
# O3_Good_High = 50
#
# O3_Sati_low = 51
# O3_Sati_High = 100
#
# O3_Mode_low = 101
# O3_Mode_High = 168
#
# O3_Poor_low = 169
# O3_Poor_High = 208
#
# O3_Vpoor_low = 209
# O3_Vpoor_High = 748
#
#
# #O3_Sever = 748
#
#
# def Get_AQI_PM25():
#     global AQI_PM25
#     print("Current PM2.5 :", UMux_Sensors.pm2)
#     Check_AQI_Range(UMux_Sensors.pm2)
#     if PM25_Good_low <= UMux_Sensors.pm2 <= PM25_Good_High:
#         CH = PM25_Good_High
#         CL = PM25_Good_low
#         print("PM2.5 in Good")
#         print("CH:", CH)
#         print("CH:", CL)
#
#     if PM25_Sati_low <= UMux_Sensors.pm2 <= PM25_Sati_High:
#         CH = PM25_Sati_High
#         CL = PM25_Sati_low
#         print("PM2.5 in Satisfactory")
#         print("CH:", CH)
#         print("CH:", CL)
#     if PM25_Mode_low <= UMux_Sensors.pm2 <= PM25_Mode_High:
#         CH = PM25_Mode_High
#         CL = PM25_Mode_low
#         print("PM2.5 in Moderate")
#         print("CH:", CH)
#         print("CH:", CL)
#     if PM25_Poor_low <= UMux_Sensors.pm2 <= PM25_Poor_High:
#         CH = PM25_Poor_High
#         CL = PM25_Poor_low
#         print("PM2.5 in Poor")
#         print("CH:", CH)
#         print("CH:", CL)
#     if PM25_Vpoor_low <= UMux_Sensors.pm2 <= PM25_Vpoor_High:
#         CH = PM25_Vpoor_High
#         CL = PM25_Vpoor_low
#         print("PM2.5 in Very Poor")
#         print("CH:", CH)
#         print("CH:", CL)
#
#     AQI_PM25 = (((IH - IL) / (CH - CL)) * (UMux_Sensors.pm2 - CL)) + IL
#     print("AQI of PM2.5 : ", AQI_PM25)
#
#
# def Get_AQI_PM10():
#     global AQI_PM10
#     print("Current PM2.5 :", UMux_Sensors.pm10)
#     Check_AQI_Range(UMux_Sensors.pm10)
#     if PM10_Good_low <= UMux_Sensors.pm10 <= PM10_Good_High:
#         CH = PM10_Good_High
#         CL = PM10_Good_low
#         print("PM10 in Good")
#         print("CH:", CH)
#         print("CH:", CL)
#     if PM10_Sati_low <= UMux_Sensors.pm10 <= PM10_Sati_High:
#         CH = PM10_Sati_High
#         CL = PM10_Sati_low
#         print("PM10 in Satisfactory")
#         print("CH:", CH)
#         print("CH:", CL)
#     if PM10_Mode_low <= UMux_Sensors.pm10 <= PM10_Mode_High:
#         CH = PM10_Mode_High
#         CL = PM10_Mode_low
#         print("PM10 in Moderate")
#         print("CH:", CH)
#         print("CH:", CL)
#     if PM10_Poor_low <= UMux_Sensors.pm10 <= PM10_Poor_High:
#         CH = PM10_Poor_High
#         CL = PM10_Poor_low
#         print("PM10 in Poor")
#         print("CH:", CH)
#         print("CH:", CL)
#     if PM10_Vpoor_low <= UMux_Sensors.pm10 <= PM10_Vpoor_High:
#         CH = PM10_Vpoor_High
#         CL = PM10_Vpoor_low
#         print("PM10 in Very Poor")
#         print("CH:", CH)
#         print("CH:", CL)
#     # if PM10_Sever > 250:
#     #     print("PM2.5 is very sever")
#
#     AQI_PM10 = (((IH - IL) / (CH - CL)) * (UMux_Sensors.pm10 - CL)) + IL
#     print("AQI of PM10 : ", AQI_PM10)
#
#
# def Get_AQI_O3():
#     global AQI_O3
#     Convert_O3_PPB_UgM3()
#     Check_AQI_Range(O3_UGM3)
#     print("Current O3 (PPB) :", UMux_Sensors.O3)
#     print("Current O3 (ug/m3) :", O3_UGM3)
#     if O3_Good_low <= O3_UGM3 <= O3_Good_High:
#         CH = O3_Good_High
#         CL = O3_Good_low
#         print("03 in Good")
#         print("CH:", CH)
#         print("CH:", CL)
#     if O3_Sati_low <= O3_UGM3 <= O3_Sati_High:
#         CH = O3_Sati_High
#         CL = O3_Sati_low
#         print("03 in Satisfactory")
#         print("CH:", CH)
#         print("CH:", CL)
#     if O3_Mode_low <= O3_UGM3 <= O3_Mode_High:
#         CH = O3_Mode_High
#         CL = O3_Mode_low
#         print("03 in Moderate")
#         print("CH:", CH)
#         print("CH:", CL)
#     if O3_Poor_low <= O3_UGM3 <= O3_Poor_High:
#         CH = O3_Poor_High
#         CL = O3_Poor_low
#         print("03 in Poor")
#         print("CH:", CH)
#         print("CH:", CL)
#     if O3_Vpoor_low <= O3_UGM3 <= O3_Vpoor_High:
#         CH = O3_Vpoor_High
#         CL = O3_Vpoor_low
#         print("03 in VeryPoor")
#         print("CH:", CH)
#         print("CH:", CL)
#     # if PM10_Sever > 250:
#     #     print("PM2.5 is very sever")
#
#     AQI_O3 = (((IH - IL) / (CH - CL)) * (UMux_Sensors.O3 - CL)) + IL
#     print("AQI of O3 : ", AQI_O3)
#
#
# def Check_AQI_Range(Pollutant_AQI):
#     global IH, IL
#
#     if AQI_Good_low <= Pollutant_AQI <= AQI_Good_High:
#         IH = AQI_Good_High
#         IL = AQI_Good_low
#         print("AQI is Good")
#         print("IH:", IH)
#         print("IL:", IL)
#
#     if AQI_Sati_low <= Pollutant_AQI <= AQI_Sati_High:
#         IH = AQI_Sati_High
#         IL = AQI_Sati_low
#         print("AQI is Satisfactory")
#         print("IH:", IH)
#         print("IL:", IL)
#
#     if AQI_Mode_low <= Pollutant_AQI <= AQI_Mode_High:
#         IH = AQI_Mode_High
#         IL = AQI_Mode_low
#         print("AQI is Moderate")
#         print("IH:", IH)
#         print("IL:", IL)
#
#     if AQI_Poor_low <= Pollutant_AQI <= AQI_Poor_High:
#         IH = AQI_Poor_High
#         IL = AQI_Poor_low
#         print("AQI is Poor")
#         print("IH:", IH)
#         print("IL:", IL)
#
#     if AQI_Vpoor_low <= Pollutant_AQI <= AQI_Vpoor_High:
#         IH = AQI_Vpoor_High
#         IL = AQI_Vpoor_low
#         print("AQI is Very Poor")
#         print("IH:", IH)
#         print("IL:", IL)
#
#
# def Convert_O3_PPB_UgM3():
#     global O3_UGM3
#     O3_UGM3 = UMux_Sensors.O3 * (O3_molecular_Wt / molar_vlm_air)
#     print("O3 in ug/m3:", O3_UGM3)
#
#
# def find_max(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
#
#
# def Get_AQI():
#     global AQI_D
#     try:
#         Get_AQI_PM25()
#         Get_AQI_PM10()
#         Get_AQI_O3()
#         maximum = find_max(AQI_PM25, AQI_PM10, AQI_O3)
#         print(f"The AQI of This Area is: {maximum}")
#         Check_AQI_Range(maximum)
#         AQI_D = int(maximum)
#         Display.AQI_Parameters_Data(Display.AQI_VP, AQI_D)
#
#     except OSError as e:
#         print("Sensor read error:", e)
#     except Exception as e:
#         print("Unexpected error:", e)

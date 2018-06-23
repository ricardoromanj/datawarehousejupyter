"""
     1  Health Service Area
     2  Hospital County
     3  Operating Certificate Number
     4  Facility Id
     5  Facility Name
     6  Age Group
     7  Zip Code - 3 digits
     8  Gender
     9  Race
    10  Ethnicity
    11  Length of Stay
    12  Type of Admission
    13  Patient Disposition
    14  Discharge Year
    15  CCS Diagnosis Code
    16  CCS Diagnosis Description
    17  CCS Procedure Code
    18  CCS Procedure Description
    19  APR DRG Code
    20  APR DRG Description
    21  APR MDC Code
    22  APR MDC Description
    23  APR Severity of Illness Code
    24  APR Severity of Illness Description
    25  APR Risk of Mortality
    26  APR Medical Surgical Description
    27  Payment Typology 1
    28  Payment Typology 2
    29  Payment Typology 3
    30  Attending Provider License Number
    31  Operating Provider License Number
    32  Other Provider License Number
    33  Birth Weight
    34  Abortion Edit Indicator
    35  Emergency Department Indicator
    36  Total Charges
    37  Total Costs
"""

HEALTH_SERVICE_AREA = 0
HOSPITAL_COUNTY = 1
OPERATING_CERTIFICATE_NUMBER = 2
FACILITY_ID = 3
FACILITY_NAME = 4
AGE_GROUP = 5
ZIP_CODE = 6
GENDER = 7
RACE = 8
ETHNICITY = 9
LENGTH_STAY = 10
TYPE_ADMISSION = 11
PATIENT_DISPOSITION = 12
DISCHARGE_YEAR = 13
CCS_DIAGNOSIS_CODE = 14
CCS_DIAGNOSIS_DESC = 15
CCS_PROCEDURE_CODE = 16
CCS_PROCEDURE_DESC = 17
APR_DRG_CODE = 18
APR_DRG_DESC = 19
APR_MDC_CODE = 20
APR_MDC_DESC = 21
APR_SEVERITY_ILLNESS_CODE = 22
APR_SEVERITY_ILLNESS_DESC = 23
APR_RISK_MORTALITY = 24
APR_MEDICAL_SURGICAL_DESC = 25
PAYMENT_TYPO_1 = 26
PAYMENT_TYPO_2 = 27
PAYMENT_TYPO_3 = 28
ATTEN_PROV_LIC = 29
OPERA_PROV_LIC = 30
OTHER_PROV_LIC = 31
BIRTH_WEIGHT = 32
ABORTION_IND = 33
EMERGENCY_IND = 34
TOTAL_CHARG = 35
TOTAL_COSTS = 36



class DischargeRecord():

    def __init__(self, row=None):
        self.row = row
        self.COLUMN_INDECES = []
        self.COLUMN_NAMES = []
        self.COLUMN_TYPES = {}
        self.COLUMN_CONV = {}

    def conv_indToInt(self, charInd):
        intInd = 0
        if charInd == 'Y' or charInd == 'y':
            intInd = 1
        return intInd

    def conv_zipcode(self, zipcode):
        if type(zipcode) is str and zipcode == 'OOS':
            return 0
        else:
            return int(zipcode)

    def conv_money(self, amount):
        amountStr = str(amount)
        amountStr = amountStr.replace('$', '')
        amountStr = amountStr.replace(',', '')
        return amountStr

    def get_column_indeces(self):
        return self.COLUMN_INDECES

    def get_column_names(self):
        return self.COLUMN_NAMES

    def get_column_types(self):
        return self.COLUMN_TYPES

    def get_column_converters(self):
        return self.COLUMN_CONV

class DimDateRecord(DischargeRecord):

    def __init__(self, row=None):
        self.row = row
        self.COLUMN_INDECES = [DISCHARGE_YEAR]
        self.COLUMN_NAMES = [
            'DischargeYear',
        ]
        self.COLUMN_TYPES = {
            'DischargeYear': 'int64'
        }

    def get_row(self):
        return [self.row[DISCHARGE_YEAR]]

class DimProviderRecord(DischargeRecord):

    def __init__(self, row=None):
        self.row = row
        self.COLUMN_INDECES = [
            ATTEN_PROV_LIC,
            OPERA_PROV_LIC,
            OTHER_PROV_LIC
        ]
        self.COLUMN_NAMES = [
            'AttendingLicenseNo',
            'OperatingLicenseNo',
            'OtherLicenseNo'
        ]
        self.COLUMN_TYPES = {
            'AttendingLicenseNo': 'str',
            'OperatingLicenseNo': 'str',
            'OtherLicenseNo': 'str'
        }

    def get_row(self):
        return [self.row[ATTEN_PROV_LIC], self.row[OPERA_PROV_LIC], self.row[OTHER_PROV_LIC]]

class DimAdmissionRecord(DischargeRecord):

    def __init__(self, row=None):
        self.row = row
        self.COLUMN_INDECES = [
            TYPE_ADMISSION,
            PATIENT_DISPOSITION,
            ABORTION_IND,
            EMERGENCY_IND
        ]
        self.COLUMN_NAMES = [
            'TypeAdmission',
            'PatientDisposition',
            'AbortionIndicator',
            'EmergencyIndicator'
        ]
        self.COLUMN_TYPES = {
            'TypeAdmission': 'str',
            'PatientDisposition': 'str'
        }
        self.COLUMN_CONV = {
            'AbortionIndicator': self.conv_indToInt,
            'EmergencyIndicator': self.conv_indToInt
        }

class DimAPRClassificationRecord(DischargeRecord):

    def __init__(self, row=None):
        self.row = row
        self.COLUMN_INDECES = [
            APR_DRG_CODE,
            APR_DRG_DESC,
            APR_MDC_CODE,
            APR_MDC_DESC,
            APR_SEVERITY_ILLNESS_CODE,
            APR_SEVERITY_ILLNESS_DESC,
            APR_RISK_MORTALITY,
            APR_MEDICAL_SURGICAL_DESC
            ]
        self.COLUMN_NAMES = [
            'DrgCode',
            'DrgDescription',
            'MdcCode',
            'MdcDescription',
            'SeverityIllnessCode',
            'SeverityIllnessDescription',
            'RiskOfMortality',
            'MedicalSurgicalDescription'
        ]
        self.COLUMN_TYPES = {
            'DrgCode': 'int64',
            'DrgDescription': 'str',
            'MdcCode': 'int64',
            'MdcDescription': 'str',
            'SeverityIllnessCode': 'int64',
            'SeverityIllnessDescription': 'str',
            'RiskOfMortality': 'str',
            'MedicalSurgicalDescription': 'str'
        }

class DimClinicClassRecord(DischargeRecord):

    def __init__(self, row=None):
        self.row = row
        self.COLUMN_INDECES = [
            CCS_DIAGNOSIS_CODE,
            CCS_DIAGNOSIS_DESC,
            CCS_PROCEDURE_CODE,
            CCS_PROCEDURE_DESC
        ]
        self.COLUMN_NAMES = [
            'DiagnosisCode',
            'DiagnosisDescription',
            'ProcedureCode',
            'ProcedureDescription'
        ]
        self.COLUMN_TYPES = {
            'DiagnosisCode': 'int64',
            'DiagnosisDescription': 'str',
            'ProcedureCode': 'int64',
            'ProcedureDescription': 'str'
        }

class DimPaymentRecord(DischargeRecord):

    def __init__(self, row=None):
        self.row = row
        self.COLUMN_INDECES = [
            PAYMENT_TYPO_1,
            PAYMENT_TYPO_2,
            PAYMENT_TYPO_3
        ]
        self.COLUMN_NAMES = [
            'PaymentTypology1',
            'PaymentTypology2',
            'PaymentTypology3'
        ]
        self.COLUMN_TYPES = {
            'PaymentTypology1': 'str',
            'PaymentTypology2': 'str',
            'PaymentTypology3': 'str'
        }

class DimDemographicsRecord(DischargeRecord):

    def __init__(self, row=None):
        self.row = row
        self.COLUMN_INDECES = [
            AGE_GROUP,
            GENDER,
            RACE,
            ETHNICITY
        ]
        self.COLUMN_NAMES = [
            'AgeGroup',
            'Gender',
            'Race',
            'Ethnicity'
        ]
        self.COLUMN_TYPES = {
            'AgeGroup': 'str',
            'Gender': 'str',
            'Race': 'str',
            'Ethnicity': 'str'
        }

class DimLocationRecord(DischargeRecord):

    def __init__(self, row=None):
        self.row = row
        self.COLUMN_INDECES = [
            HEALTH_SERVICE_AREA,
            HOSPITAL_COUNTY,
            FACILITY_ID,
            FACILITY_NAME,
            ZIP_CODE
        ]
        self.COLUMN_NAMES = [
            'HealthServiceArea',
            'HospitalCounty',
            'FacilityID',
            'FacilityName',
            'ZipCode'
        ]
        self.COLUMN_TYPES = {
            'HealthServiceArea': 'str',
            'HospitalCounty': 'str',
            'FacilityID': 'int64',
            'FacilityName': 'str'
        }
        self.COLUMN_CONV = {
            'ZipCode': self.conv_zipcode
        }

class FactDischarge(DischargeRecord):

    def __init__(self, row=None):
        self.row = row
        self.COLUMN_INDECES = [
            HEALTH_SERVICE_AREA,
            HOSPITAL_COUNTY,
            OPERATING_CERTIFICATE_NUMBER,
            FACILITY_ID,
            FACILITY_NAME,
            AGE_GROUP,
            ZIP_CODE,
            GENDER,
            RACE,
            ETHNICITY,
            LENGTH_STAY,
            TYPE_ADMISSION,
            PATIENT_DISPOSITION,
            DISCHARGE_YEAR,
            CCS_DIAGNOSIS_CODE,
            CCS_DIAGNOSIS_DESC,
            CCS_PROCEDURE_CODE,
            CCS_PROCEDURE_DESC,
            APR_DRG_CODE,
            APR_DRG_DESC,
            APR_MDC_CODE,
            APR_MDC_DESC,
            APR_SEVERITY_ILLNESS_CODE,
            APR_SEVERITY_ILLNESS_DESC,
            APR_RISK_MORTALITY,
            APR_MEDICAL_SURGICAL_DESC,
            PAYMENT_TYPO_1,
            PAYMENT_TYPO_2,
            PAYMENT_TYPO_3,
            ATTEN_PROV_LIC,
            OPERA_PROV_LIC,
            OTHER_PROV_LIC,
            BIRTH_WEIGHT,
            ABORTION_IND,
            EMERGENCY_IND,
            TOTAL_CHARG,
            TOTAL_COSTS
        ]
        self.COLUMN_NAMES = [
            'HealthServiceArea',
            'HospitalCounty',
            'OperatingCertNo',
            'FacilityID',
            'FacilityName',
            'AgeGroup',
            'ZipCode',
            'Gender',
            'Race',
            'Ethnicity',
            'LengthStay',
            'TypeAdmission',
            'PatientDisposition',
            'DischargeYear',
            'DiagnosisCode',
            'DiagnosisDescription',
            'ProcedureCode',
            'ProcedureDescription',
            'DrgCode',
            'DrgDescription',
            'MdcCode',
            'MdcDescription',
            'SeverityIllnessCode',
            'SeverityIllnessDescription',
            'RiskOfMortality',
            'MedicalSurgicalDescription',
            'PaymentTypology1',
            'PaymentTypology2',
            'PaymentTypology3',
            'AttendingLicenseNo',
            'OperatingLicenseNo',
            'OtherLicenseNo',
            'BirthWeight',
            'AbortionIndicator',
            'EmergencyIndicator',
            'TotalCharges',
            'TotalCosts'
        ]
        self.COLUMN_TYPES = {
            'DischargeYear': 'int64',
            'AttendingLicenseNo': 'str',
            'OperatingLicenseNo': 'str',
            'OtherLicenseNo': 'str',
            'TypeAdmission': 'str',
            'PatientDisposition': 'str',
            'DrgCode': 'int64',
            'DrgDescription': 'str',
            'MdcCode': 'int64',
            'MdcDescription': 'str',
            'SeverityIllnessCode': 'int64',
            'SeverityIllnessDescription': 'str',
            'RiskOfMortality': 'str',
            'MedicalSurgicalDescription': 'str',
            'DiagnosisCode': 'int64',
            'DiagnosisDescription': 'str',
            'ProcedureCode': 'int64',
            'ProcedureDescription': 'str',
            'PaymentTypology1': 'str',
            'PaymentTypology2': 'str',
            'PaymentTypology3': 'str',
            'AgeGroup': 'str',
            'Gender': 'str',
            'Race': 'str',
            'Ethnicity': 'str',
            'HealthServiceArea': 'str',
            'HospitalCounty': 'str',
            'FacilityID': 'int64',
            'FacilityName': 'str',
            'BirthWeight': 'float64',
            'LengthStay': 'float64'
        }
        self.COLUMN_CONV = {
            'AbortionIndicator': self.conv_indToInt,
            'EmergencyIndicator': self.conv_indToInt,
            'TotalCharges': self.conv_money,
            'TotalCosts': self.conv_money,
            'ZipCode': self.conv_zipcode
        }

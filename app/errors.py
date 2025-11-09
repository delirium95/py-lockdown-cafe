class VaccineError(Exception):
    def __init__(self, message="Vaccine error"):
        super().__init__(message)


class NotVaccinatedError(VaccineError):
    def __init__(self, message="Visitor is not vaccinated"):
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    def __init__(self, message="Vaccine is expired"):
        super().__init__(message)


class NotWearingMaskError(Exception):
    def __init__(self, message="Visitor is not wearing a mask"):
        super().__init__(message)

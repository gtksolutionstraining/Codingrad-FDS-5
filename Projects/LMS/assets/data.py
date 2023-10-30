from commons.config import (
    BRANCHES, 
    YEARS,
    SEMS
)

LMS = {}

LMS["ADMINS"] = []
LMS["ADMINS"].append({"USERNAME":"Admin", "PASSWORD":"Admin123"})

LMS["BOOKS"] = {}

for branch in BRANCHES:
    LMS["BOOKS"][branch] = {}
    for year in YEARS:
        LMS["BOOKS"][branch][year] = {}
        for sem in SEMS:
            LMS["BOOKS"][branch][year][sem] = []
from commons.config import (
    BRANCHES, 
    YEARS,
    SEMS
)

LMS = {}

LMS["BOOKS"] = {}

for branch in BRANCHES:
    LMS["BOOKS"][branch] = {}
    for year in YEARS:
        LMS["BOOKS"][branch][year] = {}
        for sem in SEMS:
            LMS["BOOKS"][branch][year][sem] = []
#!/usr/bin/python3

loginsuccess = 0

with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    for line in kfile:
        if "-] Authorization failed" in line:

            loginsuccess += 1

print("successes: " , loginsuccess)

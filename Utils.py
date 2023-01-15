def get_name_time(s):
    for i in s:
        if not i.isnumeric():
            return s[s.find(i):], s[:s.find(i)]

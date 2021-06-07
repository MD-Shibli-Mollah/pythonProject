m_str = "shibli_glil_lilili"
sub_string = "li"

m_len = len(m_str)
count = 0
for i in range(len(m_str)):
    print("test")
    print(i)
    print(m_str[i:])
    if m_str[i:].startswith(sub_string):
        count += 1
print(count)

class Demo():

    def fun(self, num):
        out_list = []
        if num % 2 == 0:
            list_len = 3
            va = 2
            while num % list_len == 0 and num // list_len - list_len // 2 > 0:
                in_list = []
                for index in range(list_len):
                    in_list.append(num // list_len - list_len // 2 + index)
                out_list.append(in_list)
                list_len = list_len + va
        else:
            list_len = 2
            va = 1
            isLoop = True
            while isLoop:
                if list_len % 2 == 0:
                    if num / list_len - num // list_len == 0.5:
                        if num // list_len - list_len // 2 + 1 > 0:
                            in_list = []
                            for index in range(list_len):
                                in_list.append(num // list_len - list_len // 2 + 1 + index)
                            out_list.append(in_list)
                            list_len = list_len + va
                        else:
                            isLoop = False
                    else:
                        list_len = list_len + va
                else:
                    if num % list_len == 0:
                        if num // list_len - list_len // 2 > 0:
                            in_list = []
                            for index in range(list_len):
                                in_list.append(num // list_len - list_len // 2 + index)
                            out_list.append(in_list)
                            list_len = list_len + va
                        else:
                            isLoop = False
                    else:
                        list_len = list_len + va
        if len(out_list):
            return out_list
        else:
            return None


a = Demo().fun(21)
print(a)

from collections import OrderedDict

def main():

    in_str = list('SEARCHEXAMPLE')
    l = len(in_str)
    res_dict = {}
    order_res_dict = OrderedDict()

    for i in range(l):
        res_dict[in_str[i]] = i
        order_res_dict[in_str[i]] = i

    for k in res_dict.keys():
        print(k, res_dict[k])

    print("ordered dict: ")
    for k in order_res_dict.keys():
        print(k, order_res_dict[k])


if __name__ == "__main__":
    main()
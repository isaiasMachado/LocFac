import random
import math

INSTANCE_NUMBER = 1 # Ao testar, Ã© 1ï¼ŒNa verdade, um total de 71 exemplos de teste
LOOP_LENGTH = 1000
MAX_TEMPERATURE = 100
MIN_TEMPERATURE = 0.5
ATTENUATION_QUOTIENT = 0.99


def init_alloc_customer(customer_number, facility_number, customer_allocation, facility_capacity, customer_demand, distance_to_facility, facility_open_list, facility_open_cost, total_cost):
    for i in range(0, customer_number):
        while True:
            choose_facility = random.randint(0, facility_number - 1)
            if facility_capacity[choose_facility] >=  customer_demand[i]:
                if facility_open_list[choose_facility] == 0:
                     total_cost +=  facility_open_cost[choose_facility]
                facility_open_list[choose_facility] += 1
                facility_capacity[choose_facility] -=  customer_demand[i]
                total_cost +=  distance_to_facility[i][choose_facility]

                customer_allocation.append(choose_facility)
                break


    return facility_open_list, customer_allocation, total_cost


def generate_neighbor_by_change_facility(customer_number, facility_number, customer_allocation, facility_capacity, customer_demand, distance_to_facility, facility_open_list, facility_open_cost, total_cost):
    while True:
        choose_customer = random.randint(0, customer_number - 1)
        choose_facility = random.randint(0, facility_number - 1)
        if customer_allocation[choose_customer] == choose_facility:
            continue  # 产生的是这个点本身而不是邻居，重来
        if facility_capacity[choose_facility] < customer_demand[choose_customer]:
            continue  # 交换被拒绝，因为目标工厂容量不足
        # 交换操作可进行，计算总花费是否减少，如果减少则接受邻居解，总花费包括 到工厂距离+开工厂费用
        allocated_facility_before = customer_allocation[choose_customer]
        # print('尝试操作：将顾客', choose_customer, '从工厂', allocated_facility_before, '转到工厂', choose_facility)
        cost_before = distance_to_facility[choose_customer][allocated_facility_before]
        if facility_open_list[allocated_facility_before] == 1:
            cost_before += facility_open_cost[allocated_facility_before]
        cost_after = distance_to_facility[choose_customer][choose_facility]
        if facility_open_list[choose_facility] == 0:
            cost_after += facility_open_cost[choose_facility]

        if cost_before <= cost_after and \
                random.random() > math.exp((cost_before - cost_after) / MAX_TEMPERATURE):
            return False

        facility_capacity[allocated_facility_before] += customer_demand[choose_customer]
        facility_capacity[choose_facility] -= customer_demand[choose_customer]

        facility_open_list[allocated_facility_before] -= 1
        facility_open_list[choose_facility] += 1

        customer_allocation[choose_customer] = choose_facility
        total_cost = total_cost - cost_before + cost_after

        return True

def generate_neighbor_by_swap_customer(customer_number, facility_number, customer_allocation, facility_capacity, customer_demand, distance_to_facility, facility_open_list, facility_open_cost, total_cost):  # 产生方式是交换两个不同工厂的顾客，缺点是无法开厂，应配合1使用
    while True:
        customer_1 = random.randint(0, customer_number - 1)
        customer_2 = random.randint(0, customer_number - 1)
        facility_cus_1 = customer_allocation[customer_1]
        facility_cus_2 = customer_allocation[customer_2]
        if customer_1 == customer_2 or facility_cus_1 == facility_cus_2:
            continue  # 产生的是这个点本身而不是邻居，重来
        if facility_capacity[facility_cus_1] + customer_demand[customer_1] - \
                 customer_demand[customer_2] < 0 or  facility_capacity[facility_cus_2] + \
                 customer_demand[customer_2] -  customer_demand[customer_1] < 0:
            continue  # 交换被拒绝，有一个工厂的容量不足
        # 交换操作可进行，计算总花费是否减少，如果减少则接受邻居解，总花费仅仅包括到工厂距离
        cost_before =  distance_to_facility[customer_1][facility_cus_1] \
                      +  distance_to_facility[customer_2][facility_cus_2]
        cost_after =  distance_to_facility[customer_1][facility_cus_2] \
                     +  distance_to_facility[customer_2][facility_cus_1]
        if cost_before <= cost_after and \
                random.random() > math.exp((cost_before - cost_after) / cost_before /  MAX_TEMPERATURE):
            return False

        facility_capacity[facility_cus_1] = facility_capacity[facility_cus_1] + \
                                                  customer_demand[customer_1] - customer_demand[customer_2]
        facility_capacity[facility_cus_2] = facility_capacity[facility_cus_2] + \
                                                  customer_demand[customer_2] - customer_demand[customer_1]
        customer_allocation[customer_1] = facility_cus_2
        customer_allocation[customer_2] = facility_cus_1
        total_cost = total_cost - cost_before + cost_after

        return True

def solve(total_cost):
    init_alloc_customer()
    print('使用模拟退火，初始分配方案花费：', total_cost)
    temperatura = MAX_TEMPERATURE
    while temperatura > MIN_TEMPERATURE:
        for i in range(0, LOOP_LENGTH):
            # if i % 3 != 0:
            #     if  generate_neighbor_by_swap_customer():
            #         print('使用模拟退火，当前温度：',  temperature, '，第', i, '循环 ', '接受新的邻居解,花费更新为：',  total_cost)
            #     continue
            if generate_neighbor_by_change_facility():
                print('使用模拟退火，当前温度：', temperatura, '，第', i, '循环 ', '接受新的邻居解,花费更新为：', total_cost)
        temperatura *= ATTENUATION_QUOTIENT
    # write_file()
    return total_cost



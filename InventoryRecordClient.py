import os
import time

from dotenv import load_dotenv

import grpc
import generated_files.InventoryRecord_pb2_grpc as InventoryRecord_pb2_grpc
from generated_files import InventoryRecord_pb2


def createConnection():
    """
    Creates a connection to the server
    :return:
    """
    load_dotenv()
    port = os.getenv('PUBLIC_IP_CLIENT') + ":50051"
    channel = grpc.insecure_channel(port)
    stub = InventoryRecord_pb2_grpc.InventoryRecordServiceStub(channel)
    return stub


def updateInventoryRecord(id, name, description, unitPrice, quantityInStock, inveneotryValue, reorderLevel,
                          reorderTimeInDays, quantityInReorder, discontinued, print_response):
    """
    Updates an inventory record on server csv
    :param id:
    :param name:
    :param description:
    :param unitPrice:
    :param quantityInStock:
    :param inveneotryValue:
    :param reorderLevel:
    :param reorderTimeInDays:
    :param quantityInReorder:
    :param discontinued:
    :param print_response:
    :return:
    """
    start_time = time.monotonic()
    stub = createConnection()
    response = stub.updateInventoryRecord(
        InventoryRecord_pb2.UpdateInventoryRecord(
            inventoryRecord=InventoryRecord_pb2.InventoryRecord(id=id, name=name, description=description,
                                                                unitPrice=unitPrice,
                                                                quantityInStock=quantityInStock,
                                                                inveneotryValue=inveneotryValue,
                                                                reorderLevel=reorderLevel,
                                                                reorderTimeInDays=reorderTimeInDays,
                                                                quantityInReorder=quantityInReorder,
                                                                discontinued=discontinued)))
    total_time = time.monotonic() - start_time

    if print_response:
        print(response)
    return total_time


def getInventoryRecordById(id, print_response=False):
    """
    Gets an inventory record by id from server csv
    :param id:
    :param print_response:
    :return:
    """
    start_time = time.monotonic()
    stub = createConnection()
    response = stub.getInventoryRecordById(InventoryRecord_pb2.InventoryRecordRequest(id=id))
    total_time = time.monotonic() - start_time

    if print_response:
        print(response)
    return total_time


def getInventoryRecordByKeyValueRange(key_name, key_value_min, key_value_max, print_response):
    """
    Gets an inventory record by key value range from server csv
    :param key_name:
    :param key_value_min:
    :param key_value_max:
    :param print_response:
    :return:
    """
    start_time = time.monotonic()
    stub = createConnection()
    response = stub.getInventoryRecordByKeyValueRange(
        InventoryRecord_pb2.InventoryRecordSearchRange(key_name=key_name, key_value_min=key_value_min,
                                                       key_value_max=key_value_max))
    total_time = time.monotonic() - start_time

    if print_response:
        print(response)
    return total_time


def getDistribution(key_name, percentile, print_response):
    """
    Get the value at percentile of a key from server csv
    :param percentile:
    :param print_response:
    :return:
    """
    start_time = time.monotonic()
    stub = createConnection()
    response = stub.getDistribution(
        InventoryRecord_pb2.GetDistribution(key_name=key_name, percentile=percentile))
    total_time = time.monotonic() - start_time

    if print_response:
        print(response)
    return total_time

import os

import grpc
import pandas as pd
from dotenv import load_dotenv

import DataProcessing
from generated_files import InventoryRecord_pb2_grpc
from concurrent import futures
from generated_files import InventoryRecord_pb2


class InventoryRecordServer(InventoryRecord_pb2_grpc.InventoryRecordServiceServicer):
    def __init__(self):
        pass

    def loadInventoryRecords(self):
        # load csv records from InvRecords.csv
        df = pd.read_csv("InvRecords.csv")
        return df

    def saveInventoryRecords(self, df):
        # save csv records to InvRecords.csv
        df.to_csv("InvRecords.csv", index=False)

    def getInventoryRecordById(self, request, context):
        # get the dataframe
        df = self.loadInventoryRecords()
        filtered_df = df[df["id"] == request.id]
        # get the first record
        if filtered_df.empty:
            response = InventoryRecord_pb2.InventoryRecordResponse()
            print(
                "Returning empty response for id: " + request.id)
            return response
        else:
            record = filtered_df.iloc[0]
            response = InventoryRecord_pb2.InventoryRecordResponse(
                inventoryRecord=InventoryRecord_pb2.InventoryRecord(
                    id=DataProcessing.process_data_and_type(record["id"]),
                    name=DataProcessing.process_data_and_type(record["name"]),
                    description=DataProcessing.process_data_and_type(record["description"]),
                    unitPrice=DataProcessing.process_data_and_type(record["unitPrice"]),
                    quantityInStock=DataProcessing.process_data_and_type(record["quantityInStock"]),
                    inveneotryValue=DataProcessing.process_data_and_type(record["inveneotryValue"]),
                    reorderLevel=DataProcessing.process_data_and_type(record["reorderLevel"]),
                    reorderTimeInDays=DataProcessing.process_data_and_type(record["reorderTimeInDays"]),
                    quantityInReorder=DataProcessing.process_data_and_type(record["quantityInReorder"]),
                    discontinued=DataProcessing.process_data_and_type(record["discontinued"])))
            print("Returning response for id: " + request.id)
            return response

    def getInventoryRecordByKeyValue(self, request, context):
        request_key_name = request.key_name
        request_key_value = request.key_value
        # process request_key_value
        # request_key_value = DataProcessing.process_data_and_type(request_key_value)

        # get the dataframe
        df = self.loadInventoryRecords()
        if request_key_name in df.columns:
            filtered_df = df[df[request_key_name] == request_key_value]
        else:
            print("No column found for key: " + request_key_name)
            filtered_df = pd.DataFrame()
        # get the first record
        if filtered_df.empty:
            response = InventoryRecord_pb2.InventoryRecordResponse()
            print(
                "Returning empty response for search by key: " + request_key_name + " and value: " + request_key_value)
            return response
        else:
            record = filtered_df.iloc[0]
            response = InventoryRecord_pb2.InventoryRecordResponse(
                inventoryRecord=InventoryRecord_pb2.InventoryRecord(
                    id=DataProcessing.process_data_and_type(record["id"]),
                    name=DataProcessing.process_data_and_type(record["name"]),
                    description=DataProcessing.process_data_and_type(record["description"]),
                    unitPrice=DataProcessing.process_data_and_type(record["unitPrice"]),
                    quantityInStock=DataProcessing.process_data_and_type(record["quantityInStock"]),
                    inveneotryValue=DataProcessing.process_data_and_type(record["inveneotryValue"]),
                    reorderLevel=DataProcessing.process_data_and_type(record["reorderLevel"]),
                    reorderTimeInDays=DataProcessing.process_data_and_type(record["reorderTimeInDays"]),
                    quantityInReorder=DataProcessing.process_data_and_type(record["quantityInReorder"]),
                    discontinued=DataProcessing.process_data_and_type(record["discontinued"])))
            print("Returning response for " + request.key_name + " = " + request.key_value)
            return response

    def getInventoryRecordByKeyValueRange(self, request, context):
        request_key_name = request.key_name
        request_key_value_min = DataProcessing.process_data_and_type(request.key_value_min)
        request_key_value_max = DataProcessing.process_data_and_type(request.key_value_max)
        # process request_key_value
        # request_key_value = DataProcessing.process_data_and_type(request_key_value)

        # get the dataframe
        df = self.loadInventoryRecords()
        if request_key_name in df.columns:
            filtered_df = df[df[request_key_name] >= request_key_value_min]
            filtered_df = filtered_df[filtered_df[request_key_name] <= request_key_value_max]
        else:
            print("No column found for key: " + request_key_name)
            filtered_df = pd.DataFrame()
        # get the first record
        if filtered_df.empty:
            response = InventoryRecord_pb2.InventoryRecordResponse()
            print(
                "Returning empty response for search by key: " + request.key_name + " in range: "
                + request.key_value_min + " to " + request.key_value_max)
            return response
        else:
            records_list = InventoryRecord_pb2.InventoryRecordResponseList()
            for index, record in filtered_df.iterrows():
                inv_record = records_list.inventoryRecord.add()
                inv_record.id = DataProcessing.process_data_and_type(record["id"])
                inv_record.name = DataProcessing.process_data_and_type(record["name"])
                inv_record.description = DataProcessing.process_data_and_type(record["description"])
                inv_record.unitPrice = DataProcessing.process_data_and_type(record["unitPrice"])
                inv_record.quantityInStock = DataProcessing.process_data_and_type(record["quantityInStock"])
                inv_record.inveneotryValue = DataProcessing.process_data_and_type(record["inveneotryValue"])
                inv_record.reorderLevel = DataProcessing.process_data_and_type(record["reorderLevel"])
                inv_record.reorderTimeInDays = DataProcessing.process_data_and_type(record["reorderTimeInDays"])
                inv_record.quantityInReorder = DataProcessing.process_data_and_type(record["quantityInReorder"])
                inv_record.discontinued = DataProcessing.process_data_and_type(record["discontinued"])

            response = records_list
            print(
                "Returning response for " + request.key_name + " = " + request.key_name + " in range: "
                + request.key_value_min + " to " + request.key_value_max)
            return response

    def getDistribution(self, request, context):
        # get the dataframe
        df = self.loadInventoryRecords()
        request_key_name = request.key_name
        request_percentile = request.percentile

        at_percentile = df[request_key_name].quantile(request_percentile)
        response = InventoryRecord_pb2.InventoryAtPercentile(at_percentile=at_percentile)
        print("Returning response for " + request.key_name + " at percentile: " + str(request_percentile))
        return response

    def updateInventoryRecord(self, request, context):
        # update the record
        df = self.loadInventoryRecords()

        df.loc[df["id"] == request.inventoryRecord.id, "name"] = request.inventoryRecord.name
        df.loc[df["id"] == request.inventoryRecord.id, "description"] = request.inventoryRecord.description
        df.loc[df["id"] == request.inventoryRecord.id, "unitPrice"] = request.inventoryRecord.unitPrice
        df.loc[df["id"] == request.inventoryRecord.id, "quantityInStock"] = request.inventoryRecord.quantityInStock
        df.loc[df["id"] == request.inventoryRecord.id, "inveneotryValue"] = request.inventoryRecord.inveneotryValue
        df.loc[df["id"] == request.inventoryRecord.id, "reorderLevel"] = request.inventoryRecord.reorderLevel
        df.loc[df["id"] == request.inventoryRecord.id, "reorderTimeInDays"] = request.inventoryRecord.reorderTimeInDays
        df.loc[df["id"] == request.inventoryRecord.id, "quantityInReorder"] = request.inventoryRecord.quantityInReorder
        df.loc[df["id"] == request.inventoryRecord.id, "discontinued"] = request.inventoryRecord.discontinued

        # update the csv with the changes
        self.saveInventoryRecords(df)

        filtered_df = df[df["id"] == request.inventoryRecord.id]

        record = filtered_df.iloc[0]
        response = InventoryRecord_pb2.InventoryRecordResponse(
            inventoryRecord=InventoryRecord_pb2.InventoryRecord(
                id=DataProcessing.process_data_and_type(record["id"]),
                name=DataProcessing.process_data_and_type(record["name"]),
                description=DataProcessing.process_data_and_type(record["description"]),
                unitPrice=DataProcessing.process_data_and_type(record["unitPrice"]),
                quantityInStock=DataProcessing.process_data_and_type(record["quantityInStock"]),
                inveneotryValue=DataProcessing.process_data_and_type(record["inveneotryValue"]),
                reorderLevel=DataProcessing.process_data_and_type(record["reorderLevel"]),
                reorderTimeInDays=DataProcessing.process_data_and_type(record["reorderTimeInDays"]),
                quantityInReorder=DataProcessing.process_data_and_type(record["quantityInReorder"]),
                discontinued=DataProcessing.process_data_and_type(record["discontinued"])))
        print("Returning updated response for " + request.inventoryRecord.id)
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    InventoryRecord_pb2_grpc.add_InventoryRecordServiceServicer_to_server(
        InventoryRecordServer(), server
    )
    port = os.getenv('PRIVATE_IP_SERVER') + ":50051"
    server.add_insecure_port(port)
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    load_dotenv()
    serve()

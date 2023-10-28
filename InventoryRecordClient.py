import grpc
import generated_files.InventoryRecord_pb2_grpc as InventoryRecord_pb2_grpc
from generated_files import InventoryRecord_pb2

channel = grpc.insecure_channel('localhost:50051')
stub = InventoryRecord_pb2_grpc.InventoryRecordServiceStub(channel)

# Test getInventoryRecordById
# response = stub.getInventoryRecordById(InventoryRecord_pb2.InventoryRecordRequest(id="IN0001"))
# response = stub.getInventoryRecordByKeyValueRange(
#     InventoryRecord_pb2.InventoryRecordSearchRange(key_name="quantityInStock", key_value_min="25", key_value_max="110"))
response = stub.updateInventoryRecord(
    InventoryRecord_pb2.UpdateInventoryRecord(
        inventoryRecord=InventoryRecord_pb2.InventoryRecord(id="IN0001", name="Test", description="Test",
                                                            unitPrice=10.0,
                                                            quantityInStock=100, inveneotryValue=1000.0,
                                                            reorderLevel=50,
                                                            reorderTimeInDays=5, quantityInReorder=50,
                                                            discontinued=False)))
if not response.inventoryRecord:
    print("Server returned incomplete feature")

print(response.inventoryRecord)

if response.inventoryRecord and response.inventoryRecord.id:
    # print all the fields of the returned record
    print("ID: " + response.inventoryRecord.id)
    print("Name: " + response.inventoryRecord.name)
    print("Description: " + response.inventoryRecord.description)
    print("Unit Price: " + str(response.inventoryRecord.unitPrice))
    print("Quantity in Stock: " + str(response.inventoryRecord.quantityInStock))
    print("Inventory Value: " + str(response.inventoryRecord.inveneotryValue))
    print("Reorder Level: " + str(response.inventoryRecord.reorderLevel))
    print("Reorder Time in Days: " + str(response.inventoryRecord.reorderTimeInDays))
    print("Quantity in Reorder: " + str(response.inventoryRecord.quantityInReorder))
    print("Discontinued: " + str(response.inventoryRecord.discontinued))
else:
    print("No inventory record found")

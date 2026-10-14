
# Cloud Computing Cost Calculator

# Input details
cpu_rate = 5
cpu_hours = 150

storage_rate = 2
storage_gb = 600

data_transfer_rate = 1
data_transfer_gb = 400

# Calculate costs
cpu_cost = cpu_rate * cpu_hours
storage_cost = storage_rate * storage_gb
data_transfer_cost = data_transfer_rate * data_transfer_gb

# Premium rule: Add Rs. 500 if CPU usage is more than 100 hours
if cpu_hours > 100:
    premium_charge = 500
else:
    premium_charge = 0

# Calculate total bill
total_cost = (
    cpu_cost
    + storage_cost
    + data_transfer_cost
    + premium_charge
)

# Display the bill
print("===== CLOUD COMPUTING BILL =====")
print("CPU Cost: Rs.", cpu_cost)
print("Storage Cost: Rs.", storage_cost)
print("Data Transfer Cost: Rs.", data_transfer_cost)
print("Premium Charge: Rs.", premium_charge)
print("--------------------------------")
print("Total Cost: Rs.", total_cost)

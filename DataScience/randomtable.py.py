import pandas as pd
from faker import Faker
from collections import defaultdict
# Engine to push to DB's below. Not needed now...
# from sqlalchemy import create_engine
from faker_music import MusicProvider
from faker_vehicle import VehicleProvider


fake = Faker()
fake_data = defaultdict(list)
fake.add_provider(MusicProvider)
fake.add_provider(VehicleProvider)


for i in range(5000):
    fake_data["first_name"].append(fake.first_name() )
    fake_data["last_name"].append(fake.last_name() )
    fake_data["occupation"].append(fake.job() )
    fake_data["dob"].append(fake.date_of_birth() )
    fake_data["favorite_color"].append(fake.color_name() )
    fake_data["company"].append(fake.company() )
    fake_data["bank"].append(fake.aba() )
    fake_data["bank_country"].append(fake.bank_country() )
    fake_data["international_bank"].append(fake.iban() )
    fake_data["bank_value"].append(fake.iban() )
    fake_data["license_plate"].append(fake.license_plate() )
    fake_data["children"].append(fake.random_digit() )
    fake_data["email"].append(fake.free_email() )
    fake_data["music"].append(fake.music_genre() )
    fake_data["instrument"].append(fake.music_instrument() )
    fake_data["vehicle_year"].append(fake.vehicle_year() )
    fake_data["vehicle_type"].append(fake.vehicle_category() )
    fake_data["vehicle_make"].append(fake.vehicle_make() )
    
    
df_fake_data = pd.DataFrame(fake_data)
df_fake_data.to_csv('dummydata.csv', index=False)
print(df_fake_data)
# cleaning credentials for github...
# engine = create_engine('null://nate:null@null', echo=False)

print("pushing to engine now")
# df_fake_data.to_sql('arctictest', con=engine,index=False)
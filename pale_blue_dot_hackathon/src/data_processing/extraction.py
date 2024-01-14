from DataInmet import DataInmet

teste = DataInmet(path="/home/lucianbell/Documents/Projetos_Hackathons/PaleBlueDot_entry/pale_blue_dot_hackathon/data/raw/Dados_INMET/dados_B803_D_2023-01-01_2023-12-31.csv")

teste.convert_df()
teste.save_df(path="/home/lucianbell/Documents/Projetos_Hackathons/PaleBlueDot_entry/pale_blue_dot_hackathon/data/processed/INMET_Data/teste.csv")
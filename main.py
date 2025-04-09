import sys
import pandas as pd
import os
from datetime import datetime
import pytz    

def fecha_hora():
    # Define the Madrid timezone
    madrid_tz = pytz.timezone('Europe/Madrid')

    # Get the current date and time in Madrid timezone
    madrid_time = datetime.now(madrid_tz)

    # Format the time in ISO 8601 format without milliseconds or timezone info
    iso_format_time = madrid_time.strftime('%Y_%m_%dT%H_%M_%S')

    return iso_format_time

def process(fp:str="cursos.xls")->str:
    file_path = os.path.abspath(fp)


    # Load the Excel file
    # file_path = 'cursos.xls'  # Replace with your file path
    df = pd.read_excel(file_path)

    # Group by company and course
    columnas_grupo = ['EMPRESA', 'Curso']
    grouped = df.groupby(columnas_grupo)

    input_dir = os.path.dirname(file_path)
    # Create a directory to save the files if it doesn't exist
    output_dir = os.path.join(input_dir, f'convertido_{fecha_hora()}')  # Directory to hold the output files
    os.makedirs(output_dir, exist_ok=True)
    # for subdir in ["excels", "csvs"]:
        # os.makedirs(os.path.join(output_dir, subdir), exist_ok=True)

    # Iterate through each group and save to a separate Excel file
    last_path = ""
    for (company, course), group in grouped:
        company = company.strip()
        course = course.strip()
        columnas_salida = ["NIF", "APELLIDO1", "APELLIDO2", "NOMBRE", "Email"]

        # Create a new DataFrame without the company and course columns
        # group = group.drop(columns=columnas_grupo)
        group = group[columnas_salida]

        
        # Define the file name
        file_name = os.path.abspath(os.path.join(output_dir, f"{company}_{course}.xlsx"))
        # Save the group to an Excel file
        group.to_excel(file_name, index=False)
        # group.to_csv(os.path.abspath(os.path.join(output_dir, f"{company}_{course}.csv")), index=False)

        # print(f"Saved: {file_name}")
        # with open("results.txt", 'a') as f:
        #     f.write(f"[{fecha_hora()}] Saved: {file_name}\n")
    return f"\nGuardado en carpeta {output_dir}"



if __name__ == "__main__":
    process()

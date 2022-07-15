from colorama import Fore, init; init()
import httpx, json

class PmxLang:
    @staticmethod
    def parse(file_name: str):
        data = []

        with open(file_name, encoding='utf-8', errors='ignore') as pmx_file:
            for line in pmx_file:
                line = line.split('\n')[0].strip()

                # check if line is comment or blank
                if line.startswith('#') or line == '':
                    continue

                splitted = line.split('|')

                # METHOD|URL|PAYLOAD|HEADER
                data.append([splitted[0], splitted[1], None if splitted[2] == "NONE" else splitted[2], None if splitted[3] == "NONE" else splitted[3]])
        
        # [[url, method, payload, header], [url, method, payload, header], ...]
        return data

    def execute(parsed: list):
        responses = []

        for chunck in parsed:
            method, url, payload, header = chunck

            with httpx.Client(headers= json.loads(header)) as client:
                data = json.loads(payload) if payload != None else None

                if method == 'PUT':
                    requests_response = client.put(url, json=data)
                
                elif method == 'GET':
                    requests_response = client.get(url)
                
                if method == 'POST':
                    requests_response = client.post(url, json=data)

                # STATUS-CODE|TEXT
                responses.append(f'{str(requests_response.status_code)}|{requests_response.text}')
        
        return responses
    
    def beautify_response(responses: list):

        i = 0
        for response in responses:
            parsed = response.split('|')

            status_code = parsed[0]
            if status_code.startswith('2'):
                status_code = f'{Fore.LIGHTGREEN_EX}{status_code}{Fore.RESET}'
                
            elif status_code.startswith('4'):
                status_code = f'{Fore.LIGHTYELLOW_EX}{status_code}{Fore.RESET}'

            elif status_code.startswith('5'):
                status_code = f'{Fore.RED}{status_code}{Fore.RESET}'

            print(f'|-> REQUESTS #{Fore.YELLOW}{i}{Fore.RESET}\n| ╭ STATUS-CODE: {status_code}\n| ╰ JSON: {parsed[1]}\n\n')
            i += 1

parsed = PmxLang.parse('./step.pmx')
response = PmxLang.execute(parsed)
PmxLang.beautify_response(response)
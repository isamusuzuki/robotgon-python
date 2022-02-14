import json
import shutil
from os import mkdir, path

from apps.util.result import Result


def read_json() -> Result:
    """
    JSONファイルを読む

    Returns
    -------
    Result.data: dict
        command: str
        input_files: List[str]
        output_file: str
        input_file: str
        output_folder: str
        pages: List[int]
        clockwise: bool
    """
    result = Result(__name__)
    result.data = {
        'command': 'no_command',
        'input_files': [],
        'output_file': '',
        'input_file': '',
        'output_folder': '',
        "pages": [],
        "clockwise": False
    }

    json_file = 'temp/pdftool.json'
    if not path.exists(json_file):
        result.message = f'{json_file}がありません'
        return result
    else:
        # order.json を読む
        with open(json_file, mode='r', encoding='utf-8') as f:
            order_dict = json.loads(f.read())
        if 'command' not in order_dict:
            result.message = f'{json_file}にcommandキーがありません'
            return result
        else:
            command = order_dict['command']

            if command == 'merge':
                if 'input_files' not in order_dict:
                    result.message = f'{json_file}にinput_filesがありません'
                    return result
                elif 'output_file' not in order_dict:
                    result.message = f'{json_file}にoutput_fileがありません'
                    return result
                else:
                    result.data['command'] = command
                    result.data['input_files'] = order_dict['input_files']
                    result.data['output_file'] = order_dict['output_file']
                    result.success = True
                    return result
            elif command == 'split':
                if 'input_file' not in order_dict:
                    result.message = f'{json_file}にinput_fileがありません'
                    return result
                else:
                    input_file = order_dict['input_file']
                    # 出力先のフォルダを用意する
                    name_list = input_file.split('/')
                    file_name = name_list[len(name_list) - 1]
                    folder_name = file_name.replace('.pdf', '')
                    output_folder = f'temp/{folder_name}'
                    if path.exists(output_folder):
                        shutil.rmtree(output_folder)
                    mkdir(output_folder)
                    result.data['command'] = command
                    result.data['input_file'] = input_file
                    result.data['output_folder'] = output_folder
                    result.success = True
                    return result
            elif command == 'rotate':
                if 'input_file' not in order_dict:
                    result.message = f'{json_file}にinput_fileがありません'
                    return result
                elif 'output_file' not in order_dict:
                    result.message = f'{json_file}にoutput_fileがありません'
                    return result
                elif 'pages' not in order_dict:
                    result.message = f'{json_file}にpagesがありません'
                    return result
                elif 'clockwise' not in order_dict:
                    result.message = f'{json_file}にclockwiseがありません'
                    return result
                else:
                    result.data['command'] = command
                    result.data['input_file'] = order_dict['input_file']
                    result.data['output_file'] = order_dict['output_file']
                    result.data['pages'] = order_dict['pages']
                    result.data['clockwise'] = order_dict['clockwise']
                    result.success = True
                    return result
            else:
                result.message = f'「{command}」は想定外のコマンドです'
                return result

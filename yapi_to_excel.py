import requests
import json
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

class YapiToExcel:
    def __init__(self, yapi_url, token):
        self.yapi_url = yapi_url.rstrip('/')
        self.token = token
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'{token}'
        }
    
    def get_project_list(self):
        """获取项目列表"""
        url = f"{self.yapi_url}/api/project/list"
        params = {
            'page': 1,
            'limit': 100,
            'token': self.token
        }
        response = requests.get(url, headers=self.headers, params=params)
        result = response.json()
        if result and result.get('errcode') == 0:
            return result.get('data', {})
        return {}

    def get_interface_list(self, project_id):
        """获取项目下的接口列表"""
        url = f"{self.yapi_url}/api/interface/list"
        all_interfaces = []
        page = 1
        limit = 10  # 每页获取10条数据
        
        while True:
            params = {
                'project_id': project_id,
                'token': self.token,
                'page': page,
                'limit': limit
            }
            response = requests.get(url, params=params)
            result = response.json()
            if result and result.get('errcode') == 0:
                data = result.get('data', {})
                interfaces = data.get('list', [])
                all_interfaces.extend(interfaces)
                
                # 获取总数和当前数据数量
                total_count = data.get('count', 0)
                current_count = len(all_interfaces)
                
                # 如果已获取的数据量大于等于总数，或者当前页没有数据，则停止循环
                if not interfaces or current_count >= total_count:
                    break
                    
                page += 1
            else:
                break
                
        return all_interfaces
    
    def get_interface_detail(self, interface_id):
        """获取接口详情"""
        url = f"{self.yapi_url}/api/interface/get"
        params = {
            'id': interface_id,
            'token': self.token
        }
        response = requests.get(url, params=params)
        result = response.json()
        if result and result.get('errcode') == 0:
            return result.get('data', {})
        return {}
    
    def get_test_case_list(self, project_id):
        """获取项目下的测试用例列表"""
        url = f"{self.yapi_url}/api/test/list"
        params = {
            'project_id': project_id,
            'token': self.token
        }
        response = requests.get(url, params=params)
        result = response.json()
        if result and result.get('errcode') == 0:
            return result.get('data', [])
        return []
    
    def get_test_case_detail(self, test_case_id):
        """获取测试用例详情"""
        url = f"{self.yapi_url}/api/test/get"
        params = {
            'id': test_case_id,
            'token': self.token
        }
        response = requests.get(url, params=params)
        result = response.json()
        if result and result.get('errcode') == 0:
            return result.get('data', {})
        return {}
    
    def extract_test_case_data(self, interface_detail):
        """提取测试用例数据"""
        if not interface_detail:
            return None
            
        # 请求路径
        path = interface_detail.get('path', '')
        
        # 请求方法
        method = interface_detail.get('method', '')
        
        # 请求头
        req_headers = interface_detail.get('req_headers', [])
        headers_str = json.dumps(req_headers, ensure_ascii=False) if req_headers else ''
        
        # 请求参数
        req_params = interface_detail.get('req_params', [])
        req_query = interface_detail.get('req_query', [])
        req_body = interface_detail.get('req_body_other', '') or interface_detail.get('req_body_form', '')
        
        # 合并所有请求参数
        params_info = {
            'req_params': req_params,
            'req_query': req_query,
            'req_body': req_body
        }
        params_str = json.dumps(params_info, ensure_ascii=False)
        
        # 返回结果
        res_body = interface_detail.get('res_body', '')
        
        return {
            '接口名称': interface_detail.get('title', ''),
            '请求路径': path,
            '请求方法': method,
            '请求头': headers_str,
            '请求参数': params_str,
            '返回结果': res_body,
            '接口ID': interface_detail.get('_id', ''),
            '创建人': interface_detail.get('username', ''),
            '创建时间': interface_detail.get('add_time', ''),
            '更新时间': interface_detail.get('up_time', '')
        }
    
    def extract_test_collection_data(self, test_case_detail, project_name=""):
        """提取测试集合数据"""
        if not test_case_detail:
            return None
            
        # 提取测试用例基本信息
        case_name = test_case_detail.get('name', '')
        case_desc = test_case_detail.get('desc', '')
        
        # 提取请求信息
        case_req = test_case_detail.get('req', {})
        if case_req:
            path = case_req.get('url', '')
            method = case_req.get('method', '')
            
            # 请求头
            headers = case_req.get('headers', [])
            headers_str = json.dumps(headers, ensure_ascii=False) if headers else ''
            
            # 请求参数
            params = case_req.get('params', [])
            data = case_req.get('data', '')
            params_info = {
                'params': params,
                'data': data
            }
            params_str = json.dumps(params_info, ensure_ascii=False)
            
            # 预期响应
            res_body = case_req.get('res_body', '')
        else:
            path = ''
            method = ''
            headers_str = ''
            params_str = ''
            res_body = ''
        
        return {
            '项目名称': project_name,
            '测试用例名称': case_name,
            '测试用例描述': case_desc,
            '请求路径': path,
            '请求方法': method,
            '请求头': headers_str,
            '请求参数': params_str,
            '预期结果': res_body,
            '测试用例ID': test_case_detail.get('_id', ''),
            '创建人': test_case_detail.get('username', ''),
            '创建时间': test_case_detail.get('add_time', ''),
            '更新时间': test_case_detail.get('up_time', ''),
            '类型': '测试集合'
        }
    
    def export_project_to_excel(self, project_id, output_file):
        """导出项目接口到Excel"""
        # 获取接口列表
        interfaces = self.get_interface_list(project_id)
        if not interfaces:
            print("获取接口列表失败")
            return
        
        test_cases = []
        
        for interface in interfaces:
            interface_id = interface.get('_id')
            if interface_id:
                # 获取接口详情
                detail = self.get_interface_detail(interface_id)
                test_case_data = self.extract_test_case_data(detail)
                if test_case_data:
                    test_cases.append(test_case_data)
        
        # 创建DataFrame并导出到Excel
        if test_cases:
            df = pd.DataFrame(test_cases)
            df.to_excel(output_file, index=False)
            print(f"成功导出 {len(test_cases)} 个接口到 {output_file}")
        else:
            print("没有找到有效的接口数据")
    
    def export_all_projects_to_excel(self, output_file):
        """导出所有项目接口到Excel"""
        # 获取项目列表
        project_data = self.get_project_list()
        if not project_data:
            print("获取项目列表失败")
            return
        
        all_test_cases = []
        projects = project_data.get('list', [])
        
        for project in projects:
            project_id = project.get('_id')
            project_name = project.get('name')
            print(f"正在处理项目: {project_name}")
            
            # 获取接口列表
            interfaces = self.get_interface_list(project_id)
            if not interfaces:
                continue
            
            for interface in interfaces:
                interface_id = interface.get('_id')
                if interface_id:
                    # 获取接口详情
                    detail = self.get_interface_detail(interface_id)
                    test_case_data = self.extract_test_case_data(detail)
                    if test_case_data:
                        test_case_data['项目名称'] = project_name
                        all_test_cases.append(test_case_data)
            
            # 获取测试用例列表
            test_cases = self.get_test_case_list(project_id)
            if test_cases:
                for test_case in test_cases:
                    test_case_id = test_case.get('_id')
                    if test_case_id:
                        # 获取测试用例详情
                        detail = self.get_test_case_detail(test_case_id)
                        test_collection_data = self.extract_test_collection_data(detail, project_name)
                        if test_collection_data:
                            all_test_cases.append(test_collection_data)
        
        # 创建DataFrame并导出到Excel
        if all_test_cases:
            df = pd.DataFrame(all_test_cases)
            # 调整列顺序，将项目名称放在前面
            cols = df.columns.tolist()
            if '项目名称' in cols:
                cols.remove('项目名称')
                cols.insert(0, '项目名称')
                df = df[cols]
            
            df.to_excel(output_file, index=False)
            print(f"成功导出 {len(all_test_cases)} 个接口到 {output_file}")
        else:
            print("没有找到有效的接口数据")

def main():
    
    # 直接定义常量
    YAPI_URL = "your_yapi_server_url"  # 替换为你的Yapi服务器地址
    TOKEN = "your_token"  # 替换为你的Yapi访问token
    PROJECT_ID = None  # 项目ID，如果为None则导出所有项目
    OUTPUT_FILE = "yapi_test_cases.xlsx"  # 输出Excel文件名
    
    yapi_client = YapiToExcel(YAPI_URL, TOKEN)
    
    if PROJECT_ID:
        yapi_client.export_project_to_excel(PROJECT_ID, OUTPUT_FILE)
    else:
        yapi_client.export_all_projects_to_excel(OUTPUT_FILE)

if __name__ == "__main__":
    main()

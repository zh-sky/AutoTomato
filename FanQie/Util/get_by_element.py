from Util.read_ini import ReadIni


class GetByElement:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, section, key):
        read_ini = ReadIni()
        local_element = read_ini.get_value(section, key)
        print(local_element)
        if local_element is not None:
            by = local_element.split('>')[0]
            print(by)
            local_by = local_element.split('>')[1]
            print(local_by)
            try:
                if by == 'id':
                    return self.driver.find_element_by_id(str(local_by))
                elif by == 'ios_predicate':
                    return self.driver.find_elements_by_ios_predicate(str(local_by))
            except:
                return None
        else:
            return None


if __name__ == '__main__':
    by = GetByElement()
    by.get_element('login_element', 'username')
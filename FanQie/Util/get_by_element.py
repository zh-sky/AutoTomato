from Util.read_ini import ReadIni


class GetByElement:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, section, key):
        read_ini = ReadIni()
        local_element = read_ini.get_value(section, key)
        if local_element is not None:
            by = local_element.split('>')[0]
            local_by = local_element.split('>')[1]
            try:
                if by == 'id':
                    return self.driver.find_element_by_id(local_by)
                elif by == 'ios_predicate':
                    return self.driver.find_element_by_ios_predicate(local_by)
            except:
                return None
        else:
            return None

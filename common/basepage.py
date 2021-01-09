"""
Description: 对webdriver的二次封装
Version: 2.0
Autor: byh
Date: 2020-11-23 14:28:20
LastEditors: byh
LastEditTime: 2020-12-11 17:16:20
还需改进
"""
import time
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from middleware.logger_handler import logger
from config.config_path import Configuration
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    """
    将元素的一些常用操作封装在basepage类，其他页面操作类直接继承这个模块即可
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_ele_visible(self, loc, page_name, timeout=20, poll_time=0.5):
        """
        description : 等待元素可见
        loc: 元素定位表达式
        page_name ： 页面名称
        timeout：超时时间
        poll_time：轮询时间
        """
        logger.info("在{} 等待元素{}可见".format(page_name, loc))
        try:
            WebDriverWait(self.driver, timeout, poll_time).until(EC.visibility_of_element_located(loc))
        except Exception as e:
            self.save_page_Screenshot(page_name)
            logger.exception("等待{}元素可见失败".format(loc))
            raise e
        else:
            logger.info("{}元素可见".format(loc))

    def get_element(self, loc, page_name):
        """
        description : 查找元素,不需要设置等待
        loc: 元素定位表达式
        page_name : 页面名称
        """
        logger.info("在{} 查找{}元素".format(page_name, loc))
        try:
            ele = self.driver.find_element(*loc)
        except Exception as e:
            self.save_page_Screenshot(page_name)
            logger.exception("查找{}元素失败".format(loc))
            raise e
        else:
            logger.info("{}元素找到，返回值为：{}".format(loc, ele))
            return ele

    def get_elements(self, loc, page_name):
        """
        description : 根据一个定位表达式查找多个元素,返回值为列表，不设置显性等待
        loc：元素定位表达式
        page_name：页面名称
        """
        logger.info("在{} 获取{}的多个元素")
        try:
            eles = self.driver.find_elements(*loc)
        except Exception as e:
            self.save_page_Screenshot(page_name)
            logger.exception("查找{}元素们失败".format(loc))
            raise e
        else:
            logger.info("{}元素们找到，返回值为：{}".format(loc, eles))
            return eles

    def click_ele(self, loc, page_name, timeout=20, poll_time=0.5):
        """
        description : 对元素进行点击操作
        loc : 元素定位表达式
        page_name：页面名称
        timeout：超时时间
        poll_time：轮询时间
        """
        # 等待该元素可见
        self.wait_ele_visible(loc, page_name, timeout, poll_time)
        logger.info("在{} 点击{}元素".format(page_name, loc))
        try:
            self.driver.find_element(*loc).click()
        except Exception as e:
            self.save_page_Screenshot(page_name)
            logger.exception("点击元素{}失败".format(loc))
            raise e
        else:
            logger.info("点击{}元素成功".format(loc))

    def input_keys(self, loc, keys, page_name, timeout=20, poll_time=0.5):
        """
        description : 输入框中输入文本
        loc: 元素定位表达式
        keys: 文本值
        page_name ： 页面名称
        timeout：超时时间
        poll_time：轮询时间
        """
        self.wait_ele_visible(loc, page_name, timeout=20, poll_time=0.5)
        logger.info("在{} 的文本框{}进行输入".format(page_name, loc))
        try:
            self.driver.find_element(*loc).send_keys(keys)
        except Exception as e:
            self.save_page_Screenshot(page_name)
            logger.exception("在输入框{}输入文本失败".format(e))
            raise e
        else:
            logger.info("输入的内容为：{}".format(keys))

    def get_ele_attr(self, loc, Attribute_name, page_name, timeout=20, poll_time=0.5):
        """
        description : 获取元素的属性值
        loc: 元素定位表达式
        Attribute_name：属性名
        page_name ： 页面名称
        timeout：超时时间
        poll_time：轮询时间
        """
        self.wait_ele_visible(loc, page_name, timeout=20, poll_time=0.5)
        logger.info("在{} 获取{}元素的属性".format(page_name, loc))
        try:
            value = self.driver.find_element(*loc).get_attribute(Attribute_name)
        except Exception as e:
            self.save_page_Screenshot(page_name)
            logger.exception("获取{}元素的属性失败".format(loc))
            raise e
        else:
            logger.info("该元素的属性值为:{}".format(value))
            return value

    def get_ele_text(self, loc, page_name, timeout=20, poll_time=0.5):
        """
        description : 获取元素的文本值
        loc：元素定位表达式
        page_name ： 页面名称
        timeout：超时时间
        poll_time：轮询时间
        """
        self.wait_ele_visible(loc, page_name, timeout, poll_time)
        logger.info("在{} 获取{}元素的文本值".format(page_name, loc))
        try:
            text = self.driver.find_element(*loc).text
        except Exception as e:
            self.save_page_Screenshot(page_name)
            logger.exception("获取元素{}的文本失败".format(loc))
            raise e
        else:
            logger.info("该元素的文本值为：{}".format(text))
            return text

    def get_ele_texts(self, loc, page_name, timeout=20, poll_time=0.5):
        """
        description : 获取多个元素的文本值，为列表
        loc：元素定位表达式
        page_name ： 页面名称
        timeout：超时时间
        poll_time：轮询时间
        """
        # 设置等待时间
        self.wait_ele_visible(loc, page_name, timeout=20, poll_time=0.5)
        logger.info("在{} 获取{}元素们的文本".format(page_name, loc))
        try:
            eles_list = self.driver.find_elements(*loc)
        except Exception as e:
            self.save_page_Screenshot(page_name)
            logger.exception("获取多个元素{}失败".format(loc))
            raise e
        else:
            texts_list = []
            if len(eles_list) == 1:
                logger.info("获取的文本为：{}".format(eles_list[0].text))
                return eles_list[0].text
            else:
                for ele in eles_list:
                    texts_list.append(ele.text)
                logger.info("获取的文本为：{}".format(texts_list))
                return texts_list

    def save_page_Screenshot(self, page_name):
        """
        description : 对页面进行截图
        page_name: 页面的名字
        """
        now = time.strftime("%y-%m-%d %H_%M_%S")
        name = "{}_{}.png".format(page_name, now)
        shot_path = os.path.join(Configuration.screenshot, name)
        self.driver.save_screenshot(shot_path)
        logger.info("当前截图存储在:{}".format(shot_path))

    def move_to_ele(self, loc, page_name, timeout=20, poll_time=0.5):
        """
        description : 获取多个元素的文本值，为列表
        loc：元素定位表达式
        page_name ： 页面名称
        timeout：超时时间
        poll_time：轮询时间
        """
        # 设置等待时间
        self.wait_ele_visible(loc, page_name, timeout, poll_time)
        ele = self.get_element(loc, page_name)
        logger.info("在{} 将鼠标移动到{}元素上".format(page_name, loc))
        try:
            ActionChains(self.driver).move_to_element(ele).perform()
        except Exception as e:
            self.save_page_Screenshot(page_name)
            logger.expection("鼠标移动到元素上操作失败")
            raise e
        else:
            logger.info("鼠标移动到元素上操作成功")

    def wait_ele_clickale(self, loc, page_name, timeout=20, poll_time=0.5):
        """
        description : 等待元素可见并且可以被点击,然后进行点击
        loc：元素定位表达式
        page_name：页面名称
        time_out: 超时时间
        polling_time:轮询时间
        """
        logger.info("在{} 等待{}元素可见并且可以被点击".format(page_name, loc))
        try:
            WebDriverWait(self.driver, timeout, poll_time).until(EC.element_to_be_clickable(loc))
        except Exception as e:
            self.save_page_Screenshot(page_name)
            logger.exception("等待元素{}可见可点击失败".format(loc))
        else:
            logger.info("对{}进行点击".format(loc))
            self.driver.find_element(*loc).click()
            logger.info("点击操作成功")

    def switch_to_window(self, subscript, page_name):
        """
        description : 切换到新的窗口
        Subscript : 窗口下标
        page_name : 页面名称
        """
        wins = self.driver.window_handles
        logger.info("在{} 进行切换窗口".format(page_name))
        try:
            self.driver.switch_to.window(wins[subscript])
        except Exception as e:
            self.save_page_Screenshot(page_name)
            logger.exception("切换窗口失败")
            raise e
        else:
            logger.info("切换窗口成功")

    def switch_to_iframe(self, loc, page_name, time_out=20, poll_time=0.5):
        """
        description : 切换到内联框架iframe中
        loc：元素定位表达式，也可以是下标，name，ele对象
        page_name：页面名称
        time_out: 超时时间
        polling_time:轮询时间
        """
        logger.info("在{} 切换到{}iframe框架中".format(page_name, loc))
        try:
            WebDriverWait(self.driver, time_out, poll_time).until(EC.frame_to_be_available_and_switch_to_it(loc))
        except Exception as e:
            self.save_page_Screenshot(page_name)
            logger.exception("切换到{}iframe框架失败".format(loc))
            raise e
        else:
            logger.info("切换到{}iframe框架成功".format(loc))

    def switch_to_alert(self, page_name, dismiss=False, keys=None):
        """
        description :切换到警告框并进行操作
        dismiss : 取消按钮，默认为False，
        keys ： 输入的文本值
        """
        logger.info("在{} 切换到alert框".format(page_name))
        try:
            alert = self.driver.switch_to.alert()
        except Exception as e:
            self.save_page_Screenshot(page_name)
            logger.exception("切换到alert框失败")
            raise e
        else:
            if keys:
                alert.send_keys(keys)
                if dismiss:
                    alert.dismiss()
                else:
                    alert.accept()
            else:
                if dismiss:
                    alert.dismiss()
                else:
                    alert.accept()


if __name__ == "__main__":
    # driver = webdriver.Chrome()
    # driver.get("http://www.baidu.com")
    # driver.maximize_window()

    # a=(By.XPATH,'//span[@id="s-usersetting-top"]')
    # b=(By.XPATH,'//span[@id="adv-setting-ft"]//p[@class="c-select-item"]')
    # b1=(By.XPATH,'//span[@id="adv-setting-ft"]//i[@class="c-icon c-select-arrow"]')
    # c = (By.XPATH,'//a[text()="高级搜索"]')
    # bp = BasePage(driver)
    # bp.move_to_ele(a,"百度首页_设置按钮")
    # bp.click_ele(c,"百度首页_点击高级搜索")
    # bp.click_ele(b1,"百度首页_点击向下按钮")
    # li = bp.get_ele_texts(b,"百度首页_获取搜索框中的文本")
    # print(li)
    # driver.close()
    pass

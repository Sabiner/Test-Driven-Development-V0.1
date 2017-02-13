# -*- coding:utf-8 -*-

from .base import FunctionalTest

class LayoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling(self):
        # 伊迪丝访问首页
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        # 她会看到输入框完美的居中显示
        inputbox = self.get_item_input_box()
        ## 通过一定数学计算，判断输入框是否位于正中，指定结果在正负五像素范围内都可以接受
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )

        import time
        time.sleep(1)

        # 她新建了一个清单，看到输入框仍完美的居中显示
        inputbox.send_keys('testing\n')
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )

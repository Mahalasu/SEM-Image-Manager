import os
import psycopg2
import time as time_module
import shutil

from PyQt5.QtWidgets import QMessageBox

from getMGLMFeatures import getGLCMFeatures

SEM_IMAGE_DIRECTORY_PATH = './SEM_Image'
CRAFT_IMAGE_DIRECTORY_PATH = './Craft_Image'
FORCE_IMAGE_DIRECTORY_PATH = './Force_Image'
BARK_IMAGE_DIRECTORY_PATH = './Bark_Image'


# search whether file with name 'filename' is in path
def search_file(path, filename):
    content = os.listdir(path)
    for each in content:
        if filename == each:
            return path + os.sep + each
    return ''


# manipulate sem images when inserting
def manipulate_sem_image_insert(src, dist, image_name):
    os.rename(src, dist + os.sep + image_name)


# manipulate sem images when modifying
def manipulate_sem_image_modify(file_info, dist, image_name, prev_file_info):
    os.remove(prev_file_info[8])
    os.rename(file_info.image_path, dist + os.sep + image_name)


# manipulate images other than sem when inserting
def manipulate_other_image_insert(src, dist):
    content = os.listdir(dist)
    if src.split('/')[-1] in content:
        return
    else:
        shutil.copy(src, dist)


# move images when inserting
def move_images_insert(file_info, name):
    manipulate_sem_image_insert(file_info.image_path, SEM_IMAGE_DIRECTORY_PATH, name)

    if file_info.craft_image_path:
        manipulate_other_image_insert(file_info.craft_image_path, CRAFT_IMAGE_DIRECTORY_PATH)

    if file_info.force_image_path:
        manipulate_other_image_insert(file_info.force_image_path, FORCE_IMAGE_DIRECTORY_PATH)

    if file_info.bark_image_path:
        manipulate_other_image_insert(file_info.bark_image_path, BARK_IMAGE_DIRECTORY_PATH)


# manipulate images other than SEM when modifying
def manipulate_other_images_modify(file_info, prev_image_info):
    if file_info.craft_image_path and file_info.craft_image_path != prev_image_info[9]:
        manipulate_other_image_insert(file_info.craft_image_path, CRAFT_IMAGE_DIRECTORY_PATH)

    if file_info.force_image_path and file_info.force_image_path != prev_image_info[10]:
        manipulate_other_image_insert(file_info.force_image_path, FORCE_IMAGE_DIRECTORY_PATH)

    if file_info.bark_image_path and file_info.bark_image_path != prev_image_info[11]:
        manipulate_other_image_insert(file_info.bark_image_path, BARK_IMAGE_DIRECTORY_PATH)


class Database:

    def __init__(self):
        self.conn = psycopg2.connect(database="sem_image_manager", user="postgres",
                                     password="123456", host="127.0.0.1", port="5432")
        print("连接成功")

    # return all rows
    def get_all_rows(self):
        with self.conn.cursor() as cur:
            cur.execute("select * from image_info;")
            rows = cur.fetchall()

        return rows

    # return info from metallographic_info
    def get_all_rows_from_metallographic(self):
        with self.conn.cursor() as cur:
            cur.execute("select metallographic from metallographic_info;")
            rows = cur.fetchall()

        return rows

    # search information of image named with name
    def search_info(self, name):
        with self.conn.cursor() as cur:
            cur.execute("select * from image_info where name = {1}{0}{1};".format(name, "'"))
            result = cur.fetchall()[0]

        return result

    # search information of metallographic using mid
    def search_metal(self, mid):
        with self.conn.cursor() as cur:
            cur.execute("select metallographic from metallographic_info where id = {0}".format(mid))
            result = cur.fetchall()[0][0]

        return result

    # return information of image after searching
    def search_image(self, temp, time, craft, amp_factor):
        temp = "temp = " + temp if temp else ""
        time = "time = " + time if time else ""
        craft = "craft = {1}{0}{1}".format(craft, "'") if craft else ""
        amp_factor = "amp_factor = " + amp_factor if amp_factor else ""
        seq = []
        if temp:
            seq.append(temp)
        if time:
            seq.append(time)
        if craft:
            seq.append(craft)
        if amp_factor:
            seq.append(amp_factor)
        condition = " where " + " and ".join(seq)
        with self.conn.cursor() as cur:
            cur.execute("select name from image_info" + condition)
            result = cur.fetchall()

        return result

    # check whether the info imputed is sufficient and correct
    def check(self, name, amp_factor, file_info, mid):
        if not name:
            msg_box = QMessageBox(QMessageBox.Warning, "警告", "请输入图片名称！")
            msg_box.exec_()
            return False

        if mid == 0:
            msg_box = QMessageBox(QMessageBox.Warning, "警告", "请选择组织名称！")
            msg_box.exec_()
            return False

        if not amp_factor:
            msg_box = QMessageBox(QMessageBox.Warning, "警告", "请输入放大倍数！")
            msg_box.exec_()
            return False

        if not file_info.image_path:
            msg_box = QMessageBox(QMessageBox.Warning, "警告", "请选择SEM图片！")
            msg_box.exec_()
            return False

        return True

    # insert an image
    def insert(self, name, temp, time, amp_factor, craft, no, content, mid, file_info):

        is_sufficient = self.check(name, amp_factor, file_info, mid)
        if not is_sufficient:
            return

        name = name + '.' + file_info.image_path.split('/')[-1].split('.')[-1]
        path = search_file(SEM_IMAGE_DIRECTORY_PATH, name)
        if path:
            msg_box = QMessageBox(QMessageBox.Warning, "警告", "图片名已存在！")
            msg_box.exec_()
            return
        temp = temp if temp else None
        time = time if time else None
        craft = craft if craft else ''
        no = no if no else ''
        content = content if content else ''

        image_path = SEM_IMAGE_DIRECTORY_PATH + '/' + name
        craft_image_path = CRAFT_IMAGE_DIRECTORY_PATH + '/' + file_info.craft_image_path.split('/')[
            -1] if file_info.craft_image_path else file_info.craft_image_path
        force_image_path = FORCE_IMAGE_DIRECTORY_PATH + '/' + file_info.force_image_path.split('/')[
            -1] if file_info.force_image_path else file_info.force_image_path
        bark_image_path = BARK_IMAGE_DIRECTORY_PATH + '/' + file_info.bark_image_path.split('/')[
            -1] if file_info.bark_image_path else file_info.bark_image_path
        category_feature_descriptor = getGLCMFeatures(file_info.image_path)
        category_feature_descriptor = category_feature_descriptor.tobytes().hex()

        with self.conn.cursor() as cur:
            sql = """insert into image_info (name, mid, temp, time, craft, amp_factor, no, content, 
            image_path, craft_image_path, force_image_path, bark_image_path, category_feature_descriptor, update_time) 
            values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
            para = [name, mid, temp, time, craft, amp_factor, no, content, image_path, craft_image_path,
                    force_image_path, bark_image_path, category_feature_descriptor, time_module.strftime("%Y-%m-%d",
                                                                                                         time_module.
                                                                                                         localtime())]
            cur.execute(sql, para)
            self.conn.commit()

        move_images_insert(file_info, name)

    # delete image
    def delete(self, image_info):
        with self.conn.cursor() as cur:
            image_name = image_info[0]
            image_path = image_info[8]
            os.remove(image_path)

            craft_image_path = image_info[9]
            if craft_image_path:
                cur.execute(
                    """select count(*) from image_info where craft_image_path = '{0}'""".format(craft_image_path))
                count = cur.fetchall()[0][0]
                if count == 1:
                    os.remove(craft_image_path)

            force_image_path = image_info[10]
            if force_image_path:
                cur.execute(
                    """select count(*) from image_info where force_image_path = '{0}'""".format(force_image_path))
                count = cur.fetchall()[0][0]
                if count == 1:
                    os.remove(force_image_path)

            bark_image_path = image_info[11]
            if bark_image_path:
                cur.execute(
                    """select count(*) from image_info where bark_image_path = '{0}'""".format(bark_image_path))
                count = cur.fetchall()[0][0]
                if count == 1:
                    os.remove(bark_image_path)

            cur.execute("delete from image_info where name = '{0}';".format(image_name))
            self.conn.commit()

    # modify an image
    def modify(self, name, temp, time, amp_factor, craft, no, content, mid, file_info, prev_image_info):
        is_sufficient = self.check(name, amp_factor, file_info, mid)
        if not is_sufficient:
            return

        prev_name = prev_image_info[0]
        prev_image_type = prev_name.split('.')[-1]
        if '.' not in name:
            name = name + '.' + prev_image_type
        if name != prev_name:
            path = search_file(SEM_IMAGE_DIRECTORY_PATH, name)
            if path:
                msg_box = QMessageBox(QMessageBox.Warning, "警告", "图片名已存在！")
                msg_box.exec_()
                return

            if file_info.image_path == prev_image_info[8]:
                src = file_info.image_path
                file_info.image_path = SEM_IMAGE_DIRECTORY_PATH + '/' + name
                os.rename(src, file_info.image_path)
        else:
            if file_info.image_path != prev_image_info[8]:
                manipulate_sem_image_modify(file_info, SEM_IMAGE_DIRECTORY_PATH, name, prev_image_info)
                file_info.image_path = SEM_IMAGE_DIRECTORY_PATH + '/' + name

        with self.conn.cursor() as cur:
            sql = """update image_info set name = %s, mid = %s, temp = %s, time = %s, craft = %s, amp_factor = %s, no = 
            %s, content = %s, image_path = %s, craft_image_path = %s, force_image_path = %s, bark_image_path = %s, 
            category_feature_descriptor = %s, update_time = %s where name = %s;"""

            original_name = prev_image_info[0]
            temp = None if temp == 'None' else temp
            time = None if time == 'None' else time
            image_path = file_info.image_path
            craft_image_path = file_info.craft_image_path
            force_image_path = file_info.force_image_path
            bark_image_path = file_info.bark_image_path
            category_feature_descriptor = getGLCMFeatures(file_info.image_path)
            category_feature_descriptor = category_feature_descriptor.tobytes().hex()
            para = [name, mid, temp, time, craft, amp_factor, no, content, image_path, craft_image_path,
                    force_image_path, bark_image_path, category_feature_descriptor,
                    time_module.strftime("%Y-%m-%d", time_module.localtime()), original_name]
            cur.execute(sql, para)
            self.conn.commit()

        manipulate_other_images_modify(file_info, prev_image_info)

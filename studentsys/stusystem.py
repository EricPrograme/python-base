# --*--coding:utf-8--*--

# author : hmchen
# email  : hmchen@cenboomh.com
# date   : 2021/1/29 9:38


"""
学生管理系统，主函数

"""
import os

filename ='student.txt'


def main():
    while True:
        menu()
        choice = int(input("请选择系统功能:"))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice == 0:
                answer = input("你确定要退出系统吗 ? Y/N")
                if answer == "Y" or answer == "y":
                    print("谢谢你的使用。")
                    break
                else:
                    continue
            elif choice == 1:
                # 1.录入学生信息
                insert()
            elif choice == 2:
                # 2.查询学生信息
                search()
            elif choice == 3:
                # 3.删除学生信息
                delete()
            elif choice == 4:
                # 4.修改学生信息
                modify()
            elif choice == 5:
                # 5.排序
                sort()
            elif choice == 6:
                # 6.统计学生总人数
                total()
            elif choice == 7:
                # 7.显示所有学生信息
                show()


def insert():
    students_list =[]
    while True:
        id = input("请输入学生编号(如：ID 1001)")
        if not id:
            break
        name = input("请输入学生姓名")
        if not name:
            break
        try:
            english = int(input("请输入英语成绩"))
            python = int(input("请输入Python成绩"))
            java = int(input("请输入java成绩"))
        except:
            print("输入无效，不是数字类型，请重新输入。")
            continue

        # 将录入的信息保存到字典中
        student = {'id': id, 'name': name, 'english': english, 'python': python, 'java': java}
        # 将学生的信息添加到学生列表中
        students_list.append(student)

        answer = input("是否继续添加学生信息？ Y/N \n")
        if answer == 'Y' or answer == 'y':
            continue
        else:
            break

    # 保存学生信息Save()
    save(students_list)
    print("学生信息录入完毕！")


def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()


def search():
    student_query = []
    while True:
        id = ""
        name = ""
        if os.path.exists(filename):
            mode = input("按照ID查找，请输入1，按姓名查找，请输入2")
            if mode == '1':
                id = input("请输入学生ID")
            elif mode == '2':
                name = input("请输入学生姓名")
            else:
                print("您的输入有误，请重新输入")
                search()

            with open(filename, 'r', encoding="utf-8") as rfile:
                student = rfile.readlines()
                for item in student:
                    d = dict(eval(str(item)))
                    if id != "":
                        if d['id'] == id:
                            student_query.append(d)
                    elif name != "":
                        if d['name'] == name:
                            student_query.append(d)

            # 显示查询结果
            show_student(student_query)
            # 清空列表
            student_query.clear()
            answer = input("是否继续查询? Y/N \n")
            if answer == "Y" or answer == "y":
                continue
            else:
                break

        else:
            print("暂未保存学生信息")
            return


def show_student(lst):
    if len(lst) == 0:
        print("没有查询到学生信息,无数据显示")
        return
    # 定义标题格式显示
    format_title = "{:^6}\t {:^12}\t {:^8}\t{:^10}\t{:^10}\t{:^8}"
    print(format_title.format("ID", "姓名", "英语成绩", "Python成绩", "JAVA成绩", "总成绩"))
    # 定义内容的显示格式
    format_date = "{:^6}\t {:^12}\t {:^9}\t{:^15}\t{:^11}\t{:^8}"
    for item in lst:
        print(format_date.format(item.get("id"),
                                 item.get("name"),
                                 item.get("english"),
                                 item.get("python"),
                                 item.get("java"),
                                 int(item.get("english")+item.get("python")+item.get("java"))))


def delete():
    while True:
        student_id = input("请选择需要删除的学生编号")
        if student_id != "":
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()
            else:
                student_old= []
            #  标记是否删除
            flag = False
            if student_old:
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d = {}
                    for item in student_old:
                        # 将字符串转换为字典
                        d = dict(eval(str(item)))
                        if d['id'] != student_id:
                            wfile.write(str(d)+'\n')
                        else:
                            flag = True

                    if flag:
                        print(f"id为{student_id}的学生信息已经被删除。")
                    else:
                        print(f"没有找到id为{student_id}的学生信息。")
            else:
                print("无学生信息")
                break

            show()

            answer = input("是否继续删除? Y/N \n")
            if answer == 'Y' or answer == 'y':
                continue
            else:
                break


def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_old = rfile.readlines()
            print("student_old", student_old)
    else:
        return
    student_id = int(input("请输入要修改学员的ID："))
    with open(filename, 'w', encoding='utf-8') as wfile:
        for item in student_old:
            d = dict(eval(item))
            print("d['id'] = ",type(d['id']))
            print("id(d['id'])) =", id(d['id']))
            print("id(student_id)", id(student_id))
            print("type(student_id)", type(student_id))
            print("student_id = ", student_id)
            print(d['id']==student_id)

            if d['id'] == student_id:
                print("找到学生信息，可以修改他的相关信息了")
                while True:
                    try:
                        d['name']=input("请输入姓名")
                        d['english'] = input("请输入英语成绩")
                        d['python'] = input("请输入Python成绩")
                        d['java'] = input("请输入JAVA成绩")
                    except:
                        print("您输入有误，请重新输入")
                    else:
                        break
                wfile.write(str(d)+'\n')
                print("修改成功！")
            else:
                wfile.write(str(d)+'\n')

        answer = input("是否继续修改其他学生信息？ Y/N \n")
        if answer == 'Y' or answer == 'y':
            modify()



def sort():
    pass


def total():
    pass


def show():
    pass


def menu():
    print("======================学生信息管理系统===========================")
    print("-----------------------功能菜单----------------------------------")
    print("\t\t\t\t  1.录入学生信息")
    print("\t\t\t\t  2.查询学生信息")
    print("\t\t\t\t  3.删除学生信息")
    print("\t\t\t\t  4.修改学生信息")
    print("\t\t\t\t  5.排序")
    print("\t\t\t\t  6.统计学生总人数")
    print("\t\t\t\t  7.显示所有学生信息")
    print("\t\t\t\t  0.退出")
    print("------------------------------------------------------------------")


if __name__ == '__main__':
    main()
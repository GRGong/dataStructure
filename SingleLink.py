#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: Gong
'''
single link list implemented in python.
'''

class Node(object):
    def __init__(self,ele):
        self.next = None
        self.ele = ele


class SingleLinkList(object):
    def __init__(self,header = None):
        self.__head = header

    def index(self, item):
        '''
        :param item:
        :return: index of item else None
        '''
        count = 0
        cur = self.__head
        result = None
        if not self.is_empty():
            while cur.next:
                if cur.ele == item:
                    result = count
                    break
                else:
                    count += 1
                    cur = cur.next
            if cur.ele == item:
                result = count
        return result

    def search(self, item):
        '''
        :param item:
        :return: True or False
        '''
        cur = self.__head
        while cur:
            if cur.ele == item:
                return True
            cur = cur.next
        return False

    def removeall(self, item):
        '''
        remove all nodes equal item
        '''
        pre = self.__head
        while pre.ele == item:
            self.__head = pre.next
            pre = self.__head
        while pre.next:
            if pre.next.ele == item:

                pre.next = pre.next.next
            else:
                pre = pre.next

    def remove(self, item):
        '''
        remove first node equal item
        '''
        pre = self.__head
        if pre.ele == item:
            self.__head = pre.next
            pre = self.__head
        else:
            while pre.next:
                if pre.next.ele == item:
                    pre.next = pre.next.next
                    break
                else:
                    pre = pre.next


    def insert(self, pos, item):
        '''
        insert node in front of certain position
        :param pos:
        :param item:
        '''
        pre = self.__head
        count = 1
        if 0 < pos <= self.length()-1 :
            while count != pos:
                pre = pre.next
                count += 1
            node = Node(item)
            node.next = pre.next
            pre.next = node
        elif pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)


    def travel(self):
        cur = self.__head
        while cur:
            print(cur.ele)
            cur = cur.next

    def append(self, item):
        '''
        add item behind the last
        :param item:
        '''
        node = Node(item)
        cur = self.__head
        if self.__head:
            while cur.next:
                cur = cur.next
            cur.next = node
        else:
            self.__head = node

    def is_empty(self):
        '''
        if empty
        '''
        return self.__head == None

    def add(self,item):
        '''
        :param item:
        add item in front of head
        '''
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def length(self):
        cur = self.__head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

# if __name__ == "__main__":
#     a = SingleLinkList()
#     print(a.is_empty())
#     print(a.length())
#     a.travel()
#     a.append(1)
#     a.append(2)
#     a.append(3)
#     a.append(3)
#     a.append(3)
#     a.append(4)
#     a.append(4)
#     a.append(4)
#     a.add(0)
#     a.add(0)
#     a.add(0)
#     a.add(0)
#     a.add(0)
#     print(a.length())
#     a.travel()
#     print(a.is_empty())
#     a.insert(10,"test")
#     a.travel()
#     #print(a.search(0))
#     a.removeall(4)
#
#     a.travel()






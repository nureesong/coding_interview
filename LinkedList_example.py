'''
Linked List 클래스 구현하기
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        dummy = Node("dummy")
        self.head = dummy
        self.tail = dummy
        self.current = None
        self.before = None
        self.num_of_data = 0


    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node # 맨 뒤(tail 뒤)에 노드 추가
        self.tail = new_node      # tail을 새로 추가된 노드로 변경
        self.num_of_data += 1


    def delete(self):
        pop_data = self.current.data # current 노드 삭제

        if self.current is self.tail: # 만약 current 노드가 tail이었다면
            self.tail = self.before   # tail을 before 노드로 변경

        self.before.next = self.current.next # before를 current의 next에 연결
        self.current = self.before  # current를 next가 아닌 before로 변경!!
        self.num_of_data -= 1
        return pop_data


    def first(self):  # 맨 앞 노드 검색 (head 말고)
        if self.num_of_data == 0: 
            return None  # 데이터가 없는 경우 첫번째 노드도 없기 때문에 None 리턴

        self.before = self.head   # before는 head 즉, dummy가 된다.
        self.current = self.head.next  # current는 head가 가르키는 곳
        return self.current.data


    # next를 호출하기 이전에 first 메소드가 한번은 실행되어야 함.
    def next(self):  # current 노드의 다음 노드 검색
        if self.current.next == None:
            return None

        # 현 위치의 다음 노드를 검색+출력만 해주는 게 아니라 포커스를 이동시켜줘야 한다.
        # 따라서, 바로 self.current.next를 리턴하면 안 되고
        # before에 current를 할당하고 current에 next를 할당하여 포커스를 이동시킨 후
        # self.current.data(요청한 위치의 next 노드)를 리턴한다.
        self.before = self.current 
        self.current = self.current.next
        return self.current.data


    def size(self):
        return self.num_of_data



if __name__ == '__main__':
    l_list = LinkedList()
    l_list.append(5)
    l_list.append(2)
    l_list.append(1)
    l_list.append(2)
    l_list.append(7)
    l_list.append(2)
    l_list.append(11)

    print('='*20)
    print('first :', l_list.first())        # first : 5
    print('next :', l_list.next())          # next : 2, [5 2(current) 1 2 7 2 11]
    print('size :', l_list.size())          # size : 7
    print('delete :', l_list.delete())      # delete : 2, [5(current) 1 2 7 2 11]
    print('size :', l_list.size())          # size : 6
    print('current :', l_list.current.data) # current: 5
    print('tail :', l_list.tail.data)       # tail: 11, [5(current) 1 2 7 2 11], tail을 호출해도 current는 안 변함!
    print('first :', l_list.first())        # first : 5, [5(current) 1 2 7 2 11]
    print('next :', l_list.next())          # next : 1, [5 1(current) 2 7 2 11]
    print('next :', l_list.next())          # next : 2, [5 1 2(current) 7 2 11]
    print('next :', l_list.next())          # next : 7, [5 1 2 7(current) 2 11]
    print('='*20)

    # 전체 노드 data 표시하기 [5 1 2 7 2 11]
    data = l_list.first()  # 5
    if data:  # 빈 연결 리스트 아님.
        print(data, end=' ')
        while True:
            data = l_list.next()
            if data:
                print(data, end= ' ')
            else:  # current가 tail에 다다르면 l_list.next() = None이므로 종료
                break

    # 2인 데이터 삭제 후 그 자리에 'deleted' 출력: 5 1 deleted 7 deleted 11
    print('\n' + '='*20)
    data = l_list.first()  # 5
    if data and data == 2:
        l_list.delete()
        print('deleted', end=' ')
    else:
        print(data, end= ' ') # 데이터가 존재하지 않거나 2가 아니면 그대로 출력

    while True:
        data = l_list.next()
        if data == 2:
            l_list.delete()
            print('deleted', end=' ')
        elif data:
            print(data, end=' ')
        else:
            break
CPPREF = {
    'main':
        'int main();\n'
        'int main(int argc, char *argv[]);',

    'deque':
        '<deque>\n'
        'constructs the deque\n\n'

        'explicit deque(const Allocator &alloc=Allocator()); (until C++14)\n\n'

        'deque():\n'
        'deque(Allocator()) {}\n\n'

        'explicit deque(const Allocator &alloc); (since C++14)\n\n'

        'explicit deque( \n'
        '    size_type count, const T &value=T(), const Allocator &alloc=Allocator() \n'
        '); (until C++11)\n\n'

        'deque( \n'
        '    size_type count, const T &value, const Allocator &alloc=Allocator() \n'
        '); (since C++11)\n\n'

        'explicit deque(size_type count); (since C++11) (until C++14)\n\n'

        'explicit deque( \n'
        '    size_type count, const Allocator &alloc=Allocator() \n'
        '); (since C++14)\n\n'

        'template <class InputIt>\n'
        'deque(InputIt first, InputIt last, const Allocator &alloc=Allocator());\n\n'

        'deque(const deque &other);\n\n'

        'deque(const deque &other, const Allocator &alloc); (since C++11)\n\n'

        'deque(deque &&other); (since C++11)\n\n'

        'deque(deque &&other, const Allocator &alloc); (since C++11)\n\n'

        'deque( \n'
        '    std::initializer_list<T> init, const Allocator &alloc=Allocator() \n'
        '); (since C++11)',

    'deque::~deque':
        '<deque>\n'
        'destructs the deque\n\n'

        '~deque();',

    'deque::assign':
        '<deque>\n'
        'assigns values to the container\n\n'

        'void assign(size_type count, const T &value);\n\n'

        'template <class InputIt>\n'
        'void assign(InputIt first, InputIt last);\n\n'

        'void assign(std::initializer_list<T> ilist); (since C++11)',

    'deque::get_allocator':
        '<deque>\n'
        'returns the associated allocator\n\n'

        'allocator_type get_allocator() const;',

    'deque::at':
        '<deque>\n'
        'access specified element with bounds checking\n\n'

        'reference at(size_type pos);\n\n'

        'const_reference at(size_type pos) const;',

    'deque::front':
        '<deque>\n'
        'access the first element\n\n'

        'reference front();\n\n'

        'const_reference front() const;',

    'deque::back':
        '<deque>\n'
        'access the last element\n\n'

        'reference back();\n\n'

        'const_reference back() const;',

    'deque::begin':
        '<deque>\n'
        'returns an iterator to the beginning\n\n'

        'iterator begin();\n\n'

        'const_iterator begin() const;',

    'deque::cbegin':
        '<deque>\n'
        'returns an iterator to the beginning\n\n'

        'const_iterator cbegin() const; (since C++11)',

    'deque::end':
        '<deque>\n'
        'returns an iterator to the end\n\n'

        'iterator end();\n\n'

        'const_iterator end() const;',

    'deque::cend':
        '<deque>\n'
        'returns an iterator to the end\n\n'

        'const_iterator cend() const; (since C++11)',

    'deque::rbegin':
        '<deque>\n'
        'returns a reverse iterator to the beginning\n\n'

        'reverse_iterator rbegin();\n\n'

        'const_reverse_iterator rbegin() const;',

    'deque::crbegin':
        '<deque>\n'
        'returns a reverse iterator to the beginning\n\n'

        'const_reverse_iterator crbegin() const; (since C++11)',

    'deque::rend':
        '<deque>\n'
        'returns a reverse iterator to the end\n\n'

        'reverse_iterator rend();\n\n'

        'const_reverse_iterator rend() const;',

    'deque::crend':
        '<deque>\n'
        'returns a reverse iterator to the end\n\n'

        'const_reverse_iterator crend() const; (since C++11)',

    'deque::empty':
        '<deque>\n'
        'checks whether the container is empty\n\n'

        'bool empty() const;',

    'deque::size':
        '<deque>\n'
        'returns the number of elements\n\n'

        'size_type size() const;',

    'deque::max_size':
        '<deque>\n'
        'returns the maximum possible number of elements\n\n'

        'size_type max_size() const;',

    'deque::shrink_to_fit':
        '<deque>\n'
        'reduces memory usage by freeing unused memory\n\n'

        'void shrink_to_fit(); (since C++11)',

    'deque::clear':
        '<deque>\n'
        'clears the contents\n\n'

        'void clear();',

    'deque::insert':
        '<deque>\n'
        'inserts elements\n\n'

        'iterator insert(iterator pos, const T &value); (until C++11)\n\n'

        'iterator insert(const_iterator pos, const T &value); (since C++11)\n\n'

        'iterator insert(const_iterator pos, T &&value); (since C++11)\n\n'

        'void insert(iterator pos, size_type count, const T &value); (until C++11)\n\n'

        'iterator insert( \n'
        '    const_iterator pos, size_type count, const T &value \n'
        '); (since C++11)\n\n'

        'template <class InputIt>\n'
        'void insert(iterator pos, InputIt first, InputIt last); (until C++11)\n\n'

        'template <class InputIt>\n'
        'iterator insert(const_iterator pos, InputIt first, InputIt last); (since C++11)\n\n'

        'iterator insert( \n'
        '    const_iterator pos, std::initializer_list<T> ilist \n'
        '); (since C++11)',

    'deque::emplace':
        '<deque>\n'
        'constructs element in-place\n\n'

        'template <class... Args>\n'
        'iterator emplace(const_iterator pos, Args&&... args); (since C++11)',

    'deque::erase':
        '<deque>\n'
        'erases elements\n\n'

        'iterator erase(iterator pos); (until C++11)\n\n'

        'iterator erase(const_iterator pos); (since C++11)\n\n'

        'iterator erase(iterator first, iterator last); (until C++11)\n\n'

        'iterator erase(const_iterator first, const_iterator last); (since C++11)',

    'deque::push_back':
        '<deque>\n'
        'adds an element to the end\n\n'

        'void push_back(const T &value);\n\n'

        'void push_back(T &&value); (since C++11)',

    'deque::emplace_back':
        '<deque>\n'
        'constructs an element in-place at the end\n\n'

        'template <class... Args>\n'
        'void emplace_back(Args&&... args); (since C++11) (until C++17)',

    'deque::pop_back':
        '<deque>\n'
        'removes the last element\n\n'

        'void pop_back();',

    'deque::push_front':
        '<deque>\n'
        'inserts an element to the beginning\n\n'

        'void push_front(const T &value);\n\n'

        'void push_front(T &&value); (since C++11)',

    'deque::emplace_front':
        '<deque>\n'
        'constructs an element in-place at the beginning\n\n'

        'template <class... Args>\n'
        'void emplace_front(Args&&... args); (since C++11) (until C++17)',

    'deque::pop_front':
        '<deque>\n'
        'removes the first element\n\n'

        'void pop_front();',

    'deque::resize':
        '<deque>\n'
        'changes the number of elements stored\n\n'

        'void resize(size_type count, T value=T()); (until C++11)\n\n'

        'void resize(size_type count); (since C++11)\n\n'

        'void resize(size_type count, const value_type &value); (since C++11)',

    'deque::swap':
        '<deque>\n'
        'swaps the contents\n\n'

        'void swap(deque &other);',

    'std::swap':
        '<deque>\n'
        'specializes the std::swap algorithm\n\n'

        'template <class T, class Alloc>\n'
        'void swap(deque<T, Alloc> &lhs, deque<T, Alloc> &rhs);',

    'forward_list':
        '<forward_list>\n'
        'constructs the forward_list\n\n'

        'explicit forward_list( \n'
        '    const Allocator &alloc=Allocator() \n'
        '); (since C++11) (until C++14)\n\n'

        'forward_list():\n'
        'forward_list(Allocator()) {}\n\n'

        'explicit forward_list(const Allocator &alloc); (since C++14)\n\n'

        'forward_list( \n'
        '    size_type count, const T &value, const Allocator &alloc=Allocator() \n'
        '); (since C++11)\n\n'

        'explicit forward_list(size_type count); (since C++11) (until C++14)\n\n'

        'explicit forward_list( \n'
        '    size_type count, const Allocator &alloc=Allocator() \n'
        '); (since C++14)\n\n'

        'template <class InputIt>\n'
        'forward_list( \n'
        '    InputIt first, InputIt last, const Allocator &alloc=Allocator() \n'
        '); (since C++11)\n\n'

        'forward_list(const forward_list &other); (since C++11)\n\n'

        'forward_list(const forward_list &other, const Allocator &alloc); (since C++11)\n\n'

        'forward_list(forward_list &&other); (since C++11)\n\n'

        'forward_list(forward_list &&other, const Allocator &alloc); (since C++11)\n\n'

        'forward_list( \n'
        '    std::initializer_list<T> init, const Allocator &alloc=Allocator() \n'
        '); (since C++11)',

    'forward_list::~forward_list':
        '<forward_list>\n'
        'destructs the forward_list\n\n'

        '~forward_list(); (since C++11)',

    'forward_list::assign':
        '<forward_list>\n'
        'assigns values to the container\n\n'

        'void assign(size_type count, const T &value); (since C++11)\n\n'

        'template <class InputIt>\n'
        'void assign(InputIt first, InputIt last); (since C++11)\n\n'

        'void assign(std::initializer_list<T> ilist); (since C++11)',

    'forward_list::get_allocator':
        '<forward_list>\n'
        'returns the associated allocator\n\n'

        'allocator_type get_allocator() const; (since C++11)',

    'forward_list::front':
        '<forward_list>\n'
        'access the first element\n\n'

        'reference front(); (since C++11)\n\n'

        'const_reference front() const; (since C++11)',

    'forward_list::before_begin':
        '<forward_list>\n'
        'returns an iterator to the element before beginning\n\n'

        'iterator before_begin(); (since C++11)\n\n'

        'const_iterator before_begin() const; (since C++11)',

    'forward_list::cbefore_begin':
        '<forward_list>\n'
        'returns an iterator to the element before beginning\n\n'

        'const_iterator cbefore_begin() const; (since C++11)',

    'forward_list::begin':
        '<forward_list>\n'
        'returns an iterator to the beginning\n\n'

        'iterator begin(); (since C++11)\n\n'

        'const_iterator begin() const; (since C++11)',

    'forward_list::cbegin':
        '<forward_list>\n'
        'returns an iterator to the beginning\n\n'

        'const_iterator cbegin() const; (since C++11)',

    'forward_list::end':
        '<forward_list>\n'
        'returns an iterator to the end\n\n'

        'iterator end(); (since C++11)\n\n'

        'const_iterator end() const; (since C++11)',

    'forward_list::cend':
        '<forward_list>\n'
        'returns an iterator to the end\n\n'

        'const_iterator cend() const; (since C++11)',

    'forward_list::empty':
        '<forward_list>\n'
        'checks whether the container is empty\n\n'

        'bool empty() const; (since C++11)',

    'forward_list::max_size':
        '<forward_list>\n'
        'returns the maximum possible number of elements\n\n'

        'size_type max_size() const; (since C++11)',

    'forward_list::clear':
        '<forward_list>\n'
        'clears the contents\n\n'

        'void clear(); (since C++11)',

    'forward_list::insert_after':
        '<forward_list>\n'
        'inserts elements after an element\n\n'

        'iterator insert_after(const_iterator pos, const T &value); (since C++11)\n\n'

        'iterator insert_after(const_iterator pos, T &&value); (since C++11)\n\n'

        'iterator insert_after( \n'
        '    const_iterator pos, size_type count, const T &value \n'
        '); (since C++11)\n\n'

        'template <class InputIt>\n'
        'iterator insert_after( \n'
        '    const_iterator pos, InputIt first, InputIt last \n'
        '); (since C++11)\n\n'

        'iterator insert_after( \n'
        '    const_iterator pos, std::initializer_list<T> ilist \n'
        '); (since C++11)',

    'forward_list::emplace_after':
        '<forward_list>\n'
        'constructs elements in-place after an element\n\n'

        'template <class... Args>\n'
        'iterator emplace_after(const_iterator pos, Args&&... args); (since C++11)',

    'forward_list::erase_after':
        '<forward_list>\n'
        'erases an element after an element\n\n'

        'iterator erase_after(const_iterator pos); (since C++11)\n\n'

        'iterator erase_after(const_iterator first, const_iterator last); (since C++11)',

    'forward_list::push_front':
        '<forward_list>\n'
        'inserts an element to the beginning\n\n'

        'void push_front(const T &value); (since C++11)\n\n'

        'void push_front(T &&value); (since C++11)',

    'forward_list::emplace_front':
        '<forward_list>\n'
        'constructs an element in-place at the beginning\n\n'

        'template <class... Args>\n'
        'void emplace_front(Args&&... args); (since C++11) (until C++17)',

    'forward_list::pop_front':
        '<forward_list>\n'
        'removes the first element\n\n'

        'void pop_front(); (since C++11)',

    'forward_list::resize':
        '<forward_list>\n'
        'changes the number of elements stored\n\n'

        'void resize(size_type count);\n\n'

        'void resize(size_type count, const value_type &value);',

    'forward_list::swap':
        '<forward_list>\n'
        'swaps the contents\n\n'

        'void swap(forward_list &other); (since C++11)',

    'forward_list::merge':
        '<forward_list>\n'
        'merges two sorted lists\n\n'

        'void merge(forward_list &other); (since C++11)\n\n'

        'void merge(forward_list &&other); (since C++11)\n\n'

        'template <class Compare>\n'
        'void merge(forward_list &other, Compare comp); (since C++11)\n\n'

        'template <class Compare>\n'
        'void merge(forward_list &&other, Compare comp); (since C++11)',

    'forward_list::splice_after':
        '<forward_list>\n'
        'moves elements from another forward_list\n\n'

        'void splice_after(const_iterator pos, forward_list &other); (since C++11)\n\n'

        'void splice_after(const_iterator pos, forward_list &&other); (since C++11)\n\n'

        'void splice_after( \n'
        '    const_iterator pos, forward_list &other, const_iterator it \n'
        '); (since C++11)\n\n'

        'void splice_after( \n'
        '    const_iterator pos, forward_list &&other, const_iterator it \n'
        '); (since C++11)\n\n'

        'void splice_after( \n'
        '    const_iterator pos, forward_list &other, const_iterator first, \n'
        '    const_iterator last \n'
        '); (since C++11)\n\n'

        'void splice_after( \n'
        '    const_iterator pos, forward_list &&other, const_iterator first, \n'
        '    const_iterator last \n'
        '); (since C++11)',

    'forward_list::remove':
        '<forward_list>\n'
        'removes elements satisfying specific criteria\n\n'

        'void remove(const T &value); (since C++11)',

    'forward_list::remove_if':
        '<forward_list>\n'
        'removes elements satisfying specific criteria\n\n'

        'template <class UnaryPredicate>\n'
        'void remove_if(UnaryPredicate p); (since C++11)',

    'forward_list::reverse':
        '<forward_list>\n'
        'reverses the order of the elements\n\n'

        'void reverse(); (since C++11)',

    'forward_list::unique':
        '<forward_list>\n'
        'removes consecutive duplicate elements\n\n'

        'void unique(); (since C++11)\n\n'

        'template <class BinaryPredicate>\n'
        'void unique(BinaryPredicate p); (since C++11)',

    'forward_list::sort':
        '<forward_list>\n'
        'sorts the elements\n\n'

        'void sort(); (since C++11)\n\n'

        'template <class Compare>\n'
        'void sort(Compare comp); (since C++11)',

    'std::swap':
        '<forward_list>\n'
        'specializes the std::swap algorithm\n\n'

        'template <class T, class Alloc>\n'
        'void swap( \n'
        '    forward_list<T, Alloc> &lhs, forward_list<T, Alloc> &rhs \n'
        '); (since C++11)',

    'list':
        '<list>\n'
        'constructs the list\n\n'

        'explicit list(const Allocator &alloc=Allocator()); (until C++14)\n\n'

        'list():\n'
        'list(Allocator()) {}\n\n'

        'explicit list(const Allocator &alloc); (since C++14)\n\n'

        'explicit list( \n'
        '    size_type count, const T &value=T(), const Allocator &alloc=Allocator() \n'
        '); (until C++11)\n\n'

        'list( \n'
        '    size_type count, const T &value, const Allocator &alloc=Allocator() \n'
        '); (since C++11)\n\n'

        'explicit list(size_type count); (since C++11) (until C++14)\n\n'

        'explicit list( \n'
        '    size_type count, const Allocator &alloc=Allocator() \n'
        '); (since C++14)\n\n'

        'template <class InputIt>\n'
        'list(InputIt first, InputIt last, const Allocator &alloc=Allocator());\n\n'

        'list(const list &other);\n\n'

        'list(const list &other, const Allocator &alloc); (since C++11)\n\n'

        'list(list &&other); (since C++11)\n\n'

        'list(list &&other, const Allocator &alloc); (since C++11)\n\n'

        'list( \n'
        '    std::initializer_list<T> init, const Allocator &alloc=Allocator() \n'
        '); (since C++11)',

    'list::~list':
        '<list>\n'
        'destructs the list\n\n'

        '~list();',

    'list::assign':
        '<list>\n'
        'assigns values to the container\n\n'

        'void assign(size_type count, const T &value);\n\n'

        'template <class InputIt>\n'
        'void assign(InputIt first, InputIt last);\n\n'

        'void assign(std::initializer_list<T> ilist); (since C++11)',

    'list::get_allocator':
        '<list>\n'
        'returns the associated allocator\n\n'

        'allocator_type get_allocator() const;',

    'list::front':
        '<list>\n'
        'access the first element\n\n'

        'reference front();\n\n'

        'const_reference front() const;',

    'list::back':
        '<list>\n'
        'access the last element\n\n'

        'reference back();\n\n'

        'const_reference back() const;',

    'list::begin':
        '<list>\n'
        'returns an iterator to the beginning\n\n'

        'iterator begin();\n\n'

        'const_iterator begin() const;',

    'list::cbegin':
        '<list>\n'
        'returns an iterator to the beginning\n\n'

        'const_iterator cbegin() const; (since C++11)',

    'list::end':
        '<list>\n'
        'returns an iterator to the end\n\n'

        'iterator end();\n\n'

        'const_iterator end() const;',

    'list::cend':
        '<list>\n'
        'returns an iterator to the end\n\n'

        'const_iterator cend() const; (since C++11)',

    'list::rbegin':
        '<list>\n'
        'returns a reverse iterator to the beginning\n\n'

        'reverse_iterator rbegin();\n\n'

        'const_reverse_iterator rbegin() const;',

    'list::crbegin':
        '<list>\n'
        'returns a reverse iterator to the beginning\n\n'

        'const_reverse_iterator crbegin() const; (since C++11)',

    'list::rend':
        '<list>\n'
        'returns a reverse iterator to the end\n\n'

        'reverse_iterator rend();\n\n'

        'const_reverse_iterator rend() const;',

    'list::crend':
        '<list>\n'
        'returns a reverse iterator to the end\n\n'

        'const_reverse_iterator crend() const; (since C++11)',

    'list::empty':
        '<list>\n'
        'checks whether the container is empty\n\n'

        'bool empty() const;',

    'list::size':
        '<list>\n'
        'returns the number of elements\n\n'

        'size_type size() const;',

    'list::max_size':
        '<list>\n'
        'returns the maximum possible number of elements\n\n'

        'size_type max_size() const;',

    'list::clear':
        '<list>\n'
        'clears the contents\n\n'

        'void clear();',

    'list::insert':
        '<list>\n'
        'inserts elements\n\n'

        'iterator insert(iterator pos, const T &value); (until C++11)\n\n'

        'iterator insert(const_iterator pos, const T &value); (since C++11)\n\n'

        'iterator insert(const_iterator pos, T &&value); (since C++11)\n\n'

        'void insert(iterator pos, size_type count, const T &value); (until C++11)\n\n'

        'iterator insert( \n'
        '    const_iterator pos, size_type count, const T &value \n'
        '); (since C++11)\n\n'

        'template <class InputIt>\n'
        'void insert(iterator pos, InputIt first, InputIt last); (until C++11)\n\n'

        'template <class InputIt>\n'
        'iterator insert(const_iterator pos, InputIt first, InputIt last); (since C++11)\n\n'

        'iterator insert( \n'
        '    const_iterator pos, std::initializer_list<T> ilist \n'
        '); (since C++11)',

    'list::emplace':
        '<list>\n'
        'constructs element in-place\n\n'

        'template <class... Args>\n'
        'iterator emplace(const_iterator pos, Args&&... args); (since C++11)',

    'list::erase':
        '<list>\n'
        'erases elements\n\n'

        'iterator erase(iterator pos); (until C++11)\n\n'

        'iterator erase(const_iterator pos); (since C++11)\n\n'

        'iterator erase(iterator first, iterator last); (until C++11)\n\n'

        'iterator erase(const_iterator first, const_iterator last); (since C++11)',

    'list::push_back':
        '<list>\n'
        'adds an element to the end\n\n'

        'void push_back(const T &value);\n\n'

        'void push_back(T &&value); (since C++11)',

    'list::emplace_back':
        '<list>\n'
        'constructs an element in-place at the end\n\n'

        'template <class... Args>\n'
        'void emplace_back(Args&&... args); (since C++11) (until C++17)',

    'list::pop_back':
        '<list>\n'
        'removes the last element\n\n'

        'void pop_back();',

    'list::push_front':
        '<list>\n'
        'inserts an element to the beginning\n\n'

        'void push_front(const T &value);\n\n'

        'void push_front(T &&value); (since C++11)',

    'list::emplace_front':
        '<list>\n'
        'constructs an element in-place at the beginning\n\n'

        'template <class... Args>\n'
        'void emplace_front(Args&&... args); (since C++11) (until C++17)',

    'list::pop_front':
        '<list>\n'
        'removes the first element\n\n'

        'void pop_front();',

    'list::resize':
        '<list>\n'
        'changes the number of elements stored\n\n'

        'void resize(size_type count, T value=T()); (until C++11)\n\n'

        'void resize(size_type count); (since C++11)\n\n'

        'void resize(size_type count, const value_type &value); (since C++11)',

    'list::swap':
        '<list>\n'
        'swaps the contents\n\n'

        'void swap(list &other);',

    'list::merge':
        '<list>\n'
        'merges two sorted lists\n\n'

        'void merge(list &other);\n\n'

        'void merge(list &&other); (since C++11)\n\n'

        'template <class Compare>\n'
        'void merge(list &other, Compare comp);\n\n'

        'template <class Compare>\n'
        'void merge(list &&other, Compare comp); (since C++11)',

    'list::splice':
        '<list>\n'
        'moves elements from another list\n\n'

        'void splice(const_iterator pos, list &other);\n\n'

        'void splice(const_iterator pos, list &&other); (since C++11)\n\n'

        'void splice(const_iterator pos, list &other, const_iterator it);\n\n'

        'void splice(const_iterator pos, list &&other, const_iterator it); (since C++11)\n\n'

        'void splice( \n'
        '    const_iterator pos, list &other, const_iterator first, const_iterator last \n'
        ');\n\n'

        'void splice( \n'
        '    const_iterator pos, list &&other, const_iterator first, const_iterator last \n'
        '); (since C++11)',

    'list::remove':
        '<list>\n'
        'removes elements satisfying specific criteria\n\n'

        'void remove(const T &value);',

    'list::remove_if':
        '<list>\n'
        'removes elements satisfying specific criteria\n\n'

        'template <class UnaryPredicate>\n'
        'void remove_if(UnaryPredicate p);',

    'list::reverse':
        '<list>\n'
        'reverses the order of the elements\n\n'

        'void reverse();',

    'list::unique':
        '<list>\n'
        'removes consecutive duplicate elements\n\n'

        'void unique();\n\n'

        'template <class BinaryPredicate>\n'
        'void unique(BinaryPredicate p);',

    'list::sort':
        '<list>\n'
        'sorts the elements\n\n'

        'void sort();\n\n'

        'template <class Compare>\n'
        'void sort(Compare comp);',

    'std::swap':
        '<list>\n'
        'specializes the std::swap algorithm\n\n'

        'template <class T, class Alloc>\n'
        'void swap(list<T, Alloc> &lhs, list<T, Alloc> &rhs);',

    'map':
        '<map>\n'
        'constructs the map\n\n'

        'explicit map( \n'
        '    const Compare &comp=Compare(), const Allocator &alloc=Allocator() \n'
        '); (until C++14)\n\n'

        'map():\n'
        'map(Compare()) {}\n\n'

        'explicit map( \n'
        '    const Compare &comp, const Allocator &alloc=Allocator() \n'
        '); (since C++14)\n\n'

        'explicit map(const Allocator &alloc); (since C++11)\n\n'

        'template <class InputIterator>\n'
        'map( \n'
        '    InputIterator first, InputIterator last, const Compare &comp=Compare(), \n'
        '    const Allocator &alloc=Allocator() \n'
        ');\n\n'

        'template <class InputIterator>\n'
        'map( \n'
        '    InputIterator first, InputIterator last, const Allocator &alloc \n'
        '); (since C++14)\n\n'

        'map(const map &other);\n\n'

        'map(const map &other, const Allocator &alloc); (since C++11)\n\n'

        'map(map &&other); (since C++11)\n\n'

        'map(map &&other, const Allocator &alloc); (since C++11)\n\n'

        'map( \n'
        '    std::initializer_list<value_type> init, const Compare &comp=Compare(), \n'
        '    const Allocator &alloc=Allocator() \n'
        '); (since C++11)\n\n'

        'map(std::initializer_list<value_type> init, const Allocator &); (since C++14)',

    'map::~map':
        '<map>\n'
        'destructs the map\n\n'

        '~map();',

    'map::get_allocator':
        '<map>\n'
        'returns the associated allocator\n\n'

        'allocator_type get_allocator() const;',

    'map::at':
        '<map>\n'
        'access specified element with bounds checking\n\n'

        'T &at(const Key &key); (since C++11)\n\n'

        'const T &at(const Key &key) const; (since C++11)',

    'map::begin':
        '<map>\n'
        'returns an iterator to the beginning\n\n'

        'iterator begin();\n\n'

        'const_iterator begin() const;',

    'map::cbegin':
        '<map>\n'
        'returns an iterator to the beginning\n\n'

        'const_iterator cbegin() const; (since C++11)',

    'map::end':
        '<map>\n'
        'returns an iterator to the end\n\n'

        'iterator end();\n\n'

        'const_iterator end() const;',

    'map::cend':
        '<map>\n'
        'returns an iterator to the end\n\n'

        'const_iterator cend() const; (since C++11)',

    'map::rbegin':
        '<map>\n'
        'returns a reverse iterator to the beginning\n\n'

        'reverse_iterator rbegin();\n\n'

        'const_reverse_iterator rbegin() const;',

    'map::crbegin':
        '<map>\n'
        'returns a reverse iterator to the beginning\n\n'

        'const_reverse_iterator crbegin() const; (since C++11)',

    'map::rend':
        '<map>\n'
        'returns a reverse iterator to the end\n\n'

        'reverse_iterator rend();\n\n'

        'const_reverse_iterator rend() const;',

    'map::crend':
        '<map>\n'
        'returns a reverse iterator to the end\n\n'

        'const_reverse_iterator crend() const; (since C++11)',

    'map::empty':
        '<map>\n'
        'checks whether the container is empty\n\n'

        'bool empty() const;',

    'map::size':
        '<map>\n'
        'returns the number of elements\n\n'

        'size_type size() const;',

    'map::max_size':
        '<map>\n'
        'returns the maximum possible number of elements\n\n'

        'size_type max_size() const;',

    'map::clear':
        '<map>\n'
        'clears the contents\n\n'

        'void clear();',

    'map::insert':
        '<map>\n'
        'inserts elements or nodes (since C++17)\n\n'

        'std::pair<iterator, bool> insert(const value_type &value);\n\n'

        'template <class P>\n'
        'std::pair<iterator, bool> insert(P &&value); (since C++11)\n\n'

        'iterator insert(iterator hint, const value_type &value); (until C++11)\n\n'

        'iterator insert(const_iterator hint, const value_type &value); (since C++11)\n\n'

        'template <class P>\n'
        'iterator insert(const_iterator hint, P &&value); (since C++11)\n\n'

        'template <class InputIt>\n'
        'void insert(InputIt first, InputIt last);\n\n'

        'void insert(std::initializer_list<value_type> ilist); (since C++11)',

    'map::emplace':
        '<map>\n'
        'constructs element in-place\n\n'

        'template <class... Args>\n'
        'std::pair<iterator, bool> emplace(Args&&... args); (since C++11)',

    'map::emplace_hint':
        '<map>\n'
        'constructs elements in-place using a hint\n\n'

        'template <class... Args>\n'
        'iterator emplace_hint(const_iterator hint, Args&&... args); (since C++11)',

    'map::erase':
        '<map>\n'
        'erases elements\n\n'

        'void erase(iterator pos); (until C++11)\n\n'

        'iterator erase(const_iterator pos); (since C++11)\n\n'

        'void erase(iterator first, iterator last); (until C++11)\n\n'

        'iterator erase(const_iterator first, const_iterator last); (since C++11)\n\n'

        'size_type erase(const key_type &key);',

    'map::swap':
        '<map>\n'
        'swaps the contents\n\n'

        'void swap(map &other);',

    'map::count':
        '<map>\n'
        'returns the number of elements matching specific key\n\n'

        'size_type count(const Key &key) const;\n\n'

        'template <class K>\n'
        'size_type count(const K &x) const; (since C++14)',

    'map::find':
        '<map>\n'
        'finds element with specific key\n\n'

        'iterator find(const Key &key);\n\n'

        'const_iterator find(const Key &key) const;\n\n'

        'template <class K>\n'
        'iterator find(const K &x); (since C++14)\n\n'

        'template <class K>\n'
        'const_iterator find(const K &x) const; (since C++14)',

    'map::equal_range':
        '<map>\n'
        'returns range of elements matching a specific key\n\n'

        'std::pair<iterator, iterator> equal_range(const Key &key);\n\n'

        'std::pair<const_iterator, const_iterator> equal_range(const Key &key) const;\n\n'

        'template <class K>\n'
        'std::pair<iterator, iterator> equal_range(const K &x); (since C++14)\n\n'

        'template <class K>\n'
        'std::pair<const_iterator, const_iterator> equal_range( \n'
        '    const K &xconst \n'
        '); (since C++14)',

    'map::lower_bound':
        '<map>\n'
        'returns an iterator to the first element not less than the given key\n\n'

        'iterator lower_bound(const Key &key);\n\n'

        'const_iterator lower_bound(const Key &key) const;\n\n'

        'template <class K>\n'
        'iterator lower_bound(const K &x); (since C++14)\n\n'

        'template <class K>\n'
        'const_iterator lower_bound(const K &x) const; (since C++14)',

    'map::upper_bound':
        '<map>\n'
        'returns an iterator to the first element greater than the given key\n\n'

        'iterator upper_bound(const Key &key);\n\n'

        'const_iterator upper_bound(const Key &key) const;\n\n'

        'template <class K>\n'
        'iterator upper_bound(const K &x); (since C++14)\n\n'

        'template <class K>\n'
        'const_iterator upper_bound(const K &x) const; (since C++14)',

    'map::key_comp':
        '<map>\n'
        'returns the function that compares keys\n\n'

        'key_compare key_comp() const;',

    'map::value_comp':
        '<map>\n'
        'returns the function that compares keys in objects of type value_type\n\n'

        'std::map::value_compare value_comp() const;',

    'std::swap':
        '<map>\n'
        'specializes the std::swap algorithm\n\n'

        'template <class Key, class T, class Compare, class Alloc>\n'
        'void swap(map<Key, T, Compare, Alloc> &lhs, map<Key, T, Compare, Alloc> &rhs);',

    'multimap':
        '<multimap>\n'
        'constructs the multimap\n\n'

        'explicit multimap( \n'
        '    const Compare &comp=Compare(), const Allocator &alloc=Allocator() \n'
        '); (until C++14)\n\n'

        'multimap():\n'
        'multimap(Compare()) {}\n\n'

        'explicit multimap( \n'
        '    const Compare &comp, const Allocator &alloc=Allocator() \n'
        '); (since C++14)\n\n'

        'explicit multimap(const Allocator &alloc); (since C++11)\n\n'

        'template <class InputIterator>\n'
        'multimap( \n'
        '    InputIterator first, InputIterator last, const Compare &comp=Compare(), \n'
        '    const Allocator &alloc=Allocator() \n'
        ');\n\n'

        'template <class InputIterator>\n'
        'multimap( \n'
        '    InputIterator first, InputIterator last, const Allocator &alloc \n'
        '); (since C++14)\n\n'

        'multimap(const multimap &other);\n\n'

        'multimap(const multimap &other, const Allocator &alloc); (since C++11)\n\n'

        'multimap(multimap &&other); (since C++11)\n\n'

        'multimap(multimap &&other, const Allocator &alloc); (since C++11)\n\n'

        'multimap( \n'
        '    std::initializer_list<value_type> init, const Compare &comp=Compare(), \n'
        '    const Allocator &alloc=Allocator() \n'
        '); (since C++11)\n\n'

        'multimap( \n'
        '    std::initializer_list<value_type> init, const Allocator \n'
        '); (since C++14)',

    'multimap::~multimap':
        '<multimap>\n'
        'destructs the multimap\n\n'

        '~multimap();',

    'multimap::get_allocator':
        '<multimap>\n'
        'returns the associated allocator\n\n'

        'allocator_type get_allocator() const;',

    'multimap::begin':
        '<multimap>\n'
        'returns an iterator to the beginning\n\n'

        'iterator begin();\n\n'

        'const_iterator begin() const;',

    'multimap::cbegin':
        '<multimap>\n'
        'returns an iterator to the beginning\n\n'

        'const_iterator cbegin() const; (since C++11)',

    'multimap::end':
        '<multimap>\n'
        'returns an iterator to the end\n\n'

        'iterator end();\n\n'

        'const_iterator end() const;',

    'multimap::cend':
        '<multimap>\n'
        'returns an iterator to the end\n\n'

        'const_iterator cend() const; (since C++11)',

    'multimap::rbegin':
        '<multimap>\n'
        'returns a reverse iterator to the beginning\n\n'

        'reverse_iterator rbegin();\n\n'

        'const_reverse_iterator rbegin() const;',

    'multimap::crbegin':
        '<multimap>\n'
        'returns a reverse iterator to the beginning\n\n'

        'const_reverse_iterator crbegin() const; (since C++11)',

    'multimap::rend':
        '<multimap>\n'
        'returns a reverse iterator to the end\n\n'

        'reverse_iterator rend();\n\n'

        'const_reverse_iterator rend() const;',

    'multimap::crend':
        '<multimap>\n'
        'returns a reverse iterator to the end\n\n'

        'const_reverse_iterator crend() const; (since C++11)',

    'multimap::empty':
        '<multimap>\n'
        'checks whether the container is empty\n\n'

        'bool empty() const;',

    'multimap::size':
        '<multimap>\n'
        'returns the number of elements\n\n'

        'size_type size() const;',

    'multimap::max_size':
        '<multimap>\n'
        'returns the maximum possible number of elements\n\n'

        'size_type max_size() const;',

    'multimap::clear':
        '<multimap>\n'
        'clears the contents\n\n'

        'void clear();',

    'multimap::insert':
        '<multimap>\n'
        'inserts elements or nodes (since C++17)\n\n'

        'iterator insert(const value_type &value);\n\n'

        'template <class P>\n'
        'iterator insert(P &&value); (since C++11)\n\n'

        'iterator insert(iterator hint, const value_type &value); (until C++11)\n\n'

        'iterator insert(const_iterator hint, const value_type &value); (since C++11)\n\n'

        'template <class P>\n'
        'iterator insert(const_iterator hint, P &&value); (since C++11)\n\n'

        'template <class InputIt>\n'
        'void insert(InputIt first, InputIt last);\n\n'

        'void insert(std::initializer_list<value_type> ilist); (since C++11)',

    'multimap::emplace':
        '<multimap>\n'
        'constructs element in-place\n\n'

        'template <class... Args>\n'
        'iterator emplace(Args&&... args); (since C++11)',

    'multimap::emplace_hint':
        '<multimap>\n'
        'constructs elements in-place using a hint\n\n'

        'template <class... Args>\n'
        'iterator emplace_hint(const_iterator hint, Args&&... args); (since C++11)',

    'multimap::erase':
        '<multimap>\n'
        'erases elements\n\n'

        'void erase(iterator pos); (until C++11)\n\n'

        'iterator erase(const_iterator pos); (since C++11)\n\n'

        'void erase(iterator first, iterator last); (until C++11)\n\n'

        'iterator erase(const_iterator first, const_iterator last); (since C++11)\n\n'

        'size_type erase(const key_type &key);',

    'multimap::swap':
        '<multimap>\n'
        'swaps the contents\n\n'

        'void swap(multimap &other);',

    'multimap::count':
        '<multimap>\n'
        'returns the number of elements matching specific key\n\n'

        'size_type count(const Key &key) const;\n\n'

        'template <class K>\n'
        'size_type count(const K &x) const; (since C++14)',

    'multimap::find':
        '<multimap>\n'
        'finds element with specific key\n\n'

        'iterator find(const Key &key);\n\n'

        'const_iterator find(const Key &key) const;\n\n'

        'template <class K>\n'
        'iterator find(const K &x); (since C++14)\n\n'

        'template <class K>\n'
        'const_iterator find(const K &x) const; (since C++14)',

    'multimap::equal_range':
        '<multimap>\n'
        'returns range of elements matching a specific key\n\n'

        'std::pair<iterator, iterator> equal_range(const Key &key);\n\n'

        'std::pair<const_iterator, const_iterator> equal_range(const Key &key) const;\n\n'

        'template <class K>\n'
        'std::pair<iterator, iterator> equal_range(const K &x); (since C++14)\n\n'

        'template <class K>\n'
        'std::pair<const_iterator, const_iterator> equal_range( \n'
        '    const K &xconst \n'
        '); (since C++14)',

    'multimap::lower_bound':
        '<multimap>\n'
        'returns an iterator to the first element not less than the given key\n\n'

        'iterator lower_bound(const Key &key);\n\n'

        'const_iterator lower_bound(const Key &key) const;\n\n'

        'template <class K>\n'
        'iterator lower_bound(const K &x); (since C++14)\n\n'

        'template <class K>\n'
        'const_iterator lower_bound(const K &x) const; (since C++14)',

    'multimap::upper_bound':
        '<multimap>\n'
        'returns an iterator to the first element greater than the given key\n\n'

        'iterator upper_bound(const Key &key);\n\n'

        'const_iterator upper_bound(const Key &key) const;\n\n'

        'template <class K>\n'
        'iterator upper_bound(const K &x); (since C++14)\n\n'

        'template <class K>\n'
        'const_iterator upper_bound(const K &x) const; (since C++14)',

    'multimap::key_comp':
        '<multimap>\n'
        'returns the function that compares keys\n\n'

        'key_compare key_comp() const;',

    'multimap::value_comp':
        '<multimap>\n'
        'returns the function that compares keys in objects of type value_type\n\n'

        'std::multimap::value_compare value_comp() const;',

    'std::swap':
        '<multimap>\n'
        'specializes the std::swap algorithm\n\n'

        'template <class Key, class T, class Compare, class Alloc>\n'
        'void swap( \n'
        '    multimap<Key, T, Compare, Alloc> &lhs, \n'
        '    multimap<Key, T, Compare, Alloc> &rhs \n'
        ');',

    'multiset':
        '<multiset>\n'
        'constructs the multiset\n\n'

        'explicit multiset( \n'
        '    const Compare &comp=Compare(), const Allocator &alloc=Allocator() \n'
        '); (until C++14)\n\n'

        'multiset():\n'
        'multiset(Compare()) {}\n\n'

        'explicit multiset( \n'
        '    const Compare &comp, const Allocator &alloc=Allocator() \n'
        '); (since C++14)\n\n'

        'explicit multiset(const Allocator &alloc); (since C++11)\n\n'

        'template <class InputIterator>\n'
        'multiset( \n'
        '    InputIterator first, InputIterator last, const Compare &comp=Compare(), \n'
        '    const Allocator &alloc=Allocator() \n'
        ');\n\n'

        'template <class InputIterator>\n'
        'multiset( \n'
        '    InputIterator first, InputIterator last, const Allocator &alloc \n'
        '); (since C++14)\n\n'

        'multiset(const multiset &other);\n\n'

        'multiset(const multiset &other, const Allocator &alloc); (since C++11)\n\n'

        'multiset(multiset &&other); (since C++11)\n\n'

        'multiset(multiset &&other, const Allocator &alloc); (since C++11)\n\n'

        'multiset( \n'
        '    std::initializer_list<value_type> init, const Compare &comp=Compare(), \n'
        '    const Allocator &alloc=Allocator() \n'
        '); (since C++11)\n\n'

        'multiset( \n'
        '    std::initializer_list<value_type> init, const Allocator \n'
        '); (since C++14)',

    'multiset::~multiset':
        '<multiset>\n'
        'destructs the multiset\n\n'

        '~multiset();',

    'multiset::get_allocator':
        '<multiset>\n'
        'returns the associated allocator\n\n'

        'allocator_type get_allocator() const;',

    'multiset::begin':
        '<multiset>\n'
        'returns an iterator to the beginning\n\n'

        'iterator begin();\n\n'

        'const_iterator begin() const;',

    'multiset::cbegin':
        '<multiset>\n'
        'returns an iterator to the beginning\n\n'

        'const_iterator cbegin() const; (since C++11)',

    'multiset::end':
        '<multiset>\n'
        'returns an iterator to the end\n\n'

        'iterator end();\n\n'

        'const_iterator end() const;',

    'multiset::cend':
        '<multiset>\n'
        'returns an iterator to the end\n\n'

        'const_iterator cend() const; (since C++11)',

    'multiset::rbegin':
        '<multiset>\n'
        'returns a reverse iterator to the beginning\n\n'

        'reverse_iterator rbegin();\n\n'

        'const_reverse_iterator rbegin() const;',

    'multiset::crbegin':
        '<multiset>\n'
        'returns a reverse iterator to the beginning\n\n'

        'const_reverse_iterator crbegin() const; (since C++11)',

    'multiset::rend':
        '<multiset>\n'
        'returns a reverse iterator to the end\n\n'

        'reverse_iterator rend();\n\n'

        'const_reverse_iterator rend() const;',

    'multiset::crend':
        '<multiset>\n'
        'returns a reverse iterator to the end\n\n'

        'const_reverse_iterator crend() const; (since C++11)',

    'multiset::empty':
        '<multiset>\n'
        'checks whether the container is empty\n\n'

        'bool empty() const;',

    'multiset::size':
        '<multiset>\n'
        'returns the number of elements\n\n'

        'size_type size() const;',

    'multiset::max_size':
        '<multiset>\n'
        'returns the maximum possible number of elements\n\n'

        'size_type max_size() const;',

    'multiset::clear':
        '<multiset>\n'
        'clears the contents\n\n'

        'void clear();',

    'multiset::insert':
        '<multiset>\n'
        'inserts elements or nodes (since C++17)\n\n'

        'iterator insert(const value_type &value);\n\n'

        'iterator insert(value_type &&value); (since C++11)\n\n'

        'iterator insert(iterator hint, const value_type &value); (until C++11)\n\n'

        'iterator insert(const_iterator hint, const value_type &value); (since C++11)\n\n'

        'iterator insert(const_iterator hint, value_type &&value); (since C++11)\n\n'

        'template <class InputIt>\n'
        'void insert(InputIt first, InputIt last);\n\n'

        'void insert(std::initializer_list<value_type> ilist); (since C++11)',

    'multiset::emplace':
        '<multiset>\n'
        'constructs element in-place\n\n'

        'template <class... Args>\n'
        'iterator emplace(Args&&... args); (since C++11)',

    'multiset::emplace_hint':
        '<multiset>\n'
        'constructs elements in-place using a hint\n\n'

        'template <class... Args>\n'
        'iterator emplace_hint(const_iterator hint, Args&&... args); (since C++11)',

    'multiset::erase':
        '<multiset>\n'
        'erases elements\n\n'

        'void erase(iterator pos); (until C++11)\n\n'

        'iterator erase(const_iterator pos); (since C++11)\n\n'

        'void erase(iterator first, iterator last); (until C++11)\n\n'

        'iterator erase(const_iterator first, const_iterator last); (since C++11)\n\n'

        'size_type erase(const key_type &key);',

    'multiset::swap':
        '<multiset>\n'
        'swaps the contents\n\n'

        'void swap(multiset &other);',

    'multiset::count':
        '<multiset>\n'
        'returns the number of elements matching specific key\n\n'

        'size_type count(const Key &key) const;\n\n'

        'template <class K>\n'
        'size_type count(const K &x) const; (since C++14)',

    'multiset::find':
        '<multiset>\n'
        'finds element with specific key\n\n'

        'iterator find(const Key &key);\n\n'

        'const_iterator find(const Key &key) const;\n\n'

        'template <class K>\n'
        'iterator find(const K &x); (since C++14)\n\n'

        'template <class K>\n'
        'const_iterator find(const K &x) const; (since C++14)',

    'multiset::equal_range':
        '<multiset>\n'
        'returns range of elements matching a specific key\n\n'

        'std::pair<iterator, iterator> equal_range(const Key &key);\n\n'

        'std::pair<const_iterator, const_iterator> equal_range(const Key &key) const;\n\n'

        'template <class K>\n'
        'std::pair<iterator, iterator> equal_range(const K &x); (since C++14)\n\n'

        'template <class K>\n'
        'std::pair<const_iterator, const_iterator> equal_range( \n'
        '    const K &xconst \n'
        '); (since C++14)',

    'multiset::lower_bound':
        '<multiset>\n'
        'returns an iterator to the first element not less than the given key\n\n'

        'iterator lower_bound(const Key &key);\n\n'

        'const_iterator lower_bound(const Key &key) const;\n\n'

        'template <class K>\n'
        'iterator lower_bound(const K &x); (since C++14)\n\n'

        'template <class K>\n'
        'const_iterator lower_bound(const K &x) const; (since C++14)',

    'multiset::upper_bound':
        '<multiset>\n'
        'returns an iterator to the first element greater than the given key\n\n'

        'iterator upper_bound(const Key &key);\n\n'

        'const_iterator upper_bound(const Key &key) const;\n\n'

        'template <class K>\n'
        'iterator upper_bound(const K &x); (since C++14)\n\n'

        'template <class K>\n'
        'const_iterator upper_bound(const K &x) const; (since C++14)',

    'multiset::key_comp':
        '<multiset>\n'
        'returns the function that compares keys\n\n'

        'key_compare key_comp() const;',

    'multiset::value_comp':
        '<multiset>\n'
        'returns the function that compares keys in objects of type value_type\n\n'

        'std::multiset::value_compare value_comp() const;',

    'std::swap':
        '<multiset>\n'
        'specializes the std::swap algorithm\n\n'

        'template <class Key, class Compare, class Alloc>\n'
        'void swap( \n'
        '    multiset<Key, Compare, Alloc> &lhs, multiset<Key, Compare, Alloc> &rhs \n'
        ');',

    'priority_queue':
        '<priority_queue>\n'
        'constructs the priority_queue\n\n'

        'explicit priority_queue( \n'
        '    const Compare &compare=Compare(), const Container &cont=Container() \n'
        '); (until C++11)\n\n'

        'priority_queue(const Compare &compare, const Container &cont); (since C++11)\n\n'

        'explicit priority_queue( \n'
        '    const Compare &compare=Compare(), Container &&cont=Container() \n'
        '); (since C++11)\n\n'

        'priority_queue(const priority_queue &other);\n\n'

        'priority_queue(priority_queue &&other); (since C++11)\n\n'

        'template <class Alloc>\n'
        'explicit priority_queue(const Alloc &alloc); (since C++11)\n\n'

        'template <class Alloc>\n'
        'priority_queue(const Compare &compare, const Alloc &alloc); (since C++11)\n\n'

        'template <class Alloc>\n'
        'priority_queue( \n'
        '    const Compare &compare, const Container &cont, const Alloc &alloc \n'
        '); (since C++11)\n\n'

        'template <class Alloc>\n'
        'priority_queue( \n'
        '    const Compare &compare, Container &&cont, const Alloc &alloc \n'
        '); (since C++11)\n\n'

        'template <class Alloc>\n'
        'priority_queue(const priority_queue &other, const Alloc &alloc); (since C++11)\n\n'

        'template <class Alloc>\n'
        'priority_queue(priority_queue &&other, const Alloc &alloc); (since C++11)\n\n'

        'template <class InputIt>\n'
        'priority_queue( \n'
        '    InputIt first, InputIt last, const Compare &compare, const Container &cont \n'
        '); (since C++11)\n\n'

        'template <class InputIt>\n'
        'priority_queue( \n'
        '    InputIt first, InputIt last, const Compare &compare=Compare(), \n'
        '    Container &&cont=Container() \n'
        '); (since C++11)',

    'priority_queue::~priority_queue':
        '<priority_queue>\n'
        'destructs the priority_queue\n\n'

        '~priority_queue();',

    'priority_queue::top':
        '<priority_queue>\n'
        'accesses the top element\n\n'

        'const_reference top() const;',

    'priority_queue::empty':
        '<priority_queue>\n'
        'checks whether the underlying container is empty\n\n'

        'bool empty() const;',

    'priority_queue::size':
        '<priority_queue>\n'
        'returns the number of elements\n\n'

        'size_type size() const;',

    'priority_queue::push':
        '<priority_queue>\n'
        'inserts element and sorts the underlying container\n\n'

        'void push(const value_type &value);\n\n'

        'void push(value_type &&value); (since C++11)',

    'priority_queue::emplace':
        '<priority_queue>\n'
        'constructs element in-place and sorts the underlying container\n\n'

        'template <class... Args>\n'
        'void emplace(Args&&... args); (since C++11)',

    'priority_queue::pop':
        '<priority_queue>\n'
        'removes the top element\n\n'

        'void pop();',

    'priority_queue::swap':
        '<priority_queue>\n'
        'swaps the contents\n\n'

        'void swap(priority_queue &other); (since C++11)',

    'std::swap':
        '<priority_queue>\n'
        'specializes the std::swap algorithm\n\n'

        'template <class T, class Container, class Compare>\n'
        'void swap( \n'
        '    priority_queue<T, Container, Compare> &lhs, \n'
        '    priority_queue<T, Container, Compare> &rhs \n'
        ');',

    'queue':
        '<queue>\n'
        'constructs the queue\n\n'

        'explicit queue(const Container &cont=Container()); (until C++11)\n\n'

        'explicit queue(const Container &cont); (since C++11)\n\n'

        'explicit queue(Container &&cont=Container()); (since C++11)\n\n'

        'queue(const queue &other);\n\n'

        'queue(queue &&other); (since C++11)\n\n'

        'template <class Alloc>\n'
        'explicit queue(const Alloc &alloc); (since C++11)\n\n'

        'template <class Alloc>\n'
        'queue(const Container &cont, const Alloc &alloc); (since C++11)\n\n'

        'template <class Alloc>\n'
        'queue(Container &&cont, const Alloc &alloc); (since C++11)\n\n'

        'template <class Alloc>\n'
        'queue(const queue &other, const Alloc &alloc); (since C++11)\n\n'

        'template <class Alloc>\n'
        'queue(queue &&other, const Alloc &alloc); (since C++11)',

    'queue::~queue':
        '<queue>\n'
        'destructs the queue\n\n'

        '~queue();',

    'queue::front':
        '<queue>\n'
        'access the first element\n\n'

        'reference front();\n\n'

        'const_reference front() const;',

    'queue::back':
        '<queue>\n'
        'access the last element\n\n'

        'reference back();\n\n'

        'const_reference back() const;',

    'queue::empty':
        '<queue>\n'
        'checks whether the underlying container is empty\n\n'

        'bool empty() const;',

    'queue::size':
        '<queue>\n'
        'returns the number of elements\n\n'

        'size_type size() const;',

    'queue::push':
        '<queue>\n'
        'inserts element at the end\n\n'

        'void push(const value_type &value);\n\n'

        'void push(value_type &&value); (since C++11)',

    'queue::emplace':
        '<queue>\n'
        'constructs element in-place at the end\n\n'

        'template <class... Args>\n'
        'void emplace(Args&&... args); (since C++11) (until C++17)',

    'queue::pop':
        '<queue>\n'
        'removes the first element\n\n'

        'void pop();',

    'queue::swap':
        '<queue>\n'
        'swaps the contents\n\n'

        'void swap(queue &other); (since C++11)',

    'std::swap':
        '<queue>\n'
        'specializes the std::swap algorithm\n\n'

        'template <class T, class Container>\n'
        'void swap(queue<T, Container> &lhs, queue<T, Container> &rhs);',

    'set':
        '<set>\n'
        'constructs the set\n\n'

        'explicit set( \n'
        '    const Compare &comp=Compare(), const Allocator &alloc=Allocator() \n'
        '); (until C++14)\n\n'

        'set():\n'
        'set(Compare()) {}\n\n'

        'explicit set( \n'
        '    const Compare &comp, const Allocator &alloc=Allocator() \n'
        '); (since C++14)\n\n'

        'explicit set(const Allocator &alloc); (since C++11)\n\n'

        'template <class InputIt>\n'
        'set( \n'
        '    InputIt first, InputIt last, const Compare &comp=Compare(), \n'
        '    const Allocator &alloc=Allocator() \n'
        ');\n\n'

        'template <class InputIt>\n'
        'set(InputIt first, InputIt last, const Allocator &alloc):\n'
        'set(first, last, Compare(), alloc) {} (since C++14)\n\n'

        'set(const set &other);\n\n'

        'set(const set &other, const Allocator &alloc); (since C++11)\n\n'

        'set(set &&other); (since C++11)\n\n'

        'set(set &&other, const Allocator &alloc); (since C++11)\n\n'

        'set( \n'
        '    std::initializer_list<value_type> init, const Compare &comp=Compare(), \n'
        '    const Allocator &alloc=Allocator() \n'
        '); (since C++11)\n\n'

        'set(std::initializer_list<value_type> init, const Allocator &alloc):\n'
        'set(init, Compare(), alloc) {} (since C++14)',

    'set::~set':
        '<set>\n'
        'destructs the set\n\n'

        '~set();',

    'set::get_allocator':
        '<set>\n'
        'returns the associated allocator\n\n'

        'allocator_type get_allocator() const;',

    'set::begin':
        '<set>\n'
        'returns an iterator to the beginning\n\n'

        'iterator begin();\n\n'

        'const_iterator begin() const;',

    'set::cbegin':
        '<set>\n'
        'returns an iterator to the beginning\n\n'

        'const_iterator cbegin() const; (since C++11)',

    'set::end':
        '<set>\n'
        'returns an iterator to the end\n\n'

        'iterator end();\n\n'

        'const_iterator end() const;',

    'set::cend':
        '<set>\n'
        'returns an iterator to the end\n\n'

        'const_iterator cend() const; (since C++11)',

    'set::rbegin':
        '<set>\n'
        'returns a reverse iterator to the beginning\n\n'

        'reverse_iterator rbegin();\n\n'

        'const_reverse_iterator rbegin() const;',

    'set::crbegin':
        '<set>\n'
        'returns a reverse iterator to the beginning\n\n'

        'const_reverse_iterator crbegin() const; (since C++11)',

    'set::rend':
        '<set>\n'
        'returns a reverse iterator to the end\n\n'

        'reverse_iterator rend();\n\n'

        'const_reverse_iterator rend() const;',

    'set::crend':
        '<set>\n'
        'returns a reverse iterator to the end\n\n'

        'const_reverse_iterator crend() const; (since C++11)',

    'set::empty':
        '<set>\n'
        'checks whether the container is empty\n\n'

        'bool empty() const;',

    'set::size':
        '<set>\n'
        'returns the number of elements\n\n'

        'size_type size() const;',

    'set::max_size':
        '<set>\n'
        'returns the maximum possible number of elements\n\n'

        'size_type max_size() const;',

    'set::clear':
        '<set>\n'
        'clears the contents\n\n'

        'void clear();',

    'set::insert':
        '<set>\n'
        'inserts elements or nodes (since C++17)\n\n'

        'std::pair<iterator, bool> insert(const value_type &value);\n\n'

        'std::pair<iterator, bool> insert(value_type &&value); (since C++11)\n\n'

        'iterator insert(iterator hint, const value_type &value); (until C++11)\n\n'

        'iterator insert(const_iterator hint, const value_type &value); (since C++11)\n\n'

        'iterator insert(const_iterator hint, value_type &&value); (since C++11)\n\n'

        'template <class InputIt>\n'
        'void insert(InputIt first, InputIt last);\n\n'

        'void insert(std::initializer_list<value_type> ilist); (since C++11)',

    'set::emplace':
        '<set>\n'
        'constructs element in-place\n\n'

        'template <class... Args>\n'
        'std::pair<iterator, bool> emplace(Args&&... args); (since C++11)',

    'set::emplace_hint':
        '<set>\n'
        'constructs elements in-place using a hint\n\n'

        'template <class... Args>\n'
        'iterator emplace_hint(const_iterator hint, Args&&... args); (since C++11)',

    'set::erase':
        '<set>\n'
        'erases elements\n\n'

        'void erase(iterator pos); (until C++11)\n\n'

        'iterator erase(const_iterator pos); (since C++11)\n\n'

        'void erase(iterator first, iterator last); (until C++11)\n\n'

        'iterator erase(const_iterator first, const_iterator last); (since C++11)\n\n'

        'size_type erase(const key_type &key);',

    'set::swap':
        '<set>\n'
        'swaps the contents\n\n'

        'void swap(set &other);',

    'set::count':
        '<set>\n'
        'returns the number of elements matching specific key\n\n'

        'size_type count(const Key &key) const;\n\n'

        'template <class K>\n'
        'size_type count(const K &x) const; (since C++14)',

    'set::find':
        '<set>\n'
        'finds element with specific key\n\n'

        'iterator find(const Key &key);\n\n'

        'const_iterator find(const Key &key) const;\n\n'

        'template <class K>\n'
        'iterator find(const K &x); (since C++14)\n\n'

        'template <class K>\n'
        'const_iterator find(const K &x) const; (since C++14)',

    'set::equal_range':
        '<set>\n'
        'returns range of elements matching a specific key\n\n'

        'std::pair<iterator, iterator> equal_range(const Key &key);\n\n'

        'std::pair<const_iterator, const_iterator> equal_range(const Key &key) const;\n\n'

        'template <class K>\n'
        'std::pair<iterator, iterator> equal_range(const K &x); (since C++14)\n\n'

        'template <class K>\n'
        'std::pair<const_iterator, const_iterator> equal_range( \n'
        '    const K &xconst \n'
        '); (since C++14)',

    'set::lower_bound':
        '<set>\n'
        'returns an iterator to the first element not less than the given key\n\n'

        'iterator lower_bound(const Key &key);\n\n'

        'const_iterator lower_bound(const Key &key) const;\n\n'

        'template <class K>\n'
        'iterator lower_bound(const K &x); (since C++14)\n\n'

        'template <class K>\n'
        'const_iterator lower_bound(const K &x) const; (since C++14)',

    'set::upper_bound':
        '<set>\n'
        'returns an iterator to the first element greater than the given key\n\n'

        'iterator upper_bound(const Key &key);\n\n'

        'const_iterator upper_bound(const Key &key) const;\n\n'

        'template <class K>\n'
        'iterator upper_bound(const K &x); (since C++14)\n\n'

        'template <class K>\n'
        'const_iterator upper_bound(const K &x) const; (since C++14)',

    'set::key_comp':
        '<set>\n'
        'returns the function that compares keys\n\n'

        'key_compare key_comp() const;',

    'set::value_comp':
        '<set>\n'
        'returns the function that compares keys in objects of type value_type\n\n'

        'std::set::value_compare value_comp() const;',

    'std::swap':
        '<set>\n'
        'specializes the std::swap algorithm\n\n'

        'template <class Key, class Compare, class Alloc>\n'
        'void swap(set<Key, Compare, Alloc> &lhs, set<Key, Compare, Alloc> &rhs);',

    'stack':
        '<stack>\n'
        'constructs the stack\n\n'

        'explicit stack(const Container &cont=Container()); (until C++11)\n\n'

        'explicit stack(const Container &cont); (since C++11)\n\n'

        'explicit stack(Container &&cont=Container()); (since C++11)\n\n'

        'stack(const stack &other);\n\n'

        'stack(stack &&other); (since C++11)\n\n'

        'template <class Alloc>\n'
        'explicit stack(const Alloc &alloc); (since C++11)\n\n'

        'template <class Alloc>\n'
        'stack(const Container &cont, const Alloc &alloc); (since C++11)\n\n'

        'template <class Alloc>\n'
        'stack(Container &&cont, const Alloc &alloc); (since C++11)\n\n'

        'template <class Alloc>\n'
        'stack(const stack &other, const Alloc &alloc); (since C++11)\n\n'

        'template <class Alloc>\n'
        'stack(stack &&other, const Alloc &alloc); (since C++11)',

    'stack::~stack':
        '<stack>\n'
        'destructs the stack\n\n'

        '~stack();',

    'stack::top':
        '<stack>\n'
        'accesses the top element\n\n'

        'reference top();\n\n'

        'const_reference top() const;',

    'stack::empty':
        '<stack>\n'
        'checks whether the underlying container is empty\n\n'

        'bool empty() const;',

    'stack::size':
        '<stack>\n'
        'returns the number of elements\n\n'

        'size_type size() const;',

    'stack::push':
        '<stack>\n'
        'inserts element at the top\n\n'

        'void push(const value_type &value);\n\n'

        'void push(value_type &&value); (since C++11)',

    'stack::emplace':
        '<stack>\n'
        'constructs element in-place at the top\n\n'

        'template <class... Args>\n'
        'void emplace(Args&&... args); (since C++11) (until C++17)',

    'stack::pop':
        '<stack>\n'
        'removes the top element\n\n'

        'void pop();',

    'stack::swap':
        '<stack>\n'
        'swaps the contents\n\n'

        'void swap(stack &other); (since C++11)',

    'std::swap':
        '<stack>\n'
        'specializes the std::swap algorithm\n\n'

        'template <class T, class Container>\n'
        'void swap(stack<T, Container> &lhs, stack<T, Container> &rhs);',

    'unordered_map':
        '<unordered_map>\n'
        'constructs the unordered_map\n\n'

        'explicit unordered_map( \n'
        '    size_type bucket_countimplementationdefinedconst Hash &hash=Hash(), \n'
        '    const KeyEqual &equal=KeyEqual(), const Allocator &alloc=Allocator() \n'
        '); (since C++11) (until C++14)\n\n'

        'unordered_map():\n'
        'unordered_map(size_type(/*implementation-defined*/)) {}\n\n'

        'explicit unordered_map( \n'
        '    size_type bucket_count, const Hash &hash=Hash(), \n'
        '    const KeyEqual &equal=KeyEqual(), const Allocator &alloc=Allocator() \n'
        '); (since C++14)\n\n'

        'unordered_map(size_type bucket_count, const Allocator &alloc):\n'
        'unordered_map(bucket_count, Hash(), KeyEqual(), alloc) {}\n\n'

        'unordered_map( \n'
        '    size_type bucket_count, const Hash &hash, const Allocator &alloc \n'
        '):\n'
        'unordered_map(bucket_count, hash, KeyEqual(), alloc) {} (since C++14)\n\n'

        'explicit unordered_map(const Allocator &alloc); (since C++11)\n\n'

        'template <class InputIt>\n'
        'unordered_map( \n'
        '    InputIt first, InputIt last, size_type bucket_countimplementationdefined \n'
        '    const Hash &hash=Hash(), const KeyEqual &equal=KeyEqual(), \n'
        '    const Allocator &alloc=Allocator() \n'
        '); (since C++11)\n\n'

        'template <class InputIt>\n'
        'unordered_map( \n'
        '    InputIt first, InputIt last, size_type bucket_count, const Allocator &alloc \n'
        '):\n'
        'unordered_map( \n'
        '    first, last, bucket_count, HashKeyEqualalloc \n'
        '){} (since C++14)\n\n'

        'template <class InputIt>\n'
        'unordered_map( \n'
        '    InputIt first, InputIt last, size_type bucket_count, const Hash &hash, \n'
        '    const Allocator &alloc \n'
        '):\n'
        'unordered_map( \n'
        '    first, last, bucket_count, hash, KeyEqualalloc \n'
        '){} (since C++14)\n\n'

        'unordered_map(const unordered_map &other); (since C++11)\n\n'

        'unordered_map( \n'
        '    const unordered_map &other, const Allocator &alloc \n'
        '); (since C++11)\n\n'

        'unordered_map(unordered_map &&other); (since C++11)\n\n'

        'unordered_map(unordered_map &&other, const Allocator &alloc); (since C++11)\n\n'

        'unordered_map( \n'
        '    std::initializer_list<value_type> init, size_type bucket_count \n'
        '    implementationdefinedconst Hash &hash=Hash(), \n'
        '    const KeyEqual &equal=KeyEqual(), const Allocator &alloc=Allocator() \n'
        '); (since C++11)\n\n'

        'unordered_map( \n'
        '    std::initializer_list<value_type> init, size_type bucket_count, \n'
        '    const Allocator &alloc \n'
        '):\n'
        'unordered_map(init, bucket_count, Hash(), KeyEqual(), alloc) {} (since C++14)\n\n'

        'unordered_map( \n'
        '    std::initializer_list<value_type> init, size_type bucket_count, \n'
        '    const Hash &hash, const Allocator &alloc \n'
        '):\n'
        'unordered_map(init, bucket_count, hash, KeyEqual(), alloc) {} (since C++14)',

    'unordered_map::~unordered_map':
        '<unordered_map>\n'
        'destructs the unordered_map\n\n'

        '~unordered_map(); (since C++11)',

    'unordered_map::get_allocator':
        '<unordered_map>\n'
        'returns the associated allocator\n\n'

        'allocator_type get_allocator() const; (since C++11)',

    'unordered_map::begin':
        '<unordered_map>\n'
        'returns an iterator to the beginning\n\n'

        'iterator begin(); (since C++11)\n\n'

        'const_iterator begin() const; (since C++11)',

    'unordered_map::cbegin':
        '<unordered_map>\n'
        'returns an iterator to the beginning\n\n'

        'const_iterator cbegin() const; (since C++11)',

    'unordered_map::end':
        '<unordered_map>\n'
        'returns an iterator to the end\n\n'

        'iterator end(); (since C++11)\n\n'

        'const_iterator end() const; (since C++11)',

    'unordered_map::cend':
        '<unordered_map>\n'
        'returns an iterator to the end\n\n'

        'const_iterator cend() const; (since C++11)',

    'unordered_map::empty':
        '<unordered_map>\n'
        'checks whether the container is empty\n\n'

        'bool empty() const; (since C++11)',

    'unordered_map::size':
        '<unordered_map>\n'
        'returns the number of elements\n\n'

        'size_type size() const; (since C++11)',

    'unordered_map::max_size':
        '<unordered_map>\n'
        'returns the maximum possible number of elements\n\n'

        'size_type max_size() const; (since C++11)',

    'unordered_map::clear':
        '<unordered_map>\n'
        'clears the contents\n\n'

        'void clear(); (since C++11)',

    'unordered_map::insert':
        '<unordered_map>\n'
        'inserts elements or nodes (since C++17)\n\n'

        'std::pair<iterator, bool> insert(const value_type &value); (since C++11)\n\n'

        'template <class P>\n'
        'std::pair<iterator, bool> insert(P &&value); (since C++11)\n\n'

        'iterator insert(const_iterator hint, const value_type &value); (since C++11)\n\n'

        'template <class P>\n'
        'iterator insert(const_iterator hint, P &&value); (since C++11)\n\n'

        'template <class InputIt>\n'
        'void insert(InputIt first, InputIt last); (since C++11)\n\n'

        'void insert(std::initializer_list<value_type> ilist); (since C++11)',

    'unordered_map::emplace':
        '<unordered_map>\n'
        'constructs element in-place\n\n'

        'template <class... Args>\n'
        'std::pair<iterator, bool> emplace(Args&&... args); (since C++11)',

    'unordered_map::emplace_hint':
        '<unordered_map>\n'
        'constructs elements in-place using a hint\n\n'

        'template <class... Args>\n'
        'iterator emplace_hint(const_iterator hint, Args&&... args); (since C++11)',

    'unordered_map::erase':
        '<unordered_map>\n'
        'erases elements\n\n'

        'iterator erase(const_iterator pos); (since C++11)\n\n'

        'iterator erase(const_iterator first, const_iterator last); (since C++11)\n\n'

        'size_type erase(const key_type &key); (since C++11)',

    'unordered_map::swap':
        '<unordered_map>\n'
        'swaps the contents\n\n'

        'void swap(unordered_map &other); (since C++11)',

    'unordered_map::at':
        '<unordered_map>\n'
        'access specified element with bounds checking\n\n'

        'T &at(const Key &key); (since C++11)\n\n'

        'const T &at(const Key &key) const; (since C++11)',

    'unordered_map::count':
        '<unordered_map>\n'
        'returns the number of elements matching specific key\n\n'

        'size_type count(const Key &key) const; (since C++11)',

    'unordered_map::find':
        '<unordered_map>\n'
        'finds element with specific key\n\n'

        'iterator find(const Key &key);\n\n'

        'const_iterator find(const Key &key) const;',

    'unordered_map::equal_range':
        '<unordered_map>\n'
        'returns range of elements matching a specific key\n\n'

        'std::pair<iterator, iterator> equal_range(const Key &key); (since C++11)\n\n'

        'std::pair<const_iterator, const_iterator> equal_range( \n'
        '    const Key &keyconst \n'
        '); (since C++11)',

    'unordered_map::begin':
        '<unordered_map>\n'
        'returns an iterator to the beginning of the specified bucket\n\n'

        'local_iterator begin(size_type n); (since C++11)\n\n'

        'const_local_iterator begin(size_type n) const; (since C++11)',

    'unordered_map::end':
        '<unordered_map>\n'
        'returns an iterator to the end of the specified bucket\n\n'

        'local_iterator end(size_type n); (since C++11)\n\n'

        'const_local_iterator end(size_type n) const; (since C++11)',

    'unordered_map::bucket_count':
        '<unordered_map>\n'
        'returns the number of buckets\n\n'

        'size_type bucket_count() const; (since C++11)',

    'unordered_map::max_bucket_count':
        '<unordered_map>\n'
        'returns the maximum number of buckets\n\n'

        'size_type max_bucket_count() const; (since C++11)',

    'unordered_map::bucket_size':
        '<unordered_map>\n'
        'returns the number of elements in specific bucket\n\n'

        'size_type bucket_size(size_type n) const; (since C++11)',

    'unordered_map::bucket':
        '<unordered_map>\n'
        'returns the bucket for specific key\n\n'

        'size_type bucket(const Key &key) const; (since C++11)',

    'unordered_map::load_factor':
        '<unordered_map>\n'
        'returns average number of elements per bucket\n\n'

        'float load_factor() const; (since C++11)',

    'unordered_map::max_load_factor':
        '<unordered_map>\n'
        'manages maximum average number of elements per bucket\n\n'

        'float max_load_factor() const; (since C++11)\n\n'

        'void max_load_factor(float ml); (since C++11)',

    'unordered_map::rehash':
        '<unordered_map>\n'
        'reserves at least the specified number of buckets. This regenerates the hash\n'
        'table.\n\n'

        'void rehash(size_type count); (since C++11)',

    'unordered_map::reserve':
        '<unordered_map>\n'
        'reserves space for at least the specified number of elements. This regenerates\n'
        'the hash table.\n\n'

        'void reserve(size_type count); (since C++11)',

    'unordered_map::hash_function':
        '<unordered_map>\n'
        'returns function used to hash the keys\n\n'

        'hasher hash_function() const; (since C++11)',

    'unordered_map::key_eq':
        '<unordered_map>\n'
        'returns the function used to compare keys for equality\n\n'

        'key_equal key_eq() const; (since C++11)',

    'std::swap':
        '<unordered_map>\n'
        'specializes the std::swap algorithm\n\n'

        'template <class Key, class T, class Hash, class KeyEqual, class Alloc>\n'
        'void swap( \n'
        '    unordered_map<Key, T, Hash, KeyEqual, Alloc> &lhs, \n'
        '    unordered_map<Key, T, Hash, KeyEqual, Alloc> &rhs \n'
        '); (since C++11)',

    'unordered_multimap':
        '<unordered_multimap>\n'
        'constructs the unordered_multimap\n\n'

        'explicit unordered_multimap( \n'
        '    size_type bucket_countimplementationdefinedconst Hash &hash=Hash(), \n'
        '    const KeyEqual &equal=KeyEqual(), const Allocator &alloc=Allocator() \n'
        '); (since C++11) (until C++14)\n\n'

        'unordered_multimap():\n'
        'unordered_multimap(size_type(/*implementation-defined*/)) {}\n\n'

        'explicit unordered_multimap( \n'
        '    size_type bucket_count, const Hash &hash=Hash(), \n'
        '    const KeyEqual &equal=KeyEqual(), const Allocator &alloc=Allocator() \n'
        '); (since C++14)\n\n'

        'unordered_multimap(size_type bucket_count, const Allocator &alloc):\n'
        'unordered_multimap(bucket_count, Hash(), KeyEqual(), alloc) {}\n\n'

        'unordered_multimap( \n'
        '    size_type bucket_count, const Hash &hash, const Allocator &alloc \n'
        '):\n'
        'unordered_multimap(bucket_count, hash, KeyEqual(), alloc) {} (since C++14)\n\n'

        'explicit unordered_multimap(const Allocator &alloc); (since C++11)\n\n'

        'template <class InputIt>\n'
        'unordered_multimap( \n'
        '    InputIt first, InputIt last, size_type bucket_countimplementationdefined \n'
        '    const Hash &hash=Hash(), const KeyEqual &equal=KeyEqual(), \n'
        '    const Allocator &alloc=Allocator() \n'
        '); (since C++11)\n\n'

        'template <class InputIt>\n'
        'unordered_multimap( \n'
        '    InputIt first, InputIt last, size_type bucket_count, const Allocator &alloc \n'
        '):\n'
        'unordered_multimap( \n'
        '    first, last, bucket_count, HashKeyEqualalloc \n'
        '){} (since C++14)\n\n'

        'template <class InputIt>\n'
        'unordered_multimap( \n'
        '    InputIt first, InputIt last, size_type bucket_count, const Hash &hash, \n'
        '    const Allocator &alloc \n'
        '):\n'
        'unordered_multimap( \n'
        '    first, last, bucket_count, hash, KeyEqualalloc \n'
        '){} (since C++14)\n\n'

        'unordered_multimap(const unordered_multimap &other); (since C++11)\n\n'

        'unordered_multimap( \n'
        '    const unordered_multimap &other, const Allocator &alloc \n'
        '); (since C++11)\n\n'

        'unordered_multimap(unordered_multimap &&other); (since C++11)\n\n'

        'unordered_multimap( \n'
        '    unordered_multimap &&other, const Allocator &alloc \n'
        '); (since C++11)\n\n'

        'unordered_multimap( \n'
        '    std::initializer_list<value_type> init, size_type bucket_count \n'
        '    implementationdefinedconst Hash &hash=Hash(), \n'
        '    const KeyEqual &equal=KeyEqual(), const Allocator &alloc=Allocator() \n'
        '); (since C++11)\n\n'

        'unordered_multimap( \n'
        '    std::initializer_list<value_type> init, size_type bucket_count, \n'
        '    const Allocator &alloc \n'
        '):\n'
        'unordered_multimap( \n'
        '    init, bucket_count, HashKeyEqualalloc \n'
        '){} (since C++14)\n\n'

        'unordered_multimap( \n'
        '    std::initializer_list<value_type> init, size_type bucket_count, \n'
        '    const Hash &hash, const Allocator &alloc \n'
        '):\n'
        'unordered_multimap( \n'
        '    init, bucket_count, hash, KeyEqualalloc \n'
        '){} (since C++14)',

    'unordered_multimap::~unordered_multimap':
        '<unordered_multimap>\n'
        'destructs the unordered_multimap\n\n'

        '~unordered_multimap(); (since C++11)',

    'unordered_multimap::get_allocator':
        '<unordered_multimap>\n'
        'returns the associated allocator\n\n'

        'allocator_type get_allocator() const; (since C++11)',

    'unordered_multimap::begin':
        '<unordered_multimap>\n'
        'returns an iterator to the beginning\n\n'

        'iterator begin(); (since C++11)\n\n'

        'const_iterator begin() const; (since C++11)',

    'unordered_multimap::cbegin':
        '<unordered_multimap>\n'
        'returns an iterator to the beginning\n\n'

        'const_iterator cbegin() const; (since C++11)',

    'unordered_multimap::end':
        '<unordered_multimap>\n'
        'returns an iterator to the end\n\n'

        'iterator end(); (since C++11)\n\n'

        'const_iterator end() const; (since C++11)',

    'unordered_multimap::cend':
        '<unordered_multimap>\n'
        'returns an iterator to the end\n\n'

        'const_iterator cend() const; (since C++11)',

    'unordered_multimap::empty':
        '<unordered_multimap>\n'
        'checks whether the container is empty\n\n'

        'bool empty() const; (since C++11)',

    'unordered_multimap::size':
        '<unordered_multimap>\n'
        'returns the number of elements\n\n'

        'size_type size() const; (since C++11)',

    'unordered_multimap::max_size':
        '<unordered_multimap>\n'
        'returns the maximum possible number of elements\n\n'

        'size_type max_size() const; (since C++11)',

    'unordered_multimap::clear':
        '<unordered_multimap>\n'
        'clears the contents\n\n'

        'void clear(); (since C++11)',

    'unordered_multimap::insert':
        '<unordered_multimap>\n'
        'inserts elements or nodes (since C++17)\n\n'

        'iterator insert(const value_type &value); (since C++11)\n\n'

        'template <class P>\n'
        'iterator insert(P &&value); (since C++11)\n\n'

        'iterator insert(const_iterator hint, const value_type &value); (since C++11)\n\n'

        'template <class P>\n'
        'iterator insert(const_iterator hint, P &&value); (since C++11)\n\n'

        'template <class InputIt>\n'
        'void insert(InputIt first, InputIt last); (since C++11)\n\n'

        'void insert(std::initializer_list<value_type> ilist); (since C++11)',

    'unordered_multimap::emplace':
        '<unordered_multimap>\n'
        'constructs element in-place\n\n'

        'template <class... Args>\n'
        'iterator emplace(Args&&... args); (since C++11)',

    'unordered_multimap::emplace_hint':
        '<unordered_multimap>\n'
        'constructs elements in-place using a hint\n\n'

        'template <class... Args>\n'
        'iterator emplace_hint(const_iterator hint, Args&&... args); (since C++11)',

    'unordered_multimap::erase':
        '<unordered_multimap>\n'
        'erases elements\n\n'

        'iterator erase(const_iterator pos); (since C++11)\n\n'

        'iterator erase(const_iterator first, const_iterator last); (since C++11)\n\n'

        'size_type erase(const key_type &key); (since C++11)',

    'unordered_multimap::swap':
        '<unordered_multimap>\n'
        'swaps the contents\n\n'

        'void swap(unordered_multimap &other); (since C++11)',

    'unordered_multimap::count':
        '<unordered_multimap>\n'
        'returns the number of elements matching specific key\n\n'

        'size_type count(const Key &key) const; (since C++11)',

    'unordered_multimap::find':
        '<unordered_multimap>\n'
        'finds element with specific key\n\n'

        'iterator find(const Key &key);\n\n'

        'const_iterator find(const Key &key) const;',

    'unordered_multimap::equal_range':
        '<unordered_multimap>\n'
        'returns range of elements matching a specific key\n\n'

        'std::pair<iterator, iterator> equal_range(const Key &key); (since C++11)\n\n'

        'std::pair<const_iterator, const_iterator> equal_range( \n'
        '    const Key &keyconst \n'
        '); (since C++11)',

    'unordered_multimap::begin':
        '<unordered_multimap>\n'
        'returns an iterator to the beginning of the specified bucket\n\n'

        'local_iterator begin(size_type n); (since C++11)\n\n'

        'const_local_iterator begin(size_type n) const; (since C++11)',

    'unordered_multimap::end':
        '<unordered_multimap>\n'
        'returns an iterator to the end of the specified bucket\n\n'

        'local_iterator end(size_type n); (since C++11)\n\n'

        'const_local_iterator end(size_type n) const; (since C++11)',

    'unordered_multimap::bucket_count':
        '<unordered_multimap>\n'
        'returns the number of buckets\n\n'

        'size_type bucket_count() const; (since C++11)',

    'unordered_multimap::max_bucket_count':
        '<unordered_multimap>\n'
        'returns the maximum number of buckets\n\n'

        'size_type max_bucket_count() const; (since C++11)',

    'unordered_multimap::bucket_size':
        '<unordered_multimap>\n'
        'returns the number of elements in specific bucket\n\n'

        'size_type bucket_size(size_type n) const; (since C++11)',

    'unordered_multimap::bucket':
        '<unordered_multimap>\n'
        'returns the bucket for specific key\n\n'

        'size_type bucket(const Key &key) const; (since C++11)',

    'unordered_multimap::load_factor':
        '<unordered_multimap>\n'
        'returns average number of elements per bucket\n\n'

        'float load_factor() const; (since C++11)',

    'unordered_multimap::max_load_factor':
        '<unordered_multimap>\n'
        'manages maximum average number of elements per bucket\n\n'

        'float max_load_factor() const; (since C++11)\n\n'

        'void max_load_factor(float ml); (since C++11)',

    'unordered_multimap::rehash':
        '<unordered_multimap>\n'
        'reserves at least the specified number of buckets. This regenerates the hash\n'
        'table.\n\n'

        'void rehash(size_type count); (since C++11)',

    'unordered_multimap::reserve':
        '<unordered_multimap>\n'
        'reserves space for at least the specified number of elements. This regenerates\n'
        'the hash table.\n\n'

        'void reserve(size_type count); (since C++11)',

    'unordered_multimap::hash_function':
        '<unordered_multimap>\n'
        'returns function used to hash the keys\n\n'

        'hasher hash_function() const; (since C++11)',

    'unordered_multimap::key_eq':
        '<unordered_multimap>\n'
        'returns the function used to compare keys for equality\n\n'

        'key_equal key_eq() const; (since C++11)',

    'std::swap':
        '<unordered_multimap>\n'
        'specializes the std::swap algorithm\n\n'

        'template <class Key, class T, class Hash, class KeyEqual, class Alloc>\n'
        'void swap( \n'
        '    unordered_multimap<Key, T, Hash, KeyEqual, Alloc> &lhs, \n'
        '    unordered_multimap<Key, T, Hash, KeyEqual, Alloc> &rhs \n'
        '); (since C++11)',

    'unordered_multiset':
        '<unordered_multiset>\n'
        'constructs the unordered_multiset\n\n'

        'explicit unordered_multiset( \n'
        '    size_type bucket_countimplementationdefinedconst Hash &hash=Hash(), \n'
        '    const KeyEqual &equal=KeyEqual(), const Allocator &alloc=Allocator() \n'
        '); (since C++11) (until C++14)\n\n'

        'unordered_multiset():\n'
        'unordered_multiset(size_type(/*implementation-defined*/)) {}\n\n'

        'explicit unordered_multiset( \n'
        '    size_type bucket_count, const Hash &hash=Hash(), \n'
        '    const KeyEqual &equal=KeyEqual(), const Allocator &alloc=Allocator() \n'
        '); (since C++14)\n\n'

        'unordered_multiset(size_type bucket_count, const Allocator &alloc):\n'
        'unordered_multiset(bucket_count, Hash(), KeyEqual(), alloc) {}\n\n'

        'unordered_multiset( \n'
        '    size_type bucket_count, const Hash &hash, const Allocator &alloc \n'
        '):\n'
        'unordered_multiset(bucket_count, hash, KeyEqual(), alloc) {} (since C++14)\n\n'

        'explicit unordered_multiset(const Allocator &alloc); (since C++11)\n\n'

        'template <class InputIt>\n'
        'unordered_multiset( \n'
        '    InputIt first, InputIt last, size_type bucket_countimplementationdefined \n'
        '    const Hash &hash=Hash(), const KeyEqual &equal=KeyEqual(), \n'
        '    const Allocator &alloc=Allocator() \n'
        '); (since C++11)\n\n'

        'template <class InputIt>\n'
        'unordered_multiset( \n'
        '    InputIt first, InputIt last, size_type bucket_count, const Allocator &alloc \n'
        '):\n'
        'unordered_multiset( \n'
        '    first, last, bucket_count, HashKeyEqualalloc \n'
        '){} (since C++14)\n\n'

        'template <class InputIt>\n'
        'unordered_multiset( \n'
        '    InputIt first, InputIt last, size_type bucket_count, const Hash &hash, \n'
        '    const Allocator &alloc \n'
        '):\n'
        'unordered_multiset( \n'
        '    first, last, bucket_count, hash, KeyEqualalloc \n'
        '){} (since C++14)\n\n'

        'unordered_multiset(const unordered_multiset &other); (since C++11)\n\n'

        'unordered_multiset( \n'
        '    const unordered_multiset &other, const Allocator &alloc \n'
        '); (since C++11)\n\n'

        'unordered_multiset(unordered_multiset &&other); (since C++11)\n\n'

        'unordered_multiset( \n'
        '    unordered_multiset &&other, const Allocator &alloc \n'
        '); (since C++11)\n\n'

        'unordered_multiset( \n'
        '    std::initializer_list<value_type> init, size_type bucket_count \n'
        '    implementationdefinedconst Hash &hash=Hash(), \n'
        '    const KeyEqual &equal=KeyEqual(), const Allocator &alloc=Allocator() \n'
        '); (since C++11)\n\n'

        'unordered_multiset( \n'
        '    std::initializer_list<value_type> init, size_type bucket_count, \n'
        '    const Allocator &alloc \n'
        '):\n'
        'unordered_multiset( \n'
        '    init, bucket_count, HashKeyEqualalloc \n'
        '){} (since C++14)\n\n'

        'unordered_multiset( \n'
        '    std::initializer_list<value_type> init, size_type bucket_count, \n'
        '    const Hash &hash, const Allocator &alloc \n'
        '):\n'
        'unordered_multiset( \n'
        '    init, bucket_count, hash, KeyEqualalloc \n'
        '){} (since C++14)',

    'unordered_multiset::~unordered_multiset':
        '<unordered_multiset>\n'
        'destructs the unordered_multiset\n\n'

        '~unordered_multiset(); (since C++11)',

    'unordered_multiset::get_allocator':
        '<unordered_multiset>\n'
        'returns the associated allocator\n\n'

        'allocator_type get_allocator() const; (since C++11)',

    'unordered_multiset::begin':
        '<unordered_multiset>\n'
        'returns an iterator to the beginning\n\n'

        'iterator begin(); (since C++11)\n\n'

        'const_iterator begin() const; (since C++11)',

    'unordered_multiset::cbegin':
        '<unordered_multiset>\n'
        'returns an iterator to the beginning\n\n'

        'const_iterator cbegin() const; (since C++11)',

    'unordered_multiset::end':
        '<unordered_multiset>\n'
        'returns an iterator to the end\n\n'

        'iterator end(); (since C++11)\n\n'

        'const_iterator end() const; (since C++11)',

    'unordered_multiset::cend':
        '<unordered_multiset>\n'
        'returns an iterator to the end\n\n'

        'const_iterator cend() const; (since C++11)',

    'unordered_multiset::empty':
        '<unordered_multiset>\n'
        'checks whether the container is empty\n\n'

        'bool empty() const; (since C++11)',

    'unordered_multiset::size':
        '<unordered_multiset>\n'
        'returns the number of elements\n\n'

        'size_type size() const; (since C++11)',

    'unordered_multiset::max_size':
        '<unordered_multiset>\n'
        'returns the maximum possible number of elements\n\n'

        'size_type max_size() const; (since C++11)',

    'unordered_multiset::clear':
        '<unordered_multiset>\n'
        'clears the contents\n\n'

        'void clear(); (since C++11)',

    'unordered_multiset::insert':
        '<unordered_multiset>\n'
        'inserts elements or nodes (since C++17)\n\n'

        'iterator insert(const value_type &value); (since C++11)\n\n'

        'iterator insert(value_type &&value); (since C++11)\n\n'

        'iterator insert(const_iterator hint, const value_type &value); (since C++11)\n\n'

        'iterator insert(const_iterator hint, value_type &&value); (since C++11)\n\n'

        'template <class InputIt>\n'
        'void insert(InputIt first, InputIt last); (since C++11)\n\n'

        'void insert(std::initializer_list<value_type> ilist); (since C++11)',

    'unordered_multiset::emplace':
        '<unordered_multiset>\n'
        'constructs element in-place\n\n'

        'template <class... Args>\n'
        'iterator emplace(Args&&... args); (since C++11)',

    'unordered_multiset::emplace_hint':
        '<unordered_multiset>\n'
        'constructs elements in-place using a hint\n\n'

        'template <class... Args>\n'
        'iterator emplace_hint(const_iterator hint, Args&&... args); (since C++11)',

    'unordered_multiset::erase':
        '<unordered_multiset>\n'
        'erases elements\n\n'

        'iterator erase(const_iterator pos); (since C++11)\n\n'

        'iterator erase(const_iterator first, const_iterator last); (since C++11)\n\n'

        'size_type erase(const key_type &key); (since C++11)',

    'unordered_multiset::swap':
        '<unordered_multiset>\n'
        'swaps the contents\n\n'

        'void swap(unordered_multiset &other); (since C++11)',

    'unordered_multiset::count':
        '<unordered_multiset>\n'
        'returns the number of elements matching specific key\n\n'

        'size_type count(const Key &key) const; (since C++11)',

    'unordered_multiset::find':
        '<unordered_multiset>\n'
        'finds element with specific key\n\n'

        'iterator find(const Key &key);\n\n'

        'const_iterator find(const Key &key) const;',

    'unordered_multiset::equal_range':
        '<unordered_multiset>\n'
        'returns range of elements matching a specific key\n\n'

        'std::pair<iterator, iterator> equal_range(const Key &key); (since C++11)\n\n'

        'std::pair<const_iterator, const_iterator> equal_range( \n'
        '    const Key &keyconst \n'
        '); (since C++11)',

    'unordered_multiset::begin':
        '<unordered_multiset>\n'
        'returns an iterator to the beginning of the specified bucket\n\n'

        'local_iterator begin(size_type n); (since C++11)\n\n'

        'const_local_iterator begin(size_type n) const; (since C++11)',

    'unordered_multiset::end':
        '<unordered_multiset>\n'
        'returns an iterator to the end of the specified bucket\n\n'

        'local_iterator end(size_type n); (since C++11)\n\n'

        'const_local_iterator end(size_type n) const; (since C++11)',

    'unordered_multiset::bucket_count':
        '<unordered_multiset>\n'
        'returns the number of buckets\n\n'

        'size_type bucket_count() const; (since C++11)',

    'unordered_multiset::max_bucket_count':
        '<unordered_multiset>\n'
        'returns the maximum number of buckets\n\n'

        'size_type max_bucket_count() const; (since C++11)',

    'unordered_multiset::bucket_size':
        '<unordered_multiset>\n'
        'returns the number of elements in specific bucket\n\n'

        'size_type bucket_size(size_type n) const; (since C++11)',

    'unordered_multiset::bucket':
        '<unordered_multiset>\n'
        'returns the bucket for specific key\n\n'

        'size_type bucket(const Key &key) const; (since C++11)',

    'unordered_multiset::load_factor':
        '<unordered_multiset>\n'
        'returns average number of elements per bucket\n\n'

        'float load_factor() const; (since C++11)',

    'unordered_multiset::max_load_factor':
        '<unordered_multiset>\n'
        'manages maximum average number of elements per bucket\n\n'

        'float max_load_factor() const; (since C++11)\n\n'

        'void max_load_factor(float ml); (since C++11)',

    'unordered_multiset::rehash':
        '<unordered_multiset>\n'
        'reserves at least the specified number of buckets. This regenerates the hash\n'
        'table.\n\n'

        'void rehash(size_type count); (since C++11)',

    'unordered_multiset::reserve':
        '<unordered_multiset>\n'
        'reserves space for at least the specified number of elements. This regenerates\n'
        'the hash table.\n\n'

        'void reserve(size_type count); (since C++11)',

    'unordered_multiset::hash_function':
        '<unordered_multiset>\n'
        'returns function used to hash the keys\n\n'

        'hasher hash_function() const; (since C++11)',

    'unordered_multiset::key_eq':
        '<unordered_multiset>\n'
        'returns the function used to compare keys for equality\n\n'

        'key_equal key_eq() const; (since C++11)',

    'std::swap':
        '<unordered_multiset>\n'
        'specializes the std::swap algorithm\n\n'

        'template <class Key, class Hash, class KeyEqual, class Alloc>\n'
        'void swap( \n'
        '    unordered_multiset<Key, Hash, KeyEqual, Alloc> &lhs, \n'
        '    unordered_multiset<Key, Hash, KeyEqual, Alloc> &rhs \n'
        '); (since C++11)',

    'unordered_set':
        '<unordered_set>\n'
        'constructs the unordered_set\n\n'

        'explicit unordered_set( \n'
        '    size_type bucket_countimplementationdefinedconst Hash &hash=Hash(), \n'
        '    const KeyEqual &equal=KeyEqual(), const Allocator &alloc=Allocator() \n'
        '); (since C++11) (until C++14)\n\n'

        'unordered_set():\n'
        'unordered_set(size_type(/*implementation-defined*/)) {}\n\n'

        'explicit unordered_set( \n'
        '    size_type bucket_count, const Hash &hash=Hash(), \n'
        '    const KeyEqual &equal=KeyEqual(), const Allocator &alloc=Allocator() \n'
        '); (since C++14)\n\n'

        'unordered_set(size_type bucket_count, const Allocator &alloc):\n'
        'unordered_set(bucket_count, Hash(), KeyEqual(), alloc) {}\n\n'

        'unordered_set( \n'
        '    size_type bucket_count, const Hash &hash, const Allocator &alloc \n'
        '):\n'
        'unordered_set(bucket_count, hash, KeyEqual(), alloc) {} (since C++14)\n\n'

        'explicit unordered_set(const Allocator &alloc); (since C++11)\n\n'

        'template <class InputIt>\n'
        'unordered_set( \n'
        '    InputIt first, InputIt last, size_type bucket_countimplementationdefined \n'
        '    const Hash &hash=Hash(), const KeyEqual &equal=KeyEqual(), \n'
        '    const Allocator &alloc=Allocator() \n'
        '); (since C++11)\n\n'

        'template <class InputIt>\n'
        'unordered_set( \n'
        '    InputIt first, InputIt last, size_type bucket_count, const Allocator &alloc \n'
        '):\n'
        'unordered_set( \n'
        '    first, last, bucket_count, HashKeyEqualalloc \n'
        '){} (since C++14)\n\n'

        'template <class InputIt>\n'
        'unordered_set( \n'
        '    InputIt first, InputIt last, size_type bucket_count, const Hash &hash, \n'
        '    const Allocator &alloc \n'
        '):\n'
        'unordered_set( \n'
        '    first, last, bucket_count, hash, KeyEqualalloc \n'
        '){} (since C++14)\n\n'

        'unordered_set(const unordered_set &other); (since C++11)\n\n'

        'unordered_set( \n'
        '    const unordered_set &other, const Allocator &alloc \n'
        '); (since C++11)\n\n'

        'unordered_set(unordered_set &&other); (since C++11)\n\n'

        'unordered_set(unordered_set &&other, const Allocator &alloc); (since C++11)\n\n'

        'unordered_set( \n'
        '    std::initializer_list<value_type> init, size_type bucket_count \n'
        '    implementationdefinedconst Hash &hash=Hash(), \n'
        '    const KeyEqual &equal=KeyEqual(), const Allocator &alloc=Allocator() \n'
        '); (since C++11)\n\n'

        'unordered_set( \n'
        '    std::initializer_list<value_type> init, size_type bucket_count, \n'
        '    const Allocator &alloc \n'
        '):\n'
        'unordered_set(init, bucket_count, Hash(), KeyEqual(), alloc) {} (since C++14)\n\n'

        'unordered_set( \n'
        '    std::initializer_list<value_type> init, size_type bucket_count, \n'
        '    const Hash &hash, const Allocator &alloc \n'
        '):\n'
        'unordered_set(init, bucket_count, hash, KeyEqual(), alloc) {} (since C++14)',

    'unordered_set::~unordered_set':
        '<unordered_set>\n'
        'destructs the unordered_set\n\n'

        '~unordered_set(); (since C++11)',

    'unordered_set::get_allocator':
        '<unordered_set>\n'
        'returns the associated allocator\n\n'

        'allocator_type get_allocator() const; (since C++11)',

    'unordered_set::begin':
        '<unordered_set>\n'
        'returns an iterator to the beginning\n\n'

        'iterator begin(); (since C++11)\n\n'

        'const_iterator begin() const; (since C++11)',

    'unordered_set::cbegin':
        '<unordered_set>\n'
        'returns an iterator to the beginning\n\n'

        'const_iterator cbegin() const; (since C++11)',

    'unordered_set::end':
        '<unordered_set>\n'
        'returns an iterator to the end\n\n'

        'iterator end(); (since C++11)\n\n'

        'const_iterator end() const; (since C++11)',

    'unordered_set::cend':
        '<unordered_set>\n'
        'returns an iterator to the end\n\n'

        'const_iterator cend() const; (since C++11)',

    'unordered_set::empty':
        '<unordered_set>\n'
        'checks whether the container is empty\n\n'

        'bool empty() const; (since C++11)',

    'unordered_set::size':
        '<unordered_set>\n'
        'returns the number of elements\n\n'

        'size_type size() const; (since C++11)',

    'unordered_set::max_size':
        '<unordered_set>\n'
        'returns the maximum possible number of elements\n\n'

        'size_type max_size() const; (since C++11)',

    'unordered_set::clear':
        '<unordered_set>\n'
        'clears the contents\n\n'

        'void clear(); (since C++11)',

    'unordered_set::insert':
        '<unordered_set>\n'
        'inserts elements or nodes (since C++17)\n\n'

        'std::pair<iterator, bool> insert(const value_type &value); (since C++11)\n\n'

        'std::pair<iterator, bool> insert(value_type &&value); (since C++11)\n\n'

        'iterator insert(const_iterator hint, const value_type &value); (since C++11)\n\n'

        'iterator insert(const_iterator hint, value_type &&value); (since C++11)\n\n'

        'template <class InputIt>\n'
        'void insert(InputIt first, InputIt last); (since C++11)\n\n'

        'void insert(std::initializer_list<value_type> ilist); (since C++11)',

    'unordered_set::emplace':
        '<unordered_set>\n'
        'constructs element in-place\n\n'

        'template <class... Args>\n'
        'std::pair<iterator, bool> emplace(Args&&... args); (since C++11)',

    'unordered_set::emplace_hint':
        '<unordered_set>\n'
        'constructs elements in-place using a hint\n\n'

        'template <class... Args>\n'
        'iterator emplace_hint(const_iterator hint, Args&&... args); (since C++11)',

    'unordered_set::erase':
        '<unordered_set>\n'
        'erases elements\n\n'

        'iterator erase(const_iterator pos); (since C++11)\n\n'

        'iterator erase(const_iterator first, const_iterator last); (since C++11)\n\n'

        'size_type erase(const key_type &key); (since C++11)',

    'unordered_set::swap':
        '<unordered_set>\n'
        'swaps the contents\n\n'

        'void swap(unordered_set &other); (since C++11)',

    'unordered_set::count':
        '<unordered_set>\n'
        'returns the number of elements matching specific key\n\n'

        'size_type count(const Key &key) const; (since C++11)',

    'unordered_set::find':
        '<unordered_set>\n'
        'finds element with specific key\n\n'

        'iterator find(const Key &key);\n\n'

        'const_iterator find(const Key &key) const;',

    'unordered_set::equal_range':
        '<unordered_set>\n'
        'returns range of elements matching a specific key\n\n'

        'std::pair<iterator, iterator> equal_range(const Key &key); (since C++11)\n\n'

        'std::pair<const_iterator, const_iterator> equal_range( \n'
        '    const Key &keyconst \n'
        '); (since C++11)',

    'unordered_set::begin':
        '<unordered_set>\n'
        'returns an iterator to the beginning of the specified bucket\n\n'

        'local_iterator begin(size_type n); (since C++11)\n\n'

        'const_local_iterator begin(size_type n) const; (since C++11)',

    'unordered_set::end':
        '<unordered_set>\n'
        'returns an iterator to the end of the specified bucket\n\n'

        'local_iterator end(size_type n); (since C++11)\n\n'

        'const_local_iterator end(size_type n) const; (since C++11)',

    'unordered_set::bucket_count':
        '<unordered_set>\n'
        'returns the number of buckets\n\n'

        'size_type bucket_count() const; (since C++11)',

    'unordered_set::max_bucket_count':
        '<unordered_set>\n'
        'returns the maximum number of buckets\n\n'

        'size_type max_bucket_count() const; (since C++11)',

    'unordered_set::bucket_size':
        '<unordered_set>\n'
        'returns the number of elements in specific bucket\n\n'

        'size_type bucket_size(size_type n) const; (since C++11)',

    'unordered_set::bucket':
        '<unordered_set>\n'
        'returns the bucket for specific key\n\n'

        'size_type bucket(const Key &key) const; (since C++11)',

    'unordered_set::load_factor':
        '<unordered_set>\n'
        'returns average number of elements per bucket\n\n'

        'float load_factor() const; (since C++11)',

    'unordered_set::max_load_factor':
        '<unordered_set>\n'
        'manages maximum average number of elements per bucket\n\n'

        'float max_load_factor() const; (since C++11)\n\n'

        'void max_load_factor(float ml); (since C++11)',

    'unordered_set::rehash':
        '<unordered_set>\n'
        'reserves at least the specified number of buckets. This regenerates the hash\n'
        'table.\n\n'

        'void rehash(size_type count); (since C++11)',

    'unordered_set::reserve':
        '<unordered_set>\n'
        'reserves space for at least the specified number of elements. This regenerates\n'
        'the hash table.\n\n'

        'void reserve(size_type count); (since C++11)',

    'unordered_set::hash_function':
        '<unordered_set>\n'
        'returns function used to hash the keys\n\n'

        'hasher hash_function() const; (since C++11)',

    'unordered_set::key_eq':
        '<unordered_set>\n'
        'returns the function used to compare keys for equality\n\n'

        'key_equal key_eq() const; (since C++11)',

    'std::swap':
        '<unordered_set>\n'
        'specializes the std::swap algorithm\n\n'

        'template <class Key, class Hash, class KeyEqual, class Alloc>\n'
        'void swap( \n'
        '    unordered_set<Key, Hash, KeyEqual, Alloc> &lhs, \n'
        '    unordered_set<Key, Hash, KeyEqual, Alloc> &rhs \n'
        '); (since C++11)',

    'vector':
        '<vector>\n'
        'constructs the vector\n\n'

        'explicit vector(const Allocator &alloc=Allocator()); (until C++14)\n\n'

        'vector():\n'
        'vector(Allocator()) {}\n\n'

        'explicit vector(const Allocator &alloc); (since C++14)\n\n'

        'explicit vector( \n'
        '    size_type count, const T &value=T(), const Allocator &alloc=Allocator() \n'
        '); (until C++11)\n\n'

        'vector( \n'
        '    size_type count, const T &value, const Allocator &alloc=Allocator() \n'
        '); (since C++11)\n\n'

        'explicit vector(size_type count); (since C++11) (until C++14)\n\n'

        'explicit vector( \n'
        '    size_type count, const Allocator &alloc=Allocator() \n'
        '); (since C++14)\n\n'

        'template <class InputIt>\n'
        'vector(InputIt first, InputIt last, const Allocator &alloc=Allocator());\n\n'

        'vector(const vector &other);\n\n'

        'vector(const vector &other, const Allocator &alloc); (since C++11)\n\n'

        'vector(vector &&other); (since C++11)\n\n'

        'vector(vector &&other, const Allocator &alloc); (since C++11)\n\n'

        'vector( \n'
        '    std::initializer_list<T> init, const Allocator &alloc=Allocator() \n'
        '); (since C++11)',

    'vector::~vector':
        '<vector>\n'
        'destructs the vector\n\n'

        '~vector();',

    'vector::assign':
        '<vector>\n'
        'assigns values to the container\n\n'

        'void assign(size_type count, const T &value);\n\n'

        'template <class InputIt>\n'
        'void assign(InputIt first, InputIt last);\n\n'

        'void assign(std::initializer_list<T> ilist); (since C++11)',

    'vector::get_allocator':
        '<vector>\n'
        'returns the associated allocator\n\n'

        'allocator_type get_allocator() const;',

    'vector::at':
        '<vector>\n'
        'access specified element with bounds checking\n\n'

        'reference at(size_type pos);\n\n'

        'const_reference at(size_type pos) const;',

    'vector::front':
        '<vector>\n'
        'access the first element\n\n'

        'reference front();\n\n'

        'const_reference front() const;',

    'vector::back':
        '<vector>\n'
        'access the last element\n\n'

        'reference back();\n\n'

        'const_reference back() const;',

    'vector::data':
        '<vector>\n'
        'direct access to the underlying array\n\n'

        'T *data(); (since C++11)\n\n'

        'const T *data() const; (since C++11)',

    'vector::begin':
        '<vector>\n'
        'returns an iterator to the beginning\n\n'

        'iterator begin();\n\n'

        'const_iterator begin() const;',

    'vector::cbegin':
        '<vector>\n'
        'returns an iterator to the beginning\n\n'

        'const_iterator cbegin() const; (since C++11)',

    'vector::end':
        '<vector>\n'
        'returns an iterator to the end\n\n'

        'iterator end();\n\n'

        'const_iterator end() const;',

    'vector::cend':
        '<vector>\n'
        'returns an iterator to the end\n\n'

        'const_iterator cend() const; (since C++11)',

    'vector::rbegin':
        '<vector>\n'
        'returns a reverse iterator to the beginning\n\n'

        'reverse_iterator rbegin();\n\n'

        'const_reverse_iterator rbegin() const;',

    'vector::crbegin':
        '<vector>\n'
        'returns a reverse iterator to the beginning\n\n'

        'const_reverse_iterator crbegin() const; (since C++11)',

    'vector::rend':
        '<vector>\n'
        'returns a reverse iterator to the end\n\n'

        'reverse_iterator rend();\n\n'

        'const_reverse_iterator rend() const;',

    'vector::crend':
        '<vector>\n'
        'returns a reverse iterator to the end\n\n'

        'const_reverse_iterator crend() const; (since C++11)',

    'vector::empty':
        '<vector>\n'
        'checks whether the container is empty\n\n'

        'bool empty() const;',

    'vector::size':
        '<vector>\n'
        'returns the number of elements\n\n'

        'size_type size() const;',

    'vector::max_size':
        '<vector>\n'
        'returns the maximum possible number of elements\n\n'

        'size_type max_size() const;',

    'vector::reserve':
        '<vector>\n'
        'reserves storage\n\n'

        'void reserve(size_type new_cap);',

    'vector::capacity':
        '<vector>\n'
        'returns the number of elements that can be held in currently allocated storage\n\n'

        'size_type capacity() const;',

    'vector::shrink_to_fit':
        '<vector>\n'
        'reduces memory usage by freeing unused memory\n\n'

        'void shrink_to_fit(); (since C++11)',

    'vector::clear':
        '<vector>\n'
        'clears the contents\n\n'

        'void clear();',

    'vector::insert':
        '<vector>\n'
        'inserts elements\n\n'

        'iterator insert(iterator pos, const T &value); (until C++11)\n\n'

        'iterator insert(const_iterator pos, const T &value); (since C++11)\n\n'

        'iterator insert(const_iterator pos, T &&value); (since C++11)\n\n'

        'void insert(iterator pos, size_type count, const T &value); (until C++11)\n\n'

        'iterator insert( \n'
        '    const_iterator pos, size_type count, const T &value \n'
        '); (since C++11)\n\n'

        'template <class InputIt>\n'
        'void insert(iterator pos, InputIt first, InputIt last); (until C++11)\n\n'

        'template <class InputIt>\n'
        'iterator insert(const_iterator pos, InputIt first, InputIt last); (since C++11)\n\n'

        'iterator insert( \n'
        '    const_iterator pos, std::initializer_list<T> ilist \n'
        '); (since C++11)',

    'vector::emplace':
        '<vector>\n'
        'constructs element in-place\n\n'

        'template <class... Args>\n'
        'iterator emplace(const_iterator pos, Args&&... args); (since C++11)',

    'vector::erase':
        '<vector>\n'
        'erases elements\n\n'

        'iterator erase(iterator pos); (until C++11)\n\n'

        'iterator erase(const_iterator pos); (since C++11)\n\n'

        'iterator erase(iterator first, iterator last); (until C++11)\n\n'

        'iterator erase(const_iterator first, const_iterator last); (since C++11)',

    'vector::push_back':
        '<vector>\n'
        'adds an element to the end\n\n'

        'void push_back(const T &value);\n\n'

        'void push_back(T &&value); (since C++11)',

    'vector::emplace_back':
        '<vector>\n'
        'constructs an element in-place at the end\n\n'

        'template <class... Args>\n'
        'void emplace_back(Args&&... args); (since C++11) (until C++17)',

    'vector::pop_back':
        '<vector>\n'
        'removes the last element\n\n'

        'void pop_back();',

    'vector::resize':
        '<vector>\n'
        'changes the number of elements stored\n\n'

        'void resize(size_type count, T value=T()); (until C++11)\n\n'

        'void resize(size_type count); (since C++11)\n\n'

        'void resize(size_type count, const value_type &value); (since C++11)',

    'vector::swap':
        '<vector>\n'
        'swaps the contents\n\n'

        'void swap(vector &other);',

    'std::swap':
        '<vector>\n'
        'specializes the std::swap algorithm\n\n'

        'template <class T, class Alloc>\n'
        'void swap(vector<T, Alloc> &lhs, vector<T, Alloc> &rhs);',

    'flip':
        '<vector_bool>\n'
        'flips all the bits\n\n'

        'void flip();',

    'std::swap':
        '<vector_bool>\n'
        'specializes the std::swap algorithm\n\n'

        'template <class T, class Alloc>\n'
        'void swap(vector<T, Alloc> &lhs, vector<T, Alloc> &rhs);',

    'all_of':
        '<algorithm>\n'
        'checks if a predicate is true for all, any or none of the elements in a range\n\n'

        'template <class InputIt, class UnaryPredicate>\n'
        'bool all_of(InputIt first, InputIt last, UnaryPredicate p); (since C++11)',

    'any_of':
        '<algorithm>\n'
        'checks if a predicate is true for all, any or none of the elements in a range\n\n'

        'template <class InputIt, class UnaryPredicate>\n'
        'bool any_of(InputIt first, InputIt last, UnaryPredicate p); (since C++11)',

    'none_of':
        '<algorithm>\n'
        'checks if a predicate is true for all, any or none of the elements in a range\n\n'

        'template <class InputIt, class UnaryPredicate>\n'
        'bool none_of(InputIt first, InputIt last, UnaryPredicate p); (since C++11)',

    'for_each':
        '<algorithm>\n'
        'applies a function to a range of elements\n\n'

        'template <class InputIt, class UnaryFunction>\n'
        'UnaryFunction for_each(InputIt first, InputIt last, UnaryFunction f);',

    'count':
        '<algorithm>\n'
        'returns the number of elements satisfying specific criteria\n\n'

        'template <class InputIt, class T>\n'
        'typename iterator_traits<InputIt>::difference_type count( \n'
        '    InputIt first, InputIt last, const T &value \n'
        ');',

    'count_if':
        '<algorithm>\n'
        'returns the number of elements satisfying specific criteria\n\n'

        'template <class InputIt, class UnaryPredicate>\n'
        'typename iterator_traits<InputIt>::difference_type count_if( \n'
        '    InputIt first, InputIt last, UnaryPredicate p \n'
        ');',

    'mismatch':
        '<algorithm>\n'
        'finds the first position where two ranges differ\n\n'

        'template <class InputIt1, class InputIt2>\n'
        'std::pair<InputIt1, InputIt2> mismatch( \n'
        '    InputIt1 first1, InputIt1 last1, InputIt2 first2 \n'
        ');\n\n'

        'template <class InputIt1, class InputIt2, class BinaryPredicate>\n'
        'std::pair<InputIt1, InputIt2> mismatch( \n'
        '    InputIt1 first1, InputIt1 last1, InputIt2 first2, BinaryPredicate p \n'
        ');\n\n'

        'template <class InputIt1, class InputIt2>\n'
        'std::pair<InputIt1, InputIt2> mismatch( \n'
        '    InputIt1 first1, InputIt1 last1, InputIt2 first2, InputIt2 last2 \n'
        '); (since C++14)\n\n'

        'template <class InputIt1, class InputIt2, class BinaryPredicate>\n'
        'std::pair<InputIt1, InputIt2> mismatch( \n'
        '    InputIt1 first1, InputIt1 last1, InputIt2 first2, InputIt2 last2, \n'
        '    BinaryPredicate p \n'
        '); (since C++14)',

    'equal':
        '<algorithm>\n'
        'determines if two sets of elements are the same\n\n'

        'template <class InputIt1, class InputIt2>\n'
        'bool equal(InputIt1 first1, InputIt1 last1, InputIt2 first2);\n\n'

        'template <class InputIt1, class InputIt2, class BinaryPredicate>\n'
        'bool equal( \n'
        '    InputIt1 first1, InputIt1 last1, InputIt2 first2, BinaryPredicate p \n'
        ');\n\n'

        'template <class InputIt1, class InputIt2>\n'
        'bool equal( \n'
        '    InputIt1 first1, InputIt1 last1, InputIt2 first2, InputIt2 last2 \n'
        '); (since C++14)\n\n'

        'template <class InputIt1, class InputIt2, class BinaryPredicate>\n'
        'bool equal( \n'
        '    InputIt1 first1, InputIt1 last1, InputIt2 first2, InputIt2 last2, \n'
        '    BinaryPredicate p \n'
        '); (since C++14)',

    'find':
        '<algorithm>\n'
        'finds the first element satisfying specific criteria\n\n'

        'template <class InputIt, class T>\n'
        'InputIt find(InputIt first, InputIt last, const T &value);',

    'find_if':
        '<algorithm>\n'
        'finds the first element satisfying specific criteria\n\n'

        'template <class InputIt, class UnaryPredicate>\n'
        'InputIt find_if(InputIt first, InputIt last, UnaryPredicate p);',

    'find_if_not':
        '<algorithm>\n'
        'finds the first element satisfying specific criteria\n\n'

        'template <class InputIt, class UnaryPredicate>\n'
        'InputIt find_if_not( \n'
        '    InputIt first, InputIt last, UnaryPredicate q \n'
        '); (since C++11)',

    'find_end':
        '<algorithm>\n'
        'finds the last sequence of elements in a certain range\n\n'

        'template <class ForwardIt1, class ForwardIt2>\n'
        'ForwardIt1 find_end( \n'
        '    ForwardIt1 first, ForwardIt1 last, ForwardIt2 s_first, ForwardIt2 s_last \n'
        ');\n\n'

        'template <class ForwardIt1, class ForwardIt2, class BinaryPredicate>\n'
        'ForwardIt1 find_end( \n'
        '    ForwardIt1 first, ForwardIt1 last, ForwardIt2 s_first, ForwardIt2 s_last, \n'
        '    BinaryPredicate p \n'
        ');',

    'find_first_of':
        '<algorithm>\n'
        'searches for any one of a set of elements\n\n'

        'template <class ForwardIt1, class ForwardIt2>\n'
        'ForwardIt1 find_first_of( \n'
        '    ForwardIt1 first, ForwardIt1 last, ForwardIt2 s_first, ForwardIt2 s_last \n'
        '); (until C++11)\n\n'

        'template <class InputIt, class ForwardIt>\n'
        'InputIt find_first_of( \n'
        '    InputIt first, InputIt last, ForwardIt s_first, ForwardIt s_last \n'
        '); (since C++11)\n\n'

        'template <class ForwardIt1, class ForwardIt2, class BinaryPredicate>\n'
        'ForwardIt1 find_first_of( \n'
        '    ForwardIt1 first, ForwardIt1 last, ForwardIt2 s_first, ForwardIt2 s_last, \n'
        '    BinaryPredicate p \n'
        '); (until C++11)\n\n'

        'template <class InputIt, class ForwardIt, class BinaryPredicate>\n'
        'InputIt find_first_of( \n'
        '    InputIt first, InputIt last, ForwardIt s_first, ForwardIt s_last, \n'
        '    BinaryPredicate p \n'
        '); (since C++11)',

    'search':
        '<algorithm>\n'
        'searches for a range of elements\n\n'

        'template <class ForwardIt1, class ForwardIt2>\n'
        'ForwardIt1 search( \n'
        '    ForwardIt1 first, ForwardIt1 last, ForwardIt2 s_first, ForwardIt2 s_last \n'
        ');\n\n'

        'template <class ForwardIt1, class ForwardIt2, class BinaryPredicate>\n'
        'ForwardIt1 search( \n'
        '    ForwardIt1 first, ForwardIt1 last, ForwardIt2 s_first, ForwardIt2 s_last, \n'
        '    BinaryPredicate p \n'
        ');',

    'search_n':
        '<algorithm>\n'
        'searches for a number consecutive copies of an element in a range\n\n'

        'template <class ForwardIt, class Size, class T>\n'
        'ForwardIt search_n( \n'
        '    ForwardIt first, ForwardIt last, Size count, const T &value \n'
        ');\n\n'

        'template <class ForwardIt, class Size, class T, class BinaryPredicate>\n'
        'ForwardIt search_n( \n'
        '    ForwardIt first, ForwardIt last, Size count, const T &value, \n'
        '    BinaryPredicate p \n'
        ');',

    'copy':
        '<algorithm>\n'
        'copies a range of elements to a new location\n\n'

        'template <class InputIt, class OutputIt>\n'
        'OutputIt copy(InputIt first, InputIt last, OutputIt d_first);',

    'copy_if':
        '<algorithm>\n'
        'copies a range of elements to a new location\n\n'

        'template <class InputIt, class OutputIt, class UnaryPredicate>\n'
        'OutputIt copy_if( \n'
        '    InputIt first, InputIt last, OutputIt d_first, UnaryPredicate pred \n'
        '); (since C++11)',

    'copy_n':
        '<algorithm>\n'
        'copies a number of elements to a new location\n\n'

        'template <class InputIt, class Size, class OutputIt>\n'
        'OutputIt copy_n(InputIt first, Size count, OutputIt result); (since C++11)',

    'copy_backward':
        '<algorithm>\n'
        'copies a range of elements in backwards order\n\n'

        'template <class BidirIt1, class BidirIt2>\n'
        'BidirIt2 copy_backward(BidirIt1 first, BidirIt1 last, BidirIt2 d_last);',

    'move':
        '<algorithm>\n'
        'moves a range of elements to a new location\n\n'

        'template <class InputIt, class OutputIt>\n'
        'OutputIt move(InputIt first, InputIt last, OutputIt d_first); (since C++11)',

    'move_backward':
        '<algorithm>\n'
        'moves a range of elements to a new location in backwards order\n\n'

        'template <class BidirIt1, class BidirIt2>\n'
        'BidirIt2 move_backward( \n'
        '    BidirIt1 first, BidirIt1 last, BidirIt2 d_last \n'
        '); (since C++11)',

    'fill':
        '<algorithm>\n'
        'assigns a range of elements a certain value\n\n'

        'template <class ForwardIt, class T>\n'
        'void fill(ForwardIt first, ForwardIt last, const T &value);',

    'fill_n':
        '<algorithm>\n'
        'assigns a value to a number of elements\n\n'

        'template <class OutputIt, class Size, class T>\n'
        'void fill_n(OutputIt first, Size count, const T &value); (until C++11)\n\n'

        'template <class OutputIt, class Size, class T>\n'
        'OutputIt fill_n(OutputIt first, Size count, const T &value); (since C++11)',

    'transform':
        '<algorithm>\n'
        'applies a function to a range of elements\n\n'

        'template <class InputIt, class OutputIt, class UnaryOperation>\n'
        'OutputIt transform( \n'
        '    InputIt first1, InputIt last1, OutputIt d_first, UnaryOperation unary_op \n'
        ');\n\n'

        'template < \n'
        '    class InputIt1, class InputIt2, class OutputIt, class BinaryOperation \n'
        '>\n'
        'OutputIt transform( \n'
        '    InputIt1 first1, InputIt1 last1, InputIt2 first2, OutputIt d_first, \n'
        '    BinaryOperation binary_op \n'
        ');',

    'generate':
        '<algorithm>\n'
        'saves the result of a function in a range\n\n'

        'template <class ForwardIt, class Generator>\n'
        'void generate(ForwardIt first, ForwardIt last, Generator g);',

    'generate_n':
        '<algorithm>\n'
        'saves the result of N applications of a function\n\n'

        'template <class OutputIt, class Size, class Generator>\n'
        'void generate_n(OutputIt first, Size count, Generator g); (until C++11)\n\n'

        'template <class OutputIt, class Size, class Generator>\n'
        'OutputIt generate_n(OutputIt first, Size count, Generator g); (since C++11)',

    'remove':
        '<algorithm>\n'
        'removes elements satisfying specific criteria\n\n'

        'template <class ForwardIt, class T>\n'
        'ForwardIt remove(ForwardIt first, ForwardIt last, const T &value);',

    'remove_if':
        '<algorithm>\n'
        'removes elements satisfying specific criteria\n\n'

        'template <class ForwardIt, class UnaryPredicate>\n'
        'ForwardIt remove_if(ForwardIt first, ForwardIt last, UnaryPredicate p);',

    'remove_copy':
        '<algorithm>\n'
        'copies a range of elements omitting those that satisfy specific criteria\n\n'

        'template <class InputIt, class OutputIt, class T>\n'
        'OutputIt remove_copy( \n'
        '    InputIt first, InputIt last, OutputIt d_first, const T &value \n'
        ');',

    'remove_copy_if':
        '<algorithm>\n'
        'copies a range of elements omitting those that satisfy specific criteria\n\n'

        'template <class InputIt, class OutputIt, class UnaryPredicate>\n'
        'OutputIt remove_copy_if( \n'
        '    InputIt first, InputIt last, OutputIt d_first, UnaryPredicate p \n'
        ');',

    'replace':
        '<algorithm>\n'
        'replaces all values satisfying specific criteria with another value\n\n'

        'template <class ForwardIt, class T>\n'
        'void replace( \n'
        '    ForwardIt first, ForwardIt last, const T &old_value, const T &new_value \n'
        ');',

    'replace_if':
        '<algorithm>\n'
        'replaces all values satisfying specific criteria with another value\n\n'

        'template <class ForwardIt, class UnaryPredicate, class T>\n'
        'void replace_if( \n'
        '    ForwardIt first, ForwardIt last, UnaryPredicate p, const T &new_value \n'
        ');',

    'replace_copy':
        '<algorithm>\n'
        'copies a range, replacing elements satisfying specific criteria with another\n'
        'value\n\n'

        'template <class InputIt, class OutputIt, class T>\n'
        'OutputIt replace_copy( \n'
        '    InputIt first, InputIt last, OutputIt d_first, const T &old_value, \n'
        '    const T &new_value \n'
        ');',

    'replace_copy_if':
        '<algorithm>\n'
        'copies a range, replacing elements satisfying specific criteria with another\n'
        'value\n\n'

        'template <class InputIt, class OutputIt, class UnaryPredicate, class T>\n'
        'OutputIt replace_copy_if( \n'
        '    InputIt first, InputIt last, OutputIt d_first, UnaryPredicate p, \n'
        '    const T &new_value \n'
        ');',

    'swap':
        '<algorithm>\n'
        'swaps the values of two objects\n\n'

        'template <class T>\n'
        'void swap(T &a, T &b);\n\n'

        'template <class T2, size_t N>\n'
        'void swap(T2 (&a)[N], T2 (&b)[N]); (since C++11)',

    'swap_ranges':
        '<algorithm>\n'
        'swaps two ranges of elements\n\n'

        'template <class ForwardIt1, class ForwardIt2>\n'
        'ForwardIt2 swap_ranges(ForwardIt1 first1, ForwardIt1 last1, ForwardIt2 first2);',

    'iter_swap':
        '<algorithm>\n'
        'swaps the elements pointed to by two iterators\n\n'

        'template <class ForwardIt1, class ForwardIt2>\n'
        'void iter_swap(ForwardIt1 a, ForwardIt2 b);',

    'reverse':
        '<algorithm>\n'
        'reverses the order of elements in a range\n\n'

        'template <class BidirIt>\n'
        'void reverse(BidirIt first, BidirIt last);',

    'reverse_copy':
        '<algorithm>\n'
        'creates a copy of a range that is reversed\n\n'

        'template <class BidirIt, class OutputIt>\n'
        'OutputIt reverse_copy(BidirIt first, BidirIt last, OutputIt d_first);',

    'rotate':
        '<algorithm>\n'
        'rotates the order of elements in a range\n\n'

        'template <class ForwardIt>\n'
        'void rotate(ForwardIt first, ForwardIt n_first, ForwardIt last); (until C++11)\n\n'

        'template <class ForwardIt>\n'
        'ForwardIt rotate( \n'
        '    ForwardIt first, ForwardIt n_first, ForwardIt last \n'
        '); (since C++11)',

    'rotate_copy':
        '<algorithm>\n'
        'copies and rotate a range of elements\n\n'

        'template <class ForwardIt, class OutputIt>\n'
        'OutputIt rotate_copy( \n'
        '    ForwardIt first, ForwardIt n_first, ForwardIt last, OutputIt d_first \n'
        ');',

    'random_shuffle':
        '<algorithm>\n'
        'randomly re-orders elements in a range\n\n'

        'template <class RandomIt>\n'
        'void random_shuffle( \n'
        '    RandomIt first, RandomIt last \n'
        '); (until C++17) (deprecated in C++14)\n\n'

        'template <class RandomIt, class RandomFunc>\n'
        'void random_shuffle( \n'
        '    RandomIt first, RandomIt last, RandomFunc &r \n'
        '); (until C++11)\n\n'

        'template <class RandomIt, class RandomFunc>\n'
        'void random_shuffle( \n'
        '    RandomIt first, RandomIt last, RandomFunc &&r \n'
        '); (since C++11) (until C++17) (deprecated in C++14)',

    'shuffle':
        '<algorithm>\n'
        'randomly re-orders elements in a range\n\n'

        'template <class RandomIt, class URBG>\n'
        'void shuffle(RandomIt first, RandomIt last, URBG &&g); (since C++11)',

    'unique':
        '<algorithm>\n'
        'removes consecutive duplicate elements in a range\n\n'

        'template <class ForwardIt>\n'
        'ForwardIt unique(ForwardIt first, ForwardIt last);\n\n'

        'template <class ForwardIt, class BinaryPredicate>\n'
        'ForwardIt unique(ForwardIt first, ForwardIt last, BinaryPredicate p);',

    'unique_copy':
        '<algorithm>\n'
        'creates a copy of some range of elements that contains no consecutive duplicates\n\n'

        'template <class InputIt, class OutputIt>\n'
        'OutputIt unique_copy(InputIt first, InputIt last, OutputIt d_first);\n\n'

        'template <class InputIt, class OutputIt, class BinaryPredicate>\n'
        'OutputIt unique_copy( \n'
        '    InputIt first, InputIt last, OutputIt d_first, BinaryPredicate p \n'
        ');',

    'is_partitioned':
        '<algorithm>\n'
        'determines if the range is partitioned by the given predicate\n\n'

        'template <class InputIt, class UnaryPredicate>\n'
        'bool is_partitioned( \n'
        '    InputIt first, InputIt last, UnaryPredicate p \n'
        '); (since C++11)',

    'partition':
        '<algorithm>\n'
        'divides a range of elements into two groups\n\n'

        'template <class BidirIt, class UnaryPredicate>\n'
        'BidirIt partition(BidirIt first, BidirIt last, UnaryPredicate p); (until C++11)\n\n'

        'template <class ForwardIt, class UnaryPredicate>\n'
        'ForwardIt partition( \n'
        '    ForwardIt first, ForwardIt last, UnaryPredicate p \n'
        '); (since C++11)',

    'partition_copy':
        '<algorithm>\n'
        'copies a range dividing the elements into two groups\n\n'

        'template < \n'
        '    class InputIt, class OutputIt1, class OutputIt2, class UnaryPredicate \n'
        '>\n'
        'std::pair<OutputIt1, OutputIt2> partition_copy( \n'
        '    InputIt first, InputIt last, OutputIt1 d_first_true, \n'
        '    OutputIt2 d_first_false, UnaryPredicate p \n'
        '); (since C++11)',

    'stable_partition':
        '<algorithm>\n'
        'divides elements into two groups while preserving their relative order\n\n'

        'template <class BidirIt, class UnaryPredicate>\n'
        'BidirIt stable_partition(BidirIt first, BidirIt last, UnaryPredicate p);',

    'partition_point':
        '<algorithm>\n'
        'locates the partition point of a partitioned range\n\n'

        'template <class ForwardIt, class UnaryPredicate>\n'
        'ForwardIt partition_point( \n'
        '    ForwardIt first, ForwardIt last, UnaryPredicate p \n'
        '); (since C++11)',

    'is_sorted':
        '<algorithm>\n'
        'checks whether a range is sorted into ascending order\n\n'

        'template <class ForwardIt>\n'
        'bool is_sorted(ForwardIt first, ForwardIt last); (since C++11)\n\n'

        'template <class ForwardIt, class Compare>\n'
        'bool is_sorted(ForwardIt first, ForwardIt last, Compare comp); (since C++11)',

    'is_sorted_until':
        '<algorithm>\n'
        'finds the largest sorted subrange\n\n'

        'template <class ForwardIt>\n'
        'ForwardIt is_sorted_until(ForwardIt first, ForwardIt last); (since C++11)\n\n'

        'template <class ForwardIt, class Compare>\n'
        'ForwardIt is_sorted_until( \n'
        '    ForwardIt first, ForwardIt last, Compare comp \n'
        '); (since C++11)',

    'sort':
        '<algorithm>\n'
        'sorts a range into ascending order\n\n'

        'template <class RandomIt>\n'
        'void sort(RandomIt first, RandomIt last);\n\n'

        'template <class RandomIt, class Compare>\n'
        'void sort(RandomIt first, RandomIt last, Compare comp);',

    'partial_sort':
        '<algorithm>\n'
        'sorts the first N elements of a range\n\n'

        'template <class RandomIt>\n'
        'void partial_sort(RandomIt first, RandomIt middle, RandomIt last);\n\n'

        'template <class RandomIt, class Compare>\n'
        'void partial_sort( \n'
        '    RandomIt first, RandomIt middle, RandomIt last, Compare comp \n'
        ');',

    'partial_sort_copy':
        '<algorithm>\n'
        'copies and partially sorts a range of elements\n\n'

        'template <class InputIt, class RandomIt>\n'
        'RandomIt partial_sort_copy( \n'
        '    InputIt first, InputIt last, RandomIt d_first, RandomIt d_last \n'
        ');\n\n'

        'template <class InputIt, class RandomIt, class Compare>\n'
        'RandomIt partial_sort_copy( \n'
        '    InputIt first, InputIt last, RandomIt d_first, RandomIt d_last, \n'
        '    Compare comp \n'
        ');',

    'stable_sort':
        '<algorithm>\n'
        'sorts a range of elements while preserving order between equal elements\n\n'

        'template <class RandomIt>\n'
        'void stable_sort(RandomIt first, RandomIt last);\n\n'

        'template <class RandomIt, class Compare>\n'
        'void stable_sort(RandomIt first, RandomIt last, Compare comp);',

    'nth_element':
        '<algorithm>\n'
        'partially sorts the given range making sure that it is partitioned by the given\n'
        'element\n\n'

        'template <class RandomIt>\n'
        'void nth_element(RandomIt first, RandomIt nth, RandomIt last);\n\n'

        'template <class RandomIt, class Compare>\n'
        'void nth_element(RandomIt first, RandomIt nth, RandomIt last, Compare comp);',

    'lower_bound':
        '<algorithm>\n'
        'returns an iterator to the first element not less than the given value\n\n'

        'template <class ForwardIt, class T>\n'
        'ForwardIt lower_bound(ForwardIt first, ForwardIt last, const T &value);\n\n'

        'template <class ForwardIt, class T, class Compare>\n'
        'ForwardIt lower_bound( \n'
        '    ForwardIt first, ForwardIt last, const T &value, Compare comp \n'
        ');',

    'upper_bound':
        '<algorithm>\n'
        'returns an iterator to the first element greater than a certain value\n\n'

        'template <class ForwardIt, class T>\n'
        'ForwardIt upper_bound(ForwardIt first, ForwardIt last, const T &value);\n\n'

        'template <class ForwardIt, class T, class Compare>\n'
        'ForwardIt upper_bound( \n'
        '    ForwardIt first, ForwardIt last, const T &value, Compare comp \n'
        ');',

    'binary_search':
        '<algorithm>\n'
        'determines if an element exists in a certain range\n\n'

        'template <class ForwardIt, class T>\n'
        'bool binary_search(ForwardIt first, ForwardIt last, const T &value);\n\n'

        'template <class ForwardIt, class T, class Compare>\n'
        'bool binary_search( \n'
        '    ForwardIt first, ForwardIt last, const T &value, Compare comp \n'
        ');',

    'equal_range':
        '<algorithm>\n'
        'returns range of elements matching a specific key\n\n'

        'template <class ForwardIt, class T>\n'
        'std::pair<ForwardIt, ForwardIt> equal_range( \n'
        '    ForwardIt first, ForwardIt last, const T &value \n'
        ');\n\n'

        'template <class ForwardIt, class T, class Compare>\n'
        'std::pair<ForwardIt, ForwardIt> equal_range( \n'
        '    ForwardIt first, ForwardIt last, const T &value, Compare comp \n'
        ');',

    'merge':
        '<algorithm>\n'
        'merges two sorted ranges\n\n'

        'template <class InputIt1, class InputIt2, class OutputIt>\n'
        'OutputIt merge( \n'
        '    InputIt1 first1, InputIt1 last1, InputIt2 first2, InputIt2 last2, \n'
        '    OutputIt d_first \n'
        ');\n\n'

        'template <class InputIt1, class InputIt2, class OutputIt, class Compare>\n'
        'OutputIt merge( \n'
        '    InputIt1 first1, InputIt1 last1, InputIt2 first2, InputIt2 last2, \n'
        '    OutputIt d_first, Compare comp \n'
        ');',

    'inplace_merge':
        '<algorithm>\n'
        'merges two ordered ranges in-place\n\n'

        'template <class BidirIt>\n'
        'void inplace_merge(BidirIt first, BidirIt middle, BidirIt last);\n\n'

        'template <class BidirIt, class Compare>\n'
        'void inplace_merge(BidirIt first, BidirIt middle, BidirIt last, Compare comp);',

    'includes':
        '<algorithm>\n'
        'returns true if one set is a subset of another\n\n'

        'template <class InputIt1, class InputIt2>\n'
        'bool includes( \n'
        '    InputIt1 first1, InputIt1 last1, InputIt2 first2, InputIt2 last2 \n'
        ');\n\n'

        'template <class InputIt1, class InputIt2, class Compare>\n'
        'bool includes( \n'
        '    InputIt1 first1, InputIt1 last1, InputIt2 first2, InputIt2 last2, \n'
        '    Compare comp \n'
        ');',

    'set_difference':
        '<algorithm>\n'
        'computes the difference between two sets\n\n'

        'template <class InputIt1, class InputIt2, class OutputIt>\n'
        'OutputIt set_difference( \n'
        '    InputIt1 first1, InputIt1 last1, InputIt2 first2, InputIt2 last2, \n'
        '    OutputIt d_first \n'
        ');\n\n'

        'template <class InputIt1, class InputIt2, class OutputIt, class Compare>\n'
        'OutputIt set_difference( \n'
        '    InputIt1 first1, InputIt1 last1, InputIt2 first2, InputIt2 last2, \n'
        '    OutputIt d_first, Compare comp \n'
        ');',

    'set_intersection':
        '<algorithm>\n'
        'computes the intersection of two sets\n\n'

        'template <class InputIt1, class InputIt2, class OutputIt>\n'
        'OutputIt set_intersection( \n'
        '    InputIt1 first1, InputIt1 last1, InputIt2 first2, InputIt2 last2, \n'
        '    OutputIt d_first \n'
        ');\n\n'

        'template <class InputIt1, class InputIt2, class OutputIt, class Compare>\n'
        'OutputIt set_intersection( \n'
        '    InputIt1 first1, InputIt1 last1, InputIt2 first2, InputIt2 last2, \n'
        '    OutputIt d_first, Compare comp \n'
        ');',

    'set_symmetric_difference':
        '<algorithm>\n'
        'computes the symmetric difference between two sets\n\n'

        'template <class InputIt1, class InputIt2, class OutputIt>\n'
        'OutputIt set_symmetric_difference( \n'
        '    InputIt1 first1, InputIt1 last1, InputIt2 first2, InputIt2 last2, \n'
        '    OutputIt d_first \n'
        ');\n\n'

        'template <class InputIt1, class InputIt2, class OutputIt, class Compare>\n'
        'OutputIt set_symmetric_difference( \n'
        '    InputIt1 first1, InputIt1 last1, InputIt2 first2, InputIt2 last2, \n'
        '    OutputIt d_first, Compare comp \n'
        ');',

    'set_union':
        '<algorithm>\n'
        'computes the union of two sets\n\n'

        'template <class InputIt1, class InputIt2, class OutputIt>\n'
        'OutputIt set_union( \n'
        '    InputIt1 first1, InputIt1 last1, InputIt2 first2, InputIt2 last2, \n'
        '    OutputIt d_first \n'
        ');\n\n'

        'template <class InputIt1, class InputIt2, class OutputIt, class Compare>\n'
        'OutputIt set_union( \n'
        '    InputIt1 first1, InputIt1 last1, InputIt2 first2, InputIt2 last2, \n'
        '    OutputIt d_first, Compare comp \n'
        ');',

    'is_heap':
        '<algorithm>\n'
        'checks if the given range is a max heap\n\n'

        'template <class RandomIt>\n'
        'bool is_heap(RandomIt first, RandomIt last); (since C++11)\n\n'

        'template <class RandomIt, class Compare>\n'
        'bool is_heap(RandomIt first, RandomIt last, Compare comp); (since C++11)',

    'is_heap_until':
        '<algorithm>\n'
        'finds the largest subrange that is a max heap\n\n'

        'template <class RandomIt>\n'
        'RandomIt is_heap_until(RandomIt first, RandomIt last); (since C++11)\n\n'

        'template <class RandomIt, class Compare>\n'
        'RandomIt is_heap_until( \n'
        '    RandomIt first, RandomIt last, Compare comp \n'
        '); (since C++11)',

    'make_heap':
        '<algorithm>\n'
        'creates a max heap out of a range of elements\n\n'

        'template <class RandomIt>\n'
        'void make_heap(RandomIt first, RandomIt last);\n\n'

        'template <class RandomIt, class Compare>\n'
        'void make_heap(RandomIt first, RandomIt last, Compare comp);',

    'push_heap':
        '<algorithm>\n'
        'adds an element to a max heap\n\n'

        'template <class RandomIt>\n'
        'void push_heap(RandomIt first, RandomIt last);\n\n'

        'template <class RandomIt, class Compare>\n'
        'void push_heap(RandomIt first, RandomIt last, Compare comp);',

    'pop_heap':
        '<algorithm>\n'
        'removes the largest element from a max heap\n\n'

        'template <class RandomIt>\n'
        'void pop_heap(RandomIt first, RandomIt last);\n\n'

        'template <class RandomIt, class Compare>\n'
        'void pop_heap(RandomIt first, RandomIt last, Compare comp);',

    'sort_heap':
        '<algorithm>\n'
        'turns a max heap into a range of elements sorted in ascending order\n\n'

        'template <class RandomIt>\n'
        'void sort_heap(RandomIt first, RandomIt last);\n\n'

        'template <class RandomIt, class Compare>\n'
        'void sort_heap(RandomIt first, RandomIt last, Compare comp);',

    'max':
        '<algorithm>\n'
        'returns the greater of the given values\n\n'

        'template <class T>\n'
        'const T &max(const T &a, const T &b); (until C++14)\n\n'

        'template <class T>\n'
        'constexpr const T &max(const T &a, const T &b); (since C++14)\n\n'

        'template <class T, class Compare>\n'
        'const T &max(const T &a, const T &b, Compare comp); (until C++14)\n\n'

        'template <class T, class Compare>\n'
        'constexpr const T &max(const T &a, const T &b, Compare comp); (since C++14)\n\n'

        'template <class T>\n'
        'T max(std::initializer_list<T> ilist); (since C++11) (until C++14)\n\n'

        'template <class T>\n'
        'constexpr T max(std::initializer_list<T> ilist); (since C++14)\n\n'

        'template <class T, class Compare>\n'
        'T max( \n'
        '    std::initializer_list<T> ilist, Compare comp \n'
        '); (since C++11) (until C++14)\n\n'

        'template <class T, class Compare>\n'
        'constexpr T max(std::initializer_list<T> ilist, Compare comp); (since C++14)',

    'max_element':
        '<algorithm>\n'
        'returns the largest element in a range\n\n'

        'template <class ForwardIt>\n'
        'ForwardIt max_element(ForwardIt first, ForwardIt last); (until C++17)\n\n'

        'template <class ForwardIt, class Compare>\n'
        'ForwardIt max_element( \n'
        '    ForwardIt first, ForwardIt last, Compare cmp \n'
        '); (until C++17)',

    'min':
        '<algorithm>\n'
        'returns the smaller of the given values\n\n'

        'template <class T>\n'
        'const T &min(const T &a, const T &b); (until C++14)\n\n'

        'template <class T>\n'
        'constexpr const T &min(const T &a, const T &b); (since C++14)\n\n'

        'template <class T, class Compare>\n'
        'const T &min(const T &a, const T &b, Compare comp); (until C++14)\n\n'

        'template <class T, class Compare>\n'
        'constexpr const T &min(const T &a, const T &b, Compare comp); (since C++14)\n\n'

        'template <class T>\n'
        'T min(std::initializer_list<T> ilist); (since C++11) (until C++14)\n\n'

        'template <class T>\n'
        'constexpr T min(std::initializer_list<T> ilist); (since C++14)\n\n'

        'template <class T, class Compare>\n'
        'T min( \n'
        '    std::initializer_list<T> ilist, Compare comp \n'
        '); (since C++11) (until C++14)\n\n'

        'template <class T, class Compare>\n'
        'constexpr T min(std::initializer_list<T> ilist, Compare comp); (since C++14)',

    'min_element':
        '<algorithm>\n'
        'returns the smallest element in a range\n\n'

        'template <class ForwardIt>\n'
        'ForwardIt min_element(ForwardIt first, ForwardIt last); (until C++17)\n\n'

        'template <class ForwardIt, class Compare>\n'
        'ForwardIt min_element( \n'
        '    ForwardIt first, ForwardIt last, Compare comp \n'
        '); (until C++17)',

    'minmax':
        '<algorithm>\n'
        'returns the smaller and larger of two elements\n\n'

        'template <class T>\n'
        'std::pair<const T&, const T&> minmax( \n'
        '    const T &a, const T &b \n'
        '); (since C++11) (until C++14)\n\n'

        'template <class T>\n'
        'constexpr std::pair<const T&, const T&> minmax( \n'
        '    const T &a, const T &b \n'
        '); (since C++14)\n\n'

        'template <class T, class Compare>\n'
        'std::pair<const T&, const T&> minmax( \n'
        '    const T &a, const T &b, Compare comp \n'
        '); (since C++11) (until C++14)\n\n'

        'template <class T, class Compare>\n'
        'constexpr std::pair<const T&, const T&> minmax( \n'
        '    const T &a, const T &b, Compare comp \n'
        '); (since C++14)\n\n'

        'template <class T>\n'
        'std::pair<T, T> minmax( \n'
        '    std::initializer_list<T> ilist \n'
        '); (since C++11) (until C++14)\n\n'

        'template <class T>\n'
        'constexpr std::pair<T, T> minmax(std::initializer_list<T> ilist); (since C++14)\n\n'

        'template <class T, class Compare>\n'
        'std::pair<T, T> minmax( \n'
        '    std::initializer_list<T> ilist, Compare comp \n'
        '); (since C++11) (until C++14)\n\n'

        'template <class T, class Compare>\n'
        'constexpr std::pair<T, T> minmax( \n'
        '    std::initializer_list<T> ilist, Compare comp \n'
        '); (since C++14)',

    'minmax_element':
        '<algorithm>\n'
        'returns the smallest and the largest elements in a range\n\n'

        'template <class ForwardIt>\n'
        'std::pair<ForwardIt, ForwardIt> minmax_element( \n'
        '    ForwardIt first, ForwardIt last \n'
        '); (since C++11) (until C++17)\n\n'

        'template <class ForwardIt, class Compare>\n'
        'std::pair<ForwardIt, ForwardIt> minmax_element( \n'
        '    ForwardIt first, ForwardIt last, Compare comp \n'
        '); (since C++11) (until C++17)',

    'lexicographical_compare':
        '<algorithm>\n'
        'returns true if one range is lexicographically less than another\n\n'

        'template <class InputIt1, class InputIt2>\n'
        'bool lexicographical_compare( \n'
        '    InputIt1 first1, InputIt1 last1, InputIt2 first2, InputIt2 last2 \n'
        ');\n\n'

        'template <class InputIt1, class InputIt2, class Compare>\n'
        'bool lexicographical_compare( \n'
        '    InputIt1 first1, InputIt1 last1, InputIt2 first2, InputIt2 last2, \n'
        '    Compare comp \n'
        ');',

    'is_permutation':
        '<algorithm>\n'
        'determines if a sequence is a permutation of another sequence\n\n'

        'template <class ForwardIt1, class ForwardIt2>\n'
        'bool is_permutation( \n'
        '    ForwardIt1 first1, ForwardIt1 last1, ForwardIt2 first2 \n'
        '); (since C++11)\n\n'

        'template <class ForwardIt1, class ForwardIt2, class BinaryPredicate>\n'
        'bool is_permutation( \n'
        '    ForwardIt1 first1, ForwardIt1 last1, ForwardIt2 first2, BinaryPredicate p \n'
        '); (since C++11)\n\n'

        'template <class ForwardIt1, class ForwardIt2>\n'
        'bool is_permutation( \n'
        '    ForwardIt1 first1, ForwardIt1 last1, ForwardIt2 first2, ForwardIt2 last2 \n'
        '); (since C++14)\n\n'

        'template <class ForwardIt1, class ForwardIt2, class BinaryPredicate>\n'
        'bool is_permutation( \n'
        '    ForwardIt1 first1, ForwardIt1 last1, ForwardIt2 first2, ForwardIt2 last2, \n'
        '    BinaryPredicate p \n'
        '); (since C++14)',

    'next_permutation':
        '<algorithm>\n'
        'generates the next greater lexicographic permutation of a range of elements\n\n'

        'template <class BidirIt>\n'
        'bool next_permutation(BidirIt first, BidirIt last);\n\n'

        'template <class BidirIt, class Compare>\n'
        'bool next_permutation(BidirIt first, BidirIt last, Compare comp);',

    'prev_permutation':
        '<algorithm>\n'
        'generates the next smaller lexicographic permutation of a range of elements\n\n'

        'template <class BidirIt>\n'
        'bool prev_permutation(BidirIt first, BidirIt last);\n\n'

        'template <class BidirIt, class Compare>\n'
        'bool prev_permutation(BidirIt first, BidirIt last, Compare comp);',

    'fmod':
        '<cmath>\n'
        'remainder of the floating point division operation\n\n'

        'float fmod(float x, float y);\n\n'

        'double fmod(double x, double y);\n\n'

        'long double fmod(long double x, long double y);\n\n'

        'Promoted fmod(Arithmetic1 x, Arithmetic2 y); (since C++11)',

    'remainder':
        '<cmath>\n'
        'signed remainder of the division operation\n\n'

        'float remainder(float x, float y); (since C++11)\n\n'

        'double remainder(double x, double y); (since C++11)\n\n'

        'long double remainder(long double x, long double y); (since C++11)\n\n'

        'Promoted remainder(Arithmetic1 x, Arithmetic2 y); (since C++11)',

    'remquo':
        '<cmath>\n'
        'signed remainder as well as the three last bits of the division operation\n\n'

        'float remquo(float x, float y, int *quo); (since C++11)\n\n'

        'double remquo(double x, double y, int *quo); (since C++11)\n\n'

        'long double remquo(long double x, long double y, int *quo); (since C++11)\n\n'

        'Promoted remquo(Arithmetic1 x, Arithmetic2 y, int *quo); (since C++11)',

    'fma':
        '<cmath>\n'
        'fused multiply-add operation\n\n'

        'float fma(float x, float y, float z); (since C++11)\n\n'

        'double fma(double x, double y, double z); (since C++11)\n\n'

        'long double fma(long double x, long double y, long double z); (since C++11)\n\n'

        'Promoted fma(Arithmetic1 x, Arithmetic2 y, Arithmetic3 z); (since C++11)',

    'fmax':
        '<cmath>\n'
        'larger of two floating point values\n\n'

        'float fmax(float x, float y); (since C++11)\n\n'

        'double fmax(double x, double y); (since C++11)\n\n'

        'long double fmax(long double x, long double y); (since C++11)\n\n'

        'Promoted fmax(Arithmetic1 x, Arithmetic2 y); (since C++11)',

    'fmin':
        '<cmath>\n'
        'smaller of two floating point values\n\n'

        'float fmin(float x, float y); (since C++11)\n\n'

        'double fmin(double x, double y); (since C++11)\n\n'

        'long double fmin(long double x, long double y); (since C++11)\n\n'

        'Promoted fmin(Arithmetic x, Arithmetic y); (since C++11)',

    'fdim':
        '<cmath>\n'
        'positive difference of two floating point values (max(0, x-y))\n\n'

        'float fdim(float x, float y); (since C++11)\n\n'

        'double fdim(double x, double y); (since C++11)\n\n'

        'long double fdim(long double x, long double y); (since C++11)\n\n'

        'Promoted fdim(Arithmetic1 x, Arithmetic2 y); (since C++11)',

    'expm1':
        '<cmath>\n'
        'returns e raised to the given power, minus one (ex-1)\n\n'

        'float expm1(float arg); (since C++11)\n\n'

        'double expm1(double arg); (since C++11)\n\n'

        'long double expm1(long double arg); (since C++11)\n\n'

        'double expm1(Integral arg); (since C++11)',

    'log2':
        '<cmath>\n'
        'base 2 logarithm of the given number (log2(x))\n\n'

        'float log2(float arg); (since C++11)\n\n'

        'double log2(double arg); (since C++11)\n\n'

        'long double log2(long double arg); (since C++11)\n\n'

        'double log2(Integral arg); (since C++11)',

    'sqrt':
        '<cmath>\n'
        'computes square root\n\n'

        'float sqrt(float arg);\n\n'

        'double sqrt(double arg);\n\n'

        'long double sqrt(long double arg);\n\n'

        'double sqrt(Integral arg); (since C++11)',

    'cbrt':
        '<cmath>\n'
        'computes cubic root\n\n'

        'float cbrt(float arg); (since C++11)\n\n'

        'double cbrt(double arg); (since C++11)\n\n'

        'long double cbrt(long double arg); (since C++11)\n\n'

        'double cbrt(Integral arg); (since C++11)',

    'hypot':
        '<cmath>\n'
        'computes square root of the sum of the squares of two given numbers\n\n'

        'float hypot(float x, float y); (since C++11)\n\n'

        'double hypot(double x, double y); (since C++11)\n\n'

        'long double hypot(long double x, long double y); (since C++11)\n\n'

        'Promoted hypot(Arithmetic1 x, Arithmetic2 y); (since C++11)',

    'sin':
        '<cmath>\n'
        'computes sine (sin(x))\n\n'

        'float sin(float arg);\n\n'

        'double sin(double arg);\n\n'

        'long double sin(long double arg);\n\n'

        'double sin(Integral arg); (since C++11)',

    'cos':
        '<cmath>\n'
        'computes cosine (cos(x))\n\n'

        'float cos(float arg);\n\n'

        'double cos(double arg);\n\n'

        'long double cos(long double arg);\n\n'

        'double cos(Integral arg); (since C++11)',

    'tan':
        '<cmath>\n'
        'computes tangent (tan(x))\n\n'

        'float tan(float arg);\n\n'

        'double tan(double arg);\n\n'

        'long double tan(long double arg);\n\n'

        'double tan(Integral arg); (since C++11)',

    'asin':
        '<cmath>\n'
        'computes arc sine (arcsin(x))\n\n'

        'float asin(float arg);\n\n'

        'double asin(double arg);\n\n'

        'long double asin(long double arg);\n\n'

        'double asin(Integral arg); (since C++11)',

    'acos':
        '<cmath>\n'
        'computes arc cosine (arccos(x))\n\n'

        'float acos(float arg);\n\n'

        'double acos(double arg);\n\n'

        'long double acos(long double arg);\n\n'

        'double acos(Integral arg); (since C++11)',

    'atan':
        '<cmath>\n'
        'computes arc tangent (arctan(x))\n\n'

        'float atan(float arg);\n\n'

        'double atan(double arg);\n\n'

        'long double atan(long double arg);\n\n'

        'double atan(Integral arg); (since C++11)',

    'atan2':
        '<cmath>\n'
        'arc tangent, using signs to determine quadrants\n\n'

        'float atan2(float y, float x);\n\n'

        'double atan2(double y, double x);\n\n'

        'long double atan2(long double y, long double x);\n\n'

        'Promoted atan2(Arithmetic1 y, Arithmetic2 x); (since C++11)',

    'sinh':
        '<cmath>\n'
        'computes hyperbolic sine (sh(x))\n\n'

        'float sinh(float arg);\n\n'

        'double sinh(double arg);\n\n'

        'long double sinh(long double arg);\n\n'

        'double sinh(Integral arg); (since C++11)',

    'cosh':
        '<cmath>\n'
        'computes hyperbolic cosine (ch(x))\n\n'

        'float cosh(float arg);\n\n'

        'double cosh(double arg);\n\n'

        'long double cosh(long double arg);\n\n'

        'double cosh(Integral arg); (since C++11)',

    'tanh':
        '<cmath>\n'
        'hyperbolic tangent\n\n'

        'float tanh(float arg);\n\n'

        'double tanh(double arg);\n\n'

        'long double tanh(long double arg);\n\n'

        'double tanh(Integral arg); (since C++11)',

    'asinh':
        '<cmath>\n'
        'computes the inverse hyperbolic sine (arsinh(x))\n\n'

        'float asinh(float arg); (since C++11)\n\n'

        'double asinh(double arg); (since C++11)\n\n'

        'long double asinh(long double arg); (since C++11)\n\n'

        'double asinh(Integral arg); (since C++11)',

    'acosh':
        '<cmath>\n'
        'computes the inverse hyperbolic cosine (arcosh(x))\n\n'

        'float acosh(float arg); (since C++11)\n\n'

        'double acosh(double arg); (since C++11)\n\n'

        'long double acosh(long double arg); (since C++11)\n\n'

        'double acosh(Integral arg); (since C++11)',

    'atanh':
        '<cmath>\n'
        'computes the inverse hyperbolic tangent (artanh(x))\n\n'

        'float atanh(float arg); (since C++11)\n\n'

        'double atanh(double arg); (since C++11)\n\n'

        'long double atanh(long double arg); (since C++11)\n\n'

        'double atanh(Integral arg); (since C++11)',

    'erf':
        '<cmath>\n'
        'error function\n\n'

        'float erf(float arg); (since C++11)\n\n'

        'double erf(double arg); (since C++11)\n\n'

        'long double erf(long double arg); (since C++11)\n\n'

        'double erf(Integral arg); (since C++11)',

    'erfc':
        '<cmath>\n'
        'complementary error function\n\n'

        'float erfc(float arg); (since C++11)\n\n'

        'double erfc(double arg); (since C++11)\n\n'

        'long double erfc(long double arg); (since C++11)\n\n'

        'double erfc(Integral arg); (since C++11)',

    'tgamma':
        '<cmath>\n'
        'gamma function\n\n'

        'float tgamma(float arg); (since C++11)\n\n'

        'double tgamma(double arg); (since C++11)\n\n'

        'long double tgamma(long double arg); (since C++11)\n\n'

        'double tgamma(Integral arg); (since C++11)',

    'lgamma':
        '<cmath>\n'
        'natural logarithm of the gamma function\n\n'

        'float lgamma(float arg); (since C++11)\n\n'

        'double lgamma(double arg); (since C++11)\n\n'

        'long double lgamma(long double arg); (since C++11)\n\n'

        'double lgamma(Integral arg); (since C++11)',

    'ceil':
        '<cmath>\n'
        'nearest integer not less than the given value\n\n'

        'float ceil(float arg);\n\n'

        'double ceil(double arg);\n\n'

        'long double ceil(long double arg);\n\n'

        'double ceil(Integral arg); (since C++11)',

    'floor':
        '<cmath>\n'
        'nearest integer not greater than the given value\n\n'

        'float floor(float arg);\n\n'

        'double floor(double arg);\n\n'

        'long double floor(long double arg);\n\n'

        'double floor(Integral arg); (since C++11)',

    'trunc':
        '<cmath>\n'
        'nearest integer not greater in magnitude than the given value\n\n'

        'float trunc(float arg); (since C++11)\n\n'

        'double trunc(double arg); (since C++11)\n\n'

        'long double trunc(long double arg); (since C++11)\n\n'

        'double trunc(Integral arg); (since C++11)',

    'round':
        '<cmath>\n'
        'nearest integer, rounding away from zero in halfway cases\n\n'

        'float round(float arg); (since C++11)\n\n'

        'double round(double arg); (since C++11)\n\n'

        'long double round(long double arg); (since C++11)\n\n'

        'double round(Integral arg); (since C++11)',

    'lround':
        '<cmath>\n'
        'nearest integer, rounding away from zero in halfway cases\n\n'

        'long lround(float arg); (since C++11)\n\n'

        'long lround(double arg); (since C++11)\n\n'

        'long lround(long double arg); (since C++11)\n\n'

        'long lround(Integral arg); (since C++11)',

    'llround':
        '<cmath>\n'
        'nearest integer, rounding away from zero in halfway cases\n\n'

        'long long llround(float arg); (since C++11)\n\n'

        'long long llround(double arg); (since C++11)\n\n'

        'long long llround(long double arg); (since C++11)\n\n'

        'long long llround(Integral arg); (since C++11)',

    'nearbyint':
        '<cmath>\n'
        'nearest integer using current rounding mode\n\n'

        'float nearbyint(float arg); (since C++11)\n\n'

        'double nearbyint(double arg); (since C++11)\n\n'

        'long double nearbyint(long double arg); (since C++11)\n\n'

        'double nearbyint(Integral arg); (since C++11)',

    'rint':
        '<cmath>\n'
        'nearest integer using current rounding mode with exception if the result differs\n\n'

        'float rint(float arg); (since C++11)\n\n'

        'double rint(double arg); (since C++11)\n\n'

        'long double rint(long double arg); (since C++11)\n\n'

        'double rint(Integral arg); (since C++11)',

    'lrint':
        '<cmath>\n'
        'nearest integer using current rounding mode with exception if the result differs\n\n'

        'long lrint(float arg); (since C++11)\n\n'

        'long lrint(double arg); (since C++11)\n\n'

        'long lrint(long double arg); (since C++11)\n\n'

        'long lrint(Integral arg); (since C++11)',

    'llrint':
        '<cmath>\n'
        'nearest integer using current rounding mode with exception if the result differs\n\n'

        'long long llrint(float arg); (since C++11)\n\n'

        'long long llrint(double arg); (since C++11)\n\n'

        'long long llrint(long double arg); (since C++11)\n\n'

        'long long llrint(Integral arg); (since C++11)',

    'frexp':
        '<cmath>\n'
        'decomposes a number into significand and a power of 2\n\n'

        'float frexp(float arg, int *exp);\n\n'

        'double frexp(double arg, int *exp);\n\n'

        'long double frexp(long double arg, int *exp);\n\n'

        'double frexp(Integral arg, int *exp); (since C++11)',

    'ldexp':
        '<cmath>\n'
        'multiplies a number by 2 raised to a power\n\n'

        'float ldexp(float x, int exp);\n\n'

        'double ldexp(double x, int exp);\n\n'

        'long double ldexp(long double x, int exp);\n\n'

        'double ldexp(Integral x, int exp); (since C++11)',

    'modf':
        '<cmath>\n'
        'decomposes a number into integer and fractional parts\n\n'

        'float modf(float x, float *iptr);\n\n'

        'double modf(double x, double *iptr);\n\n'

        'long double modf(long double x, long double *iptr);',

    'scalbn':
        '<cmath>\n'
        'multiplies a number by FLT_RADIX raised to a power\n\n'

        'float scalbn(float x, int exp); (since C++11)\n\n'

        'double scalbn(double x, int exp); (since C++11)\n\n'

        'long double scalbn(long double x, int exp); (since C++11)\n\n'

        'double scalbn(Integral x, int exp); (since C++11)',

    'scalbln':
        '<cmath>\n'
        'multiplies a number by FLT_RADIX raised to a power\n\n'

        'float scalbln(float x, long exp); (since C++11)\n\n'

        'double scalbln(double x, long exp); (since C++11)\n\n'

        'long double scalbln(long double x, long exp); (since C++11)\n\n'

        'double scalbln(Integral x, long exp); (since C++11)',

    'ilogb':
        '<cmath>\n'
        'extracts exponent of the number\n\n'

        'int ilogb(float arg); (since C++11)\n\n'

        'int ilogb(double arg); (since C++11)\n\n'

        'int ilogb(long double arg); (since C++11)\n\n'

        'int ilogb(Integral arg); (since C++11)',

    'logb':
        '<cmath>\n'
        'extracts exponent of the number\n\n'

        'float logb(float arg); (since C++11)\n\n'

        'double logb(double arg); (since C++11)\n\n'

        'long double logb(long double arg); (since C++11)\n\n'

        'double logb(Integral arg); (since C++11)',

    'nextafter':
        '<cmath>\n'
        'next representable floating point value towards the given value\n\n'

        'float nextafter(float from, float to); (since C++11)\n\n'

        'double nextafter(double from, double to); (since C++11)\n\n'

        'long double nextafter(long double from, long double to); (since C++11)\n\n'

        'Promoted nextafter(Arithmetic from, Arithmetic to); (since C++11)',

    'nexttoward':
        '<cmath>\n'
        'next representable floating point value towards the given value\n\n'

        'float nexttoward(float from, long double to); (since C++11)\n\n'

        'double nexttoward(double from, long double to); (since C++11)\n\n'

        'long double nexttoward(long double from, long double to); (since C++11)\n\n'

        'double nexttoward(Integral from, long double to); (since C++11)',

    'copysign':
        '<cmath>\n'
        'copies the sign of a floating point value\n\n'

        'float copysign(float x, float y); (since C++11)\n\n'

        'double copysign(double x, double y); (since C++11)\n\n'

        'long double copysign(long double x, long double y); (since C++11)\n\n'

        'Promoted copysign(Arithmetic1 x, Arithmetic2 y); (since C++11)',

    'fpclassify':
        '<cmath>\n'
        'categorizes the given floating point value\n\n'

        'int fpclassify(float arg); (since C++11)\n\n'

        'int fpclassify(double arg); (since C++11)\n\n'

        'int fpclassify(long double arg); (since C++11)\n\n'

        'int fpclassify(Integral arg); (since C++11)',

    'isfinite':
        '<cmath>\n'
        'checks if the given number has finite value\n\n'

        'bool isfinite(float arg); (since C++11)\n\n'

        'bool isfinite(double arg); (since C++11)\n\n'

        'bool isfinite(long double arg); (since C++11)\n\n'

        'bool isfinite(Integral arg); (since C++11)',

    'isinf':
        '<cmath>\n'
        'checks if the given number is infinite\n\n'

        'bool isinf(float arg); (since C++11)\n\n'

        'bool isinf(double arg); (since C++11)\n\n'

        'bool isinf(long double arg); (since C++11)\n\n'

        'bool isinf(Integral arg); (since C++11)',

    'isnan':
        '<cmath>\n'
        'checks if the given number is NaN\n\n'

        'bool isnan(float arg); (since C++11)\n\n'

        'bool isnan(double arg); (since C++11)\n\n'

        'bool isnan(long double arg); (since C++11)\n\n'

        'bool isnan(Integral arg); (since C++11)',

    'isnormal':
        '<cmath>\n'
        'checks if the given number is normal\n\n'

        'bool isnormal(float arg); (since C++11)\n\n'

        'bool isnormal(double arg); (since C++11)\n\n'

        'bool isnormal(long double arg); (since C++11)\n\n'

        'bool isnormal(Integral arg); (since C++11)',

    'signbit':
        '<cmath>\n'
        'checks if the given number is negative\n\n'

        'bool signbit(float arg); (since C++11)\n\n'

        'bool signbit(double arg); (since C++11)\n\n'

        'bool signbit(long double arg); (since C++11)\n\n'

        'bool signbit(Integral arg); (since C++11)',

    'isgreater':
        '<cmath>\n'
        'checks if the first floating-point argument is greater than the second\n\n'

        'bool isgreater(float x, float y); (since C++11)\n\n'

        'bool isgreater(double x, double y); (since C++11)\n\n'

        'bool isgreater(long double x, long double y); (since C++11)\n\n'

        'bool isgreater(Arithmetic x, Arithmetic y); (since C++11)',

    'isgreaterequal':
        '<cmath>\n'
        'checks if the first floating-point argument is greater or equal than the second\n\n'

        'bool isgreaterequal(float x, float y); (since C++11)\n\n'

        'bool isgreaterequal(double x, double y); (since C++11)\n\n'

        'bool isgreaterequal(long double x, long double y); (since C++11)\n\n'

        'bool isgreaterequal(Arithmetic x, Arithmetic y); (since C++11)',

    'isless':
        '<cmath>\n'
        'checks if the first floating-point argument is less than the second\n\n'

        'bool isless(float x, float y); (since C++11)\n\n'

        'bool isless(double x, double y); (since C++11)\n\n'

        'bool isless(long double x, long double y); (since C++11)\n\n'

        'bool isless(Arithmetic x, Arithmetic y); (since C++11)',

    'islessequal':
        '<cmath>\n'
        'checks if the first floating-point argument is less or equal than the second\n\n'

        'bool islessequal(float x, float y); (since C++11)\n\n'

        'bool islessequal(double x, double y); (since C++11)\n\n'

        'bool islessequal(long double x, long double y); (since C++11)\n\n'

        'bool islessequal(Arithmetic x, Arithmetic y); (since C++11)',

    'islessgreater':
        '<cmath>\n'
        'checks if the first floating-point argument is less or greater than the second\n\n'

        'bool islessgreater(float x, float y); (since C++11)\n\n'

        'bool islessgreater(double x, double y); (since C++11)\n\n'

        'bool islessgreater(long double x, long double y); (since C++11)\n\n'

        'bool islessgreater(Arithmetic x, Arithmetic y); (since C++11)',

    'isunordered':
        '<cmath>\n'
        'checks if two floating-point values are unordered\n\n'

        'bool isunordered(float x, float y); (since C++11)\n\n'

        'bool isunordered(double x, double y); (since C++11)\n\n'

        'bool isunordered(long double x, long double y); (since C++11)\n\n'

        'bool isunordered(Arithmetic x, Arithmetic y); (since C++11)',

    'fopen':
        '<cstdio>\n'
        'opens a file\n\n'

        'std::FILE *fopen(const char *filename, const char *mode);',

    'freopen':
        '<cstdio>\n'
        'open an existing stream with a different name\n\n'

        'std::FILE *freopen(const char *filename, const char *mode, std::FILE *stream);',

    'fclose':
        '<cstdio>\n'
        'closes a file\n\n'

        'int fclose(std::FILE *stream);',

    'fflush':
        '<cstdio>\n'
        'synchronizes an output stream with the actual file\n\n'

        'int fflush(std::FILE *stream);',

    'setbuf':
        '<cstdio>\n'
        'sets the buffer for a file stream\n\n'

        'void setbuf(std::FILE *stream, char *buffer);',

    'setvbuf':
        '<cstdio>\n'
        'sets the buffer and its size for a file stream\n\n'

        'int setvbuf(std::FILE *stream, char *buffer, int mode, std::size_t size);',

    'fread':
        '<cstdio>\n'
        'reads from a file\n\n'

        'std::size_t fread( \n'
        '    void *buffer, std::size_t size, std::size_t count, std::FILE *stream \n'
        ');',

    'fwrite':
        '<cstdio>\n'
        'writes to a file\n\n'

        'std::size_t fwrite( \n'
        '    const void *buffer, std::size_t size, std::size_t count, std::FILE *stream \n'
        ');',

    'fgetc':
        '<cstdio>\n'
        'gets a character from a file stream\n\n'

        'int fgetc(std::FILE *stream);',

    'getc':
        '<cstdio>\n'
        'gets a character from a file stream\n\n'

        'int getc(std::FILE *stream);',

    'fgets':
        '<cstdio>\n'
        'gets a character string from a file stream\n\n'

        'char *fgets(char *str, int count, std::FILE *stream);',

    'fputc':
        '<cstdio>\n'
        'writes a character to a file stream\n\n'

        'int fputc(int ch, std::FILE *stream);',

    'putc':
        '<cstdio>\n'
        'writes a character to a file stream\n\n'

        'int putc(int ch, std::FILE *stream);',

    'fputs':
        '<cstdio>\n'
        'writes a character string to a file stream\n\n'

        'int fputs(const char *str, std::FILE *stream);',

    'getchar':
        '<cstdio>\n'
        'reads a character from stdin\n\n'

        'int getchar();',

    'gets':
        '<cstdio>\n'
        'reads a character string from stdin\n\n'

        'char *gets(char *str); (until C++14)',

    'putchar':
        '<cstdio>\n'
        'writes a character to stdout\n\n'

        'int putchar(int ch);',

    'puts':
        '<cstdio>\n'
        'writes a character string to stdout\n\n'

        'int puts(const char *str);',

    'ungetc':
        '<cstdio>\n'
        'puts a character back into a file stream\n\n'

        'int ungetc(int ch, std::FILE *stream);',

    'scanf':
        '<cstdio>\n'
        'reads formatted input from stdin, a file stream or a buffer\n\n'

        'int scanf(const char *format, ...);',

    'fscanf':
        '<cstdio>\n'
        'reads formatted input from stdin, a file stream or a buffer\n\n'

        'int fscanf(std::FILE *stream, const char *format, ...);',

    'sscanf':
        '<cstdio>\n'
        'reads formatted input from stdin, a file stream or a buffer\n\n'

        'int sscanf(const char *buffer, const char *format, ...);',

    'vscanf':
        '<cstdio>\n'
        'reads formatted input from stdin, a file stream or a buffer using variable\n'
        'argument list\n\n'

        'int vscanf(const char *format, va_list vlist); (since C++11)',

    'vfscanf':
        '<cstdio>\n'
        'reads formatted input from stdin, a file stream or a buffer using variable\n'
        'argument list\n\n'

        'int vfscanf( \n'
        '    std::FILE *stream, const char *format, va_list vlist \n'
        '); (since C++11)',

    'vsscanf':
        '<cstdio>\n'
        'reads formatted input from stdin, a file stream or a buffer using variable\n'
        'argument list\n\n'

        'int vsscanf( \n'
        '    const char *buffer, const char *format, va_list vlist \n'
        '); (since C++11)',

    'printf':
        '<cstdio>\n'
        'prints formatted output to stdout, a file stream or a buffer\n\n'

        'int printf(const char *format, ...);',

    'fprintf':
        '<cstdio>\n'
        'prints formatted output to stdout, a file stream or a buffer\n\n'

        'int fprintf(std::FILE *stream, const char *format, ...);',

    'sprintf':
        '<cstdio>\n'
        'prints formatted output to stdout, a file stream or a buffer\n\n'

        'int sprintf(char *buffer, const char *format, ...);',

    'snprintf':
        '<cstdio>\n'
        'prints formatted output to stdout, a file stream or a buffer\n\n'

        'int snprintf( \n'
        '    char *buffer, std::size_t buf_size, const char *format, \n'
        '); (since C++11)',

    'vprintf':
        '<cstdio>\n'
        'prints formatted output to stdout, a file stream or a buffer using variable\n'
        'argument list\n\n'

        'int vprintf(const char *format, va_list vlist);',

    'vfprintf':
        '<cstdio>\n'
        'prints formatted output to stdout, a file stream or a buffer using variable\n'
        'argument list\n\n'

        'int vfprintf(std::FILE *stream, const char *format, va_list vlist);',

    'vsprintf':
        '<cstdio>\n'
        'prints formatted output to stdout, a file stream or a buffer using variable\n'
        'argument list\n\n'

        'int vsprintf(char *buffer, const char *format, va_list vlist);',

    'vsnprintf':
        '<cstdio>\n'
        'prints formatted output to stdout, a file stream or a buffer using variable\n'
        'argument list\n\n'

        'int vsnprintf( \n'
        '    char *buffer, std::size_t buf_size, const char *format, va_list vlist \n'
        '); (since C++11)',

    'ftell':
        '<cstdio>\n'
        'returns the current file position indicator\n\n'

        'long ftell(std::FILE *stream);',

    'fgetpos':
        '<cstdio>\n'
        'gets the file position indicator\n\n'

        'int fgetpos(std::FILE *stream, std::fpos_t *pos);',

    'fseek':
        '<cstdio>\n'
        'moves the file position indicator to a specific location in a file\n\n'

        'int fseek(std::FILE *stream, long offset, int origin);',

    'fsetpos':
        '<cstdio>\n'
        'moves the file position indicator to a specific location in a file\n\n'

        'int fsetpos(std::FILE *stream, const std::fpos_t *pos);',

    'rewind':
        '<cstdio>\n'
        'moves the file position indicator to the beginning in a file\n\n'

        'void rewind(std::FILE *stream);',

    'clearerr':
        '<cstdio>\n'
        'clears errors\n\n'

        'void clearerr(std::FILE *stream);',

    'feof':
        '<cstdio>\n'
        'checks for the end-of-file\n\n'

        'int feof(std::FILE *stream);',

    'ferror':
        '<cstdio>\n'
        'checks for a file error\n\n'

        'int ferror(std::FILE *stream);',

    'perror':
        '<cstdio>\n'
        'displays a character string corresponding of the current error to stderr\n\n'

        'void perror(const char *s);',

    'remove':
        '<cstdio>\n'
        'erases a file\n\n'

        'int remove(const char *fname);',

    'rename':
        '<cstdio>\n'
        'renames a file\n\n'

        'int rename(const char *old_filename, const char *new_filename);',

    'tmpfile':
        '<cstdio>\n'
        'creates and opens a temporary, auto-removing file\n\n'

        'std::FILE *tmpfile();',

    'tmpnam':
        '<cstdio>\n'
        'returns a unique filename\n\n'

        'char *tmpnam(char *filename);',

    'iota':
        '<numeric>\n'
        'fills a range with successive increments of the starting value\n\n'

        'template <class ForwardIterator, class T>\n'
        'void iota(ForwardIterator first, ForwardIterator last, T value); (since C++11)',

    'accumulate':
        '<numeric>\n'
        'sums up a range of elements\n\n'

        'template <class InputIt, class T>\n'
        'T accumulate(InputIt first, InputIt last, T init);\n\n'

        'template <class InputIt, class T, class BinaryOperation>\n'
        'T accumulate(InputIt first, InputIt last, T init, BinaryOperation op);',

    'inner_product':
        '<numeric>\n'
        'computes the inner product of two ranges of elements\n\n'

        'template <class InputIt1, class InputIt2, class T>\n'
        'T inner_product(InputIt1 first1, InputIt1 last1, InputIt2 first2, T value);\n\n'

        'template < \n'
        '    class InputIt1, class InputIt2, class T, class BinaryOperation1, \n'
        '    class BinaryOperation2 \n'
        '>\n'
        'T inner_product( \n'
        '    InputIt1 first1, InputIt1 last1, InputIt2 first2, T value, \n'
        '    BinaryOperation1 op1, BinaryOperation2 op2 \n'
        ');',

    'adjacent_difference':
        '<numeric>\n'
        'computes the differences between adjacent elements in a range\n\n'

        'template <class InputIt, class OutputIt>\n'
        'OutputIt adjacent_difference(InputIt first, InputIt last, OutputIt d_first);\n\n'

        'template <class InputIt, class OutputIt, class BinaryOperation>\n'
        'OutputIt adjacent_difference( \n'
        '    InputIt first, InputIt last, OutputIt d_first, BinaryOperation op \n'
        ');',

    'partial_sum':
        '<numeric>\n'
        'computes the partial sum of a range of elements\n\n'

        'template <class InputIt, class OutputIt>\n'
        'OutputIt partial_sum(InputIt first, InputIt last, OutputIt d_first);\n\n'

        'template <class InputIt, class OutputIt, class BinaryOperation>\n'
        'OutputIt partial_sum( \n'
        '    InputIt first, InputIt last, OutputIt d_first, BinaryOperation op \n'
        ');',

    'complex':
        '<complex>\n'
        'constructs a complex number\n\n'

        'complex(const T &re=T(), const T &im=T()); (until C++14)\n\n'

        'constexpr complex(const T &re=T(), const T &im=T()); (since C++14)\n\n'

        'complex(const complex &other); (until C++14)\n\n'

        'constexpr complex(const complex &other); (since C++14)\n\n'

        'template <class X>\n'
        'complex(const complex<X> &other); (until C++14)\n\n'

        'template <class X>\n'
        'constexpr complex(const complex<X> &other); (since C++14)\n\n'

        'complex(float re=0.0f, float im=0.0f); (until C++11)\n\n'

        'constexpr complex(float re=0.0f, float im=0.0f); (since C++11)\n\n'

        'explicit complex(const complex<double> &other);\n\n'

        'explicit complex(const complex<long double> &other); (until C++11)\n\n'

        'explicit constexpr complex(const complex<double> &other);\n\n'

        'explicit constexpr complex(const complex<long double> &other); (since C++11)\n\n'

        'complex(double re=0.0, double im=0.0); (until C++11)\n\n'

        'constexpr complex(double re=0.0, double im=0.0); (since C++11)\n\n'

        'complex(const complex<float> &other);\n\n'

        'explicit complex(const complex<long double> &other); (until C++11)\n\n'

        'constexpr complex(const complex<float> &other);\n\n'

        'explicit constexpr complex(const complex<long double> &other); (since C++11)\n\n'

        'complex(long double re=0.0L, long double im=0.0L); (until C++11)\n\n'

        'constexpr complex(long double re=0.0L, long double im=0.0L); (since C++11)\n\n'

        'complex(const complex<float> &other);\n\n'

        'complex(const complex<double> &other); (until C++11)\n\n'

        'constexpr complex(const complex<float> &other);\n\n'

        'constexpr complex(const complex<double> &other); (since C++11)',

    'complex::real':
        '<complex>\n'
        'accesses the real part of the complex number\n\n'

        'T real() const; (until C++14)\n\n'

        'constexpr T real() const; (since C++14)\n\n'

        'void real(T value);\n\n'

        'float real() const; (until C++11)\n\n'

        'constexpr float real(); (since C++11) (until C++14)\n\n'

        'constexpr float real() const; (since C++14)\n\n'

        'void real(float value);\n\n'

        'double real() const; (until C++11)\n\n'

        'constexpr double real(); (since C++11) (until C++14)\n\n'

        'constexpr double real() const; (since C++14)\n\n'

        'void real(double value);\n\n'

        'long double real() const; (until C++11)\n\n'

        'constexpr long double real(); (since C++11) (until C++14)\n\n'

        'constexpr long double real() const; (since C++14)\n\n'

        'void real(long double value);',

    'complex::imag':
        '<complex>\n'
        'accesses the imaginary part of the complex number\n\n'

        'T imag() const; (until C++14)\n\n'

        'constexpr T imag() const; (since C++14)\n\n'

        'void imag(T value);\n\n'

        'float imag() const; (until C++11)\n\n'

        'constexpr float imag(); (since C++11) (until C++14)\n\n'

        'constexpr float imag() const; (since C++14)\n\n'

        'void imag(float value);\n\n'

        'double imag() const; (until C++11)\n\n'

        'constexpr double imag(); (since C++11) (until C++14)\n\n'

        'constexpr double imag() const; (since C++14)\n\n'

        'void imag(double value);\n\n'

        'long double imag() const; (until C++11)\n\n'

        'constexpr long double imag(); (since C++11) (until C++14)\n\n'

        'constexpr long double imag() const; (since C++14)\n\n'

        'void imag(long double value);',

    'real':
        '<complex>\n'
        'returns the real component\n\n'

        'template <class T>\n'
        'T real(const complex<T> &z); (until C++14)\n\n'

        'template <class T>\n'
        'constexpr T real(const complex<T> &z); (since C++14)\n\n'

        'long double real(long double z); (since C++11)\n\n'

        'template <class DoubleOrInteger>\n'
        'double real(DoubleOrInteger z); (since C++11)\n\n'

        'float real(float z); (since C++11)',

    'imag':
        '<complex>\n'
        'returns the imaginary component\n\n'

        'template <class T>\n'
        'T imag(const complex<T> &z); (until C++14)\n\n'

        'template <class T>\n'
        'constexpr T imag(const complex<T> &z); (since C++14)\n\n'

        'long double imag(long double z); (since C++11)\n\n'

        'template <class DoubleOrInteger>\n'
        'double imag(DoubleOrInteger z); (since C++11)\n\n'

        'float imag(float z); (since C++11)',

    'abs':
        '<complex>\n'
        'returns the magnitude of a complex number\n\n'

        'template <class T>\n'
        'T abs(const complex<T> &z);',

    'arg':
        '<complex>\n'
        'returns the phase angle\n\n'

        'template <class T>\n'
        'T arg(const complex<T> &z);\n\n'

        'long double arg(long double z); (since C++11)\n\n'

        'template <class DoubleOrInteger>\n'
        'double arg(DoubleOrInteger z); (since C++11)\n\n'

        'float arg(float z); (since C++11)',

    'norm':
        '<complex>\n'
        'returns the squared magnitude\n\n'

        'template <class T>\n'
        'T norm(const complex<T> &z);\n\n'

        'long double norm(long double z); (since C++11)\n\n'

        'template <class DoubleOrInteger>\n'
        'double norm(DoubleOrInteger z); (since C++11)\n\n'

        'float norm(float z); (since C++11)',

    'conj':
        '<complex>\n'
        'returns the complex conjugate\n\n'

        'template <class T>\n'
        'complex<T> conj(const complex<T> &z);\n\n'

        'std::complex<long double> conj(long double z); (since C++11)\n\n'

        'template <class DoubleOrInteger>\n'
        'std::complex<double> conj(DoubleOrInteger z); (since C++11)\n\n'

        'std::complex<float> conj(float z); (since C++11)',

    'proj':
        '<complex>\n'
        'returns the projection onto the Riemann sphere\n\n'

        'template <class T>\n'
        'complex<T> proj(const complex<T> &z); (since C++11)\n\n'

        'std::complex<long double> proj(long double z); (since C++11)\n\n'

        'template <class DoubleOrInteger>\n'
        'std::complex<double> proj(DoubleOrInteger z); (since C++11)\n\n'

        'std::complex<float> proj(float z); (since C++11)',

    'polar':
        '<complex>\n'
        'constructs a complex number from magnitude and phase angle\n\n'

        'template <class T>\n'
        'complex<T> polar(const T &r, const T &theta=0);',

    'exp':
        '<complex>\n'
        'complex base e exponential\n\n'

        'template <class T>\n'
        'complex<T> exp(const complex<T> &z);',

    'log':
        '<complex>\n'
        'complex natural logarithm with the branch cuts along the negative real axis\n\n'

        'template <class T>\n'
        'complex<T> log(const complex<T> &z);',

    'log10':
        '<complex>\n'
        'complex common logarithm with the branch cuts along the negative real axis\n\n'

        'template <class T>\n'
        'complex<T> log10(const complex<T> &z);',

    'pow':
        '<complex>\n'
        'complex power, one or both arguments may be a complex number\n\n'

        'template <class T>\n'
        'complex<T> pow(const complex<T> &x, const complex<T> &y);\n\n'

        'template <class T>\n'
        'complex<T> pow(const complex<T> &x, const T &y);\n\n'

        'template <class T>\n'
        'complex<T> pow(const T &x, const complex<T> &y);\n\n'

        'template <class T, class U>\n'
        'complex</*Promoted*/> pow( \n'
        '    const complex<T> &x, const complex<U> &y \n'
        '); (since C++11)\n\n'

        'template <class T, class U>\n'
        'complex</*Promoted*/> pow(const complex<T> &x, const U &y); (since C++11)\n\n'

        'template <class T, class U>\n'
        'complex</*Promoted*/> pow(const T &x, const complex<U> &y); (since C++11)',

    'sqrt':
        '<complex>\n'
        'complex square root in the range of the right half-plane\n\n'

        'template <class T>\n'
        'complex<T> sqrt(const complex<T> &z);',

    'sin':
        '<complex>\n'
        'computes sine of a complex number (sin(z))\n\n'

        'template <class T>\n'
        'complex<T> sin(const complex<T> &z);',

    'cos':
        '<complex>\n'
        'computes cosine of a complex number (cos(z))\n\n'

        'template <class T>\n'
        'complex<T> cos(const complex<T> &z);',

    'tan':
        '<complex>\n'
        'computes tangent of a complex number (tan(z))\n\n'

        'template <class T>\n'
        'complex<T> tan(const complex<T> &z);',

    'asin':
        '<complex>\n'
        'computes arc sine of a complex number (arcsin(z))\n\n'

        'template <class T>\n'
        'complex<T> asin(const complex<T> &z); (since C++11)',

    'acos':
        '<complex>\n'
        'computes arc cosine of a complex number (arccos(z))\n\n'

        'template <class T>\n'
        'complex<T> acos(const complex<T> &z); (since C++11)',

    'atan':
        '<complex>\n'
        'computes arc tangent of a complex number (arctan(z))\n\n'

        'template <class T>\n'
        'complex<T> atan(const complex<T> &z); (since C++11)',

    'sinh':
        '<complex>\n'
        'computes hyperbolic sine of a complex number (sh(z))\n\n'

        'template <class T>\n'
        'complex<T> sinh(const complex<T> &z); (since C++11)',

    'cosh':
        '<complex>\n'
        'computes hyperbolic cosine of a complex number (ch(z))\n\n'

        'template <class T>\n'
        'complex<T> cosh(const complex<T> &z); (since C++11)',

    'tanh':
        '<complex>\n'
        'computes hyperbolic tangent of a complex number\n\n'

        'template <class T>\n'
        'complex<T> tanh(const complex<T> &z); (since C++11)',

    'asinh':
        '<complex>\n'
        'computes area hyperbolic sine of a complex number\n\n'

        'template <class T>\n'
        'complex<T> asinh(const complex<T> &z); (since C++11)',

    'acosh':
        '<complex>\n'
        'computes area hyperbolic cosine of a complex number\n\n'

        'template <class T>\n'
        'complex<T> acosh(const complex<T> &z); (since C++11)',

    'atanh':
        '<complex>\n'
        'computes area hyperbolic tangent of a complex number\n\n'

        'template <class T>\n'
        'complex<T> atanh(const complex<T> &z); (since C++11)',

    'basic_string':
        '<basic_string>\n'
        'constructs a basic_string\n\n'

        'explicit basic_string(const Allocator &alloc=Allocator()); (until C++14)\n\n'

        'basic_string():\n'
        'basic_string(Allocator()) {}\n\n'

        'explicit basic_string(const Allocator &alloc); (since C++14)\n\n'

        'basic_string(size_type count, CharT ch, const Allocator &alloc=Allocator());\n\n'

        'basic_string( \n'
        '    const basic_string &other, size_type pos, \n'
        '    size_type count=std::basic_string::npos, const Allocator &alloc=Allocator() \n'
        '); (until C++17)\n\n'

        'basic_string( \n'
        '    const CharT *s, size_type count, const Allocator &alloc=Allocator() \n'
        ');\n\n'

        'basic_string(const CharT *s, const Allocator &alloc=Allocator());\n\n'

        'template <class InputIt>\n'
        'basic_string(InputIt first, InputIt last, const Allocator &alloc=Allocator());\n\n'

        'basic_string(const basic_string &other);\n\n'

        'basic_string(const basic_string &other, const Allocator &alloc); (since C++11)\n\n'

        'basic_string(basic_string &&other); (since C++11)\n\n'

        'basic_string(basic_string &&other, const Allocator &alloc); (since C++11)\n\n'

        'basic_string( \n'
        '    std::initializer_list<CharT> init, const Allocator &alloc=Allocator() \n'
        '); (since C++11)',

    'basic_string::assign':
        '<basic_string>\n'
        'assign characters to a string\n\n'

        'basic_string &assign(size_type count, CharT ch);\n\n'

        'basic_string &assign(const basic_string &str);\n\n'

        'basic_string &assign( \n'
        '    const basic_string &str, size_type pos, size_type count \n'
        '); (until C++14)\n\n'

        'basic_string &assign( \n'
        '    const basic_string &str, size_type pos, size_type count=npos \n'
        '); (since C++14)\n\n'

        'basic_string &assign(basic_string &&str); (since C++11)\n\n'

        'basic_string &assign(const CharT *s, size_type count);\n\n'

        'basic_string &assign(const CharT *s);\n\n'

        'template <class InputIt>\n'
        'basic_string &assign(InputIt first, InputIt last);\n\n'

        'basic_string &assign(std::initializer_list<CharT> ilist); (since C++11)',

    'basic_string::get_allocator':
        '<basic_string>\n'
        'returns the associated allocator\n\n'

        'allocator_type get_allocator() const;',

    'basic_string::at':
        '<basic_string>\n'
        'access specified character with bounds checking\n\n'

        'reference at(size_type pos);\n\n'

        'const_reference at(size_type pos) const;',

    'basic_string::front':
        '<basic_string>\n'
        'accesses the first character\n\n'

        'CharT &front(); (since C++11)\n\n'

        'const CharT &front() const; (since C++11)',

    'basic_string::back':
        '<basic_string>\n'
        'accesses the last character\n\n'

        'CharT &back(); (since C++11)\n\n'

        'const CharT &back() const; (since C++11)',

    'basic_string::data':
        '<basic_string>\n'
        'returns a pointer to the first character of a string\n\n'

        'const CharT *data() const;',

    'basic_string::c_str':
        '<basic_string>\n'
        'returns a non-modifiable standard C character array version of the string\n\n'

        'const CharT *c_str() const;',

    'basic_string::begin':
        '<basic_string>\n'
        'returns an iterator to the beginning\n\n'

        'iterator begin();\n\n'

        'const_iterator begin() const;',

    'basic_string::cbegin':
        '<basic_string>\n'
        'returns an iterator to the beginning\n\n'

        'const_iterator cbegin() const; (since C++11)',

    'basic_string::end':
        '<basic_string>\n'
        'returns an iterator to the end\n\n'

        'iterator end();\n\n'

        'const_iterator end() const;',

    'basic_string::cend':
        '<basic_string>\n'
        'returns an iterator to the end\n\n'

        'const_iterator cend() const; (since C++11)',

    'basic_string::rbegin':
        '<basic_string>\n'
        'returns a reverse iterator to the beginning\n\n'

        'reverse_iterator rbegin();\n\n'

        'const_reverse_iterator rbegin() const;',

    'basic_string::crbegin':
        '<basic_string>\n'
        'returns a reverse iterator to the beginning\n\n'

        'const_reverse_iterator crbegin() const; (since C++11)',

    'basic_string::rend':
        '<basic_string>\n'
        'returns a reverse iterator to the end\n\n'

        'reverse_iterator rend();\n\n'

        'const_reverse_iterator rend() const;',

    'basic_string::crend':
        '<basic_string>\n'
        'returns a reverse iterator to the end\n\n'

        'const_reverse_iterator crend() const; (since C++11)',

    'basic_string::empty':
        '<basic_string>\n'
        'checks whether the string is empty\n\n'

        'bool empty() const;',

    'basic_string::size':
        '<basic_string>\n'
        'returns the number of characters\n\n'

        'size_type size() const;',

    'basic_string::length':
        '<basic_string>\n'
        'returns the number of characters\n\n'

        'size_type length() const;',

    'basic_string::max_size':
        '<basic_string>\n'
        'returns the maximum number of characters\n\n'

        'size_type max_size() const;',

    'basic_string::reserve':
        '<basic_string>\n'
        'reserves storage\n\n'

        'void reserve(size_type new_cap=0);',

    'basic_string::capacity':
        '<basic_string>\n'
        'returns the number of characters that can be held in currently allocated storage\n\n'

        'size_type capacity() const;',

    'basic_string::shrink_to_fit':
        '<basic_string>\n'
        'reduces memory usage by freeing unused memory\n\n'

        'void shrink_to_fit(); (since C++11)',

    'basic_string::clear':
        '<basic_string>\n'
        'clears the contents\n\n'

        'void clear();',

    'basic_string::insert':
        '<basic_string>\n'
        'inserts characters\n\n'

        'basic_string &insert(size_type index, size_type count, CharT ch);\n\n'

        'basic_string &insert(size_type index, const CharT *s);\n\n'

        'basic_string &insert(size_type index, const CharT *s, size_type count);\n\n'

        'basic_string &insert(size_type index, const basic_string &str);\n\n'

        'basic_string &insert( \n'
        '    size_type index, const basic_string &str, size_type index_str, \n'
        '    size_type count \n'
        '); (until C++14)\n\n'

        'basic_string &insert( \n'
        '    size_type index, const basic_string &str, size_type index_str, \n'
        '    size_type count=npos \n'
        '); (since C++14)\n\n'

        'iterator insert(iterator pos, CharT ch); (until C++11)\n\n'

        'iterator insert(const_iterator pos, CharT ch); (since C++11)\n\n'

        'void insert(iterator pos, size_type count, CharT ch); (until C++11)\n\n'

        'iterator insert(const_iterator pos, size_type count, CharT ch); (since C++11)\n\n'

        'template <class InputIt>\n'
        'void insert(iterator pos, InputIt first, InputIt last); (until C++11)\n\n'

        'template <class InputIt>\n'
        'iterator insert(const_iterator pos, InputIt first, InputIt last); (since C++11)\n\n'

        'iterator insert( \n'
        '    const_iterator pos, std::initializer_list<CharT> ilist \n'
        '); (since C++11)',

    'basic_string::erase':
        '<basic_string>\n'
        'removes characters\n\n'

        'basic_string &erase(size_type index=0, size_type count=npos);\n\n'

        'iterator erase(iterator position); (until C++11)\n\n'

        'iterator erase(const_iterator position); (since C++11)\n\n'

        'iterator erase(iterator first, iterator last); (until C++11)\n\n'

        'iterator erase(const_iterator first, const_iterator last); (since C++11)',

    'basic_string::push_back':
        '<basic_string>\n'
        'appends a character to the end\n\n'

        'void push_back(CharT ch);',

    'basic_string::pop_back':
        '<basic_string>\n'
        'removes the last character\n\n'

        'void pop_back(); (since C++11)',

    'basic_string::append':
        '<basic_string>\n'
        'appends characters to the end\n\n'

        'basic_string &append(size_type count, CharT ch);\n\n'

        'basic_string &append(const basic_string &str);\n\n'

        'basic_string &append( \n'
        '    const basic_string &str, size_type pos, size_type count \n'
        '); (until C++14)\n\n'

        'basic_string &append( \n'
        '    const basic_string &str, size_type pos, size_type count=npos \n'
        '); (since C++14)\n\n'

        'basic_string &append(const CharT *s, size_type count);\n\n'

        'basic_string &append(const CharT *s);\n\n'

        'template <class InputIt>\n'
        'basic_string &append(InputIt first, InputIt last);\n\n'

        'basic_string &append(std::initializer_list<CharT> ilist); (since C++11)',

    'basic_string::compare':
        '<basic_string>\n'
        'compares two strings\n\n'

        'int compare(const basic_string &str) const;\n\n'

        'int compare(size_type pos1, size_type count1, const basic_string &str) const;\n\n'

        'int compare( \n'
        '    size_type pos1, size_type count1, const basic_string &str, size_type pos2, \n'
        '    size_type count2const \n'
        '); (until C++14)\n\n'

        'int compare( \n'
        '    size_type pos1, size_type count1, const basic_string &str, size_type pos2, \n'
        '    size_type count2=nposconst \n'
        '); (since C++14)\n\n'

        'int compare(const CharT *s) const;\n\n'

        'int compare(size_type pos1, size_type count1, const CharT *s) const;\n\n'

        'int compare( \n'
        '    size_type pos1, size_type count1, const CharT *s, size_type count2const \n'
        ');',

    'basic_string::replace':
        '<basic_string>\n'
        'replaces specified portion of a string\n\n'

        'basic_string &replace(size_type pos, size_type count, const basic_string &str);\n\n'

        'basic_string &replace( \n'
        '    const_iterator first, const_iterator last, const basic_string &str \n'
        ');\n\n'

        'basic_string &replace( \n'
        '    size_type pos, size_type count, const basic_string &str, size_type pos2, \n'
        '    size_type count2 \n'
        '); (until C++14)\n\n'

        'basic_string &replace( \n'
        '    size_type pos, size_type count, const basic_string &str, size_type pos2, \n'
        '    size_type count2=npos \n'
        '); (since C++14)\n\n'

        'template <class InputIt>\n'
        'basic_string &replace( \n'
        '    const_iterator first, const_iterator last, InputIt first2, InputIt last2 \n'
        ');\n\n'

        'basic_string &replace( \n'
        '    size_type pos, size_type count, const CharT *cstr, size_type count2 \n'
        ');\n\n'

        'basic_string &replace( \n'
        '    const_iterator first, const_iterator last, const CharT *cstr, \n'
        '    size_type count2 \n'
        ');\n\n'

        'basic_string &replace(size_type pos, size_type count, const CharT *cstr);\n\n'

        'basic_string &replace( \n'
        '    const_iterator first, const_iterator last, const CharT *cstr \n'
        ');\n\n'

        'basic_string &replace( \n'
        '    size_type pos, size_type count, size_type count2, CharT ch \n'
        ');\n\n'

        'basic_string &replace( \n'
        '    const_iterator first, const_iterator last, size_type count2, CharT ch \n'
        ');\n\n'

        'basic_string &replace( \n'
        '    const_iterator first, const_iterator last, \n'
        '    std::initializer_list<CharT> ilist \n'
        '); (since C++11)',

    'basic_string::substr':
        '<basic_string>\n'
        'returns a substring\n\n'

        'basic_string substr(size_type pos=0, size_type count=npos) const;',

    'basic_string::copy':
        '<basic_string>\n'
        'copies characters\n\n'

        'size_type copy(CharT *dest, size_type count, size_type pos=0) const;',

    'basic_string::resize':
        '<basic_string>\n'
        'changes the number of characters stored\n\n'

        'void resize(size_type count);\n\n'

        'void resize(size_type count, CharT ch);',

    'basic_string::swap':
        '<basic_string>\n'
        'swaps the contents\n\n'

        'void swap(basic_string &other);',

    'basic_string::find':
        '<basic_string>\n'
        'find characters in the string\n\n'

        'size_type find(const basic_string &str, size_type pos=0) const;\n\n'

        'size_type find(const CharT *s, size_type pos, size_type count) const;\n\n'

        'size_type find(const CharT *s, size_type pos=0) const;\n\n'

        'size_type find(CharT ch, size_type pos=0) const;',

    'basic_string::rfind':
        '<basic_string>\n'
        'find the last occurrence of a substring\n\n'

        'size_type rfind(const basic_string &str, size_type pos=npos) const;\n\n'

        'size_type rfind(const CharT *s, size_type pos, size_type count) const;\n\n'

        'size_type rfind(const CharT *s, size_type pos=npos) const;\n\n'

        'size_type rfind(CharT ch, size_type pos=npos) const;',

    'basic_string::find_first_of':
        '<basic_string>\n'
        'find first occurrence of characters\n\n'

        'size_type find_first_of(const basic_string &str, size_type pos=0) const;\n\n'

        'size_type find_first_of(const CharT *s, size_type pos, size_type count) const;\n\n'

        'size_type find_first_of(const CharT *s, size_type pos=0) const;\n\n'

        'size_type find_first_of(CharT ch, size_type pos=0) const;',

    'basic_string::find_first_not_of':
        '<basic_string>\n'
        'find first absence of characters\n\n'

        'size_type find_first_not_of(const basic_string &str, size_type pos=0) const;\n\n'

        'size_type find_first_not_of( \n'
        '    const CharT *s, size_type pos, size_type countconst \n'
        ');\n\n'

        'size_type find_first_not_of(const CharT *s, size_type pos=0) const;\n\n'

        'size_type find_first_not_of(CharT ch, size_type pos=0) const;',

    'basic_string::find_last_of':
        '<basic_string>\n'
        'find last occurrence of characters\n\n'

        'size_type find_last_of(const basic_string &str, size_type pos=npos) const;\n\n'

        'size_type find_last_of(const CharT *s, size_type pos, size_type count) const;\n\n'

        'size_type find_last_of(const CharT *s, size_type pos=npos) const;\n\n'

        'size_type find_last_of(CharT ch, size_type pos=npos) const;',

    'basic_string::find_last_not_of':
        '<basic_string>\n'
        'find last absence of characters\n\n'

        'size_type find_last_not_of(const basic_string &str, size_type pos=npos) const;\n\n'

        'size_type find_last_not_of( \n'
        '    const CharT *s, size_type pos, size_type countconst \n'
        ');\n\n'

        'size_type find_last_not_of(const CharT *s, size_type pos=npos) const;\n\n'

        'size_type find_last_not_of(CharT ch, size_type pos=npos) const;',

    'std::swap':
        '<basic_string>\n'
        'specializes the std::swap algorithm\n\n'

        'template <class CharT, class Traits, class Alloc>\n'
        'void swap( \n'
        '    basic_string<CharT, Traits, Alloc> &lhs, \n'
        '    basic_string<CharT, Traits, Alloc> &rhs \n'
        ');',

    'getline':
        '<basic_string>\n'
        'read data from an I/O stream into a string\n\n'

        'template <class CharT, class Traits, class Allocator>\n'
        'std::basic_istream<CharT, Traits> &getline( \n'
        '    std::basic_istream<CharT, Traits> &input, \n'
        '    std::basic_string<CharT, Traits, Allocator> &str, CharT delim \n'
        ');\n\n'

        'template <class CharT, class Traits, class Allocator>\n'
        'std::basic_istream<CharT, Traits> &getline( \n'
        '    std::basic_istream<CharT, Traits> &&input, \n'
        '    std::basic_string<CharT, Traits, Allocator> &str, CharT delim \n'
        '); (since C++11)\n\n'

        'template <class CharT, class Traits, class Allocator>\n'
        'std::basic_istream<CharT, Traits> &getline( \n'
        '    std::basic_istream<CharT, Traits> &input, \n'
        '    std::basic_string<CharT, Traits, Allocator> &str \n'
        ');\n\n'

        'template <class CharT, class Traits, class Allocator>\n'
        'std::basic_istream<CharT, Traits> &getline( \n'
        '    std::basic_istream<CharT, Traits> &&input, \n'
        '    std::basic_string<CharT, Traits, Allocator> &str \n'
        '); (since C++11)',

    'stoi':
        '<basic_string>\n'
        'converts a string to a signed integer\n\n'

        'int stoi(const std::string &str, std::size_t *pos=0, int base=10);\n\n'

        'int stoi( \n'
        '    const std::wstring &str, std::size_t *posint base \n'
        '); (since C++11)',

    'stol':
        '<basic_string>\n'
        'converts a string to a signed integer\n\n'

        'long stol(const std::string &str, std::size_t *pos=0, int base=10);\n\n'

        'long stol( \n'
        '    const std::wstring &str, std::size_t *posint base \n'
        '); (since C++11)',

    'stoll':
        '<basic_string>\n'
        'converts a string to a signed integer\n\n'

        'long long stoll(const std::string &str, std::size_t *pos=0, int base=10);\n\n'

        'long long stoll( \n'
        '    const std::wstring &str, std::size_t *posint base \n'
        '); (since C++11)',

    'stoul':
        '<basic_string>\n'
        'converts a string to an unsigned integer\n\n'

        'unsigned long stoul(const std::string &str, std::size_t *pos=0, int base=10);\n\n'

        'unsigned long stoul( \n'
        '    const std::wstring &str, std::size_t *posint base \n'
        '); (since C++11)',

    'stoull':
        '<basic_string>\n'
        'converts a string to an unsigned integer\n\n'

        'unsigned long long stoull( \n'
        '    const std::string &str, std::size_t *posint base \n'
        ');\n\n'

        'unsigned long long stoull( \n'
        '    const std::wstring &str, std::size_t *posint base \n'
        '); (since C++11)',

    'stof':
        '<basic_string>\n'
        'converts a string to a floating point value\n\n'

        'float stof(const std::string &str, std::size_t *pos=0);\n\n'

        'float stof(const std::wstring &str, std::size_t *pos=0); (since C++11)',

    'stod':
        '<basic_string>\n'
        'converts a string to a floating point value\n\n'

        'double stod(const std::string &str, std::size_t *pos=0);\n\n'

        'double stod(const std::wstring &str, std::size_t *pos=0); (since C++11)',

    'stold':
        '<basic_string>\n'
        'converts a string to a floating point value\n\n'

        'long double stold(const std::string &str, std::size_t *pos=0);\n\n'

        'long double stold(const std::wstring &str, std::size_t *pos=0); (since C++11)',

    'to_string':
        '<basic_string>\n'
        'converts an integral or floating point value to string\n\n'

        'std::string to_string(int value); (since C++11)\n\n'

        'std::string to_string(long value); (since C++11)\n\n'

        'std::string to_string(long long value); (since C++11)\n\n'

        'std::string to_string(unsigned value); (since C++11)\n\n'

        'std::string to_string(unsigned long value); (since C++11)\n\n'

        'std::string to_string(unsigned long long value); (since C++11)\n\n'

        'std::string to_string(float value); (since C++11)\n\n'

        'std::string to_string(double value); (since C++11)\n\n'

        'std::string to_string(long double value); (since C++11)',

    'to_wstring':
        '<basic_string>\n'
        'converts an integral or floating point value to wstring\n\n'

        'std::wstring to_wstring(int value); (since C++11)\n\n'

        'std::wstring to_wstring(long value); (since C++11)\n\n'

        'std::wstring to_wstring(long long value); (since C++11)\n\n'

        'std::wstring to_wstring(unsigned value); (since C++11)\n\n'

        'std::wstring to_wstring(unsigned long value); (since C++11)\n\n'

        'std::wstring to_wstring(unsigned long long value); (since C++11)\n\n'

        'std::wstring to_wstring(float value); (since C++11)\n\n'

        'std::wstring to_wstring(double value); (since C++11)\n\n'

        'std::wstring to_wstring(long double value); (since C++11)',

    'bitset':
        '<bitset>\n'
        'constructs the bitset\n\n'

        'bitset(); (until C++11)\n\n'

        'constexpr bitset(); (since C++11)\n\n'

        'bitset(unsigned long val); (until C++11)\n\n'

        'constexpr bitset(unsigned long long val); (since C++11)\n\n'

        'template <class CharT, class Traits, class Alloc>\n'
        'explicit bitset( \n'
        '    const std::basic_string<CharT, Traits, Alloc> &str, \n'
        '    typename std::basic_string<CharT, Traits, Alloc>::size_type pos \n'
        '    typename std::basic_string<CharT, Traits, Alloc>::size_type n=std::basic_string<CharT, Traits, Alloc>::npos \n'
        '); (until C++11)\n\n'

        'template <class CharT, class Traits, class Alloc>\n'
        'explicit bitset( \n'
        '    const std::basic_string<CharT, Traits, Alloc> &str, \n'
        '    typename std::basic_string<CharT, Traits, Alloc>::size_type pos \n'
        '    typename std::basic_string<CharT, Traits, Alloc>::size_type n=std::basic_string<CharT, Traits, Alloc>::npos, \n'
        '    CharT zero=CharT(\'0\'), CharT one=CharT(\'1\') \n'
        '); (since C++11)\n\n'

        'template <class CharT>\n'
        'explicit bitset( \n'
        '    const CharT *str, \n'
        '    typename std::basic_string<CharT>::size_type n=std::basic_string<CharT>::npos, \n'
        '    CharT zero=CharT(\'0\'), CharT one=CharT(\'1\') \n'
        '); (since C++11)',

    'bitset::test':
        '<bitset>\n'
        'accesses specific bit\n\n'

        'bool test(size_t pos) const;',

    'bitset::all':
        '<bitset>\n'
        'checks if all, any or none bits are set to true\n\n'

        'bool all() const; (since C++11)',

    'bitset::any':
        '<bitset>\n'
        'checks if all, any or none bits are set to true\n\n'

        'bool any() const;',

    'bitset::none':
        '<bitset>\n'
        'checks if all, any or none bits are set to true\n\n'

        'bool none() const;',

    'bitset::count':
        '<bitset>\n'
        'returns the number of bits set to true\n\n'

        'std::size_t count() const;',

    'bitset::size':
        '<bitset>\n'
        'returns the size number of bits that the bitset can hold\n\n'

        'std::size_t size() const; (until C++11)\n\n'

        'constexpr std::size_t size(); (since C++11) (until C++14)\n\n'

        'constexpr std::size_t size() const; (since C++14)',

    'bitset::set':
        '<bitset>\n'
        'sets bits to true or given value\n\n'

        'bitset<N> &set();\n\n'

        'bitset<N> &set(size_t pos, bool value=true);',

    'bitset::reset':
        '<bitset>\n'
        'sets bits to false\n\n'

        'bitset<N> &reset();\n\n'

        'bitset<N> &reset(size_t pos);',

    'bitset::flip':
        '<bitset>\n'
        'toggles the values of bits\n\n'

        'bitset<N> &flip();\n\n'

        'bitset<N> &flip(size_t pos);',

    'bitset::to_string':
        '<bitset>\n'
        'returns a string representation of the data\n\n'

        'template <class CharT, class Traits, class Alloc>\n'
        'std::basic_string<CharT, Traits, Allocator> to_string() const; (until C++11)\n\n'

        'template < \n'
        '    class CharT=char, class Traits=std::char_traits<CharT>, \n'
        '    class Allocator=std::allocator<CharT> \n'
        '>\n'
        'std::basic_string<CharT, Traits, Allocator> to_string( \n'
        '    CharT zero=CharT(\'0\'), CharT one=CharT(\'1\')const \n'
        '); (since C++11)',

    'bitset::to_ulong':
        '<bitset>\n'
        'returns an unsigned long integer representation of the data\n\n'

        'unsigned long to_ulong() const',

    'bitset::to_ullong':
        '<bitset>\n'
        'returns an unsigned long long integer representation of the data\n\n'

        'unsigned long long to_ullong() const (since C++11)',

    'pair':
        '<pair>\n'
        'constructs new pair\n\n'

        'pair(); (until C++11)\n\n'

        'constexpr pair(); (since C++11)\n\n'

        'pair(const T1 &x, const T2 &y); (until C++14)\n\n'

        'constexpr pair(const T1 &x, const T2 &y); (since C++14)\n\n'

        'template <class U1, class U2>\n'
        'pair(U1 &&x, U2 &&y); (since C++11) (until C++14)\n\n'

        'template <class U1, class U2>\n'
        'constexpr pair(U1 &&x, U2 &&y); (since C++14)\n\n'

        'template <class U1, class U2>\n'
        'pair(const pair<U1, U2> &p); (until C++14)\n\n'

        'template <class U1, class U2>\n'
        'constexpr pair(const pair<U1, U2> &p); (since C++14)\n\n'

        'template <class U1, class U2>\n'
        'pair(pair<U1, U2> &&p); (since C++11) (until C++14)\n\n'

        'template <class U1, class U2>\n'
        'constexpr pair(pair<U1, U2> &&p); (since C++14)\n\n'

        'template <class... Args1, class... Args2>\n'
        'pair( \n'
        '    std::piecewise_construct_t, std::tupleArgs1first_args, std::tupleArgs2 \n'
        '    second_args \n'
        '); (since C++11)\n\n'

        'pair(const pair &p)=default;\n\n'

        'pair(pair &&p)=default; (since C++11)',

    'pair::swap':
        '<pair>\n'
        'swaps the contents\n\n'

        'void swap(pair &other); (since C++11)',

    'make_pair':
        '<pair>\n'
        'creates a pair object of type, defined by the argument types\n\n'

        'template <class T1, class T2>\n'
        'std::pair<T1, T2> make_pair(T1 t, T2 u); (until C++11)\n\n'

        'template <class T1, class T2>\n'
        'std::pair<V1, V2> make_pair(T1 &&t, T2 &&u); (since C++11) (until C++14)\n\n'

        'template <class T1, class T2>\n'
        'constexpr std::pair<V1, V2> make_pair(T1 &&t, T2 &&u); (since C++14)',

    'std::swap':
        '<pair>\n'
        'specializes the std::swap algorithm\n\n'

        'template <class T1, class T2>\n'
        'void swap(pair<T1, T2> &lhs, pair<T1, T2> &rhs); (since C++11)',

    'std::get':
        '<pair>\n'
        'accesses an element of a pair\n\n'

        'template <size_t I, class T1, class T2>\n'
        'typename std::tuple_element<I, std::pair<T1, T2>>::type &get( \n'
        '    pair<T1, T2> &p \n'
        '); (since C++11) (until C++14)\n\n'

        'template <size_t I, class T1, class T2>\n'
        'constexpr std::tuple_element_t<I, std::pair<T1, T2>> &get( \n'
        '    pair<T1, T2> &p \n'
        '); (since C++14)\n\n'

        'template <size_t I, class T1, class T2>\n'
        'const typename std::tuple_element<I, std::pair<T1, T2>>::type &get( \n'
        '    const pair<T1, T2> &p \n'
        '); (since C++11) (until C++14)\n\n'

        'template <size_t I, class T1, class T2>\n'
        'constexpr const std::tuple_element_t<I, std::pair<T1, T2>> &get( \n'
        '    const pair<T1, T2> &p \n'
        '); (since C++14)\n\n'

        'template <size_t I, class T1, class T2>\n'
        'typename std::tuple_element<I, std::pair<T1, T2>>::type &&get( \n'
        '    std::pair<T1, T2> &&p \n'
        '); (since C++11) (until C++14)\n\n'

        'template <size_t I, class T1, class T2>\n'
        'constexpr std::tuple_element_t<I, std::pair<T1, T2>> &&get( \n'
        '    std::pair<T1, T2> &&p \n'
        '); (since C++14)\n\n'

        'template <class T, class U>\n'
        'constexpr T &get(std::pair<T, U> &p); (since C++14)\n\n'

        'template <class T, class U>\n'
        'constexpr const T &get(const std::pair<T, U> &p); (since C++14)\n\n'

        'template <class T, class U>\n'
        'constexpr T &&get(std::pair<T, U> &&p); (since C++14)\n\n'

        'template <class T, class U>\n'
        'constexpr T &get(std::pair<U, T> &p); (since C++14)\n\n'

        'template <class T, class U>\n'
        'constexpr const T &get(const std::pair<U, T> &p); (since C++14)\n\n'

        'template <class T, class U>\n'
        'constexpr T &&get(std::pair<U, T> &&p); (since C++14)',

    'tie':
        '<pair>\n'
        'creates a tuple of lvalue references or unpacks a tuple into individual objects\n\n'

        'template <class... Types>\n'
        'tuple<Types&...> tie(Types&... args); (since C++11) (until C++14)\n\n'

        'template <class... Types>\n'
        'constexpr tuple<Types&...> tie(Types&... args); (since C++14)',

    'tuple':
        '<tuple>\n'
        'constructs a new tuple\n\n'

        'constexpr tuple(); (since C++11)\n\n'

        'explicit tuple(const Types&... args); (since C++11) (until C++14)\n\n'

        'explicit constexpr tuple(const Types&... args); (since C++14)\n\n'

        'template <class... UTypes>\n'
        'explicit tuple(UTypes&&... args); (since C++11) (until C++14)\n\n'

        'template <class... UTypes>\n'
        'explicit constexpr tuple(UTypes&&... args); (since C++14)\n\n'

        'template <class... UTypes>\n'
        'tuple(const tuple<UTypes...> &other); (since C++11) (until C++14)\n\n'

        'template <class... UTypes>\n'
        'constexpr tuple(const tuple<UTypes...> &other); (since C++14)\n\n'

        'template <class... UTypes>\n'
        'tuple(tuple<UTypes...> &&other); (since C++11) (until C++14)\n\n'

        'template <class... UTypes>\n'
        'constexpr tuple(tuple<UTypes...> &&other); (since C++14)\n\n'

        'template <class U1, class U2>\n'
        'tuple(const pair<U1, U2> &p); (since C++11) (until C++14)\n\n'

        'template <class U1, class U2>\n'
        'constexpr tuple(const pair<U1, U2> &p); (since C++14)\n\n'

        'template <class U1, class U2>\n'
        'tuple(pair<U1, U2> &&p); (since C++11) (until C++14)\n\n'

        'template <class U1, class U2>\n'
        'constexpr tuple(pair<U1, U2> &&p); (since C++14)\n\n'

        'tuple(const tuple &other)=default; (since C++11)\n\n'

        'tuple(tuple &&other)=default; (since C++11)\n\n'

        'template <class Alloc>\n'
        'tuple(std::allocator_arg_t, const Alloc &a); (since C++11)\n\n'

        'template <class Alloc>\n'
        'tuple( \n'
        '    std::allocator_arg_t, const Alloc &a, const Typesargs \n'
        '); (since C++11)\n\n'

        'template <class Alloc, class... UTypes>\n'
        'tuple(std::allocator_arg_t, const Alloc &a, UTypes&&... args); (since C++11)\n\n'

        'template <class Alloc, class... UTypes>\n'
        'tuple( \n'
        '    std::allocator_arg_t, const Alloc &a, const tupleUTypesother \n'
        '); (since C++11)\n\n'

        'template <class Alloc, class... UTypes>\n'
        'tuple( \n'
        '    std::allocator_arg_t, const Alloc &a, tupleUTypesother \n'
        '); (since C++11)\n\n'

        'template <class Alloc, class U1, class U2>\n'
        'tuple( \n'
        '    std::allocator_arg_t, const Alloc &a, const pair<U1, U2> &p \n'
        '); (since C++11)\n\n'

        'template <class Alloc, class U1, class U2>\n'
        'tuple(std::allocator_arg_t, const Alloc &a, pair<U1, U2> &&p); (since C++11)\n\n'

        'template <class Alloc>\n'
        'tuple(std::allocator_arg_t, const Alloc &a, const tuple &other); (since C++11)\n\n'

        'template <class Alloc>\n'
        'tuple(std::allocator_arg_t, const Alloc &a, tuple &&other); (since C++11)',

    'tuple::swap':
        '<tuple>\n'
        'swaps the contents of two tuples\n\n'

        'void swap(tuple &other); (since C++11)',

    'make_tuple':
        '<tuple>\n'
        'creates a tuple object of the type defined by the argument types\n\n'

        'template <class... Types>\n'
        'tuple<VTypes...> make_tuple(Types&&... args); (since C++11) (until C++14)\n\n'

        'template <class... Types>\n'
        'constexpr tuple<VTypes...> make_tuple(Types&&... args); (since C++14)',

    'tie':
        '<tuple>\n'
        'creates a tuple of lvalue references or unpacks a tuple into individual objects\n\n'

        'template <class... Types>\n'
        'tuple<Types&...> tie(Types&... args); (since C++11) (until C++14)\n\n'

        'template <class... Types>\n'
        'constexpr tuple<Types&...> tie(Types&... args); (since C++14)',

    'forward_as_tuple':
        '<tuple>\n'
        'creates a tuple of rvalue references\n\n'

        'template <class... Types>\n'
        'tuple<Types&&...> forward_as_tuple( \n'
        '    Typesargs \n'
        '); (since C++11) (until C++14)\n\n'

        'template <class... Types>\n'
        'constexpr tuple<Types&&...> forward_as_tuple(Types&&... args); (since C++14)',

    'tuple_cat':
        '<tuple>\n'
        'creates a tuple by concatenating any number of tuples\n\n'

        'template <class... Tuples>\n'
        'std::tuple<CTypes...> tuple_cat(Tuples&&... args); (since C++11) (until C++14)\n\n'

        'template <class... Tuples>\n'
        'constexpr std::tuple<CTypes...> tuple_cat(Tuples&&... args); (since C++14)',

    'std::get':
        '<tuple>\n'
        'tuple accesses specified element\n\n'

        'template <std::size_t I, class... Types>\n'
        'typename std::tuple_element<I, tuple<Types...>>::type &get( \n'
        '    tupleTypes \n'
        '); (since C++11) (until C++14)\n\n'

        'template <std::size_t I, class... Types>\n'
        'constexpr std::tuple_element_t<I, tuple<Types...>> &get( \n'
        '    tupleTypes \n'
        '); (since C++14)\n\n'

        'template <std::size_t I, class... Types>\n'
        'typename std::tuple_element<I, tuple<Types...>>::type &&get( \n'
        '    tupleTypes \n'
        '); (since C++11) (until C++14)\n\n'

        'template <std::size_t I, class... Types>\n'
        'constexpr std::tuple_element_t<I, tuple<Types...>> &&get( \n'
        '    tupleTypes \n'
        '); (since C++14)\n\n'

        'template <std::size_t I, class... Types>\n'
        'typename std::tuple_element<I, tuple<Types...>>::type const &get( \n'
        '    const tupleTypes \n'
        '); (since C++11) (until C++14)\n\n'

        'template <std::size_t I, class... Types>\n'
        'constexpr std::tuple_element_t<I, tuple<Types...>>const &get( \n'
        '    const tupleTypes \n'
        '); (since C++14)\n\n'

        'template <class T, class... Types>\n'
        'constexpr T &get(tuple<Types...> &t); (since C++14)\n\n'

        'template <class T, class... Types>\n'
        'constexpr T &&get(tuple<Types...> &&t); (since C++14)\n\n'

        'template <class T, class... Types>\n'
        'constexpr const T &get(const tuple<Types...> &t); (since C++14)',

    'std::swap':
        '<tuple>\n'
        'specializes the std::swap algorithm\n\n'

        'template <class... Types>\n'
        'void swap(tuple<Types...> &lhs, tuple<Types...> &rhs); (since C++11)',

    'abort':
        '<cstdlib>\n'
        'causes abnormal program termination (without cleaning up)\n\n'

        'void abort(); (until C++11)\n\n'

        '[[noreturn]] void abort(); (since C++11)',

    'exit':
        '<cstdlib>\n'
        'causes normal program termination with cleaning up\n\n'

        'void exit(int exit_code); (until C++11)\n\n'

        '[[noreturn]] void exit(int exit_code); (since C++11)',

    'quick_exit':
        '<cstdlib>\n'
        'causes quick program termination without completely cleaning up\n\n'

        '[[noreturn]] void quick_exit(int exit_code); (since C++11)',

    '_Exit':
        '<cstdlib>\n'
        'causes normal program termination without cleaning up\n\n'

        '[[noreturn]] void _Exit(int exit_code); (since C++11)',

    'atexit':
        '<cstdlib>\n'
        'registers a function to be called on std::exit() invocation\n\n'

        'int atexit(/*c-atexit-handler*/ *func);\n\n'

        'int atexit(/*atexit-handler*/ *func);',

    'at_quick_exit':
        '<cstdlib>\n'
        'registers a function to be called on quick_exit invocation\n\n'

        'int at_quick_exit(/*atexit-handler*/ *func);\n\n'

        'int at_quick_exit(/*c-atexit-handler*/ *func); (since C++11)',

    'system':
        '<cstdlib>\n'
        'calls the host environment\'s command processor\n\n'

        'int system(const char *command);',

    'getenv':
        '<cstdlib>\n'
        'access to the list of environment variables\n\n'

        'char *getenv(const char *env_var);',

    'malloc':
        '<cstdlib>\n'
        'allocates memory\n\n'

        'void *malloc(std::size_t size);',

    'calloc':
        '<cstdlib>\n'
        'allocates and zeroes memory\n\n'

        'void *calloc(std::size_t num, std::size_t size);',

    'realloc':
        '<cstdlib>\n'
        'expands previously allocated memory block\n\n'

        'void *realloc(void *ptr, std::size_t new_size);',

    'free':
        '<cstdlib>\n'
        'deallocates previously allocated memory\n\n'

        'void free(void *ptr);',

    'atof':
        '<cstdlib>\n'
        'converts a byte string to a floating point value\n\n'

        'double atof(const char *str);',

    'atoi':
        '<cstdlib>\n'
        'converts a byte string to an integer value\n\n'

        'int atoi(const char *str);',

    'atol':
        '<cstdlib>\n'
        'converts a byte string to an integer value\n\n'

        'long atol(const char *str);',

    'atoll':
        '<cstdlib>\n'
        'converts a byte string to an integer value\n\n'

        'long long atoll(const char *str); (since C++11)',

    'strtol':
        '<cstdlib>\n'
        'converts a byte string to an integer value\n\n'

        'long strtol(const char *str, char **str_end, int base);',

    'strtoll':
        '<cstdlib>\n'
        'converts a byte string to an integer value\n\n'

        'long long strtoll(const char *str, char **str_end, int base); (since C++11)',

    'strtoul':
        '<cstdlib>\n'
        'converts a byte string to an unsigned integer value\n\n'

        'unsigned long strtoul(const char *str, char **str_end, int base);',

    'strtoull':
        '<cstdlib>\n'
        'converts a byte string to an unsigned integer value\n\n'

        'unsigned long long strtoull( \n'
        '    const char *str, char **str_end, int base \n'
        '); (since C++11)',

    'strtof':
        '<cstdlib>\n'
        'converts a byte string to a floating point value\n\n'

        'float strtof(const char *str, char **str_end); (since C++11)',

    'strtod':
        '<cstdlib>\n'
        'converts a byte string to a floating point value\n\n'

        'double strtod(const char *str, char **str_end);',

    'strtold':
        '<cstdlib>\n'
        'converts a byte string to a floating point value\n\n'

        'long double strtold(const char *str, char **str_end); (since C++11)',

    'mblen':
        '<cstdlib>\n'
        'returns the number of bytes in the next multibyte character\n\n'

        'int mblen(const char *s, std::size_t n);',

    'mbtowc':
        '<cstdlib>\n'
        'converts the next multibyte character to wide character\n\n'

        'int mbtowc(wchar_t *pwc, const char *s, std::size_t n);',

    'wctomb':
        '<cstdlib>\n'
        'converts a wide character to its multibyte representation\n\n'

        'int wctomb(char *s, wchar_t wc);',

    'mbstowcs':
        '<cstdlib>\n'
        'converts a narrow multibyte character string to wide string\n\n'

        'std::size_t mbstowcs(wchar_t *dst, const char *src, std::size_t len);',

    'wcstombs':
        '<cstdlib>\n'
        'converts a wide string to narrow multibyte character string\n\n'

        'std::size_t wcstombs(char *dst, const wchar_t *src, std::size_t len);',

    'rand':
        '<cstdlib>\n'
        'generates a pseudo-random number\n\n'

        'int rand();',

    'srand':
        '<cstdlib>\n'
        'seeds pseudo-random number generator\n\n'

        'void srand(unsigned seed);',

    'qsort':
        '<cstdlib>\n'
        'sorts a range of elements with unspecified type\n\n'

        'void qsort( \n'
        '    void *ptr, std::size_t count, std::size_t size, comparepredcomp \n'
        ');\n\n'

        'void qsort( \n'
        '    void *ptr, std::size_t count, std::size_t size, comparepredcomp \n'
        ');',

    'bsearch':
        '<cstdlib>\n'
        'searches an array for an element of unspecified type\n\n'

        'void *bsearch( \n'
        '    const void *key, const void *ptr, std::size_t count, std::size_t size, \n'
        '    comparepredcomp \n'
        ');\n\n'

        'void *bsearch( \n'
        '    const void *key, const void *ptr, std::size_t count, std::size_t size, \n'
        '    comparepredcomp \n'
        ');',

    'div':
        '<cstdlib>\n'
        'computes quotient and remainder of integer division\n\n'

        'std::div_t div(int x, int y);\n\n'

        'std::ldiv_t div(long x, long y);\n\n'

        'std::lldiv_t div(long long x, long long y); (since C++11)\n\n'

        'std::imaxdiv_t div(std::intmax_t x, std::intmax_t y); (since C++11)',

    'strcpy':
        '<cstring>\n'
        'copies one string to another\n\n'

        'char *strcpy(char *dest, const char *src);',

    'strncpy':
        '<cstring>\n'
        'copies a certain amount of characters from one string to another\n\n'

        'char *strncpy(char *dest, const char *src, std::size_t count);',

    'strcat':
        '<cstring>\n'
        'concatenates two strings\n\n'

        'char *strcat(char *dest, const char *src);',

    'strncat':
        '<cstring>\n'
        'concatenates a certain amount of characters of two strings\n\n'

        'char *strncat(char *dest, const char *src, std::size_t count);',

    'strxfrm':
        '<cstring>\n'
        'transform a string so that strcmp would produce the same result as strcoll\n\n'

        'std::size_t strxfrm(char *dest, const char *src, std::size_t count);',

    'strlen':
        '<cstring>\n'
        'returns the length of a given string\n\n'

        'std::size_t strlen(const char *str);',

    'strcmp':
        '<cstring>\n'
        'compares two strings\n\n'

        'int strcmp(const char *lhs, const char *rhs);',

    'strncmp':
        '<cstring>\n'
        'compares a certain amount of characters of two strings\n\n'

        'int strncmp(const char *lhs, const char *rhs, size_t count);',

    'strcoll':
        '<cstring>\n'
        'compares two strings in accordance to the current locale\n\n'

        'int strcoll(const char *lhs, const char *rhs);',

    'strchr':
        '<cstring>\n'
        'finds the first occurrence of a character\n\n'

        'const char *strchr(const char *str, int ch);\n\n'

        'char *strchr(char *str, int ch);',

    'strrchr':
        '<cstring>\n'
        'finds the last occurrence of a character\n\n'

        'const char *strrchr(const char *str, int ch);\n\n'

        'char *strrchr(char *str, int ch);',

    'strspn':
        '<cstring>\n'
        'returns the length of the maximum initial segment that consists of only the\n'
        'characters found in another byte string\n\n'

        'size_t strspn(const char *dest, const char *src);',

    'strcspn':
        '<cstring>\n'
        'returns the length of the maximum initial segment that consists of only the\n'
        'characters not found in another byte string\n\n'

        'size_t strcspn(const char *dest, const char *src);',

    'strpbrk':
        '<cstring>\n'
        'finds the first location of any character from a set of separators\n\n'

        'const char *strpbrk(const char *dest, const char *breakset);\n\n'

        'char *strpbrk(char *dest, const char *breakset);',

    'strstr':
        '<cstring>\n'
        'finds the first occurrence of a substring of characters\n\n'

        'const char *strstr(const char *str, const char *target);\n\n'

        'char *strstr(char *str, const char *target);',

    'strtok':
        '<cstring>\n'
        'finds the next token in a byte string\n\n'

        'char *strtok(char *str, const char *delim);',

    'memchr':
        '<cstring>\n'
        'searches an array for the first occurrence of a character\n\n'

        'const void *memchr(const void *ptr, int ch, std::size_t count);\n\n'

        'void *memchr(void *ptr, int ch, std::size_t count);',

    'memcmp':
        '<cstring>\n'
        'compares two buffers\n\n'

        'int memcmp(const void *lhs, const void *rhs, std::size_t count);',

    'memset':
        '<cstring>\n'
        'fills a buffer with a character\n\n'

        'void *memset(void *dest, int ch, std::size_t count);',

    'memcpy':
        '<cstring>\n'
        'copies one buffer to another\n\n'

        'void *memcpy(void *dest, const void *src, std::size_t count);',

    'memmove':
        '<cstring>\n'
        'moves one buffer to another\n\n'

        'void *memmove(void *dest, const void *src, std::size_t count);',

    'strerror':
        '<cstring>\n'
        'returns a text version of a given error code\n\n'

        'char *strerror(int errnum);',
}

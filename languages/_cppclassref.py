CPP_CLASSREF = {
    'bitset':
        'Defined in header <bitset>\n'
        'represents a fixed-size sequence of N bits \n\n'

        'template <std::size_t N>\n'
        'class bitset;\n\n'

        'Template parameters:\n'
        '  N - the number of bits to allocate storage for',

    'pair':
        'Defined in header <utility>\n'
        'provides a way to store two heterogeneous objects as a single unit \n\n'

        'template <class T1, class T2>\n'
        'struct pair;\n\n'

        'Template parameters:\n'
        '  T1, T2 - the types of the elements that the pair stores',

    'tuple':
        'Defined in header <tuple>\n'
        'a fixed-size collection of heterogeneous values \n\n'

        'template <class... Types>\n'
        'class tuple;  (since C++11)\n\n'

        'Template parameters:\n'
        '  Types... - the types of the elements that the tuple stores.  Empty list is \n'
        '             supported',

    'vector':
        'Defined in header <vector>\n'
        'a sequence container that encapsulates dynamic size arrays \n\n'

        'template <class T, class Allocator=std::allocator<T>>\n'
        'class vector;\n\n'

        'Template parameters:\n'
        '  T - The type of the elements\n'
        '  Allocator - An allocator that is used to acquire memory to store the elements',

    'deque':
        'Defined in header <deque>\n'
        'an indexed sequence container that allows fast insertion and deletion at both \n'
        'its beginning and its end\n\n'

        'template <class T, class Allocator=std::allocator<T>>\n'
        'class deque;'

        'Template parameters:\n'
        '  T - The type of the elements\n'
        '  Allocator - An allocator that is used to acquire memory to store the elements',

    'list':
        'Defined in header <list>\n'
        'a container that supports constant time insertion and removal of elements from \n'
        'anywhere in the container\n\n'

        'template <class T, class Allocator=std::allocator<T>>\n'
        'class list;\n\n'

        'Template parameters:\n'
        '  T - The type of the elements\n'
        '  Allocator - An allocator that is used to acquire memory to store the elements',

    'forward_list':
        'Defined in header <forward_list>\n'
        'a container that supports fast insertion and removal of elements from anywhere \n'
        'in the container\n\n'

        'template <class T, class Allocator=std::allocator<T>>\n'
        'class forward_list;  (since C++11)\n\n'

        'Template parameters:\n'
        '  T - The type of the elements\n'
        '  Allocator - An allocator that is used to acquire memory to store the elements',

    'set':
        'Defined in header <set>\n'
        'an associative container that contains a sorted set of unique objects of type \n'
        'Key.  Sorting is done using key comparison function Compare\n\n'

        'template <\n'
        '    class Key, class Compare=std::less<Key>, \n'
        '    class Allocator=std::allocator<Key>\n'
        '>\n'
        'class set;  (until C++17)',

    'multiset':
        'Defined in header <set>\n'
        'an associative container that contains a sorted set of objects of type Key.\n'
        'Unlike set, multiple keys with equivalent values are allowed\n\n'

        'template <\n'
        '    class Key, class Compare=std::less<Key>, \n'
        '    class Allocator=std::allocator<Key>\n'
        '>\n'
        'class multiset;  (until C++17)',

    'map':
        'Defined in header <map>\n'
        'a sorted associative container that contains key-value pairs with unique keys.\n'
        'Keys are sorted by using the comparison function Compare\n\n'

        'template <\n'
        '    class Key, class T, class Compare=std::less<Key>, \n'
        '    class Allocator=std::allocator<std::pair<const Key, T>> \n'
        '>\n'
        'class map;  (until C++17)',

    'multimap':
        'Defined in header <map>\n'
        'an associative container that contains a sorted list of key-value pairs.\n'
        'Sorting is done according to the comparison function Compare, applied to the \n'
        'keys.  The order of the key-value pairs whose keys compare equivalent is the \n'
        'order of insertion and does not change\n\n'

        'template <\n'
        '    class Key, class T, class Compare=std::less<Key>, \n'
        '    class Allocator=std::allocator<std::pair<const Key, T>> \n'
        '>\n'
        'class multimap;  (until C++17)',

    'unordered_set':
        'Defined in header <unordered_set>\n'
        'an associative container that contains a set of unique objects of type Key\n\n'

        'template <\n'
        '    class Key, class Hash=std::hash<Key>, class KeyEqual=std::equal_to<Key>, \n'
        '    class Allocator=std::allocator<Key>, \n'
        '>\n'
        'class unordered_set;  (since C++11)',

    'unordered_multiset':
        'Defined in header <unordered_set>\n'
        'an associative container that contains set of possibly non-unique objects of \n'
        'type Key\n\n'

        'template <\n'
        '    class Key, class Hash=std::hash<Key>, class KeyEqual=std::equal_to<Key>, \n'
        '    class Allocator=std::allocator<Key> \n'
        '>\n'
        'class unordered_multiset;  (since C++11)',

    'unordered_map':
        'Defined in header <unordered_map>\n'
        'an associative container that contains key-value pairs with unique keys\n\n'

        'template <\n'
        '    class Key, class T, class Hash=std::hash<Key>, \n'
        '    class KeyEqual=std::equal_to<Key>, \n'
        '    class Allocator=std::allocator<std::pair<const Key, T>> \n'
        '>\n'
        'class unordered_map;  (since C++11)',

    'unordered_multimap':
        'Defined in header <unordered_map>\n'
        'an unordered associative container that supports equivalent keys (an \n'
        'unordered_multimap may contain multiple copies of each key value) and that \n'
        'associates values of another type with the keys.  The unordered_multimap \n'
        'class supports forward iterators\n\n'

        'template < \n'
        '    class Key, class T, class Hash=std::hash<Key>, \n'
        '    class KeyEqual=std::equal_to<Key>, \n'
        '    class Allocator=std::allocator<std::pair<const Key, T>> \n'
        '>\n'
        'class unordered_multimap;  (since C++11)',

    'stack':
        'Defined in header <stack>\n'
        'a container adapter that gives the programmer the functionality of a stack \n'
        '-- specifically, a FILO (first-in, last-out) data structure\n\n'

        'template <class T, class Container=std::deque<T>>\n'
        'class stack\n\n'

        'Template parameters:\n'
        '  T - The type of the stored elements \n'
        '  Container - The type of the underlying container to use to store the elements ',

    'queue':
        'Defined in header <queue>\n'
        'a container adapter that gives the programmer the functionality of a queue \n'
        '-- specifically, a FIFO (first-in, first-out) data structure\n\n'

        'template <class T, class Container=std::deque<T>>\n'
        'class queue;\n\n'

        'Template parameters:\n'
        '  T - The type of the stored elements \n'
        '  Container - The type of the underlying container to use to store the elements ',

    'priority_queue':
        'Defined in header <queue>\n'
        'a container adaptor that provides constant time lookup of the largest (by \n'
        'default) element.  A user-provided Compare can be supplied to change the \n'
        'ordering.  e.g. using std::greater<T> would cause the smallest element to \n'
        'appear as the top()\n\n'

        'template <\n'
        '    class T, class Container=std::vector<T>, \n'
        '    class Compare=std::less<typename Container::value_type> \n'
        '>\n'
        'class priority_queue\n\n'

        'Template parameters:\n'
        '  T - The types of the stored elements \n'
        '  Container - The type of the underlying container to use to store the elements \n'
        '  Compare - A Compare type providing a strict weak ordering ',

    'basic_string':
        'Defined in header <string>\n'
        'stores and manipulates sequences of char-like objects\n\n'

        'template <\n'
        '    class CharT, class Traits=std::char_traits<CharT>, \n'
        '    class Allocator=std::allocator<CharT> \n'
        '>\n'
        'class basic_string;\n\n'

        'Template parameters:\n'
        '  CharT - character type \n'
        '  Traits - traits class specifying the operations on the character type \n'
        '  Allocator - Allocator type used to allocate internal storage ',
}

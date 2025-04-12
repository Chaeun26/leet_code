class LRUCache {
private:
    int capacity;

    struct Node{
        int key,value;
        Node* prev;
        Node* next;
        Node(int k, int v): key(k),value(v),prev(nullptr),next(nullptr){}
    };

    unordered_map<int,Node*> cache;
    Node* head;
    Node* tail;

    void removeNode(Node* node){
        node->prev->next=node->next;
        node->next->prev=node->prev;
    }

    void addToHead(Node* node){
        node->prev=head;
        node->next=head->next;
        head->next->prev=node;
        head->next=node;
    }

    void moveToHead(Node* node){
        removeNode(node);
        addToHead(node);
    }

    Node* removeTail(){
        Node* node = tail->prev;
        removeNode(node);
        return node;
    }
public:
    LRUCache(int capacity) {
        this->capacity=capacity;
        head = new Node(0,0);
        tail = new Node(0,0);

        head->next=tail;
        tail->prev=head;
    }
    
    int get(int key) {
        if(cache.count(key)){
            Node* node=cache[key];
            moveToHead(node);
            return node->value;
        }
        return -1;
    }
    
    void put(int key, int value) {
        if(cache.count(key)){
            Node* node=cache[key];
            node->value=value;
            moveToHead(node);
        }else{
            if(cache.size()==capacity){
                Node* lru=removeTail();
                cache.erase(lru->key);
                delete lru;
            }
            Node* node=new Node(key,value);
            addToHead(node);
            cache[key]=node;
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
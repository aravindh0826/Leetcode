/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head){
    struct ListNode *first = head;
    struct ListNode *second = head;

    while (first!= NULL && first->next != NULL){
        second = second->next;           
        first= first->next->next;     
        if (first== second){
            return true;             
        }
    }
    return false;                    
}
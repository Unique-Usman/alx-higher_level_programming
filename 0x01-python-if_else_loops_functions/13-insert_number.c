#include "lists.h"
/**
 * insert_node - Inserts a node with a given number into a sorted linked list.
 * @head: A pointer to a pointer to the head of the linked list.
 * @number: The number to insert into the linked list.
 *
 * Return: A pointer to the newly inserted node.
 */
listint_t *insert_node(listint_t **head, int number)
{
        listint_t *tmp, *traversal;
        traversal = *head;

        tmp = malloc(sizeof(listint_t *));
        tmp->n = number;
        tmp->next = NULL;
        if (tmp == NULL)
            return (NULL);
        if (traversal == NULL)
        {
            *head = tmp;
            return (tmp);
        }
	if ((*head)->n <= number)
	{
		tmp->next = *head;
		*head = tmp;
		return (tmp);
	}
        while (traversal->next != NULL)
        {
            if (traversal->n >= number)
            {
                tmp->next = traversal;
                traversal = tmp;
                return (tmp);
            }
            else if (traversal->next->n >= number)
            {
                tmp->next = traversal->next;
                traversal->next = tmp;
                return (tmp);
            }
            if (traversal->next == NULL && traversal->n < number)
            {
                traversal->next = tmp;
                return tmp;
            }
	    traversal = traversal->next;
        }

        return (NULL);
}

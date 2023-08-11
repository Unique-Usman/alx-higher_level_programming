#include "lists.h"
/**
 * check_cycle - Checks if a singly linked list has a cycle.
 * @listint_t: A pointer to the head of the linked list.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp;

	if (list == NULL) return (0);
	tmp = list->next;
	while (tmp != NULL)
	{
		if (tmp == list) return (1);
		tmp = tmp->next;
	}

	return (0);
}

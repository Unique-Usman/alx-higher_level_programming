#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *tmp;
	int *list, size, count, i;

	tmp = *head;
	size = 0;
	count = 0;
	if (tmp == NULL)
		return (1);
	while (tmp)
	{
		size++;
		tmp = tmp->next;
	}

	list = malloc(sizeof(int) * size);
	tmp = *head;

	while (tmp)
	{
		list[count] = tmp->n;
		tmp = tmp->next;
		count++;
	}

	for (i = 0; i <= size / 2; i++)
	{
		if (list[i] != list[size - i - 1])
			return (0);
	}
	free(list);
	return (1);
}

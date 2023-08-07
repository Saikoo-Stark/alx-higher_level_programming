#include "lists.h"

/**
 * check_cycle - to check cycle in linked list
 * @list: pointer to list to be checked
 * Return: int
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_p = list, *fast_p = list;

	while (slow_p && fast_p && fast_p->next)
	{
		slow_p = slow_p->next;
		fast_p = fast_p->next->next;
		if (slow_p == fast_p)
		{
			return (1);
		}
	}
	return (0);
}

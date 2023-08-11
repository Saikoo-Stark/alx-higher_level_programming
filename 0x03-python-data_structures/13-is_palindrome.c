#include "lists.h"

/**
 * add_front - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_front(listint_t **head, const int n)
{
	listint_t *new;
	listint_t *current;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = current;
	*head = new;
	return (new);
}

/**
 * pop_front - function
 * @head: pointer to head of list
 */
void pop_front(listint_t **head)
{
	listint_t *current;

	if (head == NULL || *head == NULL)
		return;

	current = *head;
	*head = (*head)->next;
	free(current);
}

/**
 * is_palindrome - function
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *revhead = NULL;
	listint_t *cur = NULL;
	listint_t *currev = NULL;

	if (!head || !(*head))
		return (1);

	cur = *head;

	while (cur)
	{
		add_front(&revhead, cur->n);
		cur = cur->next;
	}

	cur = *head;
	currev = revhead;

	while (cur && currev)
	{
		if (cur->n != currev->n)
			return (0);
		cur = cur->next;
		currev = currev->next;
	}

	return (1);
}

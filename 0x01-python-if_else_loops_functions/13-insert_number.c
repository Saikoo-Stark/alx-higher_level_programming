#include "lists.h"

/**
 * insert_node - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{

	listint_t *new_node = NULL;
	listint_t *temp = NULL;

	if (head == NULL)
		return (NULL);

	if (*head == NULL)
		return (add_nodeint_end(head, (const int)number));

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	temp = *head;

	if (number <= temp->n)
	{
		new_node->next = temp;
		*head = new_node;
		return (new_node);
	}

	while (temp->next != NULL && number >= temp->next->n)
		temp = temp->next;

	new_node->next = temp->next;
	temp->next = new_node;

	return (new_node);
}

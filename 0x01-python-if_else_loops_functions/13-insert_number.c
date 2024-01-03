#include <stdlib.h>
#include <stdio.h>
#include "lists.h"
/**
 * insert_node - Insert node in order mode to linkedlist
 * @head: head of list
 * @number: nummber to be added
 * Return: the address of new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newone = malloc(sizeof(listint_t));
	listint_t *active = *head;

	if (!newone)
		return (NULL);

	newone->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		newone->next = *head;
		*head = newone;
		return (newone);
	}
	while (active->next)
	{
		if ((active->next)->n >= number)
		{
			newone->next = active->next;
			active->next = newone;
			return (newone);
		}
		active = active->next;
	}

	newone->next = NULL;
	active->next = newone;

	return (newone);
}

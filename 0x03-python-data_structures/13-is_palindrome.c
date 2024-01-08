#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - is palindrome
 *@head: head of list
 * Return: 0 on successe 1 other wise
 */
int is_palindrome(listint_t **head)
{
	listint_t *help = NULL;
	int *tab = NULL;
	int i = 0;
	int j = 0;
	int k = 0;

	help = *head;
	if (*head)
	{
		while (help != NULL)
		{
			j++;
			help = help->next;
		}
		tab = malloc(sizeof(int) * j);
		help = *head;
		while (help != NULL)
		{
			tab[i] = help->n;
			i++;
			help = help->next;
		}
		while (k < j / 2)
		{
			if (tab[k] == tab[j - k - 1])
				k++;
			else
				return (0);
		}
	}
	return (1);
}

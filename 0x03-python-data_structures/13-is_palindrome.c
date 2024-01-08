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
	int tab[2048];
	int i = 0;
	int j = 0;

	help = *head;
	if (*head)
	{
		while (help != NULL)
		{
			tab[j] = help->n;
			j++;
			help = help->next;
		}
		while (i < j / 2)
		{
			if (tab[i] == tab[j - i - 1])
				i++;
			else
				return (0);
		}
	}
	return (1);
}

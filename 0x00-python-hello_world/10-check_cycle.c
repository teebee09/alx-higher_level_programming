#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - fncs checks if a singly linked list has a cycle in it.
 * @list: head of linked list
 *
 * Description - check for loops in a singly linked list
 * Return: 1 if cycled, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list)
	{
		return (0);
	}
	slow = list;
	fast = list->next;
	while (fast && slow && fast->next)
	{
		if (slow == fast)
		{
			return (1);
		}
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}

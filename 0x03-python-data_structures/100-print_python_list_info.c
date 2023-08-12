#include "listobject.h"
#include "object.h"

/**
 * print_python_list_info - frees a listint_t list
 * @p: pointer to list to be freed
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int i, l;

	l = PyList_Size(p) for (i = 0; i < l; i++)
		printf("[*] Size of the Python List = %d", l);
}

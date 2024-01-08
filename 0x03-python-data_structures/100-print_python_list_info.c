#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - data of the PyListObject
 * @p: the PyObject
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t s = 0;
	int i = 0;

	if (PyList_CheckExact(p))
	{
		s = PyList_Size(p);

		printf("[*] Size of the Python List = %zd\n", s);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (i < s)
		{
			printf("Element %d: %s\n",
					i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
			i++;
		}
	}
}

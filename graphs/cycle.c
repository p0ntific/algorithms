#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int flag = 0;
int ind = 0;

void DFS(int v, int *visited, int *children, int **adjacency, int*path) 
{
    
    if (flag) return;
    
    visited[v] = 1;
    int u;
    
    path[ind] = v;
    ind++;
    
    for (int i = 0; i < children[v]; i++) 
    {
        u = adjacency[v][i];
        
        if (visited[u] == 1) 
        {
            path[ind] = u;
            ind++;
            flag = 1;
            return;
        }
        else 
        {
            DFS(u, visited, children, adjacency, path);
            if (flag) return;
        }
    }
    
    visited[v] = 2;
    ind -= 1;
}

int main()
{
    FILE* inputFile = fopen("cycle2.in", "r");
    FILE* outputFile = fopen("cycle2.out", "w");
  
    int n, m;
    fscanf(inputFile, "%d %d", &n, &m);
    
    int *visited = (int*)malloc((n + 1)*sizeof(int));
    int *children = (int*)malloc((n + 1)*sizeof(int));
    int *index = (int*)malloc((n + 1) * sizeof(int));
    
    for (int i = 1; i < n + 1; i++)
    {
        visited[i] = 0;
        children[i] = 0;
        index[i] = 0;
    }
        
    int x, y;
    int *x_nodes = (int*)malloc((m) * sizeof(int));
    int *y_nodes = (int*)malloc((m) * sizeof(int));
    
    for (int i = 0; i < m; i++) 
    {
        fscanf(inputFile, "%d %d", &x, &y);
        children[x]++;
        x_nodes[i] = x;
        y_nodes[i] = y;
    }
    
    int **adjacency = (int**)malloc((n + 1) * sizeof(int*));
    for (int i = 1; i < n + 1; i++)
        adjacency[i] = (int*)malloc(children[i] * sizeof(int));       

    for (int i = 0; i < m; i++) 
    {
        adjacency[x_nodes[i]][index[x_nodes[i]]] = y_nodes[i];
        index[x_nodes[i]]++;
    } 
    
    int *path = (int*)malloc((n+1) * sizeof(int));
    
    for (int i = 1; i < n + 1; i++) 
    {
        if (visited[i] == 0) 
        {
            DFS(i, visited, children, adjacency, path);
            if (flag) break;
        }
    }

    if (flag) 
    {
        fprintf(outputFile, "YES\n");
        
        int start = ind - 2;
        
        while (path[start] != path[ind-1]) start -= 1;
        
        for (int i = start; i < ind-1; i++) fprintf(outputFile, "%d ", path[i]);
    }
    else 
        fprintf(outputFile, "NO\n");
    
    fclose(inputFile);
    fclose(outputFile);

    return 0;
}
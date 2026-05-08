# GetRecentFiles Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetRecentFiles`

Gets a list of the most recently used files.
Gets a list of the most recently used files.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetRecentFiles() As System.Object
```

```

Dim instance As ISldWorks
Dim value As System.Object
 
value = instance.GetRecentFiles()
```

```

System.object GetRecentFiles()
```

```

System.Object^ GetRecentFiles(); 
```

#### Return Value

List of most recently used files (see **Remarks**)

Remarks

The list is returned in pairs of files.  For each pair, the first item is the fully qualified path to the file.  The second item is just the filename, as it appears in the most recent used list in the SOLIDWORKS File menu.

Example

'----------------------------------------

Option Explicit

Sub main()

    Dim swApp               As SldWorks.SldWorks

    Dim vFileArr            As Variant

    Dim i                   As Long

    Set swApp = Application.SldWorks

    

    vFileArr = swApp.GetRecentFiles

    

    For i = 0 To UBound(vFileArr) Step 2

        Debug.Print vFileArr(i + 1) & " --> " & vFileArr(i)

    Next i

End Sub

'----------------------------------------

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)

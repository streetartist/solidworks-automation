# IGetDocumentNames Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~IGetDocumentNames`

Gets the original paths and filenames of all of the model's documents for Pack and Go.
Gets the original paths and filenames of all of the model's documents for Pack and Go.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetDocumentNames( _
   ByVal Count As System.Integer, _
   ByRef DocumentNames As System.String _
) As System.Boolean
```

```

Dim instance As IPackAndGo
Dim Count As System.Integer
Dim DocumentNames As System.String
Dim value As System.Boolean
 
value = instance.IGetDocumentNames(Count, DocumentNames)
```

```

System.bool IGetDocumentNames( 
   System.int Count,
   out System.string DocumentNames
)
```

```

System.bool IGetDocumentNames( 
   System.int Count,
   [Out] System.String^ DocumentNames
) 
```

#### Parameters

*Count*
:   Number of model's documents

*DocumentNames*
:   - in-process, unmanaged C++: Pointer to an array of strings containing the original paths and filenames of the model's documents
    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

#### Return Value

True if the original paths and filenames of the model's documents are returned, false if not

Remarks

Before calling this method, call [IPackAndGo::GetDocumentNamesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~GetDocumentNamesCount.md) to get the value of Count.

To get the drawing documents of the model, set [IPackAndGo::IncludeDrawings](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~IncludeDrawings.md) to true; otherwise, the paths and filenames of the model's drawing documents are not returned.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPackAndGo Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.md)  
[IPackAndGo Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo_members.md)  
[IPackAndGo::GetDocumentNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~GetDocumentNames.md)

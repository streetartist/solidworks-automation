# IGetRevisionSymbols Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~IGetRevisionSymbols`

Gets the revision symbols associated with the specified revision ID.
Gets the revision symbols associated with the specified revision ID.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetRevisionSymbols( _
   ByVal RevisionId As System.Integer, _
   ByVal Count As System.Integer _
) As Note
```

```

Dim instance As IRevisionTableAnnotation
Dim RevisionId As System.Integer
Dim Count As System.Integer
Dim value As Note
 
value = instance.IGetRevisionSymbols(RevisionId, Count)
```

```

Note IGetRevisionSymbols( 
   System.int RevisionId,
   System.int Count
)
```

```

Note^ IGetRevisionSymbols( 
   System.int RevisionId,
   System.int Count
) 
```

#### Parameters

*RevisionId*
:   Revision ID

*Count*
:   Number of revision symbols

#### Return Value

- in-process, unmanaged C++: Pointer to an array of revision symbols

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [IRevisionTableAnnotation::GetRevisionSymbolCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetRevisionSymbolCount.md) before calling this method to get the value of Count.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRevisionTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation.md)  
[IRevisionTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation_members.md)  
[IRevisionTableAnnotation::GetRevisionSymbols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetRevisionSymbols.md)  
[IRevisionTableAnnotation::CurrentRevision Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~CurrentRevision.md)

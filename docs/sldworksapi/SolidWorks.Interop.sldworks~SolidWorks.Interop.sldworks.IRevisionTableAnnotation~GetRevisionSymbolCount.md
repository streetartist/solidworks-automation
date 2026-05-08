# GetRevisionSymbolCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetRevisionSymbolCount`

Gets the number of revision symbols associated with the specified revision ID.
Gets the number of revision symbols associated with the specified revision ID.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetRevisionSymbolCount( _
   ByVal RevisionId As System.Integer _
) As System.Integer
```

```

Dim instance As IRevisionTableAnnotation
Dim RevisionId As System.Integer
Dim value As System.Integer
 
value = instance.GetRevisionSymbolCount(RevisionId)
```

```

System.int GetRevisionSymbolCount( 
   System.int RevisionId
)
```

```

System.int GetRevisionSymbolCount( 
   System.int RevisionId
) 
```

#### Parameters

*RevisionId*
:   Revision ID

#### Return Value

Number of revision symbols for this revision ID

Remarks

Call this method before calling [IRevisionTableAnnotation::IGetRevisionSymbols](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetRevisionSymbols.md) to get the size of the array for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRevisionTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation.md)  
[IRevisionTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation_members.md)  
[IRevisionTableAnnotation::GetRevisionSymbols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetRevisionSymbols.md)  
[IRevisionTableAnnotation::IGetRevisionSymbols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~IGetRevisionSymbols.md)  
[IRevisionTableAnnotation::CurrentRevision Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~CurrentRevision.md)

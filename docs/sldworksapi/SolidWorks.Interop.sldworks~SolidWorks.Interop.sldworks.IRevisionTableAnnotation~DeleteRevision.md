# DeleteRevision Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~DeleteRevision`

Deletes a revision from this revision table.
Deletes a revision from this revision table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DeleteRevision( _
   ByVal RevisionId As System.Integer, _
   ByVal DeleteSymbols As System.Boolean _
) As System.Boolean
```

```

Dim instance As IRevisionTableAnnotation
Dim RevisionId As System.Integer
Dim DeleteSymbols As System.Boolean
Dim value As System.Boolean
 
value = instance.DeleteRevision(RevisionId, DeleteSymbols)
```

```

System.bool DeleteRevision( 
   System.int RevisionId,
   System.bool DeleteSymbols
)
```

```

System.bool DeleteRevision( 
   System.int RevisionId,
   System.bool DeleteSymbols
) 
```

#### Parameters

*RevisionId*
:   Revision ID

*DeleteSymbols*
:   True to delete all associated symbols, false to not

#### Return Value

True if revision ID is deleted, false if not

Remarks

This method deletes the row in which the revision ID exists.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRevisionTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation.md)  
[IRevisionTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation_members.md)  
[IRevisionTableAnnotation::AddRevision Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~AddRevision.md)  
[IRevisionTableAnnotation::GetIdForRowNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetIdForRowNumber.md)  
[IRevisionTableAnnotation::GetRevisionForId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetRevisionForId.md)  
[IRevisionTableAnnotation::GetRowNumberForId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetRowNumberForId.md)  
[IRevisionTableAnnotation::CurrentRevision Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~CurrentRevision.md)

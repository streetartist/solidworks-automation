# GetRevisionForId Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetRevisionForId`

Gets the revision text for the specified revision ID.
Gets the revision text for the specified revision ID.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetRevisionForId( _
   ByVal RevisionId As System.Integer _
) As System.String
```

```

Dim instance As IRevisionTableAnnotation
Dim RevisionId As System.Integer
Dim value As System.String
 
value = instance.GetRevisionForId(RevisionId)
```

```

System.string GetRevisionForId( 
   System.int RevisionId
)
```

```

System.String^ GetRevisionForId( 
   System.int RevisionId
) 
```

#### Parameters

*RevisionId*
:   Revision ID

#### Return Value

Revision text

Remarks

Call [IRevisionTableAnnotation::GetIdForRowNumber](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetIdForRowNumber.md) to get the revision ID for the row in which the revision text exists.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRevisionTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation.md)  
[IRevisionTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation_members.md)  
[IRevisionTableAnnotation::AddRevision Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~AddRevision.md)  
[IRevisionTableAnnotation::DeleteRevision Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~DeleteRevision.md)  
[IRevisionTableAnnotation::GetRowNumberForId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetRowNumberForId.md)  
[IRevisionTableAnnotation::CurrentRevision Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~CurrentRevision.md)

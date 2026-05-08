# GetIdForRowNumber Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetIdForRowNumber`

Gets the revision ID for the specified row number.
Gets the revision ID for the specified row number.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetIdForRowNumber( _
   ByVal RowIndex As System.Integer _
) As System.Integer
```

```

Dim instance As IRevisionTableAnnotation
Dim RowIndex As System.Integer
Dim value As System.Integer
 
value = instance.GetIdForRowNumber(RowIndex)
```

```

System.int GetIdForRowNumber( 
   System.int RowIndex
)
```

```

System.int GetIdForRowNumber( 
   System.int RowIndex
) 
```

#### Parameters

*RowIndex*
:   0-based index for this row number

#### Return Value

Revision ID

Remarks

This method is useful when working with a row via the [ITableAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md) object.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRevisionTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation.md)  
[IRevisionTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation_members.md)  
[IRevisionTableAnnotation::AddRevision Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~AddRevision.md)  
[IRevisionTableAnnotation::DeleteRevision Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~DeleteRevision.md)  
[IRevisionTableAnnotation::GetRevisionForId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetRevisionForId.md)  
[IRevisionTableAnnotation::GetRowNumberForId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetRowNumberForId.md)  
[IRevisionTableAnnotation::CurrentRevision Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~CurrentRevision.md)

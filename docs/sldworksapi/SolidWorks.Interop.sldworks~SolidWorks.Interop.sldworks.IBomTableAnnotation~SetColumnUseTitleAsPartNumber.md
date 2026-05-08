# SetColumnUseTitleAsPartNumber Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~SetColumnUseTitleAsPartNumber`

Sets whether to use the document title for the specified part-number column.
Sets whether to use the document title for the specified part-number column.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetColumnUseTitleAsPartNumber( _
   ByVal Index As System.Integer, _
   ByVal UseTitle As System.Boolean _
) As System.Boolean
```

```

Dim instance As IBomTableAnnotation
Dim Index As System.Integer
Dim UseTitle As System.Boolean
Dim value As System.Boolean
 
value = instance.SetColumnUseTitleAsPartNumber(Index, UseTitle)
```

```

System.bool SetColumnUseTitleAsPartNumber( 
   System.int Index,
   System.bool UseTitle
)
```

```

System.bool SetColumnUseTitleAsPartNumber( 
   System.int Index,
   System.bool UseTitle
) 
```

#### Parameters

*Index*
:   0-based index indicating the part-number column

*UseTitle*
:   True to use the document title for the specified part-number column, false to not

#### Return Value

True to use the document title for the specified part-number column, false if you specify an invalid column number or the specified column is not the part-number column

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.md)  
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.md)  
[IBomTableAnnotation::GetColumnCustomProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetColumnCustomProperty.md)

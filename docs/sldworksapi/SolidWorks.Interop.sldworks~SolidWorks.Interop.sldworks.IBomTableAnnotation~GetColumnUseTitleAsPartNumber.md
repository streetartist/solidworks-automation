# GetColumnUseTitleAsPartNumber Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetColumnUseTitleAsPartNumber`

Gets whether the document title is being used for the specified part-number column.
Gets whether the document title is being used for the specified part-number column.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetColumnUseTitleAsPartNumber( _
   ByVal Index As System.Integer _
) As System.Boolean
```

```

Dim instance As IBomTableAnnotation
Dim Index As System.Integer
Dim value As System.Boolean
 
value = instance.GetColumnUseTitleAsPartNumber(Index)
```

```

System.bool GetColumnUseTitleAsPartNumber( 
   System.int Index
)
```

```

System.bool GetColumnUseTitleAsPartNumber( 
   System.int Index
) 
```

#### Parameters

*Index*
:   0-based number indicating the part-number column

#### Return Value

True if document title is being used for the specified part-number column, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.md)  
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.md)  
[IBomTableAnnotation::SetColumnUseTitleAsPartNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~SetColumnUseTitleAsPartNumber.md)

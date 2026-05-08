# IGetTableAnnotations Method (IBendTable)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable~IGetTableAnnotations`

Gets the annotations for this bend table.
Gets the annotations for this bend table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetTableAnnotations( _
   ByVal Count As System.Integer _
) As BendTableAnnotation
```

```

Dim instance As IBendTable
Dim Count As System.Integer
Dim value As BendTableAnnotation
 
value = instance.IGetTableAnnotations(Count)
```

```

BendTableAnnotation IGetTableAnnotations( 
   System.int Count
)
```

```

BendTableAnnotation^ IGetTableAnnotations( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of bend table annotations

#### Return Value

- In-process, unmanaged C++: Pointer to an array of [IBendTableAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTableAnnotation.md)s
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IBendTable::GetTableAnnotationCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable~GetTableAnnotationCount.md) to populate Count.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBendTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable.md)  
[IBendTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable_members.md)  
[IBendTable::GetTableAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable~GetTableAnnotations.md)

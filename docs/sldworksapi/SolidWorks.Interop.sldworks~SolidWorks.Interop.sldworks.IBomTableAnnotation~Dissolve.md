# Dissolve Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~Dissolve`

Dissolves into individual components the subassembly or weldment at the specified row index of this BOM table annotation.
Dissolves into individual components the subassembly or weldment at the specified row index of this BOM table annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Dissolve( _
   ByVal RowIndex As System.Integer _
) As System.Boolean
```

```

Dim instance As IBomTableAnnotation
Dim RowIndex As System.Integer
Dim value As System.Boolean
 
value = instance.Dissolve(RowIndex)
```

```

System.bool Dissolve( 
   System.int RowIndex
)
```

```

System.bool Dissolve( 
   System.int RowIndex
) 
```

#### Parameters

*RowIndex*
:   1-based row index of the subassembly or weldment to dissolve

#### Return Value

True if the subassembly or weldment is dissolved, false if not

Example

[Dissolve Subassembly in a BOM Table (VBA)](Dissolve_Subassembly_in_a_BOM_Table_Example_VB.htm)  
[Dissolve Subassembly in a BOM Table (VB.NET)](Dissolve_Subassembly_in_a_BOM_Table_Example_VBNET.htm)  
[Dissolve Subassembly in a BOM Table (C#)](Dissolve_Subassembly_in_a_BOM_Table_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.md)  
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.md)  
[IBomTableAnnotation::RestoreRestructuredComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~RestoreRestructuredComponents.md)  
[IBomTableAnnotation::Collapse Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~Collapse.md)  
[IBomTableAnnotation::Expand Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~Expand.md)

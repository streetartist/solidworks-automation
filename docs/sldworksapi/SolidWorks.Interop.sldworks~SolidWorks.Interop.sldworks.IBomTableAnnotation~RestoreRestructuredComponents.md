# RestoreRestructuredComponents Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~RestoreRestructuredComponents`

Restores the previously dissolved subassembly or weldment at the specified row index of this BOM table annotation.
Restores the previously dissolved subassembly or weldment at the specified row index of this BOM table annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RestoreRestructuredComponents( _
   ByVal RowIndex As System.Integer _
) As System.Boolean
```

```

Dim instance As IBomTableAnnotation
Dim RowIndex As System.Integer
Dim value As System.Boolean
 
value = instance.RestoreRestructuredComponents(RowIndex)
```

```

System.bool RestoreRestructuredComponents( 
   System.int RowIndex
)
```

```

System.bool RestoreRestructuredComponents( 
   System.int RowIndex
) 
```

#### Parameters

*RowIndex*
:   1-based row index, if more than one subassembly or weldment are dissolved; 0, if only one subassembly or weldment is dissolved

#### Return Value

True if the subassembly or weldment is restored, false if not

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
[IBomTableAnnotation::Dissolve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~Dissolve.md)

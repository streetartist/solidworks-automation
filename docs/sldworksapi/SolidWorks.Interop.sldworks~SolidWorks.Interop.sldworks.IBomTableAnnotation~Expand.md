# Expand Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~Expand`

Expands the specified item.
Expands the specified item.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Expand( _
   ByVal ExpandType As System.Integer, _
   ByVal Index As System.Integer _
) 
```

```

Dim instance As IBomTableAnnotation
Dim ExpandType As System.Integer
Dim Index As System.Integer
 
instance.Expand(ExpandType, Index)
```

```

void Expand( 
   System.int ExpandType,
   System.int Index
)
```

```

void Expand( 
   System.int ExpandType,
   System.int Index
) 
```

#### Parameters

*ExpandType*
:   Type of item to expand as defined in [swBOMTableObjectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBOMTableObjectType_e.html)

*Index*
:   Row index; valid only if ExpandType is swBOMTableObjectType\_e.swBOMTableObjectType\_RowIndex

Remarks

If ExpandType is swBOMTableObjectType\_e.swBOMTableObjectType\_CutList, then all cut lists in the table expand.

Example

[Expand, Collapse, and Dissolve Subassembly in a BOM Table Example (VBA)](Dissolve_Subassembly_in_a_BOM_Table_Example_VB.htm)  
[Expand, Collapse, and Dissolve Subassembly in a BOM Table Example (VB.NET)](Dissolve_Subassembly_in_a_BOM_Table_Example_VBNET.htm)  
[Expand, Collapse, and Dissolve Subassembly in a BOM Table Example (C#)](Dissolve_Subassembly_in_a_BOM_Table_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.md)  
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.md)  
[IBomTableAnnotation::Collapse Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~Collapse.md)  
[IBomTableAnnotation::Dissolve Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~Dissolve.md)

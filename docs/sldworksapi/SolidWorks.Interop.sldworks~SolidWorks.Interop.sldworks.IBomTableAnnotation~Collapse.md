# Collapse Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~Collapse`

Collapses the specified item.
Collapses the specified item.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Collapse( _
   ByVal CollapseType As System.Integer, _
   ByVal Index As System.Integer _
) 
```

```

Dim instance As IBomTableAnnotation
Dim CollapseType As System.Integer
Dim Index As System.Integer
 
instance.Collapse(CollapseType, Index)
```

```

void Collapse( 
   System.int CollapseType,
   System.int Index
)
```

```

void Collapse( 
   System.int CollapseType,
   System.int Index
) 
```

#### Parameters

*CollapseType*
:   Type of item to collapse as defined in [swBOMTableObjectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBOMTableObjectType_e.html) (see **Remarks**)

*Index*
:   Row index; valid only if CollapseType is swBOMTableObjectType\_e.swBOMTableObjectType\_RowIndex

Remarks

If CollapseType is swBOMTableObjectType\_e.swBOMTableObjectType\_CutList, then all cut lists in the table collapse.

Example

[Expand, Collapse, and Dissolve a Subassembly in a BOM Table (VBA)](Dissolve_Subassembly_in_a_BOM_Table_Example_VB.htm)  
[Expand, Collapse, and Dissolve a Subassembly in a BOM Table (VB.NET)](Dissolve_Subassembly_in_a_BOM_Table_Example_VBNET.htm)  
[Expand, Collapse, and Dissolve a Subassembly in a BOM Table (C#)](Dissolve_Subassembly_in_a_BOM_Table_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.md)  
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.md)  
[IBomTableAnnotation::Expand Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~Expand.md)  
[IBomTableAnnotation::Dissolve Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~Dissolve.md)

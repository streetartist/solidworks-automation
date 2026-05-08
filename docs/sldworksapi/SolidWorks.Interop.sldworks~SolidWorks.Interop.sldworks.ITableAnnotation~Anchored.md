# Anchored Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Anchored`

Gets or sets whether this table is attached to its anchor.
Gets or sets whether this table is attached to its anchor.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Anchored As System.Boolean
```

```

Dim instance As ITableAnnotation
Dim value As System.Boolean
 
instance.Anchored = value
 
value = instance.Anchored
```

```

System.bool Anchored {get; set;}
```

```

property System.bool Anchored {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the table is attached to the anchor, false if not

Remarks

If setting this property to TRUE, then the table origin is snapped to the anchor point, according to the anchor type of this table. Use:

- [ITableAnnotation::AnchorType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~AnchorType.md) to determine where the origin is on the table.
- [IAnnotation::GetPosition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPosition.md) to determine the position of the table.

If the drawing sheet format does not contain an anchor point for this type of table, then attempting to attach the table to the anchor point has no effect.

Example

[Get and Set Table Anchor of Hole Table (C#)](Get_and_Set_Table_Anchor_of_Hole_Table_Example_CSharp.htm)  
[Get and Set Table Anchor of Hole Table (VB.NET)](Get_and_Set_Table_Anchor_of_Hole_Table_Example_VBNET.htm)  
[Get and Set Table Anchor of Hole Table (VBA)](Get_and_Set_Table_Anchor_of_Hole_Table_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)  
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.md)  
[IAnnotation::SetPosition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetPosition.md)  
[ITableAnnotation::AnchorType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~AnchorType.md)

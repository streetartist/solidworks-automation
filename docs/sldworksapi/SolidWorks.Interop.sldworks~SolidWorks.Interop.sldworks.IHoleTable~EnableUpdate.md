# EnableUpdate Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~EnableUpdate`

Gets or sets whether to update hole table and graphics after changing hole tags.
Gets or sets whether to update hole table and graphics after [changing hole tags](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~HoleTag.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EnableUpdate As System.Boolean
```

```

Dim instance As IHoleTable
Dim value As System.Boolean
 
instance.EnableUpdate = value
 
value = instance.EnableUpdate
```

```

System.bool EnableUpdate {get; set;}
```

```

property System.bool EnableUpdate {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True updates the hole table and model view, false does not

Remarks

If you plan on changing many hole tags, then consider setting this property to false to avoid a possible degradation in performance. After changing all of the hole tags, set this property to true to update the hole table and model view.

Example

[Change Tags in Hole Table (VB.NET)](Change_Tags_in_Hole_Table_Example_VBNET.htm)  
[Change Tags in Hole Table (VBA)](Change_Tags_in_Hole_Table_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHoleTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable.md)  
[IHoleTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable_members.md)  
[IHoleTable::HoleTagsVisible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~HoleTagsVisible.md)  
[IHoleTable::TagStyle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~TagStyle.md)  
[IHoleTable::HoleTag Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~HoleTag.md)

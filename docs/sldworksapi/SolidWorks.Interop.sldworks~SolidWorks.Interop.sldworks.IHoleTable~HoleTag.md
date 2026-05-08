# HoleTag Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~HoleTag`

Gets or sets the name of the specified tag in a hole table.
Gets or sets the name of the specified tag in a hole table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property HoleTag( _
   ByVal Row As System.Integer _
) As System.String
```

```

Dim instance As IHoleTable
Dim Row As System.Integer
Dim value As System.String
 
instance.HoleTag(Row) = value
 
value = instance.HoleTag(Row)
```

```

System.string HoleTag( 
   System.int Row
) {get; set;}
```

```

property System.String^ HoleTag {
   System.String^ get(System.int Row);
   void set (System.int Row, System.String^ value);
}
```

#### Parameters

*Row*
:   0-based index of the row in which you want to change the name of the tag

#### Property Value

Tag name

Remarks

[IHoleTable::CombineTags](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~CombineTags.md) must be false for IHoleTable::HoleTag to work.

If you plan on changing many hole tags, then consider setting [IHoleTable::EnableUpdate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~EnableUpdate.md) to false to avoid a possible degradation in performance. After changing all of the hole tags, set IHoleTable::EnableUpdate to true to update the hole table and model view.

Example

[Change Tags in Hole Table (VB.NET)](Change_Tags_in_Hole_Table_Example_VBNET.htm)  
[Change Tags in Hole Table (VBA)](Change_Tags_in_Hole_Table_Example_VB.htm)  
[Change Tags in Hole Table (C#)](Change_Tags_in_Hole_Table_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHoleTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable.md)  
[IHoleTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable_members.md)  
[IHoleTable::HoleTagsVisible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~HoleTagsVisible.md)  
[IHoleTable::TagStyle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~TagStyle.md)

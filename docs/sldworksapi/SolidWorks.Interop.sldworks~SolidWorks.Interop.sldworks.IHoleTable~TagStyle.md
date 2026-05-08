# TagStyle Property (IHoleTable)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~TagStyle`

Gets or sets the tag style for this hole table.
Gets or sets the tag style for this hole table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TagStyle As System.Integer
```

```

Dim instance As IHoleTable
Dim value As System.Integer
 
instance.TagStyle = value
 
value = instance.TagStyle
```

```

System.int TagStyle {get; set;}
```

```

property System.int TagStyle {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Tag style as defined by [swHoleTableTagStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swHoleTableTagStyle_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHoleTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable.md)  
[IHoleTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable_members.md)  
[IHoleTable::CombineTags Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~CombineTags.md)  
[IHoleTable::HoleTag Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~HoleTag.md)  
[IHoleTable::HoleTagsVisible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~HoleTagsVisible.md)  
[IHoleTable::EnableUpdate Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~EnableUpdate.md)

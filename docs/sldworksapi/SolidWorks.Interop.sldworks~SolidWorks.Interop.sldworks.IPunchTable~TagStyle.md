# TagStyle Property (IPunchTable)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable~TagStyle`

Gets or sets the tag style for this punch table.
Gets or sets the tag style for this punch table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TagStyle As System.Integer
```

```

Dim instance As IPunchTable
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

Tag style as defined by [swPunchTableTagStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPunchTableTagStyle_e.html)

Example

[Insert Punch Table (VBA)](Insert_Punch_Table_Example_VB.htm)  
[Insert Punch Table (VB.NET)](Insert_Punch_Table_Example_VBNET.htm)  
[Insert Punch Table (C#)](Insert_Punch_Table_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPunchTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable.md)  
[IPunchTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable_members.md)  
[IPunch::CombineTags Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable~CombineTags.md)

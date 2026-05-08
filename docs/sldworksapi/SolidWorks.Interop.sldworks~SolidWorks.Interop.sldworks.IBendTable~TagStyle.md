# TagStyle Property (IBendTable)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable~TagStyle`

Gets and sets the tag style for this bend table.
Gets and sets the tag style for this bend table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TagStyle As System.Integer
```

```

Dim instance As IBendTable
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

Tag style as defined in [swBendTableTagStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBendTableTagStyle_e.html)

Example

[Insert Bend Table (VBA)](Insert_Bend_Table_Example_VB.htm)  
[Insert Bend Table (VB.NET)](Insert_Bend_Table_Example_VBNET.htm)  
[Insert Bend Table (C#)](Insert_Bend_Table_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBendTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable.md)  
[IBendTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable_members.md)  
[IBendTable::StartingValue Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable~StartingValue.md)

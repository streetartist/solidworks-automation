# StartingValue Property (IBendTable)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable~StartingValue`

Gets and sets the starting datum tag for this bend table.
Gets and sets the starting datum tag for this bend table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property StartingValue As System.String
```

```

Dim instance As IBendTable
Dim value As System.String
 
instance.StartingValue = value
 
value = instance.StartingValue
```

```

System.string StartingValue {get; set;}
```

```

property System.String^ StartingValue {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Starting datum tag (see **Remarks**)

Remarks

This property returns:

- Letter from A to Z, if [IBendTable::TagStyle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable~TagStyle.md) is set to [swBendTableTagStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBendTableTagStyle_e.html).swBendTable\_AlphaNumericTags.
- Positive integer, if [IBendTable::TagStyle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable~TagStyle.md) is set to [swBendTableTagStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBendTableTagStyle_e.html).swBendTable\_NumericTags.

Example

[Insert Bend Table (C#)](Insert_Bend_Table_Example_CSharp.htm)  
[Insert Bend Table (VB.NET)](Insert_Bend_Table_Example_VBNET.htm)  
[Insert Bend Table (VBA)](Insert_Bend_Table_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBendTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable.md)  
[IBendTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable_members.md)

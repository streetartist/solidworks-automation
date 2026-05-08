# CombineTags Property (IPunchTable)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable~CombineTags`

Gets or sets whether to combine tags for punches having the same Punch ID.
Gets or sets whether to combine tags for punches having the same Punch ID.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CombineTags As System.Boolean
```

```

Dim instance As IPunchTable
Dim value As System.Boolean
 
instance.CombineTags = value
 
value = instance.CombineTags
```

```

System.bool CombineTags {get; set;}
```

```

property System.bool CombineTags {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to combine tags, false to not (see **Remarks**)

Example

If this property is set to false, the punch table looks like this:

| TAG | PUNCH ID | X LOCATION | Y LOCATION | ANGLE | QUANTITY |
| --- | --- | --- | --- | --- | --- |
| A1 | 135 | 107 | 300 | 90 | 1 |
| A2 | 135 | 200 | 150 | 90 | 1 |
| A3 | 135 | 300 | 200 | 90 | 1 |

If this property is set to true, the punch table looks like this:

| TAG | PUNCH ID | QUANTITY |
| --- | --- | --- |
| A | 135 | 3 |

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
[IPunch::TagStyle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable~TagStyle.md)  
[IPunchTable::CombineSameSize Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable~CombineSameSize.md)

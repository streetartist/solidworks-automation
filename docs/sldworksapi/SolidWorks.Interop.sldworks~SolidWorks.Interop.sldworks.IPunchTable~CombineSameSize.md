# CombineSameSize Property (IPunchTable)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable~CombineSameSize`

Gets or sets whether to merge Punch ID column cells that have the same contents.
Gets or sets whether to merge Punch ID column cells that have the same contents.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CombineSameSize As System.Boolean
```

```

Dim instance As IPunchTable
Dim value As System.Boolean
 
instance.CombineSameSize = value
 
value = instance.CombineSameSize
```

```

System.bool CombineSameSize {get; set;}
```

```

property System.bool CombineSameSize {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to merge Punch ID column cells that have the same contents, false to not; only valid if [IPunchTable::CombineTags](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable~CombineTags.md) is false (see **Remarks**)

Remarks

Set this property to true to create a punch table with a PUNCH ID column that contains column cells that have been merged because they contain the same value within each tag group (e.g., A1, A2, A3).

If this property is set to false, the punch table looks like this:

| TAG | PUNCH ID | X LOCATION | Y LOCATION | ANGLE | QUANTITY |
| --- | --- | --- | --- | --- | --- |
| A1 | 135 | 107 | 300 | 90 | 1 |
| A2 | 135 | 200 | 150 | 90 | 1 |
| A3 | 135 | 300 | 200 | 90 | 1 |

If this property is set to true, the punch table looks like this:

| TAG | PUNCH ID | X LOCATION | Y LOCATION | ANGLE | QUANTITY |
| --- | --- | --- | --- | --- | --- |
| A1 | 135 | 107 | 300 | 90 | 1 |
| A2 | 200 | 150 | 90 | 1 |
| A3 | 300 | 200 | 90 | 1 |

Example

[Insert Punch Table (C#)](Insert_Punch_Table_Example_CSharp.htm)  
[Insert Punch Table (VB.NET)](Insert_Punch_Table_Example_VBNET.htm)  
[Insert Punch Table (VBA)](Insert_Punch_Table_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPunchTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable.md)  
[IPunchTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable_members.md)

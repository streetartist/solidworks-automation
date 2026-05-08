# ShowUnits Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable~ShowUnits`

Gets or sets whether to show dual dimension units in this punch table.
Gets or sets whether to show dual dimension units in this punch table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ShowUnits As System.Boolean
```

```

Dim instance As IPunchTable
Dim value As System.Boolean
 
instance.ShowUnits = value
 
value = instance.ShowUnits
```

```

System.bool ShowUnits {get; set;}
```

```

property System.bool ShowUnits {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to display dual dimension units in the punch table, false to not; valid only if [IPunchTable::DualDimensions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable~DualDimensions.md) is true

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

# DualDimensions Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable~DualDimensions`

Gets or sets whether to display dual dimensions in this punch table.
Gets or sets whether to display dual dimensions in this punch table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DualDimensions As System.Boolean
```

```

Dim instance As IPunchTable
Dim value As System.Boolean
 
instance.DualDimensions = value
 
value = instance.DualDimensions
```

```

System.bool DualDimensions {get; set;}
```

```

property System.bool DualDimensions {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to display dual dimensions, false to not

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
[IPunchTable::ShowUnits Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable~ShowUnits.md)

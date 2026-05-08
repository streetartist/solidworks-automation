# StartingValue Property (IPunchTable)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable~StartingValue`

Gets or sets the starting value for the datum tags of this punch table.
Gets or sets the starting value for the datum tags of this punch table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property StartingValue As System.String
```

```

Dim instance As IPunchTable
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

Letter from A to Z, if the template of this punch table uses letter tags; a positive integer, if it uses number tags (see **Remarks**)

Remarks

See [IView::InsertPunchTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertPunchTable.md) for more information about punch table templates.

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

# StartingValue Property (IHoleTable)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~StartingValue`

Gets or sets the starting value for the datum tags of this hole table.
Gets or sets the starting value for the datum tags of this hole table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property StartingValue As System.String
```

```

Dim instance As IHoleTable
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

A letter from A to Z, if the template of this hole table uses letter tags; a positive integer, if it uses number tags (see **Remarks**)

Remarks

See [IView::InsertHoleTable2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertHoleTable2.md) for more information about hole table templates.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHoleTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable.md)  
[IHoleTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable_members.md)  
[IHoleTable::HoleTag Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~HoleTag.md)

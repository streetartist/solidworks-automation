# EnableCellDropdownLists Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~EnableCellDropdownLists`

Gets or sets whether to enable cell drop-down lists in the design table.
Gets or sets whether to enable cell drop-down lists in the design table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EnableCellDropdownLists As System.Boolean
```

```

Dim instance As IDesignTable
Dim value As System.Boolean
 
instance.EnableCellDropdownLists = value
 
value = instance.EnableCellDropdownLists
```

```

System.bool EnableCellDropdownLists {get; set;}
```

```

property System.bool EnableCellDropdownLists {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to enable cell drop-down lists in the design table, false to disable them

Remarks

You must call:

- [IDesignTable::EditFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~EditFeature.md) before setting this property.
- [IDesignTable::UpdateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable~UpdateFeature.md) after setting this property.

Example

[Disable Cell Drop-down Lists in Design Table (C#)](Disable_Cell_Drop-down_Lists_in_Design_Table_Example_CSharp.htm)  
[Disable Cell Drop-down Lists in Design Table (VB.NET)](Disable_Cell_Drop-down_Lists_in_Design_Table_Example_VBNET.htm)  
[Disable Cell Drop-down Lists in Design Table (VBA)](Disable_Cell_Drop-down_Lists_in_Design_Table_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.md)  
[IDesignTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.md)

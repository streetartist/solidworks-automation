# DisplayAsOneItem Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~DisplayAsOneItem`

Gets or sets whether all of the configurations appear with the same item number if the BOM table contains components that have multiple configurations.
Gets or sets whether all of the configurations appear with the same item number if the BOM table contains components that have multiple configurations.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DisplayAsOneItem As System.Boolean
```

```

Dim instance As IBomFeature
Dim value As System.Boolean
 
instance.DisplayAsOneItem = value
 
value = instance.DisplayAsOneItem
```

```

System.bool DisplayAsOneItem {get; set;}
```

```

property System.bool DisplayAsOneItem {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if different configurations are displayed as the same item number, false if not

Remarks

This property corresponds to the Part Configuration Grouping **> Display as one item number** check box in the Bill of Materials PropertyManager, which displays when you create or edit a BOM table in an assembly drawing.

This property applies to top-level only BOM tables. Use [IBomFeature::TableType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~TableType.md) to determine the BOM table type.

Example

See [IBomFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.md)  
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.md)  
[IBomFeature::PartConfigurationGrouping Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~PartConfigurationGrouping.md)

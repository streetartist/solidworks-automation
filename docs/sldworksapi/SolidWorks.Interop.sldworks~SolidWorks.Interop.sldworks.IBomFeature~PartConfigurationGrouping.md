# PartConfigurationGrouping Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~PartConfigurationGrouping`

Gets and sets the part configuration grouping for this BOM table.
Gets and sets the part configuration grouping for this BOM table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PartConfigurationGrouping As System.Integer
```

```

Dim instance As IBomFeature
Dim value As System.Integer
 
instance.PartConfigurationGrouping = value
 
value = instance.PartConfigurationGrouping
```

```

System.int PartConfigurationGrouping {get; set;}
```

```

property System.int PartConfigurationGrouping {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Grouping as defined in [swPartConfigurationGroupingOption\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartConfigurationGroupingOption_e.html)

Remarks

This property corresponds to the Part Configuration Grouping section in the Bill of Materials PropertyManager, which displays when you create or edit a BOM table in an assembly drawing.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.md)  
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.md)  
[IBomTableAnnotation::GetComponents2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetComponents2.md)  
[IBomTableAnnotation::IGetComponents2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~IGetComponents2.md)  
[IBomTableAnnotation::GetComponentsCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetComponentsCount2.md)  
[IBomFeature::DisplayAsOneItem Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~DisplayAsOneItem.md)

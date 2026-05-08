# Percent Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData~Percent`

Gets or sets the percent of slot length where to place the component axis in this slot mate.
Gets or sets the percent of slot length where to place the component axis in this slot mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Percent As System.Double
```

```

Dim instance As ISlotMateFeatureData
Dim value As System.Double
 
instance.Percent = value
 
value = instance.Percent
```

```

System.double Percent {get; set;}
```

```

property System.double Percent {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Percent of slot length

Remarks

This property is valid only if [ISlotMateFeatureData::Constraint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData~Constraint.md) is set to [swSlotMateConstraintOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSlotMateConstraintOptions_e.html).swSlotMateConstraintOption\_Percent.

To change the endpoint from which the distance is measured, set [ISlotMateFeatureData::FlipDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData~FlipDirection.md) to true.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISlotMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData.md)  
[ISlotMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData_members.md)

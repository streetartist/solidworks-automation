# Constraint Property (ISlotMateFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData~Constraint`

Gets or sets how to constrain the component in the slot of this slot mate.
Gets or sets how to constrain the component in the slot of this slot mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Constraint As System.Integer
```

```

Dim instance As ISlotMateFeatureData
Dim value As System.Integer
 
instance.Constraint = value
 
value = instance.Constraint
```

```

System.int Constraint {get; set;}
```

```

property System.int Constraint {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Constraint option as defined in [swSlotMateConstraintOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSlotMateConstraintOptions_e.html)

Remarks

If this property is set to swSlotMateConstraintOptions\_e:

- swSlotMateConstraintOption\_Distance, specify the [ISlotMateFeatureData::Distance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData~Distance.md) from the end of the slot where to place the component axis.
- swSlotMateConstraintOption\_Percent, specify the distance as a [ISlotMateFeatureData::Percent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData~Percent.md) of the slot length where to place the component axis.

If this is a slot-to-slot mate, the only valid constraints are:

- swSlotMateConstraintOptions\_e.swSlotMateConstraintOption\_Free
- swSlotMateConstraintOptions\_e.swSlotMateConstraintOption\_Centered

To change the endpoint from which the distance is measured, set [ISlotMateFeatureData::FlipDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData~FlipDirection.md) to true.

Example

See the [ISlotMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISlotMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData.md)  
[ISlotMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData_members.md)

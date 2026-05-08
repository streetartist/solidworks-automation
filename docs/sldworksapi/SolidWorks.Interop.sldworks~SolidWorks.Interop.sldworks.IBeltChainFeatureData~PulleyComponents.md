# PulleyComponents Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~PulleyComponents`

Gets and sets the components in this belt/chain assembly feature.
Gets and sets the components in this belt/chain assembly feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PulleyComponents As System.Object
```

```

Dim instance As IBeltChainFeatureData
Dim value As System.Object
 
instance.PulleyComponents = value
 
value = instance.PulleyComponents
```

```

System.object PulleyComponents {get; set;}
```

```

property System.Object^ PulleyComponents {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of pulley members, e.g., cylindrical faces, axes, wheels, gears

Remarks

The array maps one-to-one with the arrays of [IBeltChainFeatureData::FlipSides](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~FlipSides.md) and [IBeltChainFeatureData::PulleyDiameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~PulleyDiameters.md).

Example

See the [IBeltChainFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBeltChainFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.md)  
[IBeltChainFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData_members.md)

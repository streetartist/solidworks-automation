# FlipSides Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~FlipSides`

Gets and sets whether to flip the belt to the other side of each pulley.
Gets and sets whether to flip the belt to the other side of each pulley.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FlipSides As System.Object
```

```

Dim instance As IBeltChainFeatureData
Dim value As System.Object
 
instance.FlipSides = value
 
value = instance.FlipSides
```

```

System.object FlipSides {get; set;}
```

```

property System.Object^ FlipSides {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of booleans; true to flip pulley sides, false to not

Remarks

The array maps one-to-one with the arrays of [IBeltChainFeatureData::PulleyComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~PulleyComponents.md) and [IBeltChainFeatureData::PulleyDiameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~PulleyDiameters.md).

Example

See the [IBeltChainFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBeltChainFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.md)  
[IBeltChainFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData_members.md)

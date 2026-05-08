# BeltThickness Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~BeltThickness`

Gets and sets the belt thickness.
Gets and sets the belt thickness.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BeltThickness As System.Double
```

```

Dim instance As IBeltChainFeatureData
Dim value As System.Double
 
instance.BeltThickness = value
 
value = instance.BeltThickness
```

```

System.double BeltThickness {get; set;}
```

```

property System.double BeltThickness {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Belt thickness

Remarks

This property is valid only if [IBeltChainFeatureData::UseBeltThickness](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~UseBeltThickness.md) is true. The belt curve is offset from the cylindrical faces of the pulleys by one half the specified belt thickness.

Example

See the [IBeltChainFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBeltChainFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.md)  
[IBeltChainFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData_members.md)

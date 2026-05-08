# ReliefRatio Property (IConvertSolidFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~ReliefRatio`

Gets or sets the bend relief ratio for this convert solid feature.
Gets or sets the bend relief ratio for this convert solid feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ReliefRatio As System.Double
```

```

Dim instance As IConvertSolidFeatureData
Dim value As System.Double
 
instance.ReliefRatio = value
 
value = instance.ReliefRatio
```

```

System.double ReliefRatio {get; set;}
```

```

property System.double ReliefRatio {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

0.05 <= Relief ratio <= 2.0

Remarks

The setter of this property is valid only if:

[IConvertSolidFeatureData::OverrideDefaultAutoReliefParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~OverrideDefaultAutoReliefParameters.md) is true

 - and -

ReliefType is Rectangular or Obround.

Relief ratio = d / part thickness,

where:

d = the width of the relief cut and the depth by which it extends past the bend region

Example

See the [IConvertSolidFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConvertSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.md)  
[IConvertSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData_members.md)

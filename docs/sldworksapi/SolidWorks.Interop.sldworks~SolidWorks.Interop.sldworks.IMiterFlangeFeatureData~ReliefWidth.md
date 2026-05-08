# ReliefWidth Property (IMiterFlangeFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~ReliefWidth`

Gets or sets the relief width for this miter flange.
Gets or sets the relief width for this miter flange.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ReliefWidth As System.Double
```

```

Dim instance As IMiterFlangeFeatureData
Dim value As System.Double
 
instance.ReliefWidth = value
 
value = instance.ReliefWidth
```

```

System.double ReliefWidth {get; set;}
```

```

property System.double ReliefWidth {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Relief width for this miter flange

Remarks

SOLIDWORKS uses this property with [IMiterFlangeFeatureData::ReliefDepth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~ReliefDepth.md) only if [IMiterMiterFlangeFeatureData::UseReliefRatio](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~UseReliefRatio.md) is false. If [IMiterMiterFlangeFeatureData::UseReliefRatio](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~UseReliefRatio.md) is True, then SOLIDWORKS uses [IMiterMiterFlangeFeatureData::ReliefRatio](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~ReliefRatio.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMiterFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData.md)  
[IMiterFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData_members.md)  
[IMiterFlangeFeatureData::ReliefType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~ReliefType.md)  
[IMiterFlangeFeatureData::UseDefaultBendRelief Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~UseDefaultBendRelief.md)

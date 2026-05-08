# Angle Property (ISplitLineFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~Angle`

Gets or sets the angle by which to project the split line feature.
Gets or sets the angle by which to project the split line feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Angle As System.Double
```

```

Dim instance As ISplitLineFeatureData
Dim value As System.Double
 
instance.Angle = value
 
value = instance.Angle
```

```

System.double Angle {get; set;}
```

```

property System.double Angle {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Angle in radians by which to project the split line feature

Remarks

This property is valid only if [ISplitLineFeatureData::GetType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~GetType.md) is set to [swSplitLineFeatureType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSplitLineFeatureType_e.html).swSplitLineFeatureType\_Draft.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISplitLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData.md)  
[ISplitLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData_members.md)  
[ISplitLineFeatureData::SplitType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~SplitType.md)

# Spacing Property (ILocalCircularPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~Spacing`

Gets or sets the distance between pattern instances in Direction 1 for this circular component pattern feature.
Gets or sets the distance between pattern instances in Direction 1 for this circular component pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Spacing As System.Double
```

```

Dim instance As ILocalCircularPatternFeatureData
Dim value As System.Double
 
instance.Spacing = value
 
value = instance.Spacing
```

```

System.double Spacing {get; set;}
```

```

property System.double Spacing {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Distance in radians between pattern instances in Direction 1

Remarks

This property is automatically set to 360 if [ILocalCircularPatternFeatureData::EqualSpacing](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~EqualSpacing.md) is set to true.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILocalCircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData.md)  
[ILocalCircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData_members.md)  
[ILocalCircularPatternFeatureData::TotalInstances Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~TotalInstances.md)  
[ILocalCircularPatternFeatureData::Spacing2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~Spacing2.md)

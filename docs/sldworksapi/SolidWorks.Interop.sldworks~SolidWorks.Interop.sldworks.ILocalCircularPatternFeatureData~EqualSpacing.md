# EqualSpacing Property (ILocalCircularPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~EqualSpacing`

Gets or sets whether to equally space the pattern instances in Direction 1 in this circular component pattern feature.
Gets or sets whether to equally space the pattern instances in Direction 1 in this circular component pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EqualSpacing As System.Boolean
```

```

Dim instance As ILocalCircularPatternFeatureData
Dim value As System.Boolean
 
instance.EqualSpacing = value
 
value = instance.EqualSpacing
```

```

System.bool EqualSpacing {get; set;}
```

```

property System.bool EqualSpacing {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to equally space the pattern instances in Direction 1, false to not

Remarks

If this property is set to true, then [ILocalCircularPatternFeatureData::Spacing](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~Spacing.md) is automatically set to 360 degrees.

Example

See the [ILocalCircularPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILocalCircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData.md)  
[ILocalCircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData_members.md)  
[ILocalCircularPatternFeatureData::EqualSpacing2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~EqualSpacing2.md)

# MinimumDistance Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData~MinimumDistance`

Gets or sets the minimum distance of this limit distance mate.
Gets or sets the minimum distance of this limit distance mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MinimumDistance As System.Double
```

```

Dim instance As IDistanceMateFeatureData
Dim value As System.Double
 
instance.MinimumDistance = value
 
value = instance.MinimumDistance
```

```

System.double MinimumDistance {get; set;}
```

```

property System.double MinimumDistance {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Minimum distance

Remarks

This property is valid only if [IDistanceMateFeatureData::IsAdvancedMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData~IsAdvancedMate.md) is set to true.

Example

See the [IDistanceMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDistanceMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData.md)  
[IDistanceMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData_members.md)  
[IDistanceMateFeatureData::Distance Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData~Distance.md)

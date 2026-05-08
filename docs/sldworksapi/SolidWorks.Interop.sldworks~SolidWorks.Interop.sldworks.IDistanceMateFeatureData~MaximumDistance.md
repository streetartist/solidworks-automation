# MaximumDistance Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData~MaximumDistance`

Gets or sets the maximum distance of this limit distance mate.
Gets or sets the maximum distance of this limit distance mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MaximumDistance As System.Double
```

```

Dim instance As IDistanceMateFeatureData
Dim value As System.Double
 
instance.MaximumDistance = value
 
value = instance.MaximumDistance
```

```

System.double MaximumDistance {get; set;}
```

```

property System.double MaximumDistance {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Maximum distance

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

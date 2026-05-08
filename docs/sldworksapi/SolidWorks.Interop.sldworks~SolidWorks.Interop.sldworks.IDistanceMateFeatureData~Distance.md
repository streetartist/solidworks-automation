# Distance Property (IDistanceMateFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData~Distance`

Gets or sets the distance of this distance mate.
Gets or sets the distance of this distance mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Distance As System.Double
```

```

Dim instance As IDistanceMateFeatureData
Dim value As System.Double
 
instance.Distance = value
 
value = instance.Distance
```

```

System.double Distance {get; set;}
```

```

property System.double Distance {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Distance between mates

Remarks

If [IDistanceMateFeatureData::IsAdvancedMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData~IsAdvancedMate.md) is true, then this property specifies the starting distance of this mate.

Example

See the [IDistanceMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDistanceMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData.md)  
[IDistanceMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData_members.md)  
[IDistanceMateFeatureData::MaximumDistance Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData~MaximumDistance.md)  
[IDistanceMateFeatureData::MinimumDistance Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData~MinimumDistance.md)

# Material Property (IHoleSeriesFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~Material`

Obsolete. Superseded by IHoleSeriesFeatureData2::Material.
Obsolete. Superseded by [IHoleSeriesFeatureData2::Material](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~Material.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Material As System.String
```

```

Dim instance As IHoleSeriesFeatureData
Dim value As System.String
 
value = instance.Material
```

```

System.string Material {get;}
```

```

property System.String^ Material {
   System.String^ get();
}
```

#### Property Value

Bolt material name

Remarks

The material value is not available in the SOLIDWORKS Toolbox database.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHoleSeriesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData.md)  
[IHoleSeriesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData_members.md)  
[IHoleSeriesFeatureData::BoltDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~BoltDiameter.md)  
[IHoleSeriesFeatureData::BoltHeadDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~BoltHeadDiameter.md)

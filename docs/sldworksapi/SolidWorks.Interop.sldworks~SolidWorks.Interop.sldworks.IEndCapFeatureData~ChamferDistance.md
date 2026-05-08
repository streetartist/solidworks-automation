# ChamferDistance Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData~ChamferDistance`

Gets or sets the chamfer distance or fillet radius of the corner of this end-cap feature.
Gets or sets the chamfer distance or fillet radius of the corner of this end-cap feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ChamferDistance As System.Double
```

```

Dim instance As IEndCapFeatureData
Dim value As System.Double
 
instance.ChamferDistance = value
 
value = instance.ChamferDistance
```

```

System.double ChamferDistance {get; set;}
```

```

property System.double ChamferDistance {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Chamfer distance if [IEndCapFeatureData::UseChamferCorners](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData~UseChamferCorners.md) is true; fillet radius if IEndCapFeatureData::UseChamferCorners is false

Remarks

This property is valid only if [IEndCapFeatureData::UseCornerTreatment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData~UseCornerTreatment.md) is true.

Example

See the [IEndCapFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEndCapFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData.md)  
[IEndCapFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData_members.md)

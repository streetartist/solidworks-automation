# PlanarTrimOption Property (ISimpleCornerTreatmentFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleCornerTreatmentFeatureData~PlanarTrimOption`

Gets and sets the planar trim option for this simple corner treatment feature.
Gets and sets the planar trim option for this simple corner treatment feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PlanarTrimOption As System.Integer
```

```

Dim instance As ISimpleCornerTreatmentFeatureData
Dim value As System.Integer
 
instance.PlanarTrimOption = value
 
value = instance.PlanarTrimOption
```

```

System.int PlanarTrimOption {get; set;}
```

```

property System.int PlanarTrimOption {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Planar trim option as defined by [swCornerTreatmentPlanarTrimOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerTreatmentPlanarTrimOptions_e.html)

Remarks

This property is valid only if:

- [ISimpleCornerTreatmentFeatureData::CornerTreatmentTrimType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleCornerTreatmentFeatureData~CornerTreatmentTrimType.md) is set to [swCornerTreatmentTrimType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerTreatmentTrimType_e.html).swCornerTreatmentTrim\_PlanarTrim.

   -and -

- ISimpleCornerTreatmentFeatureData::PlanarTrimToolType is set to [swCornerTreatmentPlanarTrimToolType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerTreatmentPlanarTrimToolType_e.html).swCornerTreatmentPlanarTrimTool\_Automatic.

Example

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimpleCornerTreatmentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleCornerTreatmentFeatureData.md)  
[ISimpleCornerTreatmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleCornerTreatmentFeatureData_members.md)

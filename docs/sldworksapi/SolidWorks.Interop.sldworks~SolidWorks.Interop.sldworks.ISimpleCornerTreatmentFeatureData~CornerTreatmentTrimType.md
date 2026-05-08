# CornerTreatmentTrimType Property (ISimpleCornerTreatmentFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleCornerTreatmentFeatureData~CornerTreatmentTrimType`

Gets and sets the corner treatment trim type for this simple corner treatment feature.
Gets and sets the corner treatment trim type for this simple corner treatment feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CornerTreatmentTrimType As System.Integer
```

```

Dim instance As ISimpleCornerTreatmentFeatureData
Dim value As System.Integer
 
instance.CornerTreatmentTrimType = value
 
value = instance.CornerTreatmentTrimType
```

```

System.int CornerTreatmentTrimType {get; set;}
```

```

property System.int CornerTreatmentTrimType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Corner treatment trim type as defined by [swCornerTreatmentTrimType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerTreatmentTrimType_e.html)

Remarks

This property is valid only for swCornerTreatmentTrimType\_e.:

- swCornerTreatmentTrim\_BodyTrim
- swCornerTreatmentTrim\_PlanarTrim

Example

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimpleCornerTreatmentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleCornerTreatmentFeatureData.md)  
[ISimpleCornerTreatmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleCornerTreatmentFeatureData_members.md)

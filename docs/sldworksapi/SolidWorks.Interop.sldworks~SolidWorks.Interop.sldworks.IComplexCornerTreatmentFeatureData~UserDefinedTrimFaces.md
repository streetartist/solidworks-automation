# UserDefinedTrimFaces Property (IComplexCornerTreatmentFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData~UserDefinedTrimFaces`

Gets and sets the user-defined trim faces for this complex corner treatment feature.
Gets and sets the user-defined trim faces for this complex corner treatment feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UserDefinedTrimFaces As System.Object
```

```

Dim instance As IComplexCornerTreatmentFeatureData
Dim value As System.Object
 
instance.UserDefinedTrimFaces = value
 
value = instance.UserDefinedTrimFaces
```

```

System.object UserDefinedTrimFaces {get; set;}
```

```

property System.Object^ UserDefinedTrimFaces {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

Remarks

This property is valid only if [IComplexCornerTreatmentFeatureData::PlanarTrimToolType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData~PlanarTrimToolType.md) is set to [swCornerTreatmentPlanarTrimToolType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerTreatmentPlanarTrimToolType_e.html).CornerTreatmentPlanarTrimTool\_UserDefined.

Example

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComplexCornerTreatmentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData.md)  
[IComplexCornerTreatmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData_members.md)

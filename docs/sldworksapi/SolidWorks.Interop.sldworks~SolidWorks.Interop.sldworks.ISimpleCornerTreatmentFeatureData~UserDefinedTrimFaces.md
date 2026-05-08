# UserDefinedTrimFaces Property (ISimpleCornerTreatmentFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleCornerTreatmentFeatureData~UserDefinedTrimFaces`

Gets and sets the user-defined trim faces for this simple corner treatment feature.
Gets and sets the user-defined trim faces for this simple corner treatment feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UserDefinedTrimFaces As System.Object
```

```

Dim instance As ISimpleCornerTreatmentFeatureData
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

This property is valid only if [ISimpleCornerTreatmentFeatureData::PlanarTrimToolType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleCornerTreatmentFeatureData~PlanarTrimToolType.md) is set to [swCornerTreatmentPlanarTriimToolType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerTreatmentPlanarTrimToolType_e.html).CornerTreatmentPlanarTrimTool\_UserDefined.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimpleCornerTreatmentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleCornerTreatmentFeatureData.md)  
[ISimpleCornerTreatmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleCornerTreatmentFeatureData_members.md)

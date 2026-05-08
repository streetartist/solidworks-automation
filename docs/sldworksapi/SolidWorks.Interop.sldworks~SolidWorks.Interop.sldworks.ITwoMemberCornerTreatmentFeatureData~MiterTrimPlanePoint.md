# MiterTrimPlanePoint Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITwoMemberCornerTreatmentFeatureData~MiterTrimPlanePoint`

Gets and sets the point through which to create the miter trim for this two member corner treatment feature.
Gets and sets the point through which to create the miter trim for this two member corner treatment feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MiterTrimPlanePoint As System.Object
```

```

Dim instance As ITwoMemberCornerTreatmentFeatureData
Dim value As System.Object
 
instance.MiterTrimPlanePoint = value
 
value = instance.MiterTrimPlanePoint
```

```

System.object MiterTrimPlanePoint {get; set;}
```

```

property System.Object^ MiterTrimPlanePoint {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

[IRefPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPoint.md)

Remarks

This property is valid only if [ITwoMemberCornerTreatmentFeatureData::CornerTreatmentTrimType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITwoMemberCornerTreatmentFeatureData~CornerTreatmentTrimType.md) is set to [swCornerTreatmentTrimType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerTreatmentTrimType_e.html).swCornerTreatmentTrim\_MiterTrim.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITwoMemberCornerTreatmentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITwoMemberCornerTreatmentFeatureData.md)  
[ITwoMemberCornerTreatmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITwoMemberCornerTreatmentFeatureData_members.md)

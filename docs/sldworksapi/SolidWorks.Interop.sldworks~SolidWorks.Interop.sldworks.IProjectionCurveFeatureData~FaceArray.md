# FaceArray Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData~FaceArray`

Gets or sets the target faces for this projected curve.
Gets or sets the target faces for this projected curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FaceArray As System.Object
```

```

Dim instance As IProjectionCurveFeatureData
Dim value As System.Object
 
instance.FaceArray = value
 
value = instance.FaceArray
```

```

System.object FaceArray {get; set;}
```

```

property System.Object^ FaceArray {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of faces that describe the projected curve

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IProjectionCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData.md)  
[IProjectionCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData_members.md)  
[IProjectionCurveFeatureData::GetFaceArrayCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData~GetFaceArrayCount.md)  
[IProjectionCurveFeatureData::IGetFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData~IGetFaceArray.md)  
[IProjectionCurveFeatureData::ISetFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData~ISetFaceArray.md)  
[IProjectionCurveFeatureData::Reverse Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData~Reverse.md)

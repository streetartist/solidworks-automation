# IGetFaceArray Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData~IGetFaceArray`

Gets a list of target faces for the projected curve.
Gets a list of target faces for the projected curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetFaceArray( _
   ByVal FaceCount As System.Integer _
) As System.Object
```

```

Dim instance As IProjectionCurveFeatureData
Dim FaceCount As System.Integer
Dim value As System.Object
 
value = instance.IGetFaceArray(FaceCount)
```

```

System.object IGetFaceArray( 
   System.int FaceCount
)
```

```

System.Object^ IGetFaceArray( 
   System.int FaceCount
) 
```

#### Parameters

*FaceCount*
:   Number of target faces

#### Return Value

- in-process, unmanaged C++: Pointer to an array of target faces of size FaceCount

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [IProjectionCurveFeatureData::GetFaceArrayCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData~GetFaceArrayCount.md) before calling this method to get the value of FaceCount.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IProjectionCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData.md)  
[IProjectionCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData_members.md)  
[IProjectionCurveFeatureData::ISetFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData~ISetFaceArray.md)  
[IProjectionCurveFeatureData::FaceArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData~FaceArray.md)

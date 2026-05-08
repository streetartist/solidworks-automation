# ISetFaceArray Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData~ISetFaceArray`

Sets the target faces for the projected curve.
Sets the target faces for the projected curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetFaceArray( _
   ByVal FaceCount As System.Integer, _
   ByRef ArrayDataIn As System.Object _
) 
```

```

Dim instance As IProjectionCurveFeatureData
Dim FaceCount As System.Integer
Dim ArrayDataIn As System.Object
 
instance.ISetFaceArray(FaceCount, ArrayDataIn)
```

```

void ISetFaceArray( 
   System.int FaceCount,
   ref System.object ArrayDataIn
)
```

```

void ISetFaceArray( 
   System.int FaceCount,
   System.Object^% ArrayDataIn
) 
```

#### Parameters

*FaceCount*
:   Number of target faces

*ArrayDataIn*
:   - in-process, unmanaged C++: Pointer to an array of target faces of size FaceCount

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

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
[IProjectionCurveFeatureData::FaceArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData~FaceArray.md)

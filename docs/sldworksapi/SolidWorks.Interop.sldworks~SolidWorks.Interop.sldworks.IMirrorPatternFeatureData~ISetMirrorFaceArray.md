# ISetMirrorFaceArray Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~ISetMirrorFaceArray`

Sets the faces to mirror.
Sets the faces to mirror.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetMirrorFaceArray( _
   ByVal FaceCount As System.Integer, _
   ByRef ArrayDataIn As System.Object _
) 
```

```

Dim instance As IMirrorPatternFeatureData
Dim FaceCount As System.Integer
Dim ArrayDataIn As System.Object
 
instance.ISetMirrorFaceArray(FaceCount, ArrayDataIn)
```

```

void ISetMirrorFaceArray( 
   System.int FaceCount,
   ref System.object ArrayDataIn
)
```

```

void ISetMirrorFaceArray( 
   System.int FaceCount,
   System.Object^% ArrayDataIn
) 
```

#### Parameters

*FaceCount*
:   Number of faces

*ArrayDataIn*
:   - in-process, unmanaged C++: Pointer to an array of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) of size FaceCount

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMirrorPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData.md)  
[IMirrorPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData_members.md)  
[IMirrorPatternFeatureData::GetMirrorFaceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~GetMirrorFaceCount.md)  
[IMirrorPatternFeatureData::IGetMirrorFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~IGetMirrorFaceArray.md)  
[IMirrorPatternFeatureData::MirrorFaceArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~MirrorFaceArray.md)

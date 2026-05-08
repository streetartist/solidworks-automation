# AddAGroupOfFaces Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData~AddAGroupOfFaces`

Obsolete. See ISMNormalCutFeatureData2.
Obsolete. See [ISMNormalCutFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub AddAGroupOfFaces( _
   ByVal FaceArray As System.Object, _
   ByRef Error As System.Integer _
) 
```

```

Dim instance As ISMNormalCutFeatureData
Dim FaceArray As System.Object
Dim Error As System.Integer
 
instance.AddAGroupOfFaces(FaceArray, Error)
```

```

void AddAGroupOfFaces( 
   System.object FaceArray,
   out System.int Error
)
```

```

void AddAGroupOfFaces( 
   System.Object^ FaceArray,
   [Out] System.int Error
) 
```

#### Parameters

*FaceArray*
:   Array of cut-extrude [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

*Error*
:   Error code as defined in [swSMNormalCutError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSMNormalCutError_e.html)

Remarks

FaceArray contains the non-normal side walls of a cut in a sheet metal part.

Example

See the [IFeatureManager::AddSMNormalCutType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~AddSMNormalCutType.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISMNormalCutFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData.md)  
[ISMNormalCutFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData_members.md)  
[ISMNormalCutFeatureData::RemoveAGroupOfFaces Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData~RemoveAGroupOfFaces.md)

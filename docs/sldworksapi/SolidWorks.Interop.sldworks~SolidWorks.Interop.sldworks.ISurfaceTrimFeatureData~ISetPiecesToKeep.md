# ISetPiecesToKeep Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData~ISetPiecesToKeep`

Sets the pieces to keep for this surface trim feature.
Sets the pieces to keep for this surface trim feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetPiecesToKeep( _
   ByVal Count As System.Integer, _
   ByRef BodyArr As Body2 _
) 
```

```

Dim instance As ISurfaceTrimFeatureData
Dim Count As System.Integer
Dim BodyArr As Body2
 
instance.ISetPiecesToKeep(Count, BodyArr)
```

```

void ISetPiecesToKeep( 
   System.int Count,
   ref Body2 BodyArr
)
```

```

void ISetPiecesToKeep( 
   System.int Count,
   Body2^% BodyArr
) 
```

#### Parameters

*Count*
:   Number of pieces to keep

*BodyArr*
:   - in-process, unmanaged C++: Pointer to an array of pieces to keep of size Count

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfaceTrimFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData.md)  
[ISurfaceTrimFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData_members.md)  
[ISurfaceTrimFeatureData::GetPiecesToKeepCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData~GetPiecesToKeepCount.md)  
[ISurfaceTrimFeatureData::IGetPiecesToKeep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData~IGetPiecesToKeep.md)  
[ISurfaceTrimFeatureData::PiecesToKeep Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData~PiecesToKeep.md)

# ISetBends Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData~ISetBends`

Sets the bend features for this fold feature.
Sets the bend features for this fold feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetBends( _
   ByVal FaceCount As System.Integer, _
   ByRef FaceArray As System.Object _
) 
```

```

Dim instance As IFoldsFeatureData
Dim FaceCount As System.Integer
Dim FaceArray As System.Object
 
instance.ISetBends(FaceCount, FaceArray)
```

```

void ISetBends( 
   System.int FaceCount,
   ref System.object FaceArray
)
```

```

void ISetBends( 
   System.int FaceCount,
   System.Object^% FaceArray
) 
```

#### Parameters

*FaceCount*
:   Number of faces describing the bends

*FaceArray*
:   - in-process, unmanaged C++: Pointer to an array of bend [features](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) that describe the bends that belong to this folds feature

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFoldsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData.md)  
[IFoldsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData_members.md)  
[IFoldsFeatureData::IGetBends Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData~IGetBends.md)  
[IFoldsFeatureData::IGetBendsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData~IGetBendsCount.md)  
[IFoldsFeatureData::Bends Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData~Bends.md)

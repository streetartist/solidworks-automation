# ISetSplitTools Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~ISetSplitTools`

Sets the tools used to make the split.
Sets the tools used to make the split.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetSplitTools( _
   ByVal Count As System.Integer, _
   ByRef DispArr As System.Object _
) 
```

```

Dim instance As ISplitLineFeatureData
Dim Count As System.Integer
Dim DispArr As System.Object
 
instance.ISetSplitTools(Count, DispArr)
```

```

void ISetSplitTools( 
   System.int Count,
   ref System.object DispArr
)
```

```

void ISetSplitTools( 
   System.int Count,
   System.Object^% DispArr
) 
```

#### Parameters

*Count*
:   Number of tools used to make the split

*DispArr*
:   - in-process, unmanaged C++: Pointer to an array of tools used to make the  split (see **Remarks**)

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

[Reference planes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md), [planar model faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), and [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) are valid tools for a split.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISplitLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData.md)  
[ISplitLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData_members.md)  
[ISplitLineFeatureData::GetSplitToolsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~GetSplitToolsCount.md)  
[ISplitLineFeatureData::IGetSplitTools Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~IGetSplitTools.md)  
[ISplitLineFeatureData::SplitTools Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~SplitTools.md)

# IGetSplitBodies Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~IGetSplitBodies`

Gets the split bodies for this Split feature.
Gets the split bodies for this Split feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IGetSplitBodies( _
   ByVal Count As System.Integer, _
   ByRef BodyArr As Body2, _
   ByRef PathArr As System.String, _
   ByRef FlagArr As System.Boolean _
) 
```

```

Dim instance As ISplitBodyFeatureData
Dim Count As System.Integer
Dim BodyArr As Body2
Dim PathArr As System.String
Dim FlagArr As System.Boolean
 
instance.IGetSplitBodies(Count, BodyArr, PathArr, FlagArr)
```

```

void IGetSplitBodies( 
   System.int Count,
   out Body2 BodyArr,
   out System.string PathArr,
   out System.bool FlagArr
)
```

```

void IGetSplitBodies( 
   System.int Count,
   [Out] Body2^ BodyArr,
   [Out] System.String^ PathArr,
   [Out] System.bool FlagArr
) 
```

#### Parameters

*Count*
:   Number of split bodies (see **Remarks**)

*BodyArr*
:   - in-process, unmanaged C++: Pointer to an array of split [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

*PathArr*
:   - in-process, unmanaged C++: Pointer to an array of paths and file names of part documents to which to save BodyArr bodies

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

*FlagArr*
:   - in-process, unmanaged C++: Pointer to an array of booleans indicating whether corresponding BodyArr body is removed from the original part; true if removed, false if not
    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [ISplitBodyFeatureData::GetSplitBodiesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~GetSplitBodiesCount.md) to determine the value for Count. Call this method before calling [ISplitBodyFeatureData::SetSplitBodies2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~SetSplitBodies2.md) to change which split bodies to include in this Split feature.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISplitBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData.md)  
[ISplitBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData_members.md)  
[ISplitBodyFeatureData::GetSplitBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~GetSplitBodies.md)  
[IFeatureManager::PreSplitBody2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PreSplitBody2.md)  
[IFeatureManager::PostSplitBody Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PostSplitBody.md)

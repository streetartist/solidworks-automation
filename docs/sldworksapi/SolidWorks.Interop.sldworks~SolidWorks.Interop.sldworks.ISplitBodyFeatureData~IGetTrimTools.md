# IGetTrimTools Method (ISplitBodyFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~IGetTrimTools`

Gets the trimming surfaces used as trim tools in this Split feature.
Gets the trimming surfaces used as trim tools in this Split feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetTrimTools( _
   ByVal Count As System.Integer _
) As System.Object
```

```

Dim instance As ISplitBodyFeatureData
Dim Count As System.Integer
Dim value As System.Object
 
value = instance.IGetTrimTools(Count)
```

```

System.object IGetTrimTools( 
   System.int Count
)
```

```

System.Object^ IGetTrimTools( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of trimming surfaces used as trim tools in this Split feature

#### Return Value

- in-process, unmanaged C++: Pointer to an array of trimming surfaces used as trim tools:
  - Planar and non-planar faces
  - Reference planes
  - Reference surfaces
  - Sketches
- VBA, VB.NET, C#, and C++/CLI: Not supported
- See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [ISplitBodyFeatureData::GetTrimToolsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~GetTrimToolsCount.md) before calling this method to determine the size of the array.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISplitBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData.md)  
[ISplitBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData_members.md)  
[ISplitBodyFeatureData::TrimTools Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~TrimTools.md)  
[ISplitBodyFeatureData::ISetTrimTools Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~ISetTrimTools.md)

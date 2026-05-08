# IGetTrimTools Method (ISurfaceTrimFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData~IGetTrimTools`

Gets the trim tools for this surface trim feature.
Gets the trim tools for this surface trim feature.

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

Dim instance As ISurfaceTrimFeatureData
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
:   Number of trim tools

#### Return Value

- in-process, unmanaged C++: Pointer to an array of trim tools of size Count

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [ISurfaceTrimFeatureData::GetTrimToolsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData~GetTrimToolsCount.md) before calling this method to get the value for Count.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfaceTrimFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData.md)  
[ISurfaceTrimFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData_members.md)  
[ISurfaceTrimFeatureData::ISetTrimTools Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData~ISetTrimTools.md)  
[ISurfaceTrimFeatureData::TrimTools Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData~TrimTools.md)

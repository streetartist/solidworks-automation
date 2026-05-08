# IGetEntitiesToSplit Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~IGetEntitiesToSplit`

Gets the entities that are used to split a face.
Gets the entities that are used to split a face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetEntitiesToSplit( _
   ByVal Count As System.Integer, _
   ByRef TypeArr As System.Integer _
) As System.Object
```

```

Dim instance As IPartingLineFeatureData
Dim Count As System.Integer
Dim TypeArr As System.Integer
Dim value As System.Object
 
value = instance.IGetEntitiesToSplit(Count, TypeArr)
```

```

System.object IGetEntitiesToSplit( 
   System.int Count,
   out System.int TypeArr
)
```

```

System.Object^ IGetEntitiesToSplit( 
   System.int Count,
   [Out] System.int TypeArr
) 
```

#### Parameters

*Count*
:   Number of entities

*TypeArr*
:   - in-process, unmanaged C++: Pointer to an array of these entities as defined in [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html):

      - swSelVERTICES
      - swSelSKETCHSEGS
    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [vertices](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md) or [sketch segments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md)

- VBA, VB.NET, C#, and C++/CLI: Not supported

Remarks

The resulting edges are added to the parting line feature.

Call [IPartingLineFeatureData::GetEntitiesToSplitCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~GetEntitiesToSplitCount.md) before this method.

When two vertices are specified, then an edge is created between them for the parting line feature.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartingLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData.md)  
[IPartingLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData_members.md)  
[IPartingLineFeatureData::GetEntitiesToSplit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~GetEntitiesToSplit.md)  
[IPartingLineFeatureData::ISetEntitiesToSplit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~ISetEntitiesToSplit.md)  
[IPartingLineFeatureData::SetEntitiesToSplit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~SetEntitiesToSplit.md)  
[IPartingLineFeatureData::SplitFaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~SplitFaces.md)  
[IPartingLineFeatureData::SplitFacesOption Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~SplitFacesOption.md)

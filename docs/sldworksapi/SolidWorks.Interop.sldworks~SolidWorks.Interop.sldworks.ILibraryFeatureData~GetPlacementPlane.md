# GetPlacementPlane Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetPlacementPlane`

Obsolete. Superseded by ILibraryFeatureData::GetPlacementPlane2.
Obsolete. Superseded by [ILibraryFeatureData::GetPlacementPlane2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetPlacementPlane2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPlacementPlane( _
   ByRef Type As System.Integer _
) As System.Object
```

```

Dim instance As ILibraryFeatureData
Dim Type As System.Integer
Dim value As System.Object
 
value = instance.GetPlacementPlane(Type)
```

```

System.object GetPlacementPlane( 
   out System.int Type
)
```

```

System.Object^ GetPlacementPlane( 
   [Out] System.int Type
) 
```

#### Parameters

*Type*
:   Placement type as defined in [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

#### Return Value

[Face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) or [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md)

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Example

[Get Library Feature Data (VBA)](Get_Library_Feature_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILibraryFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.md)  
[ILibraryFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData_members.md)  
[ILibraryFeatureData::SetPlacementPlane Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~SetPlacementPlane.md)

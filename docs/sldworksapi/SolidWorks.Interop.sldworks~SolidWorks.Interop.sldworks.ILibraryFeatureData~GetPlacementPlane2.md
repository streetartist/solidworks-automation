# GetPlacementPlane2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetPlacementPlane2`

Gets the face or plane on which the library feature was placed.
Gets the face or plane on which the library feature was placed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPlacementPlane2( _
   ByVal Scope As System.Integer, _
   ByRef Type As System.Integer _
) As System.Object
```

```

Dim instance As ILibraryFeatureData
Dim Scope As System.Integer
Dim Type As System.Integer
Dim value As System.Object
 
value = instance.GetPlacementPlane2(Scope, Type)
```

```

System.object GetPlacementPlane2( 
   System.int Scope,
   out System.int Type
)
```

```

System.Object^ GetPlacementPlane2( 
   System.int Scope,
   [Out] System.int Type
) 
```

#### Parameters

*Scope*
:   Placement scope as defined in [swLibFeatureData\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLibFeatureData_e.html)

*Type*
:   Placement type as defined in [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

#### Return Value

[Face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) or [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md)

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Example

[Get Library Feature Data (VBA)](Get_Library_Feature_Data_Example_VB.htm)  
[Get Library Feature Data (VB.NET)](Get_Library_Feature_Data_Example_VBNET.htm)  
[Get Library Feature Data (C#)](Get_Library_Feature_Data_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILibraryFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.md)  
[ILibraryFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData_members.md)  
[ILibraryFeatureData::SetPlacementPlane Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~SetPlacementPlane.md)

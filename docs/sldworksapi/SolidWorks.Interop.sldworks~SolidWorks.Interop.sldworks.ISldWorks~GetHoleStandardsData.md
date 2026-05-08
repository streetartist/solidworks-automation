# GetHoleStandardsData Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetHoleStandardsData`

Gets the hole standards for the specified hole type.
Gets the hole standards for the specified hole type.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetHoleStandardsData( _
   ByVal HoleTypeID As System.Integer _
) As System.Object
```

```

Dim instance As ISldWorks
Dim HoleTypeID As System.Integer
Dim value As System.Object
 
value = instance.GetHoleStandardsData(HoleTypeID)
```

```

System.object GetHoleStandardsData( 
   System.int HoleTypeID
)
```

```

System.Object^ GetHoleStandardsData( 
   System.int HoleTypeID
) 
```

#### Parameters

*HoleTypeID*
:   Hole Wizard hole type as defined in [swWzdGeneralHoleTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swWzdGeneralHoleTypes_e.html)

#### Return Value

[IHoleStandardsData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData.md); null if HoleTypeID is 5 (swWzdLegacy)

Example

[Get Hole Standards Data (VBA)](Get_Wizard_Hole_Standards_Data_Example_VB.htm)  
[Get Hole Standards Data (C#)](Get_Wizard_Hole_Standards_Data_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[IHoleDataTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable.md)

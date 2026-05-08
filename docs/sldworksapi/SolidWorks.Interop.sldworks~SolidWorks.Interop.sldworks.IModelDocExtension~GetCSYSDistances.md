# GetCSYSDistances Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCSYSDistances`

Gets the specified distances between two selected coordinate systems.
Gets the specified distances between two selected coordinate systems.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCSYSDistances( _
   ByRef TotDistance As System.Double, _
   ByRef XDistance As System.Double, _
   ByRef YDistance As System.Double, _
   ByRef ZDistance As System.Double _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim TotDistance As System.Double
Dim XDistance As System.Double
Dim YDistance As System.Double
Dim ZDistance As System.Double
Dim value As System.Boolean
 
value = instance.GetCSYSDistances(TotDistance, XDistance, YDistance, ZDistance)
```

```

System.bool GetCSYSDistances( 
   out System.double TotDistance,
   out System.double XDistance,
   out System.double YDistance,
   out System.double ZDistance
)
```

```

System.bool GetCSYSDistances( 
   [Out] System.double TotDistance,
   [Out] System.double XDistance,
   [Out] System.double YDistance,
   [Out] System.double ZDistance
) 
```

#### Parameters

*TotDistance*
:   Distance between origins

*XDistance*
:   Distance between X axes

*YDistance*
:   Distance between Y axes

*ZDistance*
:   Distance between Z axes

#### Return Value

True if distances successfully retrieved, false if not

Remarks

This method corresponds to the SOLIDWORKS measure tool's calculation of distance between two coordinate systems. See **SOLIDWORKS online help > Fundamentals > Measure Tool** for more information.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::GetCSYSEulersAngularRotation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCSYSEulersAngularRotation.md)  
[IModelDocExtension::GetCSYSXYZAngularRotation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCSYSXYZAngularRotation.md)

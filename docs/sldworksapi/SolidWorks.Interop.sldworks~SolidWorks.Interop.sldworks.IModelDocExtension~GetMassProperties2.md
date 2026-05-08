# GetMassProperties2 Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetMassProperties2`

Obsolete. Superseded by IMassProperty2.
Obsolete. Superseded by [IMassProperty2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetMassProperties2( _
   ByVal Accuracy As System.Integer, _
   ByRef Status As System.Integer, _
   ByVal UseSelected As System.Boolean _
) As System.Object
```

```

Dim instance As IModelDocExtension
Dim Accuracy As System.Integer
Dim Status As System.Integer
Dim UseSelected As System.Boolean
Dim value As System.Object
 
value = instance.GetMassProperties2(Accuracy, Status, UseSelected)
```

```

System.object GetMassProperties2( 
   System.int Accuracy,
   out System.int Status,
   System.bool UseSelected
)
```

```

System.Object^ GetMassProperties2( 
   System.int Accuracy,
   [Out] System.int Status,
   System.bool UseSelected
) 
```

#### Parameters

*Accuracy*
:   - 0 = as is
    - 1 = default
    - 2 = maximum

*Status*
:   Error code as defined in [swMassPropertiesStatus\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMassPropertiesStatus_e.html)

*UseSelected*
:   True to return the mass properties of the selected components only, false to return the mass properties of the entire model, excluding suppressed components

#### Return Value

Array of size 12 (see **Remarks**)

Remarks

|  |  |
| --- | --- |
| **If this model is...** | **Then pre-select...** |
| An assembly | Components for which to get mass properties. This method returns the center of mass and moments of inertia in the coordinate system of the assembly. |
| A part | Solid bodies for which to get mass properties. The calculated origin for the returned values is based on the default coordinate system of the part. It is not based on the selected coordinate system. |

The return value is a 0-based array of doubles as follows:

[ CenterOfMassX, CenterOfMassY, CenterOfMassZ, Volume, SurfaceArea, Mass, MomXX, MomYY, MomZZ, MomXY, MomZX, MomYZ ]

Where:

- Mom*NN* = *NN-component* of the moment of inertia taken at the center of mass and aligned with the output coordinate system

You can use [ISldWorks::GetUserPreferenceDoubleValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceDoubleValue.md) and swMaterialPropertyDensity to get the density of the SOLIDWORKS part. If the user did not explicitly set the density, then SOLIDWORKS uses a value of 1.0. You can also derive the density of the body by calculating:

Density = ( *Mass* / *Volume* )

This method:

- returns values in metric units.
- supports multibody parts.

Example

[Get Mass Properties (VBA)](Get_Mass_Properties_of_ActiveDoc_Example_VB.htm)  
[Get Mass Properties (VB.NET)](Get_Mass_Properties_of_ActiveDoc_Example_VBNET.htm)  
[Get Mass Properties (C#)](Get_Mass_Properties_of_ActiveDoc_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::CreateMassProperty Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateMassProperty.md)  
[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.md)

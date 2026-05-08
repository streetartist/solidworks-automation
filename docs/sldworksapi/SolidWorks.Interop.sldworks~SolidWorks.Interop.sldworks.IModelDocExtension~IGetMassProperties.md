# IGetMassProperties Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetMassProperties`

Obsolete. Superseded by IModelDocExtension::GetMassProperties2.
Obsolete. Superseded by [IModelDocExtension::GetMassProperties2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetMassProperties2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetMassProperties( _
   ByVal Accuracy As System.Integer, _
   ByRef Status As System.Integer _
) As System.Double
```

```

Dim instance As IModelDocExtension
Dim Accuracy As System.Integer
Dim Status As System.Integer
Dim value As System.Double
 
value = instance.IGetMassProperties(Accuracy, Status)
```

```

System.double IGetMassProperties( 
   System.int Accuracy,
   out System.int Status
)
```

```

System.double IGetMassProperties( 
   System.int Accuracy,
   [Out] System.int Status
) 
```

#### Parameters

*Accuracy*
:   - 0 = as is
    - 1 = default
    - 2 = maximum

*Status*
:   Status of the mass property results as defined in [swMassPropertiesStatus\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMassPropertiesStatus_e.html)

#### Return Value

- in-process, unmanaged C++: Pointer to an array of size 13; the last element is the accuracy at which returned mass properties are calculated (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

The return value is a 0-based array of doubles as follows:

[ CenterOfMassX, CenterOfMassY, CenterOfMassZ, Volume, Area, Mass, MomXX, MomYY, MomZZ, MomXY, MomZX, MomYZ, Accuracy ]

You can use [ISldWorks::GetUserPreferenceDoubleValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceDoubleValue.md) and swMaterialPropertyDensity to get the density of the SOLIDWORKS part. If the user did not explicitly set the density, then SOLIDWORKS uses a value of 1.0. You can also derive the density of the body by calculating:

Density = ( Mass / Volume )

This method returns metric units unless explicitly specified otherwise.

|  |  |
| --- | --- |
| **If this object is...** | **Then...** |
| An assembly | - SOLIDWORKS does not include any suppressed components in the mass property analysis. See [IComponent2::GetSuppression](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSuppression.md) to determine the state of each assembly component. - This method returns the moments of inertia (MOI) about the assembly center-of-gravity coordinate system aligned with the assembly axes. |
| A part | The calculated origin for the returned values are based on the default coordinate systems of the model document. They are not based on the selected coordinate system. |

This method supports multibody parts.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::CreateMassProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateMassProperty.md)  
[IModelDocExtension::GetMassProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetMassProperties.md)  
[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.md)

# IGetMassProperties Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetMassProperties`

Gets the mass properties of this body.
Gets the mass properties of this body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetMassProperties( _
   ByVal Density As System.Double _
) As System.Double
```

```

Dim instance As IBody2
Dim Density As System.Double
Dim value As System.Double
 
value = instance.IGetMassProperties(Density)
```

```

System.double IGetMassProperties( 
   System.double Density
)
```

```

System.double IGetMassProperties( 
   System.double Density
) 
```

#### Parameters

*Density*
:   Density to use for the mass property calculations on this body

#### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

This method is intended for obtaining the mass properties of temporary objects but may also be used with the SOLIDWORKS [IBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) object that is created by the user. To get the mass properties of the SOLIDWORKS IBody2 object created by the user, you can also use [IModelDocExtension::IGetMassProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetMassProperties.md), which uses the density currently set for the body's material.

The return value is an array of doubles as follows:

Solid body

> [ CenterOfMassX, CenterOfMassY, CenterOfMassZ, Volume, Area, Mass(Volume\*density), MomXX, MomYY, MomZZ, MomXY, MomZX, MomYZ ]

Sheet body

> [ CenterOfMassX, CenterOfMassY, CenterOfMassZ, Area, Circumference, Mass(Area\*density), MomXX, MomYY, MomZZ, MomXY, MomZX, MomYZ ]

Wire body

> [ CenterOfMassX, CenterOfMassY, CenterOfMassZ, Length, 0, Mass(Length\*density), MomXX, MomYY, MomZZ, MomXY, MomZX, MomYZ ]

You can use [ISldWorks::GetUserPreferenceDoubleValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceDoubleValue.md) to get the density used by the SOLIDWORKS part. Consistent with all other SOLIDWORKS API functions, units are metric unless otherwise specified.

SOLIDWORKS returns information (such as the center of mass) in relation to where the body was created. For example, if you create a block in a part file that is centered at (0,0,0), then SOLIDWORKS returns the center of mass as (0,0,0). If you then use this part at some random location within an assembly, and the body is obtained from the assembly component object using [IComponent2::IGetBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetBody.md), then SOLIDWORKS still returns the center of mass as (0,0,0). If you need to determine the body's center of mass in relation to the assembly coordinate system, you need to multiply the component transform and the center of mass coordinates (see [IComponent2::Transform2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Transform2.md)).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::GetMassProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMassProperties.md)

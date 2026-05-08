# CreateMassProperty Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateMassProperty`

Obsolete. Superseded by IModelDocExtension::CreateMassProperty2.
Obsolete. Superseded by [IModelDocExtension::CreateMassProperty2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateMassProperty2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateMassProperty() As MassProperty
```

```

Dim instance As IModelDocExtension
Dim value As MassProperty
 
value = instance.CreateMassProperty()
```

```

MassProperty CreateMassProperty()
```

```

MassProperty^ CreateMassProperty(); 
```

#### Return Value

[IMassProperty](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.md) object

Remarks

The IMassProperty object obtains mass property information about one or more solid bodies in the document from which the IMassProperty object is obtained.

Only use solid bodies for the mass property calculations. You can specify the coordinate system about which the moments is calculated using [IMassProperty::SetCoordinateSystem](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~SetCoordinateSystem.md). If you do not use IMassProperty::SetCoordinateSystem, then the documents origin is the coordinate system.

The results of the mass property calculations vary based on whether or not [IMassProperty::AddBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~AddBodies.md) or [IMassProperty::IAddBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~IAddBodies.md) is used.  

|  |  |
| --- | --- |
| **If IMassProperty::AddBodies or IMassProperty::IAddBodies is...** | **Then...** |
| Called and bodies are specified | These bodies can either be from a subset of the documents body list or from temporary bodies.    NOTE: Each specified body should either come from the owning document or be a temporary body. If the body does not satisfy either case, then it is not used when calculating the mass properties. |
| Not called | Mass properties' calculations include all available bodies in the document.   - Part. All of the solid bodies are included in the calculations. - Assembly. All of the bodies in all of the components are used in the calculations. |

If the document from which the IMassProperty object came is an assembly, then any body from any of the child components can be used. To obtain the body, call [IComponent2::GetBodies2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetBodies2.md). Your application does not need to make a copy of the body or apply a transform to the body.

IModelDocExtension::CreateMassProperty gets the recalculated up-to-date values regardless of the [IModelDocExtension::NeedsRebuild](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~NeedsRebuild.md) status.

Example

[Insert Coordinate System at Center of Mass (VBA)](Insert_Coordinate_System_at_Center_of_Mass_Example_VB.htm)  
[Set Dimensions to Mid-Tolerance (VBA)](Set_Dimensions_to_Mid-Tolerance_Example_VB.htm)  
[Get Mass Properties of Multibody Assembly Component (VBA)](Get_Mass_Properties_of_Multibody_Assembly_Component_Example_VB.htm)  
[Get Mass Properties of Multibody Assembly Component (C#)](Get_Mass_Properties_of_Multibody_Assembly_Component_Example_CSharp.htm)  
[Get Mass Properties of Multibody Assembly Component (VB.NET)](Get_Mass_Properties_of_Multibody_Assembly_Component_Example_VBNET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::GetMassProperties2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetMassProperties2.md)

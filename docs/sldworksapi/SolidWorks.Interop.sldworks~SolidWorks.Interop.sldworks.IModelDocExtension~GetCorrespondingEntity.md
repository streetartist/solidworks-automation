# GetCorrespondingEntity Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCorrespondingEntity`

Obsolete. Superseded by IModelDocExtension::GetCorrespondingEntity2.
Obsolete. Superseded by [IModelDocExtension::GetCorrespondingEntity2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCorrespondingEntity2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCorrespondingEntity( _
   ByVal Entity As System.Object _
) As System.Object
```

```

Dim instance As IModelDocExtension
Dim Entity As System.Object
Dim value As System.Object
 
value = instance.GetCorrespondingEntity(Entity)
```

```

System.object GetCorrespondingEntity( 
   System.object Entity
)
```

```

System.Object^ GetCorrespondingEntity( 
   System.Object^ Entity
) 
```

#### Parameters

*Entity*
:   Dispatch pointer to a [vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md), [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), or [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) entity

#### Return Value

Dispatch pointer to the corresponding entity in the context of the component

Example

[Get Part for Corresponding Component (VBA)](Get_Part_for_Corresponding_Component_Example_VB.htm)  
[Open Part from Assembly (VBA)](Open_Part_from_Assembly_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IComponent2::GetCorresponding Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetCorresponding.md)  
[IComponent2::GetCorrespondingEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetCorrespondingEntity.md)  
[IComponent2::IGetCorrespondingEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetCorrespondingEntity.md)  
[IModelDocExtension::GetCorrespondingEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCorrespondingEntity.md)

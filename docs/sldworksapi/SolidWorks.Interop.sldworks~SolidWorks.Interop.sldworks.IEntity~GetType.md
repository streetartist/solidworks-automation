# GetType Method (IEntity)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~GetType`

Gets the type of the entity.
Gets the type of the entity.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetType() As System.Integer
```

```

Dim instance As IEntity
Dim value As System.Integer
 
value = instance.GetType()
```

```

System.int GetType()
```

```

System.int GetType(); 
```

#### Return Value

Type of entity as defined in [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

Remarks

You can use this method to determine the entity type and the appropriate function calls allowed for the specific type. For example, if this entity is a face, you can call [IFace2::GetArea](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetArea.md). However, you cannot call [IEdge::GetCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCurve.md) or [IEdge::IGetCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetCurve.md) because it is on [IEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) object. COM implementations can also use QueryInterface to determine the underlying interface supported by this [IEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md) object.

Example

[Get Knit Surface Data (VBA)](Get_Knit_Surface_Data_Example_VB.htm)  
[Get Mirror Solid Data (VBA)](Get_Mirror_Solid_Data_Example_VB.htm)  
[Get Component from Feature (VBA)](Get_Component_from_Feature_Example_VB.htm)  
[Get Component from Feature (VB.NET)](Get_Component_from_Feature_Example_VBNET.htm)  
[Get Component from Feature (C#)](Get_Component_from_Feature_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEntity Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md)  
[IEntity Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity_members.md)  
[IAnnotation::GetAttachedEntities2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntities2.md)  
[IAttribute::GetEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetEntity.md)  
[IAttribute::IGetEntity2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~IGetEntity2.md)  
[IAttribute::GetEntityState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetEntityState.md)  
[IComponent2::GetCorrespondingEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetCorrespondingEntity.md)  
[IComponent2::IGetCorrespondingEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetCorrespondingEntity.md)

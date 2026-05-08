# GetCorrespondingEntity2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCorrespondingEntity2`

Gets the entity in the underlying part or subassembly that corresponds to the specified entity in this assembly or drawing view.
Gets the entity in the underlying part or subassembly that corresponds to the specified entity in this assembly or drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCorrespondingEntity2( _
   ByVal Entity As System.Object _
) As System.Object
```

```

Dim instance As IModelDocExtension
Dim Entity As System.Object
Dim value As System.Object
 
value = instance.GetCorrespondingEntity2(Entity)
```

```

System.object GetCorrespondingEntity2( 
   System.object Entity
)
```

```

System.Object^ GetCorrespondingEntity2( 
   System.Object^ Entity
) 
```

#### Parameters

*Entity*
:   Dispatch pointer to a [vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md), [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), or [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) entity in this drawing view or assembly

#### Return Value

Corresponding [entity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md) in the underlying part or subassembly; null or Nothing if none found (see **Remarks**)

Remarks

To get the assembly entity corresponding to a given component entity, use [IComponent2::GetCorrespondingEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetCorrespondingEntity.md).

To get the drawing view entity corresponding to a given part or assembly entity, use [IView::GetCorrespondingEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCorrespondingEntity.md).

Example

[Get Corresponding Entities Between Parts and Drawing Views (VBA)](Get_Corresponding_Entities_Between_Parts_and_Views_Example_VB.htm)  
[Get Corresponding Entities Between Parts and Drawing Views (VB.NET)](Get_Corresponding_Entities_Between_Parts_and_Views_Example_VBNET.htm)  
[Get Corresponding Entities Between Parts and Drawing Views (C#)](Get_Corresponding_Entities_Between_Parts_and_Views_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::GetCorresponding2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCorresponding2.md)

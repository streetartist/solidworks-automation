# GetCorrespondingEntity Method (IView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCorrespondingEntity`

Gets the entity in this drawing view that corresponds to the specified part or assembly entity.
Gets the entity in this drawing view that corresponds to the specified part or assembly entity.

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

Dim instance As IView
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
:   Dispatch pointer to a [vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md), [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), or [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) entity in the part or assembly

#### Return Value

Corresponding [entity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md) in this drawing view; null or Nothing if none found

Remarks

Use [IModelDocExtension::GetCorrespondingEntity2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCorrespondingEntity2.md) to get the part entity that corresponds to a drawing view entity.

Example

[Get Corresponding Entities Between Parts and Drawing Views (VBA)](Get_Corresponding_Entities_Between_Parts_and_Views_Example_VB.htm)  
[Get Corresponding Entities Between Parts and Drawing Views (VB.NET)](Get_Corresponding_Entities_Between_Parts_and_Views_Example_VBNET.htm)  
[Get Corresponding Entities Between Parts and Drawing Views (C#)](Get_Corresponding_Entities_Between_Parts_and_Views_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetCorresponding Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCorresponding.md)

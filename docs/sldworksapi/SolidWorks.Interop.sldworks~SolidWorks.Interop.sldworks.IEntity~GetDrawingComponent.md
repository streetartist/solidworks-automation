# GetDrawingComponent Method (IEntity)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~GetDrawingComponent`

Gets the drawing component that owns this entity, if the entity is in a drawing view.
Gets the drawing component that owns this entity, if the entity is in a drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDrawingComponent( _
   ByVal View As View _
) As DrawingComponent
```

```

Dim instance As IEntity
Dim View As View
Dim value As DrawingComponent
 
value = instance.GetDrawingComponent(View)
```

```

DrawingComponent GetDrawingComponent( 
   View View
)
```

```

DrawingComponent^ GetDrawingComponent( 
   View^ View
) 
```

#### Parameters

*View*
:   Name of the drawing view in which the entity resides

#### Return Value

[IDrawingComponent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent.md) object that owns the entity

Remarks

If the drawing component is a child component of the referenced assembly, then the drawing component should be a child drawing component in the drawing component configuration in the FeatureManager design tree.

If the entity is in the view, then the drawing component is returned. If the entity is not in the view, then NULL is returned.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEntity Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md)  
[IEntity Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity_members.md)

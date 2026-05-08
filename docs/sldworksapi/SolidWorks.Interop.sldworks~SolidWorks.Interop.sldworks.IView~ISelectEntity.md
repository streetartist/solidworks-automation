# ISelectEntity Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ISelectEntity`

Selects an entity in this drawing view.
Selects an entity in this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ISelectEntity( _
   ByVal Entity As Entity, _
   ByVal AppendFlag As System.Boolean _
) As System.Boolean
```

```

Dim instance As IView
Dim Entity As Entity
Dim AppendFlag As System.Boolean
Dim value As System.Boolean
 
value = instance.ISelectEntity(Entity, AppendFlag)
```

```

System.bool ISelectEntity( 
   Entity Entity,
   System.bool AppendFlag
)
```

```

System.bool ISelectEntity( 
   Entity^ Entity,
   System.bool AppendFlag
) 
```

#### Parameters

*Entity*
:   [Entity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md)

*AppendFlag*
:   True appends the entity to the selection list, false replaces the selection list with the entity

#### Return Value

True if the entity was selected, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::SelectEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SelectEntity.md)  
[IModelDocExtension::SelectAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectAll.md)

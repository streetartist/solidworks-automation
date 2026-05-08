# SelectEntity Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SelectEntity`

Selects an entity in this drawing view.
Selects an entity in this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SelectEntity( _
   ByVal Entity As System.Object, _
   ByVal AppendFlag As System.Boolean _
) As System.Boolean
```

```

Dim instance As IView
Dim Entity As System.Object
Dim AppendFlag As System.Boolean
Dim value As System.Boolean
 
value = instance.SelectEntity(Entity, AppendFlag)
```

```

System.bool SelectEntity( 
   System.object Entity,
   System.bool AppendFlag
)
```

```

System.bool SelectEntity( 
   System.Object^ Entity,
   System.bool AppendFlag
) 
```

#### Parameters

*Entity*
:   [Entity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md)

*AppendFlag*
:   True appends the entity to the selection list, false replaces the selection list with the entity

Example

[Create Layer for Selected View (VBA)](Create_Layer_for_Selected_View_Example_VB.htm)  
[Dimension Edge in Drawing (VBA)](Dimension_Edge_in_Drawing_Example_VB.htm)  
[Select Entity in Drawing View (VBA)](Select_Entity_in_Drawing_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::ISelectEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ISelectEntity.md)  
[IModelDocExtension::SelectAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectAll.md)

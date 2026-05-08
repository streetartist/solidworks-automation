# AddComponent Method (IDragOperator)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~AddComponent`

Adds a component to the list of components to drag.
Adds a component to the list of components to drag.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddComponent( _
   ByVal PDisp As System.Object, _
   ByVal AppendFlag As System.Boolean _
) As System.Boolean
```

```

Dim instance As IDragOperator
Dim PDisp As System.Object
Dim AppendFlag As System.Boolean
Dim value As System.Boolean
 
value = instance.AddComponent(PDisp, AppendFlag)
```

```

System.bool AddComponent( 
   System.object PDisp,
   System.bool AppendFlag
)
```

```

System.bool AddComponent( 
   System.Object^ PDisp,
   System.bool AppendFlag
) 
```

#### Parameters

*PDisp*
:   Component to add to the list

*AppendFlag*
:   True to append the component to the list, false to clear the list before adding the component

#### Return Value

True if successful, false for failure; fixed components always return false (see **Remarks**)

Remarks

Components that are constrained via mates are not considered fixed.

Example

[Rotate Assembly Component on Axis Using IDragOperator::DragAsUI (VBA)](Rotate_Assembly_Component_on_Axis_Example2_VB.htm)  
[Rotate Assembly Component on Axis Using IDragOperator::DragAsUI (VB.NET)](Rotate_Assembly_Component_on_Axis_Example2_VBNET.htm)  
[Rotate Assembly Component on Axis Using IDragOperator::DragAsUI (C#)](Rotate_Assembly_Component_on_Axis_Example2_CSharp.htm)  
[Rotate Assembly Component on Axis Using IDragOperator::Drag (VBA)](Rotate_Assembly_Component_on_Axis_Example_VB.htm)  
[Rotate Assembly Component on Axis Using IDragOperator::Drag (VB.NET)](Rotate_Assembly_Component_on_Axis_Example_VBNET.htm)  
[Rotate Assembly Component on Axis Using IDragOperator::Drag (C#)](Rotate_Assembly_Component_on_Axis_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.md)  
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.md)  
[IDragOperator::IAddComponent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~IAddComponent.md)

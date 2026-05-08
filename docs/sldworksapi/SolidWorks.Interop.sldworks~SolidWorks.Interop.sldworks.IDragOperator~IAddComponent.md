# IAddComponent Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~IAddComponent`

Adds a component to the list of components to drag. Overload List " --&gt;Syntax " --&gt;
Adds a component to the list of components to drag. Overload List" -->Syntax

" -->

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IAddComponent( _
   ByVal PComp As Component2, _
   ByVal AppendFlag As System.Boolean _
) As System.Boolean
```

```

Dim instance As IDragOperator
Dim PComp As Component2
Dim AppendFlag As System.Boolean
Dim value As System.Boolean
 
value = instance.IAddComponent(PComp, AppendFlag)
```

```

System.bool IAddComponent( 
   Component2 PComp,
   System.bool AppendFlag
)
```

```

System.bool IAddComponent( 
   Component2^ PComp,
   System.bool AppendFlag
) 
```

#### Parameters

*PComp*
:   [Component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) to add to the list

*AppendFlag*
:   True to append the component to the list, false to clear the list before adding the component

#### Return Value

True if successful, false for failure; fixed components always return false (see **Remarks**)

Remarks

Components that are constrained via mates are not considered fixed.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.md)  
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.md)  
[IDragOperator::AddComponent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~AddComponent.md)

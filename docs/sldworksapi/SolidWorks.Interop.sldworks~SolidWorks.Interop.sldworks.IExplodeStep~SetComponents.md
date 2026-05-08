# SetComponents Method (IExplodeStep)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~SetComponents`

Specifies the components of this explode step.
Specifies the components of this explode step.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetComponents( _
   ByVal Components As System.Object _
) 
```

```

Dim instance As IExplodeStep
Dim Components As System.Object
 
instance.SetComponents(Components)
```

```

void SetComponents( 
   System.object Components
)
```

```

void SetComponents( 
   System.Object^ Components
) 
```

#### Parameters

*Components*
:   Array of [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)

Remarks

Modifying components during editing of this regular explode step modifies the rotational axis if:

- the rotational axis was not provided during creation,

    - and -

- the component to which it referred (the last component in the selection list) was removed during editing.

In that case, a rotational axis using the last selected component in the selection list is created.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.md)  
[IExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.md)  
[IExplodeStep::GetComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetComponents.md)

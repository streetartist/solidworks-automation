# SetReferencedDisplayStates Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetReferencedDisplayStates`

Sets the specified display state of this component to be referenced by the specified assembly display state(s).
Sets the specified display state of this component to be referenced by the specified assembly display state(s).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetReferencedDisplayStates( _
   ByVal ComponentDisplayStateName As System.String, _
   ByVal Option As System.Integer, _
   ByVal AssemblyDisplayStateNames As System.Object _
) As System.Boolean
```

```

Dim instance As IComponent2
Dim ComponentDisplayStateName As System.String
Dim Option As System.Integer
Dim AssemblyDisplayStateNames As System.Object
Dim value As System.Boolean
 
value = instance.SetReferencedDisplayStates(ComponentDisplayStateName, Option, AssemblyDisplayStateNames)
```

```

System.bool SetReferencedDisplayStates( 
   System.string ComponentDisplayStateName,
   System.int Option,
   System.object AssemblyDisplayStateNames
)
```

```

System.bool SetReferencedDisplayStates( 
   System.String^ ComponentDisplayStateName,
   System.int Option,
   System.Object^ AssemblyDisplayStateNames
) 
```

#### Parameters

*ComponentDisplayStateName*
:   Component display state name

*Option*
:   Display state option as defined in [swDisplayStateOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDisplayStateOpts_e.html)

*AssemblyDisplayStateNames*
:   Array of assembly display state names; valid only if Option is set to swDisplayStateOpts\_e.swSpecifyDisplayState

#### Return Value

True if component display state referenced successfully, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::GetReferencedDisplayStates Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetReferencedDisplayStates.md)  
[IComponent2::SetVisibilityInAsmDisplayStates Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetVisibilityInAsmDisplayStates.md)

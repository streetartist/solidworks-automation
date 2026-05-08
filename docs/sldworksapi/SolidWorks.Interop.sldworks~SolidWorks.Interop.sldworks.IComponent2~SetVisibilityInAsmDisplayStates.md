# SetVisibilityInAsmDisplayStates Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetVisibilityInAsmDisplayStates`

Sets the visibility of this component in the specified assembly display state(s).
Sets the visibility of this component in the specified assembly display state(s).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetVisibilityInAsmDisplayStates( _
   ByVal HideComponent As System.Integer, _
   ByVal Option As System.Integer, _
   ByVal AssemblyDisplayStateNames As System.Object _
) As System.Boolean
```

```

Dim instance As IComponent2
Dim HideComponent As System.Integer
Dim Option As System.Integer
Dim AssemblyDisplayStateNames As System.Object
Dim value As System.Boolean
 
value = instance.SetVisibilityInAsmDisplayStates(HideComponent, Option, AssemblyDisplayStateNames)
```

```

System.bool SetVisibilityInAsmDisplayStates( 
   System.int HideComponent,
   System.int Option,
   System.object AssemblyDisplayStateNames
)
```

```

System.bool SetVisibilityInAsmDisplayStates( 
   System.int HideComponent,
   System.int Option,
   System.Object^ AssemblyDisplayStateNames
) 
```

#### Parameters

*HideComponent*
:   Visibility as defined in [swComponentVisibilityState\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swComponentVisibilityState_e.html)

*Option*
:   Display state option as defined in [swDisplayStateOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDisplayStateOpts_e.html)

*AssemblyDisplayStateNames*
:   Array of assembly display state names; valid only if Option is set to swDisplayStateOpts\_e.swSpecifyDisplayState

#### Return Value

True if visibility successfully set, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::SetReferencedDisplayStates Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetReferencedDisplayStates.md)  
[IComponent2::GetVisibilityInAsmDisplayStates Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetVisibilityInAsmDisplayStates.md)

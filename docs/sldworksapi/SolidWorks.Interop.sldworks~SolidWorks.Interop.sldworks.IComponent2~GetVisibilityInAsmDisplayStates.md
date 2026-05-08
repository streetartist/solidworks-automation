# GetVisibilityInAsmDisplayStates Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetVisibilityInAsmDisplayStates`

Gets the visibilities of this component in the specified assembly display state(s).
Gets the visibilities of this component in the specified assembly display state(s).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetVisibilityInAsmDisplayStates( _
   ByVal AssemblyDisplayStateOption As System.Integer, _
   ByVal AssemblyDisplayStateNames As System.Object _
) As System.Object
```

```

Dim instance As IComponent2
Dim AssemblyDisplayStateOption As System.Integer
Dim AssemblyDisplayStateNames As System.Object
Dim value As System.Object
 
value = instance.GetVisibilityInAsmDisplayStates(AssemblyDisplayStateOption, AssemblyDisplayStateNames)
```

```

System.object GetVisibilityInAsmDisplayStates( 
   System.int AssemblyDisplayStateOption,
   System.object AssemblyDisplayStateNames
)
```

```

System.Object^ GetVisibilityInAsmDisplayStates( 
   System.int AssemblyDisplayStateOption,
   System.Object^ AssemblyDisplayStateNames
) 
```

#### Parameters

*AssemblyDisplayStateOption*
:   Display state option as defined in [swDisplayStateOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDisplayStateOpts_e.html)

*AssemblyDisplayStateNames*
:   Array of assembly display state names; valid only if AssemblyDisplayStateOption is set to swDisplayStateOpts\_e.swSpecifyDisplayState

#### Return Value

Array of visibilities as defined in [swComponentVisibilityState\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swComponentVisibilityState_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::GetReferencedDisplayStates Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetReferencedDisplayStates.md)  
[IComponent2::SetVisibilityInAsmDisplayStates Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetVisibilityInAsmDisplayStates.md)

# GetReferencedDisplayStates Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetReferencedDisplayStates`

Gets the display states of this component that are referenced by the specified assembly display state(s).
Gets the display states of this component that are referenced by the specified assembly display state(s).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetReferencedDisplayStates( _
   ByVal AssemblyDisplayStateOption As System.Integer, _
   ByVal AssemblyDisplayStateNames As System.Object _
) As System.Object
```

```

Dim instance As IComponent2
Dim AssemblyDisplayStateOption As System.Integer
Dim AssemblyDisplayStateNames As System.Object
Dim value As System.Object
 
value = instance.GetReferencedDisplayStates(AssemblyDisplayStateOption, AssemblyDisplayStateNames)
```

```

System.object GetReferencedDisplayStates( 
   System.int AssemblyDisplayStateOption,
   System.object AssemblyDisplayStateNames
)
```

```

System.Object^ GetReferencedDisplayStates( 
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

Array of referenced display state names

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::SetReferencedDisplayStates Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetReferencedDisplayStates.md)  
[IComponent2::GetVisibilityInAsmDisplayStates Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetVisibilityInAsmDisplayStates.md)

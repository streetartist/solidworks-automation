# GetDontCutAllInstances Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetDontCutAllInstances`

Gets whether all instances of the specified component are uncut in this section view or only in the specified component.
Gets whether all instances of the specified component are uncut in this section view or only in the specified component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDontCutAllInstances( _
   ByVal LpComp As Component _
) As System.Boolean
```

```

Dim instance As IDrSection
Dim LpComp As Component
Dim value As System.Boolean
 
value = instance.GetDontCutAllInstances(LpComp)
```

```

System.bool GetDontCutAllInstances( 
   Component LpComp
)
```

```

System.bool GetDontCutAllInstances( 
   Component^ LpComp
) 
```

#### Parameters

*LpComp*
:   Pointer to the [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) object

#### Return Value

True if all instances of the selected component are left uncut, false if only the selected component is left uncut

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.md)  
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.md)  
[IDrSection::SetDontCutAllInstances Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetDontCutAllInstances.md)

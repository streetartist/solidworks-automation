# SetDontCutAllInstances Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetDontCutAllInstances`

Sets whether all instances of the specified component are uncut in this section view or only in the specified component.
Sets whether all instances of the specified component are uncut in this section view or only in the specified component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetDontCutAllInstances( _
   ByVal LpComp As Component, _
   ByVal VbCut As System.Boolean _
) As System.Boolean
```

```

Dim instance As IDrSection
Dim LpComp As Component
Dim VbCut As System.Boolean
Dim value As System.Boolean
 
value = instance.SetDontCutAllInstances(LpComp, VbCut)
```

```

System.bool SetDontCutAllInstances( 
   Component LpComp,
   System.bool VbCut
)
```

```

System.bool SetDontCutAllInstances( 
   Component^ LpComp,
   System.bool VbCut
) 
```

#### Parameters

*LpComp*
:   Pointer to the [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) object

*VbCut*
:   True if all instances of the selected component are left uncut, false if only the selected component is left uncut

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.md)  
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.md)  
[IDrSection::GetDontCutAllInstances Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetDontCutAllInstances.md)

# Toolbars Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Toolbars`

Turns the specified SOLIDWORKS toolbars on and off.
Turns the specified SOLIDWORKS toolbars on and off.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Toolbars( _
   ByVal M As System.Boolean, _
   ByVal Vw As System.Boolean, _
   ByVal SkMain As System.Boolean, _
   ByVal Sk As System.Boolean, _
   ByVal Feat As System.Boolean, _
   ByVal Constr As System.Boolean, _
   ByVal Macro As System.Boolean _
) 
```

```

Dim instance As IModelDoc2
Dim M As System.Boolean
Dim Vw As System.Boolean
Dim SkMain As System.Boolean
Dim Sk As System.Boolean
Dim Feat As System.Boolean
Dim Constr As System.Boolean
Dim Macro As System.Boolean
 
instance.Toolbars(M, Vw, SkMain, Sk, Feat, Constr, Macro)
```

```

void Toolbars( 
   System.bool M,
   System.bool Vw,
   System.bool SkMain,
   System.bool Sk,
   System.bool Feat,
   System.bool Constr,
   System.bool Macro
)
```

```

void Toolbars( 
   System.bool M,
   System.bool Vw,
   System.bool SkMain,
   System.bool Sk,
   System.bool Feat,
   System.bool Constr,
   System.bool Macro
) 
```

#### Parameters

*M*
:   True for main toolbar on, false for off

*Vw*
:   True for view manipulation toolbar on, false for off

*SkMain*
:   RUE for main sketch toolbar on, false for off

*Sk*
:   True for sketch entity toolbar on, false for off

*Feat*
:   True for feature toolbar on, false for off

*Constr*
:   True for relationships toolbar on, false for off

*Macro*
:   True for macro toolbar on, false for off

Remarks

See [IModelDoc2::SetToolbarVisibility](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetToolbarVisibility.md) for control of all SOLIDWORKS toolbars.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::GetToolbarVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetToolbarVisibility.md)  
[ISldWorks::HideToolbar2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~HideToolbar2.md)  
[ISldWorks::GetToolbarState2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetToolbarState2.md)  
[ISldWorks::ShowToolbar2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ShowToolbar2.md)

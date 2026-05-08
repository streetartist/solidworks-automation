# GetToolbarVisibility Method (ISldWorks)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetToolbarVisibility`

Gets whether this toolbar is visible.
Gets whether this toolbar is visible.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetToolbarVisibility( _
   ByVal Toolbar As System.Integer _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim Toolbar As System.Integer
Dim value As System.Boolean
 
value = instance.GetToolbarVisibility(Toolbar)
```

```

System.bool GetToolbarVisibility( 
   System.int Toolbar
)
```

```

System.bool GetToolbarVisibility( 
   System.int Toolbar
) 
```

#### Parameters

*Toolbar*
:   Identifier of toolbar as defined in [swToolbar\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swToolbar_e.html)

#### Return Value

True if the toolbar is visible, false if it is hidden

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::SetToolbarVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetToolbarVisibility.md)  
[ISldWorks::HideToolbar2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~HideToolbar2.md)  
[ISldWorks::GetToolbarState2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetToolbarState2.md)  
[IModelDoc2::GetToolbarVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetToolbarVisibility.md)  
[IModelDoc2::SetToolbarVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetToolbarVisibility.md)  
[ISldWorks::AddToolbar5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbar5.md)

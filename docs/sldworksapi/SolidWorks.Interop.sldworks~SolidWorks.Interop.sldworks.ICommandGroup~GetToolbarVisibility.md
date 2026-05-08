# GetToolbarVisibility Method (ICommandGroup)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~GetToolbarVisibility`

Gets whether this toolbar is visible.
Gets whether this toolbar is visible.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetToolbarVisibility( _
   ByVal SwContext As System.Integer _
) As System.Boolean
```

```

Dim instance As ICommandGroup
Dim SwContext As System.Integer
Dim value As System.Boolean
 
value = instance.GetToolbarVisibility(SwContext)
```

```

System.bool GetToolbarVisibility( 
   System.int SwContext
)
```

```

System.bool GetToolbarVisibility( 
   System.int SwContext
) 
```

#### Parameters

*SwContext*
:   Context in which to show or hide toolbar as defined in [swDocumentTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)

#### Return Value

True to show the toolbar, false to hide it

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.md)  
[ICommandGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members.md)  
[ICommandGroup::SetToolbarVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~SetToolbarVisibility.md)  
[ICommandGroup::HasToolbar Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~HasToolbar.md)

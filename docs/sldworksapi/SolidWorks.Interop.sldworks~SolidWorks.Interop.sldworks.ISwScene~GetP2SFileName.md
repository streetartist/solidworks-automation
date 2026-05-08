# GetP2SFileName Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~GetP2SFileName`

Gets the scene file for this scene.
Gets the scene file for this scene.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetP2SFileName( _
   ByRef Val As System.String _
) 
```

```

Dim instance As ISwScene
Dim Val As System.String
 
instance.GetP2SFileName(Val)
```

```

void GetP2SFileName( 
   out System.string Val
)
```

```

void GetP2SFileName( 
   [Out] System.String^ Val
) 
```

#### Parameters

*Val*
:   Fully qualilfied path to a scene file (**\*.p2s**)

Example

See the [ISwScene](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.md)  
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.md)

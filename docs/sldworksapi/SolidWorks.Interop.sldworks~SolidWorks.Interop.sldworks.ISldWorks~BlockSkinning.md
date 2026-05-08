# BlockSkinning Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~BlockSkinning`

Blocks skinning a window, which prevents a window from looking like a SOLIDWORKS window.
Blocks skinning a window, which prevents a window from looking like a SOLIDWORKS window.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function BlockSkinning() As System.Boolean
```

```

Dim instance As ISldWorks
Dim value As System.Boolean
 
value = instance.BlockSkinning()
```

```

System.bool BlockSkinning()
```

```

System.bool BlockSkinning(); 
```

#### Return Value

True if successful, false if not

Remarks

You must call [ISldWorks::ResumeSkinning](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ResumeSkinning.md) after creating your unskinned window so that new windows created by SOLIDWORKS and other add-ins are displayed as intended.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)

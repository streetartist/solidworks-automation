# Rebuild Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Rebuild`

Obsolete. Superseded by IModelDocExtension::Rebuild.
Obsolete. Superseded by [IModelDocExtension::Rebuild](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Rebuild.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Rebuild( _
   ByVal Options As System.Integer _
) 
```

```

Dim instance As IModelDoc2
Dim Options As System.Integer
 
instance.Rebuild(Options)
```

```

void Rebuild( 
   System.int Options
)
```

```

void Rebuild( 
   System.int Options
) 
```

#### Parameters

*Options*
:   Type of rebuild as defined in [swRebuildOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRebuildOptions_e.html)

Remarks

Use [IModelDoc2::GetType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetType.md) to check the type of document.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::EditRebuild3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.md)  
[IModelDoc2::ForceRebuild3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ForceRebuild3.md)  
[IModelDocExtension::NeedsRebuild2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~NeedsRebuild2.md)

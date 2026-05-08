# NeedsRebuild Property (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~NeedsRebuild`

Obsolete. Superseded by IModelDocExtension::NeedsRebuild2.
Obsolete. Superseded by [IModelDocExtension::NeedsRebuild2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~NeedsRebuild2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property NeedsRebuild As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim value As System.Boolean
 
value = instance.NeedsRebuild
```

```

System.bool NeedsRebuild {get;}
```

```

property System.bool NeedsRebuild {
   System.bool get();
}
```

#### Property Value

True if document needs to be rebuilt, false if not

Remarks

Because this now obsoleted property does not recognize frozen features, use [IModelDocExtension::NeedsRebuild2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~NeedsRebuild2.md), which does.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)

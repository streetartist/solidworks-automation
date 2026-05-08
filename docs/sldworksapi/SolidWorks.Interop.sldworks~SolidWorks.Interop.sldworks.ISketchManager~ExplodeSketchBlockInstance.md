# ExplodeSketchBlockInstance Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ExplodeSketchBlockInstance`

Explodes the specified block instance.
Explodes the specified block instance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ExplodeSketchBlockInstance( _
   ByVal LpSketchBlockInstance As SketchBlockInstance _
) 
```

```

Dim instance As ISketchManager
Dim LpSketchBlockInstance As SketchBlockInstance
 
instance.ExplodeSketchBlockInstance(LpSketchBlockInstance)
```

```

void ExplodeSketchBlockInstance( 
   SketchBlockInstance LpSketchBlockInstance
)
```

```

void ExplodeSketchBlockInstance( 
   SketchBlockInstance^ LpSketchBlockInstance
) 
```

#### Parameters

*LpSketchBlockInstance*
:   [Block instance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.md) to explode

Remarks

If this is the only or last block instance, then:

- All sketch entities in the block instances are copied to the owning sketch of the block instance.
- Source block definition is destroyed.

See [Block Definitions and Block Instances](sldworksAPIProgGuide.chm::/OVERVIEW/Block_Definitions_and_Block_Instances.htm) for details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)  
[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.md)

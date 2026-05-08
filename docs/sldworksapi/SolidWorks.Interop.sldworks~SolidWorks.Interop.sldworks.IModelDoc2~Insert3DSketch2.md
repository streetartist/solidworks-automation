# Insert3DSketch2 Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Insert3DSketch2`

Obsolete. Superseded by ISketchManager::Insert3DSketch.
Obsolete. Superseded by [ISketchManager::Insert3DSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~Insert3DSketch.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Insert3DSketch2( _
   ByVal UpdateEditRebuild As System.Boolean _
) 
```

```

Dim instance As IModelDoc2
Dim UpdateEditRebuild As System.Boolean
 
instance.Insert3DSketch2(UpdateEditRebuild)
```

```

void Insert3DSketch2( 
   System.bool UpdateEditRebuild
)
```

```

void Insert3DSketch2( 
   System.bool UpdateEditRebuild
) 
```

#### Parameters

*UpdateEditRebuild*
:   True if you want to edit and rebuild the document, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[ISketch::Is3D Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~Is3D.md)

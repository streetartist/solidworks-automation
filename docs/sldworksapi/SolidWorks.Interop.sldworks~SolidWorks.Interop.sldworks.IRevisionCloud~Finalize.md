# Finalize Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud~Finalize`

Finalizes the creation of this revision cloud annotation.
Finalizes the creation of this revision cloud annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Finalize() As System.Boolean
```

```

Dim instance As IRevisionCloud
Dim value As System.Boolean
 
value = instance.Finalize()
```

```

System.bool Finalize()
```

```

System.bool Finalize(); 
```

#### Return Value

True if this revision cloud was successfully finalized, false if not

Remarks

You must call this method after all revision cloud path points have been added to the annotation. After finalizing the revision cloud annotation, no new points can be added to the cloud path. The positions of existing cloud path points can be modified at any time.

Example

See [IRevisionCloud](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRevisionCloud Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud.md)  
[IRevisionCloud Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud_members.md)
